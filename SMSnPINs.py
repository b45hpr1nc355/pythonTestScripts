'''
created from 1st August, 2017

Author b45hpr1nc355
'''
import csv
import uuid

import requests


PROTOCOL = "https"
HOST = "api.misika247.com"
PORT = "24799"



def create_uuid():
    new_uuid=(str(uuid.uuid4())).replace('-', '')

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





file="/tmp/new_pins_20.csv"

readfile= open(file)

msgs=[]

holdData= csv.reader(readfile, delimiter=",")

for i in holdData:
    try:
        if i[0]=="firstname":
            continue

            #print(i)

        fname=i[0]
        msisdn=i[5]
        pin=i[7]

        msgSMS="Hello %s, Your ADB Mobile Banking(*767#)  One Time Pin Is: %s.Please dial now to set a new pin." %(fname,pin)

        indmsg={"messageID":create_uuid(),"text":msgSMS,"phonenumber":msisdn}

        #print(msgSMS)

        msgs.append(indmsg)
    except:
        continue

#print(msgs)



if __name__=="__main__":

    print("UUID: " + create_uuid())

    #print(msgs)

    api_postSMS = {
        "api_key": "61b87502373649d09c01cffe9e1dcbd3",
        "service_provider_id": "3006bee1f78047e8811f536122e2877a",
        "source": "api",
        "callback": 1,
        "routeID": "8f1df72288915292efcf456df43e5b20",
        "messages": msgs,
        "senderID": "ADB",
        "messageType": "SMS",
        "priority-level": "HIGH"
    }

    call_api_interface(api_postSMS, "cowrygong", "postBulkMessage")
