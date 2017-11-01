#!/bin/env python
import requests

payload={"msisdn":"233278009427",
         "amount":"1.00",
         "misika247_transaction_id":"3123120",
        # "narration":"Credit"
         "product_name":"Debit"
        }

#url = "http://cbs2p0:24766/cbs/tigocash/creditWallet/"
url = "http://cbs2p0:24766/cbs/tigocash/debitWallet/"
call_cbs = requests.post(url,json=payload,verify=False,timeout=60)
print(call_cbs.text)
