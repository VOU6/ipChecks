# 68.100.82.139

#import api
#import cryptography

import requests
from Encryptor import decrypt


BASE_URL = "http://api.ipstack.com/"

def get_key():
    return decrypt()
def getJSON(ip):
    url = BASE_URL + ip + "?access_key=" + get_key()
    response = requests.get(url)
    return response.json()


def printDATA(ip):
    data = getJSON(ip)
    if "error" in data:
        print("Error:", data["error"]["info"])
    else:
        print("Ip Address:", data["ip"])
        print("Type of Ip:", data["type"])
        print("Ip Routing Type:", data["ip_routing_type"])
        print("Country:", data["country_name"])
        print("City:", data["city"])
        print("Zip Code:", data["zip"])
        print("Latitude:", data["latitude"])
        print("Longitude:", data["longitude"])

###
###
###
###
###
###
###
###
### End of script ###
###