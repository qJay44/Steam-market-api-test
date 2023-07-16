import tkinter as tk
from SteamItem import SteamItem
from Plot import Plot


if __name__ == '__main__':
    window = tk.Tk()
    window.title('Steam item price plot')
    window.eval('tk::PlaceWindow . center')
    window.resizable(width=False, height=False)

    btbShowPlot = tk.Button(
        master=window,
        text='Show plot',
        font=('Arial', 14),
        command=lambda: Plot.showPlot(SteamItem._items)
    )
    btbShowPlot.pack(side=tk.RIGHT, padx=10, pady=10)

    btnNewSteamItem = tk.Button(
        master=window,
        text='+',
        font=('Arial', 14),
        command=SteamItem
    )
    btnNewSteamItem.pack(side=tk.RIGHT, padx=10, pady=10)

    window.mainloop()

