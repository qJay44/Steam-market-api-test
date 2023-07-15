import requests
import tkinter as tk
import matplotlib.pyplot as plt
import pandas as pd
from config import COOKIES


def showPlot(items):
    for _, item in items.items():
        sendRequest(item['appId'].get(), item['name'].get())

    plt.grid(True)
    plt.xlabel('date')
    plt.ylabel('price')
    plt.legend()
    plt.show()


def buildPlot(data, name):
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

        plt.plot(df, label=name)
    else:
        print("Response was unsuccessful")


def sendRequest(appid, name):
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

    buildPlot(data, name)


window = tk.Tk()
window.eval('tk::PlaceWindow . center')
window.resizable(width=False, height=False)


class Item:
    items = {}
    id = 0

    def __init__(self):
        frameItem = tk.Frame(highlightbackground='#5d5f60', highlightthickness=2)

        frameAppId = tk.Frame(master=frameItem)
        labelAppId = tk.Label(master=frameAppId, **self.itemElementConf('app id'))
        labelAppId.pack(side=tk.LEFT)

        entryAppId = tk.Entry(master=frameAppId, width=60)
        entryAppId.insert(0, 730)
        entryAppId.pack(side=tk.RIGHT, padx=10)

        frameMarketHashName = tk.Frame(master=frameItem)
        labelMarketHashName = tk.Label(master=frameMarketHashName, **self.itemElementConf('name '))
        labelMarketHashName.pack(side=tk.LEFT)

        entryMarketHashName = tk.Entry(master=frameMarketHashName, width=60)
        entryMarketHashName.insert(0, 'Operation Hydra Access Pass')
        entryMarketHashName.pack(side=tk.RIGHT, padx=10)

        frameAppId.pack(side=tk.LEFT, padx=5)
        frameMarketHashName.pack(side=tk.LEFT, padx=5)

        # set self id from cls.id
        self.id = self.id

        btnDeleteFrame = tk.Button(
            master=frameItem,
            text='x',
            font=('Arial', 14),
            command=lambda: self.deleteItem(self.id)
        )
        btnDeleteFrame.pack(side=tk.RIGHT)
        frameItem.pack(padx=10, pady=10)

        self.addNewItem(frameItem, entryAppId, entryMarketHashName)

    @classmethod
    def addNewItem(cls, frameItem, appId, name):
        cls.items[cls.id] = {
            'frame': frameItem,
            'appId': appId,
            'name': name
        }
        cls.id += 1

    @classmethod
    def deleteItem(cls, id):
        cls.items[id]['frame'].destroy()
        del cls.items[id]

    @staticmethod
    def itemElementConf(name):
        return {
            'text': name,
            'font': ('Arial 14'),
        }


btbShowPlot = tk.Button(
    master=window,
    text='Show plot',
    font=('Arial', 14),
    command=lambda: showPlot(Item.items)
)
btbShowPlot.pack(side=tk.LEFT, padx=10, pady=10)

btnNewItem = tk.Button(
    master=window,
    text='+',
    font=('Arial', 14),
    command=Item
)
btnNewItem.pack(side=tk.RIGHT, padx=10, pady=10)

window.mainloop()

