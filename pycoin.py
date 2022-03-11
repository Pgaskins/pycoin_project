import json
from pip._vendor import requests
from tkinter import *


#TK init root method that produces the frame 
pycoin = Tk()
# the title of of the application on the app window
pycoin.title("PyCOIN Portfolio")

#return the green for positive and red for negative
def font_color():
    if current_val >= 0:
        return "green"
    else:
        return "red"    

def my_pycoin():
    COIN_API = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest?start=1&limit=20&convert=USD&CMC_PRO_API_KEY=510757cf-cf43-4f5e-8644-3c0b2e8f5589"

    get_api = requests.get(COIN_API)

    conv_api = json.loads(get_api.content)

    coins  = [
        {
            "symbol" : "BTC",
            "amount_owned": 55,
            "price_per_coin" : 31913
        },
        {
            "symbol" : "ETH",
            "amount_owned" : 5,
            "price_per_coin":2039
        },
        {
            "symbol" : "USDT",
            "amount_owned" : 4000,
            "price_per_coin" : 1
        },
        {
            "symbol" : "BNB",
            "amount_owned" : 200,
            "price_per_coin" : 3600
        },
        {
            "symbol" : "USDC",
            "amount_owned" : 700,
            "price_per_coin" : .25
        },
        {
            "symbol" : "LUNA",
            "amount_owned" : 200,
            "price_per_coin" : 90
        },
        {
            "symbol" : "DOGE",
            "amount_owned" : 40000,
            "price_per_coin" : .19
        }
    ]


#for loop to loop through json DOM range 0,5
#for loop through the coin in coins that have invested {coins}
#if the coin in the api = the {coins} print sympbol,name,price 
#without the if condition it would print 5 sets of data 
    totalval = 0
    coin_row = 1
    
    for i in range(0, 20):
            for coin in coins:
                if conv_api["data"][i]["symbol"] == coin["symbol"]:
                    total_payout = coin["amount_owned"] * coin["price_per_coin"]
                    current_value = coin["amount_owned"] * conv_api["data"][i]["quote"]["USD"]["price"]
                    pl_percoin = conv_api["data"][i]["quote"]["USD"]["price"] - coin["price_per_coin"]
                    total_pl = pl_percoin * current_value
                    totalval = total_payout + total_pl
                    #label text printed out within the specific row and column
                    #grid was used to place the labels 
                    name = Label(pycoin, text=conv_api["data"][i]["name"], bg="gray", fg="black")
                    name.grid(row=coin_row, column=0, sticky=N+S+E+W)

                    price = Label(pycoin, text="${0:.2f}".format(conv_api["data"][i]["quote"]["USD"]["price"]), bg="white", fg="black")
                    price.grid(row=coin_row, column=1, sticky=N+S+E+W)

                    num_coin = Label(pycoin, text=coin["amount_owned"], bg="gray", fg="black")
                    num_coin.grid(row=coin_row, column=2, sticky=N+S+E+W)

                    total_payout = Label(pycoin, text="${0:.2f}".format(total_payout), bg="white", fg="black")
                    total_payout.grid(row=coin_row, column=3, sticky=N+S+E+W)

                    current_val = Label(pycoin, text="${0:.2F}".format(current_value), bg="blue", fg="springgreen")
                    current_val.grid(row=coin_row, column=4, sticky=N+S+E+W)


                    coin_row = coin_row + 1

            current_val = Label(pycoin, text="${0:.2F}".format(totalval), bg="gray", fg="black")
            current_val.grid(row=coin_row, column=4, sticky=N+S+E+W)

            # clear the api so the refresh button can give new info
            #conv_api = ""
            update = Button(pycoin, text="UPDATE", bg="gray", fg="black", command=my_pycoin)
            update.grid(row=coin_row +1, column=4, sticky=N+S+E+W)




name = Label(pycoin, text="Coin Name", bg="blue", fg="white", font= "Lato 12 bold", padx="5", pady="5", borderwidth=3, relief="groove")
name.grid(row=0, column=0, sticky=N+S+E+W)

price = Label(pycoin, text="Price", bg="blue", fg="white",font= "Lato 12 bold", padx="5", pady="5", borderwidth=3, relief="groove")
price.grid(row=0, column=1, sticky=N+S+E+W)

num_coin = Label(pycoin, text="Coin Owned", bg="blue", fg="white",font= "Lato 12 bold", padx="5", pady="5", borderwidth=3, relief="groove")
num_coin.grid(row=0, column=2, sticky=N+S+E+W)

total_payout = Label(pycoin, text="Total Payout", bg="blue", fg="white",font= "Lato 12 bold", padx="5", pady="5", borderwidth=3, relief="groove")
total_payout.grid(row=0, column=3, sticky=N+S+E+W)

current_val = Label(pycoin, text="Current Value", bg="blue", fg="white",font= "Lato 12 bold", padx="5", pady="5", borderwidth=3, relief="groove")
current_val.grid(row=0, column=4, sticky=N+S+E+W)

my_pycoin()

pycoin.mainloop()


