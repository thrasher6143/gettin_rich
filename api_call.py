import requests


def main():
    coindesk_api_call()


# This is good usable code
def coindesk_api_call():
    url = "https://api.coindesk.com/v1/bpi/currentprice.json"
    r = requests.get(url)
    print("Status code:", r.status_code)
    response_dict = r.json()
    bpi_dict = response_dict['bpi']
    bpi_usd = bpi_dict['USD']
    btc_rate = bpi_usd['rate_float']
    timestamp = response_dict['time']
    update_call_time = timestamp['updated']
    print("Updated at: " + update_call_time + "\nCurrent rate is: " + str(btc_rate))
    return update_call_time, btc_rate


if __name__ == '__main__':
    main()



#
# url = 'https://api.coindesk.com/v1/bpi/currentprice.json'
# r = requests.get(url)
# print("Status code:", r.status_code)
#
# response_dict = r.json()
# print(response_dict['time'])
# call_time = response_dict['time']
# print(call_time['updated'])
# bpi_dict = response_dict['bpi']
# for key in sorted(bpi_dict.keys()):
#     print(key)
# print(bpi_dict['USD'])
#
# bpi_usd = bpi_dict['USD']
# for item in sorted(bpi_usd.items()):
#     print(item)
# print(bpi_usd['rate'])
# BTC_rate = bpi_usd['rate']
#
#
# print("\nBitcoin is at:", bpi_usd['rate'], "in", bpi_usd['description'] )


