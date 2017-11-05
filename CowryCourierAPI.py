'''
created from 14th December, 2016

Author t4ky1
'''

import time
import uuid

import requests

import urllib3

urllib3.disable_warnings()

http = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED',
    ca_certs='/path/to/your/certificate_bundle')


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
        'api_secret': '3006bee1f78047e8811f536122e2877a',
        'source': 'api',
        'payment_provider_id': '4'
    }
    #print "Your available balance is: %s" %str(checkWalbal)

    return checkWalbal


def checkAccountBalance():
    custAccBal= {
        'api_key': '61b87502373649d09c01cffe9e1dcbd3',
        'api_secret': '3006bee1f78047e8811f536122e2877a',
        'source': 'api',
        'provider_id': '4',
        'account_number':'0200313710'
    }
    return custAccBal


def accountLookup():
    accLook= {
        'api_key': '61b87502373649d09c01cffe9e1dcbd3',
        'api_secret': '3006bee1f78047e8811f536122e2877a',
        'source': 'api',
        'provider_id': '4',
        'account_number': '0200313710'
    }
    return accLook



def depositFunds():
    depFunds= {
        'api_key': '61b87502373649d09c01cffe9e1dcbd3',
        'service_provider_id': '3006bee1f78047e8811f536122e2877a',
        'source': 'api',
        'provider_id':'3',
        'payment_provider_id':'3',
        'account_number': '233271004649',
        'amount': 0.2,
        'currency': 'GHS',
        'narration':'',
        'transaction_id': '6578767',
        'notify_payer_after_processing': 1,
        'payer': 'Miriam Aidoo',
        'payer_msisdn': '0504169784',
        'payer_email': 'miriam.aidoomensah@misika247.com',
        'payer_address': '',
        'notify_recipient_on_success': 1,
        'recipient_name': 'Wendy Dua',
        'recipient_msisdn': '0200313710',
        'recipient_email': 'takyiwaa.dua@misika247.com',
        'recipient_address':'',
        'bank_refid':'6787687090'
    }
    #print "Amount sent: %s" %str(depFunds)

    return depFunds


def withdrawFunds():
    debitFunds= {
        'api_key': '61b87502373649d09c01cffe9e1dcbd3',
        'api_secret': '',
        'service_provider_id': '3006bee1f78047e8811f536122e2877a',
        'source': 'api',
        'payment_provider_id': '4',
        'account_number': '233200313710',
        'amount': '0.5',
        'currency': 'GHS',
        'narration':'',
        'transaction_id': '17872',
        'notify_payer_after_processing': 1,
        'debit_requester': 'GH4HUB',
        'account_holder_fullname':'',
        'account_holder_msisdn': '0200313710',
        'account_holder_email': 'takyiwaa.dua@misika247.com',
        'notify_holder_on_success': 1,
        'notification_source': 'GH4HUB',
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

    custAccBal=checkAccountBalance()
    call_api_interface(custAccBal, "cowrycourier", "checkAccountBalance")

    accLook=accountLookup()
    call_api_interface(accLook, "cowrycourier", "accountLookup")

    depFunds=depositFunds()
    call_api_interface(depFunds, "cowrycourier", "depositFunds")

    


