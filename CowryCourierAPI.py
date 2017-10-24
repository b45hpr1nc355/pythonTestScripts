'''
created from 14th December, 2016

Author t4ky1
'''

import time
import uuid

import requests


PROTOCOL ="https"
HOST ="api.misika247.com"
PORT ="24799"



def create_uuid():
    new_uuid=(str(uuid.uuid4())).replace('-', '')

    return new_uuid


def call_api_interface(api_sendMoney, module, func):
    print ("Money Sent: \n")
    print (api_sendMoney)
    print (" ")

    URL= "%s://%s:%s/api/%s/%s/" % (PROTOCOL, HOST, PORT, module, func)

    print ("To call the api_interface, \nCall it using URL %s" % URL)

    req=requests.post(URL, json=api_sendMoney, verify=False)

    print("Response from API call= %s" %req.text)

    print(" %s:" % req.status_code)

    resp_dict= req.json()

    print("Response from API call= %s" %resp_dict)




#def generateAPIkey():
#    getLoginDets= {
 #       'username': 'apiqa@misika247.com',
  #      'password': 'golpf340ev',
   #     'service_provider_id': '3006bee1f78047e8811f536122e2877a',
    #    'expiry': 1
   # }
    #print "Your credentials: %s" %str(getLoginDets)

    #return getLoginDets



def listProviders():
    listProvs= {
        'api_key': '61b87502373649d09c01cffe9e1dcbd3',
        'service_provider_id': '3006bee1f78047e8811f536122e2877a',
        'source': 'api'
    }
    print("List of Providers: %s" %str(listProvs))

    return listProvs


def checkWalletBalance():
    checkWalbal= {
        'api_key': '61b87502373649d09c01cffe9e1dcbd3',
        'service_provider_id': '3006bee1f78047e8811f536122e2877a',
        'source': 'api',
        'payment_provider_id': '4'
    }
    #print "Your available balance is: %s" %str(checkWalbal)

    return checkWalbal


def customerAccountBalance():
    custAccBal= {
        'api_key': '61b87502373649d09c01cffe9e1dcbd3',
        'api_secret': '3006bee1f78047e8811f536122e2877a',
        'source': 'api',
        'payment_provider_id': '4',
        'account_number':'0200313710'
    }

def depositFunds():
    depFunds= {
        'api_key': '61b87502373649d09c01cffe9e1dcbd3',
        'service_provider_id': '3006bee1f78047e8811f536122e2877a',
        'source': 'api',
        'provider_id': '2',
        'account_number': '233561077767',
        'amnt': 1,
        'currency': 'GHS',
        'transaction_id': 'xxxxx',
        'notify_payer_after_processing': 1,
        'payer': 'Miriam Aidoo',
        'payer_msisdn': '233561077767',
        'payer_email': 'miriam.aidoomensah@misika247.com',
        'notify_recipient_on_success': 1,
        'recipient_name': 'Wendy Dua',
        'recipient_msisdn': '233200313710',
        'recipient_email': 'wendy.dua@misika247.com'
    }
    #print "Amount sent: %s" %str(depFunds)

    return depFunds


def withdrawFunds():
    debitFunds= {
        'api_key': '',
        'service_provider_id': 'xxxx',
        'source': 'api',
        'provider_id': '0001',
        'account_number': '233555555555',
        'amount': '1',
        'currency': 'GHS',
        'transaction_id': 'xxxxx',
        'notify_payer_after_processing': 1,
        'payer': 'Wendy Dua',
        'payer_msisdn': 'xxxxx',
        'payer_email': 'xxxxx',
        'notify_recipient_on_success': 1,
        'recipient_name': 'Baby Doe',
        'recipient_msisdn': 'xxxx',
        'recipient_email': 'name@somedomain.com'
    }
    #print "Amount received: %s" %str(debitFunds)

    return debitFunds


def getTransactionStatus():
    getStat= {
        'api_key': '',
        'source': 'api',
        'misika247_refid': 'xxxxxxxx',
        'transaction_id': 'xxxxxx'
    }
    #print "Your transaction status: %s" %str(getStat)

    return getStat



if __name__=='__main__':
    print ("UUID: "+ create_uuid())

    #getLoginDets=generateAPIkey()
    #call_api_interface(getLoginDets, "cowrycourier", "generateAPIkey")

    listProvs=listProviders()
    call_api_interface(listProvs, "cowrycourier", "listProviders")

    checkWalbal=checkWalletBalance()
    call_api_interface(checkWalbal, "cowrycourier", "checkWalletBalance")

    custAccBal=customerAccountBalance()
    call_api_interface(custAccBal, "cowrycourier", "customerAccountBalance")

    #depFunds=depositFunds()
    #call_api_interface(depFunds, "cowrycourier", "depositFunds")

    


