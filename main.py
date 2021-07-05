import json
import requests

#Program for ConsumeMacAddressRestAPI


try:
    #take macaddress as input parameter
    query=input("enter company name")
    #fetch the company details using get method passing macadress as query parameter
    response=requests.get("https://api.macaddress.io/v1?apiKey=at_FADZ9k5dxSmsbaY7gOVI0qOxTdWJq&output=json&search={}".format(query))
    #parsing the response data using json loads method
    data=(json.loads(response.content))
    print("Company Name:{} And  MacAdress:{}".format(data["vendorDetails"]["companyName"],data["macAddressDetails"]["searchTerm"]))
except Exception as e:
    print(e.args)









if __name__ == '__main__':
    pass



