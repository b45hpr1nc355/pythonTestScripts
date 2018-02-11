'''
created from 21st June, 2017

Author b45hpr1nc355
'''

import time
import uuid

import requests


PROTOCOL ="https"
HOST ="cbs2p0"
PORT ="24788"



def create_uuid():
    new_uuid = (str(uuid.uuid4())).replace('-', '')
    return new_uuid



def call_sr_interface(func_inst, cbs, func):
    print("Function Details: \n")
    print(func_inst)
    print(" ")

    URL = "%s://%s:%s/%s/beige/%s/" % (PROTOCOL, HOST, PORT, cbs, func)

    print(f"To call the cbs interface use {URL}")

    req=requests.post(URL, json=func_inst, verify=False)

    print(f"Response from API Call {req.text}")

    print (f"%s{req.status_code}")

    resp_dict=req.json()

    print (f"Response from API Call {resp_dict}")




def miniStatement():
    minStat={
        "account_number":"100002441987",
        "misika247_transaction_id":"1920921"
    }
    return minStat



def accountDetails():
    accDet={
        "account_number": "100002441987",
        "misika247_transaction_id": "misika247_103331"
    }
    return accDet


def agentCollection():
    agCol={
        "account_number": "100002441987",
        "misika247_transaction_id": "misika247_102221",
        "amount":"1",
        "agent_code":"0001"
    }
    return agCol


def vodafoneAirtimePurchase():
    airPur={
        "account_number": "100002441987",
        "msisdn":"233200313710",
        "misika247_transaction_id": "misika247_1013111",
        "amount":"1"
    }
    return airPur


def onBoardCustomer():
    onBCust={
        "misika247_transaction_id":"misika247_10992",
        "short_name":"",
        "name1":"Wendy Dua",
        "name2":"Wendy Dua",
        "date_of_birth":"19920112",
        "gender":"FEMALE",
        "account_officer":"1227",
        "other_officer":"NULL",
        "sector":"8000",
        "nationality":"GH",
        "customer_type":"ACTIVE",
        "residence_region":"GH01",
        "place_of_birth":"Accra",
        "mnemonic":"LAGIFF13113",
        "marital_status":"SINGLE",
        "industry":"1000",
        "residence":"GH",
        "language":"1",
        "address":"BOX 19999 ACCRA NORTH",
        "country":"GH",
        "sms1":"+233200313710",
        "legal_id":"830183018",
        "legal_doc_name":"VOTERS.CARD",
        "legal_holder_name":"Wendy Dua",
        "legal_iss_auth":"GHANA",
        "legal_iss_date":"20120402",
        "legal_exp_date":"",
        "employment_status":"SELF-EMPLOYED",
        "net_monthly_in":"1200",
        "contact_date":"20170628",
        "aml_check":"NULL",
        "aml_result":"NULL",
        "kyc_complete":"NULL",
        "account_type":"",
        "branch_code":"006"
    }
    return onBCust





if __name__ == '__main__':
    print (f"UUID: {create_uuid()}")

    minStat=miniStatement()
    call_sr_interface(minStat, "cbs", "miniStatement")



