#!/bin/env python
import requests

payload={"msisdn":"233576226718",
         "amount":"0.1",
         "misika247_transaction_id":"3233120",
        # "narration":"Credit"
         "product_name":"Debit"

        }

#url = "http://cbs2p0:24766/cbs/tigocash/creditWallet/"
url = "http://cbs2p0:24766/cbs/tigocash/debitWallet/"
call_cbs = requests.post(url,json=payload,verify=False,timeout=60)
print(call_cbs.text)

#meSika --> 0576226718
# me --? 0278009427
# jnr --> 0271004649

#url = "https://api.misika247.com:24799/api/cowrycourier/withdrawFunds/"
#call_api = requests.post(url,json=payload,verify=False,timeout=60)
#print(call_api.text)

#{"msisdn":"233271004649",
 #        "amount":"0.1",
  #       "misika247_transaction_id":"3123120",
   #     # "narration":"Credit"
    #     "product_name":"Debit"
     #   }


#'api_key': '61b87502373649d09c01cffe9e1dcbd3',
#'service_provider_id': '3006bee1f78047e8811f536122e2877a',
#'source': 'api',
#'provider_id': '3',
#'payment_provider_id': '3',
#'account_number': '233278009427',
#'amount': 0.2,
#'currency': 'GHS',
#'narration': '',
#'transaction_id': '6578767',
#'notify_payer_after_processing': 1,
#'payer': 'Miriam Aidoo',
#'payer_msisdn': '0504169784',
#'payer_email': 'miriam.aidoomensah@misika247.com',
#'payer_address': '',
#'notify_recipient_on_success': 1,
#'recipient_name': 'Wendy Dua',
#'recipient_msisdn': '0200313710',
#'recipient_email': 'takyiwaa.dua@misika247.com',
#'recipient_address': '',
#'bank_refid': '6787687090'

#url = "https://api.misika247.com:24799/api/cowrycourier/depositFunds/"
#call_api = requests.post(url,json=payload,verify=False,timeout=60)
#print(call_api.text)


#debitFunds = {
 #   'api_key': '61b87502373649d09c01cffe9e1dcbd3',
  #  'api_secret': '',
   # 'service_provider_id': '3006bee1f78047e8811f536122e2877a',
    #'source': 'api',
    #'payment_provider_id': '3',
    #'account_number': '233278009427',
    #'amount': '0.5',
    #'currency': 'GHS',
    #'narration': '',
    #'transaction_id': '0809890',
    #'notify_payer_after_processing': 1,
    #'debit_requester': 'GH4HUB',
    #'account_holder_fullname': 'Wendy Dua',
    #'account_holder_msisdn': '0278009427',
    #'account_holder_email': 'takyiwaa.dua@misika247.com',
    #'notify_holder_on_success': 1,
    #'notification_source': 'GH4HUB',
#}
