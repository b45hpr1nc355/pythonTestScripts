#!/bin/env python
import requests

payload={"msisdn":"233278009427",
         "amount":"1.00",
         "misika247_transaction_id":"3123120",
         "narration":"Credit" }

url = "http://cbs2p0:24766/cbs/tigocash/creditWallet/"
call_cbs = requests.post(url,json=payload,verify=False,timeout=60)
print(call_cbs.text)