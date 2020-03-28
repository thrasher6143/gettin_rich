from api_call import coindesk_api_call as cd
import time
from pymsgbox import *
from tkinter import *


def main():
    bcpi_hx = {}
    while True:
        if bcpi_hx != {}:
            print(btc_rate, type(btc_rate))
            sevenup, sevendown = (btc_rate*1.007), btc_rate - (btc_rate*0.007)
            print(sevenup, sevendown)
            updated_time, btc_rate = cd()
            btc_compare(sevenup, sevendown, btc_rate)
            bcpi_hx[updated_time] = btc_rate
            print(bcpi_hx)

        else:
            updated_time, btc_rate = cd()
            bcpi_hx[updated_time] = btc_rate
            print(bcpi_hx)

        time.sleep(60)


def btc_compare(sevenup, sevendown, rate):
    if rate > sevenup or rate < sevendown:
        alert(text='bitcoin price changing rapidly', title='Bitcoin Price Tracker', button='OH NO!')


if __name__ == '__main__':
    main()

