import requests, time
import pymysql
from pymysql import cursors

def main():

    def post_json(url, payload):  # 封装的请求函数，具有重试机制
        for attempt in range(3):
            try:
                resp = requests.post(url, data=payload,  # 发送POST请求并返回解析后的JSON
                                     headers=headers, timeout=15)
                resp.raise_for_status()
                return resp.json()
            except Exception as e:  # 最多尝试3次请求，显示出错信息并等待5秒后再次请求
                print(f"[{attempt + 1}/3] 请求出错：{e}，5 秒后重试…")
                time.sleep(5)
        raise RuntimeError("请求多次失败，请检查网络或接口是否变更")  # 请求失败显示异常信息

    DB_HOST = 'localhost'
    DB_USER = 'root'
    DB_PASSWORD = '1234'
    DB_NAME = 'xinfadi'
    DB_PORT = 3306
    connection = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD,
                                 port=DB_PORT, database=DB_NAME, charset='utf8mb4', cursorclass=cursors.Cursor)

    def mysql_table_create(price_key_map, count):
        sql_table = (f"""
                         CREATE TABLE  IF NOT EXISTS {price_key_map[count]}(
                             id INT  AUTO_INCREMENT PRIMARY KEY,
                             品名 VARCHAR(255) NOT NULL,
                             平均价 DECIMAL(10, 2) NOT NULL,
                             规格 VARCHAR(255),
                             单位 VARCHAR(50) NOT NULL,
                             发布日期 DATETIME NOT NULL
                         )
                 """)
        try:
            with connection.cursor() as cursor:
                cursor.execute(sql_table)

                connection.commit()

        except pymysql.Error as e:
            print(f"数据表创建失败: {e}")
            if connection:
                connection.rollback()

    def mysql_data_insert(price_key_map, count,  record_row):

        sql_insert = (f"""
                 INSERT INTO {price_key_map[count]}(品名, 平均价, 规格, 单位, 发布日期)
                 VALUES(%(品名)s, %(平均价)s, %(规格)s, %(单位)s, %(发布日期)s)
         """)

        try:
            with connection.cursor() as cursor:

                cursor.execute(sql_insert, record_row)

                connection.commit()

        except pymysql.Error as e:
            print(f"数据插入失败: {e}")
            if connection:
                connection.rollback()

    price_url: str = "http://www.xinfadi.com.cn/getPriceData.html"  # 统一资源定位符
    headers: dict[str:str] = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "  # 请求头，声明留恋其类型
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/126.0.0.0 Safari/537.36",
        "Referer": "http://www.xinfadi.com.cn/priceDetail.html"  # 符合接口访问规则
    }

    category_map: dict[str:str] = {  # 接口参数
        "粮油": "1188",
        "豆制品": "1203",
        "调料": "1204"
    }

    key_map: dict[str:str] = {  # 接口返回字段到中文列名的映射
        "prodName": "品名",
        "avgPrice": "平均价",
        "specInfo": "规格",
        "unitInfo": "单位",
        "pubDate": "发布日期",
    }

    count_map = 0

    for cat_name, pcatid in category_map.items():  # 正式抓取，遍历每一个品类
        print(f"=== 正在抓取 {cat_name} ===")

        payload_first: dict[str: str, str: int] = {  # 该接口Payload返回的参数
            "limit": "20",  # 每页返回的条数
            "current": "1",  # 页码
            "pubDateStartTime": "2025-10-31", # 起始时间
            "pubDateEndTime": "",  # 终止时间
            "prodPcatid": pcatid,  # 对应的品类ID接口参数(大类)
            "prodCatid": "",  # 小类ID为NULL即不使用小类过滤
            "prodName": ""  # 名称ID为NULL即不使用名称过滤
        }
        # 返回的 JSON 包含 count（总记录数），用 total_cnt 保存
        data_first = post_json(price_url, payload_first)
        total_cnt = int(data_first.get("count", 0))

        ''' if total_cnt == 0:          # 判断是否有数据
            print(f"{cat_name} 在 {start_date}~{end_date} 期间未查询到数据")
            continue
        '''
        # 构造获取全部记录的Payload
        payload_all = payload_first.copy()
        payload_all["limit"] = str(total_cnt)  # 返回的 JSON 包含 count（总记录数），用 total_cnt 保存
        payload_all["current"] = "1"

        data_all = post_json(price_url, payload_all)  # 真正的商品价格列表，保存到 records。
        records = data_all.get("list", [])  # 原始数据
        print(f"抓到 {len(records)} 条记录")

        # 为可能缺失的prodCat字段补上品类中文名
        for item in records:
            if not item.get("prodCat"):
                item["prodCat"] = cat_name

        mysql_table_create(list(category_map.keys()), count_map)

        for row in records:
            # 通过 key_map 把接口返回的键映射为中文列名，row.get(k,"")防止某些字段缺失导致 KeyError，缺失时写空字符串。
            cn_row = {key_map[k]: row.get(k, "") for k in key_map}
            mysql_data_insert(list(category_map.keys()), count_map, cn_row)

        count_map += 1

if __name__ == '__main__':
    main()




