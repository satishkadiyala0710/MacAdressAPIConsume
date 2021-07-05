import json

import requests


# query=input("enter company name")

query="44:38:39:ff:ef:57"
response=requests.get("https://api.macaddress.io/v1?apiKey=at_FADZ9k5dxSmsbaY7gOVI0qOxTdWJq&output=json&search={}".format(query))


data=(json.loads(response.content))

print("Company Name:{} And  MacAdress:{}".format(data["vendorDetails"]["companyName"],data["macAddressDetails"]["searchTerm"]))









# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    pass



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
