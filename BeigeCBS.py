import requests

payload = { "account_number": "0301453754121",
            "amount": "10",
            "misika247_transaction_id": "22120",
            "agent_code": "1224"
          }

url = "http://cbs2p0:24788/cbs/beige/agentCollection/"
call_cbs = requests.post(url, json=payload, verify=False, timeout=60)

print(call_cbs.text)

#payload={  "transaction_id":"3365222",
#           "account_number":"0441453807011",
 #          "account_type":"6511",
  #         "branch_code":"044",
   #        "account_officer":"1784",
    #       "other_officer":"NULL"
     #   }




