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
HOST = "sandbox.misika247.com" # "api.misika247.com"
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
        "api_key": "bNm0YN3P0lTwTsNI6bHnkLbghK09jjrw7bmuGERG1fiqMgXkqPRdITAnsAI", # "61b87502373649d09c01cffe9e1dcbd3",
        "service_provider_id": "TYrDfyu1P7YPDXtE6uMFT3LRPKZU2kL7EmmsWI5jqg", # "3006bee1f78047e8811f536122e2877a",
        "source": "api"
    }
    print("Your SMS balance: %s" % str(checkSMSbal))

    return checkSMSbal


def getRoutes():
    getSMSroutes = {
        "api_key": "bNm0YN3P0lTwTsNI6bHnkLbghK09jjrw7bmuGERG1fiqMgXkqPRdITAnsAI", # "61b87502373649d09c01cffe9e1dcbd3",
        "service_provider_id": "TYrDfyu1P7YPDXtE6uMFT3LRPKZU2kL7EmmsWI5jqg", # "3006bee1f78047e8811f536122e2877a",
        "source": "api"
    }
    print("The configured SMS routes: %s" % str(getSMSroutes))
    return getSMSroutes


def postBulkMessage():
    postbulkSMS = {
        "api_key": "bNm0YN3P0lTwTsNI6bHnkLbghK09jjrw7bmuGERG1fiqMgXkqPRdITAnsAI", #"61b87502373649d09c01cffe9e1dcbd3",
        "service_provider_id": "TYrDfyu1P7YPDXtE6uMFT3LRPKZU2kL7EmmsWI5jqg", #"3006bee1f78047e8811f536122e2877a",
        "source": "api",
        "routeID": "297b53667470e24ca41a18c8105f6260", # "8f1df72288915292efcf456df43e5b20",
        "messages": [{"messageID": "4c2c60d1", "text": "Tests from Petra", "phonenumber": "233504169784"},
                     {"messageID": "d87801fe", "text": "Tests from Petra", "phonenumber": "233200313710"},
                     {"messageID": "d87801fe", "text": "Tests from Petra", "phonenumber": "233555055956"}],
        "senderID": "Petra",
        "messageType": "SMS",
        "callback": 1,
        "dlr-url": " ",
        "priority-level": "HIGH"
    }
    print("Your bulk message creds: %s" % str(postbulkSMS))

    return postbulkSMS


def postMessage():
    postMess = {
        "api_key": "bNm0YN3P0lTwTsNI6bHnkLbghK09jjrw7bmuGERG1fiqMgXkqPRdITAnsAI", #"61b87502373649d09c01cffe9e1dcbd3",
        #"api_secret":"TYrDfyu1P7YPDXtE6uMFT3LRPKZU2kL7EmmsWI5jqg",
        "service_provider_id": "TYrDfyu1P7YPDXtE6uMFT3LRPKZU2kL7EmmsWI5jqg",  #"3006bee1f78047e8811f536122e2877a",
        "client_id":"",
        "source": "api",
        "callback": 1,
        "routeID": "297b53667470e24ca41a18c8105f6260", # "8f1df72288915292efcf456df43e5b20",
        "text": "Petra Tests",
        "senderID": "Petra",
        "messageID": "4c2c60d1",
        "messageType": "SMS",
        "phonenumber": "233200313710",
        "priority-level": "HIGH"
    }
    print("Your SMS creds: %s" % str(postMess))

    return postMess


def getMessageStatus():
    getStatus = {
        "api_key": "bNm0YN3P0lTwTsNI6bHnkLbghK09jjrw7bmuGERG1fiqMgXkqPRdITAnsAI", # "61b87502373649d09c01cffe9e1dcbd3",
        "service_provider_id": "TYrDfyu1P7YPDXtE6uMFT3LRPKZU2kL7EmmsWI5jqg",  # "3006bee1f78047e8811f536122e2877a",
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

    #getSMSr=getRoutes()
    #call_api_interface(getSMSr, "cowrygong", "getRoutes")

    postSMS=postMessage()
    call_api_interface(postSMS, "cowrygong", "postMessage")

    postBSMS=postBulkMessage()
    call_api_interface(postBSMS, "cowrygong", "postBulkMessage")

    # getStat=getMessageStatus()
    # call_api_interface(getStat, "cowrygong", "getMessageStatus")


