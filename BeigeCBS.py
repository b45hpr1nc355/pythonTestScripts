import requests

payload = {"account_number": "0301453754121",
           "amount": "10",
           "misika247_transaction_id": "1922121",
          }

url = "http://cbs2p0:24788/cbs/beige/vodafoneToBankTransfer/"
call_cbs = requests.post(url, json=payload, verify=False, timeout=60)

print(call_cbs.text)

#payload={  "transaction_id":"3365222",
#           "account_number":"0441453807011",
 #          "account_type":"6511",
  #         "branch_code":"044",
   #        "account_officer":"1784",
    #       "other_officer":"NULL"
     #   }url = "http://cbs2p0:24788/cbs/beige/customerAccountOpening/"


#payload={ "account_number": "0301453754121",
   #         "amount": "10",
  #          "misika247_transaction_id": "22120",
 #           "agent_code": "1224"
#        }#url = "http://cbs2p0:24788/cbs/beige/agentCollection/"


#payload = { "misika247_transaction_id":"365221",
 #          "account_number":"0301453777111"
#          }
#url = "http://cbs2p0:24788/cbs/beige/miniStatement/"
#url = "http://cbs2p0:24788/cbs/beige/accountDetails/"
#url = "http://cbs2p0:24788/cbs/beige/verifyAccount/"
#url = "http://cbs2p0:24788/cbs/beige/getPhoneNumber/"
#url = "http://cbs2p0:24788/cbs/beige/vodafoneToBankTransfer/"


