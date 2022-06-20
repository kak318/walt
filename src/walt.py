import tkinter as tk
import socket
import webbrowser as wb
import random as rng

root = tk.Tk()

yip = socket.gethostbyname(socket.gethostname())
mtxt = tk.Label(text="I know your exact location.\n")
mtxt.pack()
txt = tk.Label(text=str(yip))
txt.pack()

for i in range(10):
    r = rng.randint(1, 3)
    if r == 1:
        link = "https://c.tenor.com/CpH8xAFiTrEAAAAC/funny-cat-cat.gif"
    elif r == 2:
        link = "https://c.tenor.com/ucj44kwfqW0AAAAd/i-know-your-exact-coordinates-vegito.gif"
    elif r == 3:
        link = "https://c.tenor.com/RYJ1OaF69eoAAAAM/ibuki-mioda-ibuki.gif"

    wb.open(link)

root.mainloop()