#!/bin/env python
import requests

payload={"msisdn":"233200313710",
         "amount":"0.01",
         "misika247_transaction_id":"320120",
         "product_name":"Debit", 
         "voucher_code":"671291"
 
     }

#url = "http://cbs2p0:24766/vodafonecash/creditWallet/"
url = "https://cbs1.misika247.com:44766/cbs/vodafonecash/debitWallet/"
call_cbs = requests.post(url,json=payload,verify=False,timeout=60)
print(call_cbs.text)

#url = "https://api.misika247.com:24799/api/cowrycourier/depositFunds/"
#call_api = requests.post(url,json=payload,verify=False,timeout=60)
#print(call_api.text)

	
#{"msisdn":"233200313710",
 #        "amount":"1.00",
  #       "misika247_transaction_id":"320120",
   #      "product_name":"Credit" }
   #      "voucher_code":""

#"api_key":"61b87502373649d09c01cffe9e1dcbd3",
 #        "service_provider_id":"3006bee1f78047e8811f536122e2877a",
  #       "source":"api",
   #      "provider_id":"4",
    #     "payment_provider_id": "4",
     #    "account_number":"233200313710",
      #   "amount":0.1,
       #  "currency":"GHS",
        # "narration":"",
        # "transaction_id":"3135668",
        # "notify_payer_after_processing":1,
        # "payer":"John Doe",
        # "payer_msisdn":"0504169784",
        # "payer_email":"miriam.aidoomensah@misika247.com",
        # "payer_address":"",
        # "notify_recipient_on_success":1,
        # "recipient_name":"Baby Doe",
        # "recipient_msisdn":"0200313710",
        # "recipient_email":"takyiwaa.dua@misika247.com",
        # "recipient_address":"",
        # "bank_refid": "214566856"

