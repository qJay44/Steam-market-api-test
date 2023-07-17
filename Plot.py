import requests
import matplotlib.pyplot as plt
import pandas as pd


class Plot:

    def __init__(self, items, cookie):
        self.items = items
        self.cookie = cookie

    def showPlot(self):
        _, self.__ax = plt.subplots(figsize=(15, 7))
        self.__ax.grid(True)
        self.__ax.set_xlabel('Date', size=14)
        self.__ax.set_ylabel('Price (руб.)', labelpad=20, size=14)

        for _, item in self.items.items():
            appId, name = self.__parseURL(item['entryURL'].get())
            self.__sendRequest(appId, name)

        # TODO: fix legend position
        self.__ax.legend()
        plt.show()

    def __buildPlot(self, data, name):
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

            self.__ax.plot(df, label=name)
            # cls.__ax.scatter(df.index, df.value, s=3, label=name)
        else:
            print("Response was unsuccessful")

    def __sendRequest(self, appid, name):
        params = {
            'country': 'RU',
            'currency': 5,
            'appid': appid,
            'market_hash_name': name
        }

        response = requests.get(
            'http://steamcommunity.com/market/pricehistory',
            params=params,
            cookies={ 'steamLoginSecure': self.cookie }
        )

        data = response.json()

        self.__buildPlot(data, name)

    @staticmethod
    def __parseURL(url):
        parsedURL = url.split('/')

        return parsedURL[5], parsedURL[6].replace('%20', ' ')

