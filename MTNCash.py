#!/bin/env python
import requests

payload={"msisdn":"233540119480",
         "amount":"100",
         "misika247_transaction_id":"3123120",
         "narration":"Credit" }

url = "http://cbs2p0:24766/cbs/mtncash/creditWallet/"
call_cbs = requests.post(url,json=payload,verify=False,timeout=60)
print(call_cbs.text)
