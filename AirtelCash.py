#!/bin/env python

import requests

payload={"msisdn":"233561077767",
         "amount":"0.1",
         "mno":"Airtel",
         "token":"" }

#url = "http://cbs2p0:24766/cbs/mtncash/creditWallet/"
url = "http://cbs2p0:24766/cbs/nsano/debitWallet/"
call_cbs = requests.post(url,json=payload,verify=False,timeout=60)
print(call_cbs.text)

