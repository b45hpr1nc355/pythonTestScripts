'''
created from 8th December, 2016

Author t4ky1
'''

import time
import uuid

import requests

PROTOCOL = "https"
HOST = "api.misika247.com"  #sandbox.misika247.com
PORT = "24799"


def create_uuid():
    new_uuid = (str(uuid.uuid4())).replace('-', '')

    return new_uuid


def call_api_interface(api_payMerchant, module, func):
    print ("Payload: \n")
    print (api_payMerchant)
    print ("")

    URL = "%s://%s:%s/api/%s/%s/" % (PROTOCOL, HOST, PORT, module, func)

    print ("To call the api_interface, \nCall it using URL %s" %URL)

    req=requests.post(URL, json=api_payMerchant, verify=False)

    print ("Response from API CALL = %s: "% req.text)

    print ("%s: " %req.status_code)

    resp_dict = req.json()

    print ("Response from API CALL = %s: " %resp_dict)


#def generateAPIkey():
 #   getCreds= {
  #      'username': 'apiqa@misika247.com',
   #     'password': 'golpf340ev',
    #    'service_provider_id': '3006bee1f78047e8811f536122e2877a',
     #   'expiry': 1
    #}

    #print ("Bill payment credentials: %s" % str(getCreds)

    #return getCreds


def listMerchants():
    viewBillers= {
        'api_key': '61b87502373649d09c01cffe9e1dcbd3',
        #'api_secret': '3006bee1f78047e8811f536122e2877a',
        'service_provider_id': '3006bee1f78047e8811f536122e2877a',
        'source': 'api'
    }
    print ("List of Billers to be paid: %s" %str(viewBillers))

    return viewBillers


def listMerchantProducts():
    listProds= {
        'api_key': '61b87502373649d09c01cffe9e1dcbd3',
        #'api_secret': '3006bee1f78047e8811f536122e2877a',
        'service_provider_id': '3006bee1f78047e8811f536122e2877a',
        'source': 'api',
        'merchant_id': '3'
    }
    print ("Products for this Biller: %s" %str(listProds))

    return listProds


def checkProductBalance():
    checkBalance= {
        'api_key': '61b87502373649d09c01cffe9e1dcbd3',
        'api_secret': '3006bee1f78047e8811f536122e2877a',
        'source': 'api',
        'merchant_id': '3',
        'product_id': '3'
    }
    print ("Balance for this Biller: %s" %str(checkBalance))

    return checkBalance


def lookUpAccount():
    checkAccount= {
        'api_key': '61b87502373649d09c01cffe9e1dcbd3',
        'api_secret': '3006bee1f78047e8811f536122e2877a',
        'source': 'api',
        'merchant_id': '4',
        'account_number': '0231867346'
    }
    print ("Account for this Biller: %s" % str(checkAccount))

    return checkAccount


def payMerchant():
    payBiller= {
        'api_key': '61b87502373649d09c01cffe9e1dcbd3',
        'api_secret': '3006bee1f78047e8811f536122e2877a',
        'source': 'api',
        'merchant_id': '4',
        'product_id': '4',
        'amount': '1',
        'currency': 'GHS',
        'transaction_id': '43524353',
        'payer': 'Miriam Aidoo',
        'notify_payer_after_processing': 1,
        'payer_msisdn': '233504169784',
        'payer_email': 'wendy.dua@misika247.com',
        'notify_recepient_on_success': 1,
        'recepient_account':'233231867346',
        'recepient_name': 'Elikem',
        'recepient_msisdn': '0231867346',
        'recepient_email': 'elikem.kuadey@misika247.com'
    }
    print ("Transaction was successful for: %s" % str(payBiller))

    return payBiller


def getPaymentStatus():
    payStat = {
        'api_key': '61b87502373649d09c01cffe9e1dcbd3',
        'api_secret': '3006bee1f78047e8811f536122e2877a',
        'source': 'api',
        'misika247_refid': '08408402',
        'transaction_id': '03280823'
    }
    print ("The stataus of your transaction is: %s" %str(payStat))

    return payStat



if __name__ == "__main__":

    print ("UUID: "+ create_uuid())

    #getCreds= generateAPIkey()
    #call_api_interface(getCreds, "cowrypay", "generateAPIkey")

    viewBillers = listMerchants()
    call_api_interface(viewBillers, "cowrypay", "listMerchants")


    listProds = listMerchantProducts()
    call_api_interface(listProds, "cowrypay", "listMerchantProducts")


    checkBalance = checkProductBalance()
    call_api_interface(checkBalance, "cowrypay", "checkProductBalance")

    #checkAccount = lookUpAccount()
    #call_api_interface(checkAccount, "cowrypay", "lookupAccount")

    #payBiller = payMerchant()
    #call_api_interface(payBiller, "cowrypay", "payMerchant")


    # payStat = getPaymentStatus()
    # call_api_interface(payStat, "cowrypay", "getPaymentStatus") #

