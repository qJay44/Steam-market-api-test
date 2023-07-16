import requests
import matplotlib.pyplot as plt
import pandas as pd
from config import COOKIES


class Plot:
    __ax = None

    @classmethod
    def showPlot(cls, items):
        fig, cls.__ax = plt.subplots(figsize=(15, 7))
        cls.__ax.grid(True)
        cls.__ax.set_xlabel('Date', size=14)
        cls.__ax.set_ylabel('Price (руб.)', labelpad=20, size=14)

        for _, item in items.items():
            appId, name = cls.__parseURL(item['entryURL'].get())
            cls.__sendRequest(appId, name)

        fig.legend(loc='outside upper left')
        plt.show()

    @classmethod
    def __buildPlot(cls, data, name):
        if data['success']:
            xAxis = []
            yAxis = []

            for item in data['prices']:
                """
                item[0] - date
                item[1] - price
                item[2] - quantity
                """
                xAxis.append(item[0][0:14])
                yAxis.append(item[1])

            date = pd.to_datetime(xAxis)
            df = pd.DataFrame()
            df['value'] = yAxis
            df = df.set_index(date)

            cls.__ax.plot(df, label=name)
        else:
            print("Response was unsuccessful")

    @classmethod
    def __sendRequest(cls, appid, name):
        params = {
            'country': 'RU',
            'currency': 5,
            'appid': appid,
            'market_hash_name': name
        }

        response = requests.get(
            'http://steamcommunity.com/market/pricehistory',
            params=params,
            cookies=COOKIES
        )

        data = response.json()

        cls.__buildPlot(data, name)

    @staticmethod
    def __parseURL(url):
        parsedURL = url.split('/')

        return parsedURL[5], parsedURL[6].replace('%20', ' ')

