#!/bin/env python
import requests

payload={"msisdn":"233271004649",
         "amount":"0.1",
         "misika247_transaction_id":"3123120",
        # "narration":"Credit"
         "product_name":"Debit"
        }

url = "http://cbs2p0:24766/cbs/tigocash/creditWallet/"
#url = "http://cbs2p0:24766/cbs/tigocash/debitWallet/"
call_cbs = requests.post(url,json=payload,verify=False,timeout=60)
print(call_cbs.text)

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