import tkinter as tk

class SteamItem:
    _items = {}
    __id = 0

    def __init__(self, testURL = None):
        frameSteamItem = tk.Frame(highlightbackground='#5d5f60', highlightthickness=2)

        labelURL = tk.Label(master=frameSteamItem, text='url', font=('Arial 14'))
        labelURL.pack(side=tk.LEFT)

        entryURL = tk.Entry(master=frameSteamItem, width=60)
        entryURL.pack(side=tk.LEFT, padx=10)
        entryURL.focus()
        entryURL.bind('<FocusIn>', lambda e: e.widget.select_range(0, tk.END))
        entryURL.insert(0, testURL) if testURL is not None else ...

        id = SteamItem.__id

        btnDeleteItem = tk.Button(
            master=frameSteamItem,
            text='x',
            font=('Arial', 14),
            command=lambda: self.__deleteSteamItem(id)
        )
        btnDeleteItem.pack(side=tk.RIGHT, padx=5, pady=5)
        frameSteamItem.pack(fill=tk.X, padx=10, pady=10)

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

