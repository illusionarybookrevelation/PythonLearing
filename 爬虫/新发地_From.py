import requests, time, csv,datetime

price_url: str = "http://www.xinfadi.com.cn/getPriceData.html"       # 统一资源定位符
headers: dict[str:str] = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "  # 请求头，声明留恋其类型
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/126.0.0.0 Safari/537.36",
    "Referer": "http://www.xinfadi.com.cn/priceDetail.html"     # 符合接口访问规则
}
today: time = datetime.date.today()       # 获取今天日期
seven_days_ago: time = today - datetime.timedelta(days=3)     # 往前推6天(包含今天共7天)

start_date: time = seven_days_ago.strftime("%Y/%m/%d")        # 格式化日期为YYYY/MM/DD，6天前的起始日期
end_date: time   = today.strftime("%Y/%m/%d")             # 格式化日期为YYYY/MM/DD，今天天前的中止日期

category_map: dict[str:str] = {                    # 接口参数
    "蔬菜": "1186",
    "水果": "1187",
    "肉禽蛋": "1189",
    "水产": "1190",
    "粮油": "1188",
    "豆制品": "1203",
    "调料": "1204"
}

fields: list[str]= ["分类", "品名", "最低价", "平均价", "最高价", "规格", "产地", "单位", "发布日期"]    #CSV表头字段
key_map: dict[str:str] = {     # 接口返回字段到中文列名的映射
    "prodCat":   "分类",
    "prodName":  "品名",
    "lowPrice":  "最低价",
    "avgPrice":  "平均价",
    "highPrice": "最高价",
    "specInfo":  "规格",
    "place":     "产地",
    "unitInfo":      "单位",
    "pubDate":   "发布日期",
}

def post_json(payload):             # 封装的请求函数，具有重试机制
    for attempt in range(3):
        try:
            resp = requests.post(price_url, data=payload,       # 发送POST请求并返回解析后的JSON
                                 headers=headers, timeout=15)
            resp.raise_for_status()
            return resp.json()
        except Exception as e:              # 最多尝试3次请求，显示出错信息并等待5秒后再次请求
            print(f"[{attempt+1}/3] 请求出错：{e}，5 秒后重试…")
            time.sleep(5)
    raise RuntimeError("请求多次失败，请检查网络或接口是否变更")   # 请求失败显示异常信息

for cat_name, pcatid in category_map.items():       # 正式抓取，遍历每一个品类
    print(f"\n=== 正在抓取 {cat_name} ===")

    payload_first: dict[str: str, str: int] = {           # 该接口Payload返回的参数
        "limit": "20",      # 每页返回的条数
        "current": "1",         # 页码
        "pubDateStartTime": start_date,     # 起始时间
        "pubDateEndTime":   end_date,       # 终止时间
        "prodPcatid": pcatid,       # 对应的品类ID接口参数(大类)
        "prodCatid": "",            # 小类ID为NULL即不使用小类过滤
        "prodName": ""           # 名称ID为NULL即不使用名称过滤
    }
    # 返回的 JSON 包含 count（总记录数），用 total_cnt 保存
    data_first = post_json(payload_first)
    total_cnt = int(data_first.get("count", 0))

    if total_cnt == 0:          # 判断是否有数据
        print(f"{cat_name} 在 {start_date}~{end_date} 期间未查询到数据")
        continue
    # 构造获取全部记录的Payload
    payload_all = payload_first.copy()
    payload_all["limit"] = str(total_cnt)       # 返回的 JSON 包含 count（总记录数），用 total_cnt 保存
    payload_all["current"] = "1"

    data_all = post_json(payload_all)       # 真正的商品价格列表，保存到 records。
    records = data_all.get("list", [])
    print(f"抓到 {len(records)} 条记录")

    # 为可能缺失的prodCat字段补上品类中文名
    for item in records:
        if not item.get("prodCat"):
            item["prodCat"] = cat_name

    # 生成 CSV 文件并写入数据
    csv_name = f"新发地_{cat_name}_最近3天.csv"
    with open(csv_name, "w", newline="", encoding="utf-8-sig") as f:
        writer = csv.DictWriter(f, fieldnames=fields)       # 使用中文列名写入表头
        writer.writeheader()
        for row in records:
            # 通过 key_map 把接口返回的键映射为中文列名，row.get(k,"")防止某些字段缺失导致 KeyError，缺失时写空字符串。
            cn_row = {key_map[k]: row.get(k, "") for k in key_map}
            writer.writerow(cn_row)

    print(f"CSV 已生成 → {csv_name}")

print("\n全部品类抓取完成 ")