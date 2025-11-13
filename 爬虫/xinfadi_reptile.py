import requests, pymysql, time, datetime
from pymysql import cursors

def main():

    def post_json(url, payload):
        for attempt in range(3):
            try:
                resp = requests.post(url, data=payload,
                                     headers=headers, timeout=15)
                resp.raise_for_status()
                return resp.json()
            except Exception as e:
                print(f"[{attempt + 1}/3] 请求出错：{e}，5 秒后重试…")
                time.sleep(5)
        raise RuntimeError("请求多次失败，请检查网络或接口是否变更")

    DB_HOST = 'localhost'
    DB_USER = 'root'
    DB_PASSWORD = '1234'
    DB_NAME = 'warehousing'
    DB_PORT = 3306
    connection = pymysql.connect(host=DB_HOST, user=DB_USER, password=DB_PASSWORD,
                                 port=DB_PORT, database=DB_NAME, charset='utf8mb4', cursorclass=cursors.Cursor)

    def mysql_data_insert(record_row):

        sql_insert_data = (f"""
                 INSERT INTO comparative_goods (comparative_name, comparative_price, 
                 comparative_specification, comparative_unit, comparative_time, create_time)
                 VALUES(%(comparative_name)s, %(comparative_price)s, %(comparative_specification)s, 
                 %(comparative_unit)s, %(comparative_time)s,%(create_time)s)
         """)

        try:
            with connection.cursor() as cursor:

                cursor.execute(sql_insert_data, record_row)

                connection.commit()

        except pymysql.Error as e:
            print(f"数据插入失败: {e}")
            if connection:
                connection.rollback()

    price_url: str = "http://www.xinfadi.com.cn/getPriceData.html"
    headers: dict[str:str] = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) " 
                      "AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/126.0.0.0 Safari/537.36",
        "Referer": "http://www.xinfadi.com.cn/priceDetail.html"
    }

    category_map: dict[str:str] = {
        "蔬菜": "1186",
        "水果": "1187",
        "肉禽蛋": "1189",
        "水产": "1190",
        "粮油": "1188",
        "豆制品": "1203",
        "调料": "1204"
    }

    key_map: dict[str:str] = {
        "prodName": "comparative_name",
        "avgPrice": "comparative_price",
        "specInfo": "comparative_specification",
        "unitInfo": "comparative_unit",
        "pubDate": "comparative_time",
    }

    today = datetime.date.today()
    time_online = datetime.datetime.now()
    time_without = time_online.strftime("%Y-%m-%d %H:%M:%S")

    for cat_name, pcatid in category_map.items():
        print(f"=== 正在抓取 {cat_name} ===")

        one_day_ago = today -datetime.timedelta(days=1)

        payload_first: dict[str: str, str: int] = {
            "limit": "20",
            "current": "1",
            "pubDateStartTime": one_day_ago,
            "pubDateEndTime": one_day_ago,
            "prodPcatid": pcatid,
            "prodCatid": "",
            "prodName": ""
        }

        data_first = post_json(price_url, payload_first)
        total_cnt = int(data_first.get("count", 0))

        payload_all = payload_first.copy()
        payload_all["limit"] = str(total_cnt)
        payload_all["current"] = "1"

        data_all = post_json(price_url, payload_all)
        records = data_all.get("list", [])
        print(f"抓到 {len(records)} 条记录")

        for item in records:
            if not item.get("prodCat"):
                item["prodCat"] = cat_name

        for row in records:
            cn_row = {key_map[k]: row.get(k, "") for k in key_map}
            cn_row['create_time'] = time_without
            mysql_data_insert(cn_row)


if __name__ == '__main__':
    main()




