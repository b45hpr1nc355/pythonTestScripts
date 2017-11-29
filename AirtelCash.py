#!/bin/env python

import requests

payload={"msisdn":"233268951271",
         "amount":"1",
         "mno":"Airtel",
         "token":"",
         "narration":"Credit",
         "misika247_transaction_id":"00009",
         "trxid":"00008"
        }

#url = "http://cbs2p0:24766/cbs/nsano/creditWallet/"
url = "http://cbs2p0:24766/cbs/nsano/debitWallet/"
call_cbs = requests.post(url,json=payload,verify=False,timeout=60)
print(call_cbs.text)

#meSika --> 233268951271
#CEO --> 0561077767
