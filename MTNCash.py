#!/bin/env python
import requests

payload={"msisdn":"233548434029",
         "amount":"0.2",
         "misika247_transaction_id":"313228",
	 "narration":"Credit" }

url = "http://cbs2p0:24766/cbs/mtncash/creditWallet/"
#url = "http://cbs2p0:24766/cbs/mtncash/debitWallet/"
#url = "http://cbs.misika247.com:24766/cbs/mtncash/debitWallet/"
call_cbs = requests.post(url,json=payload,verify=False,timeout=60)
print(call_cbs.text)
#Mike ----> 233241979323
#Hester ---> 0545396737
#meSika ---> 0557826718
#Edna ---> 233548434029
