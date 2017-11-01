#!/bin/env python
import requests

payload={"msisdn":"233548434029",
         "amount":"0.5",
         "misika247_transaction_id":"3123120",
	"narration":"Debit" }

#url = "http://cbs2p0:24766/cbs/mtncash/creditWallet/"
#url = "http://cbs2p0:24766/cbs/mtncash/debitWallet/"
url = "http://cbs.misika247.com:24766/cbs/mtncash/debitWallet/"
call_cbs = requests.post(url,json=payload,verify=False,timeout=60)
print(call_cbs.text)
