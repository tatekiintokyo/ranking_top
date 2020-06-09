        #!/usr/bin/<span class="searchword">python</span>2.7
        # -*- coding: utf-8 -*-
        import pandas as pd
        import requests
        import sys, codecs
        import datetime
        sys.stdout = codecs.getwriter("utf-8")(sys.stdout)

        # リストを作成
        columns = ["dt_year", "dt_month", "dt_day", "rank","itemName","itemUrl","itemCode","itemPrice","postageFlag","startTime","endTime","pointRate","shopName","shopUrl"]

        # 配列名を指定する
        df = pd.DataFrame(columns=columns)

        dt_now = datetime.datetime.now()
        dt_year = dt_now.year
        dt_month = dt_now.month
        dt_day = dt_now.day
        
        url = "https://app.rakuten.co.jp/services/api/IchibaItem/Ranking/20170628?"
        page = 1

        for num in range(3):

            st_load = {
                "page":page,
                "applicationId": ××××,
                }
            
            r = requests.get(url, params=st_load)
            
            res = r.json()
            
            for i in res["Items"]:
                item = i["Item"]

                rank = item["rank"]
                itemName = item["itemName"]
                itemUrl = item["itemUrl"]
                itemCode = item["itemCode"]
                itemPrice = item["itemPrice"]
                postageFlag = item["postageFlag"]
                startTime = item["startTime"]
                endTime = item["endTime"]
                pointRate = item["pointRate"]
                shopName = item["shopName"]
                shopUrl = item["shopUrl"]

                se = pd.Series([dt_year, dt_month, dt_day, rank, itemName, itemUrl, itemCode, itemPrice, postageFlag, startTime, endTime, pointRate, shopName, shopUrl], columns)
                print(se)
            
                df = df.append(se, columns)
                print(df)

            page += 1

        filename = "top_rank.csv"
        df.to_csv(filename, encoding="utf-8-sig",mode='a', header=False)
