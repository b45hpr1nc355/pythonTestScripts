#!/bin/env python

import requests

payload={"msisdn":"233561077767",
         "amount":"0.2",
         "mno":"Airtel",
         "token":""
         }         

url = "http://cbs2p0:24766/cbs/nsano_test/creditWallet/"
#url = "http://cbs2p0:24766/cbs/nsano/debitWallet/"
call_cbs = requests.post(url,json=payload,verify=False,timeout=60)
print(call_cbs.text)

#meSika --> 233268951271
#CEO --> 0561077767




#"msisdn":"233268951271",
        # "amount":"1",
        # "mno":"Airtel",
        # "token":"",
        # "narration":"Credit",
        # "misika247_transaction_id":"00019",
        # "trxid":"00007"
