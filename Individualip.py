
#import api
#import cryptography

import requests
from Encryptor import justGetKey
import sys


BASE_URL = "http://api.ipstack.com/"

def get_key():
    try:
        if len(sys.argv) > 2:
            if sys.argv[2] == "-aK" & len(sys.argv) == 3:
                return sys.argv[3]
    except Exception:
        try:
            return justGetKey()
        except Exception:
            print("Error: API key not found. Please provide a valid API key.")
            sys.exit(1)
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
