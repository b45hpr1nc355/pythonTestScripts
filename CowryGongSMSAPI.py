'''
created on 9th December, 2016

Author t4ky1
'''

import time
import uuid

import requests

from requests.packages.urllib3.exceptions import InsecureRequestWarning

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)

PROTOCOL = "https"
HOST = "api.misika247.com"
PORT = "24799"


def create_uuid():
    new_uuid = (str(uuid.uuid4())).replace('-', '')

    return new_uuid


def call_api_interface(api_postSMS, module, action):
    print("SMS delivered: \n")
    print(api_postSMS)
    print(" ")

    URL = "%s://%s:%s/api/%s/sms/%s/" % (PROTOCOL, HOST, PORT, module, action)

    print("To call the api_interface, \nCall it using URL %s" % URL)


    req = requests.post(URL, json=api_postSMS, verify=False)

    print("Respond from API call = %s " % req.text)

    print(" %s: " % req.status_code)

    resp_dict = req.json()

    print("Respond from API call = %s " % resp_dict)


#def generateAPIkey():
 #   getLoginDets = {
  #      "action": "generateAPIKey",
   #     "username": "apiqa@misika247.com",
    #    "password": "golpf340ev",
     #   "service_provider_id": "3006bee1f78047e8811f536122e2877a",
      #  "expiry": 1
    #}
#    print("Your login details: %s" % str(getLoginDets))

#    return getLoginDets


def getBalance():
    checkSMSbal = {
        "api_key": "61b87502373649d09c01cffe9e1dcbd3",
        "service_provider_id": "3006bee1f78047e8811f536122e2877a",
        "source": "api"
    }
    print("Your SMS balance: %s" % str(checkSMSbal))

    return checkSMSbal


def getRoutes():
    getSMSroutes = {
        "api_key": "61b87502373649d09c01cffe9e1dcbd3",
        "service_provider_id": "3006bee1f78047e8811f536122e2877a",
        "source": "api"
    }
    print("The configured SMS routes: %s" % str(getSMSroutes))
    return getSMSroutes


def postBulkMessage():
    postbulkSMS = {
        "api_key": "61b87502373649d09c01cffe9e1dcbd3",
        "service_provider_id": "3006bee1f78047e8811f536122e2877a",
        "source": "api",
        "routeID": "8f1df72288915292efcf456df43e5b20",
        "messages": [{"messageID": "4c2c60d1", "text": "Tests from MainOne", "phonenumber": "233504169784"},
                     {"messageID": "d87801fe", "text": "Tests from MainOne", "phonenumber": "233200313710"},
                     {"messageID": "d87801fe", "text": "Tests from MainOne", "phonenumber": "233555055956"}],
        "senderID": "Cowry Tests",
        "messageType": "SMS",
        "callback": 1,
        "dlr-url": " ",
        "priority-level": "HIGH"
    }
    print("Your bulk message creds: %s" % str(postbulkSMS))

    return postbulkSMS


def postMessage():
    postMess = {
        "api_key": "61b87502373649d09c01cffe9e1dcbd3",
        "service_provider_id": "3006bee1f78047e8811f536122e2877a",
        "source": "api",
        "routeID": "8f1df72288915292efcf456df43e5b20",
        "text": "ADB Tests",
        "senderID": "Cowry",
        "messageID": "4c2c60d1",
        "messageType": "SMS",
        "phonenumber": "233555055956",
        "callback": 1,
        "dlr-url": " ",
        "priority-level": "HIGH"
    }
    print("Your SMS creds: %s" % str(postMess))

    return postMess


def getMessageStatus():
    getStatus = {
        "api_key": "61b87502373649d09c01cffe9e1dcbd3",
        "service_provider_id": "3006bee1f78047e8811f536122e2877a",
        "source": "api",
        "messageID": "4c2c60d1"
    }
    print("Your message status is: %s" % str(getStatus))

    return getStatus



if __name__ == "__main__":
    print ("UUID: " + create_uuid())

    # getLoginDets= generateAPIkey()
    # call_api_interface(getLoginDets, "cowrygong", "sms")

    #checkSMSBal = getBalance()
    #call_api_interface(checkSMSBal, "cowrygong", "getBalance")

    getSMSr=getRoutes()
    call_api_interface(getSMSr, "cowrygong", "getRoutes")

    #postSMS=postMessage()
    #call_api_interface(postSMS, "cowrygong", "postMessage")

    postBSMS=postBulkMessage()
    call_api_interface(postBSMS, "cowrygong", "postBulkMessage")

    # getStat=getMessageStatus()
    # call_api_interface(getStat, "cowrygong", "getMessageStatus")


