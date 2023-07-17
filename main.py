import tkinter as tk
from SteamItem import SteamItem
from Plot import Plot
from config import TEST_LINKS

class App:

    def __init__(self, useTestLinks):
        window = tk.Tk()
        window.title('Steam item price plot')
        window.resizable(width=False, height=False)

        #=================== Create main widgets ===================#

        frameMain = tk.Frame()

        # Frame for cookie entry #

        frameCookie = tk.Frame(master=frameMain)

        labelURL = tk.Label(master=frameCookie, text='steamLoginSecure', font=('Arial 12'))
        labelURL.pack(side=tk.LEFT)

        cookieEntry = tk.Entry(master=frameCookie)
        cookieEntry.pack(side=tk.RIGHT, padx=10)
        cookieEntry.insert(0, self.__loadCookie())

        frameCookie.pack(side=tk.LEFT, pady=5)

        #========================#

        # Frame for main buttons #

        frameMainButtons = tk.Frame(master=frameMain)

        btbShowPlot = tk.Button(
            master=frameMainButtons,
            text='Show plot',
            font=('Arial', 14),
            command=lambda: self.__commandShowPlot(cookieEntry.get())
        )
        btbShowPlot.pack(side=tk.LEFT, padx=10, pady=10)

        btnNewSteamItem = tk.Button(
            master=frameMainButtons,
            text='+',
            font=('Arial', 14),
            command=SteamItem
        )
        btnNewSteamItem.pack(side=tk.RIGHT, pady=10)

        frameMainButtons.pack(side=tk.RIGHT)

        #========================#

        frameMain.pack(side=tk.TOP, fill=tk.X, padx=10)

        #===========================================================#

        if useTestLinks:
            for url in TEST_LINKS:
                SteamItem(url)

        window.protocol(
            "WM_DELETE_WINDOW",
            lambda: self.__deleteWindow(window, cookieEntry.get())
        )
        window.eval('tk::PlaceWindow . center')
        window.mainloop()

    def __commandShowPlot(self, cookie):
        plot = Plot(SteamItem._items, cookie)
        plot.showPlot()

    def __deleteWindow(self, window, cookie):
        self.__saveCookie(cookie)
        window.destroy()

    @staticmethod
    def __loadCookie():
        try:
            with open('cookie.txt', 'r') as f:
                return f.read()
        except FileNotFoundError:
            return ''

    @staticmethod
    def __saveCookie(cookie):
        with open('cookie.txt', 'w') as f:
            f.truncate(0)
            f.write(cookie)


if __name__ == '__main__':
    App(useTestLinks=True)


