import tkinter as tk

class SteamItem:
    testURL = 'https://steamcommunity.com/market/listings/730/Antwerp%202022%20Champions%20Autograph%20Capsule'
    _items = {}
    __id = 0

    def __init__(self):
        frameSteamItem = tk.Frame(highlightbackground='#5d5f60', highlightthickness=2)

        labelURL = tk.Label(master=frameSteamItem, text='url', font=('Arial 14'))
        labelURL.pack(side=tk.LEFT)

        entryURL = tk.Entry(master=frameSteamItem, width=60)
        entryURL.insert(0, SteamItem.testURL)
        entryURL.pack(side=tk.LEFT, padx=10)
        entryURL.focus()
        entryURL.bind('<FocusIn>', lambda e: e.widget.select_range(0, tk.END))

        self.__id = SteamItem.__id

        btnDeleteItem = tk.Button(
            master=frameSteamItem,
            text='x',
            font=('Arial', 14),
            command=lambda: self.__deleteSteamItem(self.__id)
        )
        btnDeleteItem.pack(side=tk.RIGHT, padx=5, pady=5)
        frameSteamItem.pack(padx=10, pady=10)

        self.__addNewSteamItem(frameSteamItem, entryURL)

    @classmethod
    def __addNewSteamItem(cls, frameSteamItem, entryURL):
        cls._items[cls.__id] = {
            'frame': frameSteamItem,
            'entryURL': entryURL
        }
        cls.__id += 1

    @classmethod
    def __deleteSteamItem(cls, __id):
        cls._items[__id]['frame'].destroy()
        del cls._items[__id]

