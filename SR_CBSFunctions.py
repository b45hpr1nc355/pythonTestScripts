'''
created from 2nd January, 2017

Author t4ky1
'''

import time
import uuid

import requests
import urllib3

urllib3.disable_warnings()

http = urllib3.PoolManager(
    cert_reqs='CERT_REQUIRED',
    ca_certs='/path/to/your/certificate_bundle')

PROTOCOL = "https"
HOST = "sr.misika247.com"
PORT = "36500"


def create_uuid():
    new_uuid = (str(uuid.uuid4())).replace('-', '')

    return new_uuid


def call_sr_interface(sr_cbs, module, func):
    print("SignUp: \n")
    print(sr_cbs)
    print(" ")

    URL = "%s://%s:%s/sr/%s/bulkpayment/%s/" % (PROTOCOL, HOST, PORT, module, func)

    print("To call the sr_interface, \nCall it using URL %s" % URL)

    req = requests.post(URL, json=sr_cbs, verify=False)

    print("Response from SR call= %s" % req.text)

    print(" %s:" % req.status_code)

    resp_dict = req.json()

    print("Response from SR call= %s" % resp_dict)


def getCBSConfigs():
    getCBSConfs = {
        "access_key": "f002fc4bd99527797f40b4678c4d7386a549c3f9f86de9bfaccaa175760a8759",
        "client_uuid": "2f42de8a806a5ae7bec74c680e9143443099805d9e23d1597b68ea6751c5ed43",
        "provider_id": "6610bac9341ac398f615a19389244ca1a8ef89008f4a7b593b6c3043ad9a5575"
    }
    return getCBSConfs


def balanceEnquiry():
    balEnq = {
        "access_key": "GU8Vptr3x9dPrZyW04llJbVPSfMGjg9P48ZHaZEGim1chtNBqpkhjtEhA",
        "client_uuid": "QkVQ3KuQVFWSEtPcdMIsBJhGAXJeb4qJ2RJMITC97O9Iu1xNsrIm7ZE",
        "provider_id": "6610bac9341ac398f615a19389244ca1a8ef89008f4a7b593b6c3043ad9a5575",
        "account_number": "1081070122148701",
        "transaction_id": "12345678"
    }
    return balEnq


def dbBalanceEnquiry():
    dbBalEnq = {
        "access_key": "GU8Vptr3x9dPrZyW04llJbVPSfMGjg9P48ZHaZEGim1chtNBqpkhjtEhA",
        "client_uuid": "QkVQ3KuQVFWSEtPcdMIsBJhGAXJeb4qJ2RJMITC97O9Iu1xNsrIm7ZE",
        "provider_id": "6610bac9341ac398f615a19389244ca1a8ef89008f4a7b593b6c3043ad9a5575",
        "account_number": "1081070126332401",
        "transaction_id": "12345678"
    }
    return dbBalEnq


def accountEnquiry():
    accEnq = {
        "access_key": "f002fc4bd99527797f40b4678c4d7386a549c3f9f86de9bfaccaa175760a8759",
        "client_uuid": "2f42de8a806a5ae7bec74c680e9143443099805d9e23d1597b68ea6751c5ed43",
        "provider_id": "6610bac9341ac398f615a19389244ca1a8ef89008f4a7b593b6c3043ad9a5575",
        "is_signup_request": False,
        "account_number": "1161030010405601",
        "transaction_id": "12345678"
    }
    return accEnq


def fundsTransfer():
    fundsT = {
        "access_key": "f002fc4bd99527797f40b4678c4d7386a549c3f9f86de9bfaccaa175760a8759",
        "client_uuid": "2f42de8a806a5ae7bec74c680e9143443099805d9e23d1597b68ea6751c5ed43",
        "provider_id": "6610bac9341ac398f615a19389244ca1a8ef89008f4a7b593b6c3043ad9a5575",
        "debit_account": "1081070118235201",
        "credit_account": "1081070126332401",
        "amount": "1.00",
        "narration": "Test",
        "transaction_id": "12345678",
        # "bank_properties":
        "productcode": "GBPT"
    }
    return fundsT


def verifyAccountNumber():
    verifyANum = {
        "access_key": "f002fc4bd99527797f40b4678c4d7386a549c3f9f86de9bfaccaa175760a8759",
        "client_uuid": "2f42de8a806a5ae7bec74c680e9143443099805d9e23d1597b68ea6751c5ed43",
        "provider_id": "6610bac9341ac398f615a19389244ca1a8ef89008f4a7b593b6c3043ad9a5575",
        "account_number": "1081070118235201",
        "transaction_id": "12345678"
    }
    return verifyANum


def forex():
    forx = {
        "access_key": "f002fc4bd99527797f40b4678c4d7386a549c3f9f86de9bfaccaa175760a8759",
        "client_uuid": "2f42de8a806a5ae7bec74c680e9143443099805d9e23d1597b68ea6751c5ed43",
        "provider_id": "6610bac9341ac398f615a19389244ca1a8ef89008f4a7b593b6c3043ad9a5575",
        "currency": "USD",
        "transaction_id": "12345678"
    }
    return forx


def checkAccountNumber():
    checkAccNum = {
        "access_key": "f002fc4bd99527797f40b4678c4d7386a549c3f9f86de9bfaccaa175760a8759",
        "client_uuid": "2f42de8a806a5ae7bec74c680e9143443099805d9e23d1597b68ea6751c5ed43",
        "provider_id": "6610bac9341ac398f615a19389244ca1a8ef89008f4a7b593b6c3043ad9a5575",
        "account_number": "1081070126332401",
        "transaction_id": "12345678"
    }
    return checkAccNum


def accountStatement():
    accState = {
        "access_key": "f002fc4bd99527797f40b4678c4d7386a549c3f9f86de9bfaccaa175760a8759",
        "client_uuid": "2f42de8a806a5ae7bec74c680e9143443099805d9e23d1597b68ea6751c5ed43",
        "provider_id": "6610bac9341ac398f615a19389244ca1a8ef89008f4a7b593b6c3043ad9a5575",
        "account_number": "1081070118235201",
        "transaction_id": "12345678",
        "start_date": "",
        "end_date": ""
    }
    return accState


def validateTransfer():
    validateT = {
        "access_key": "f002fc4bd99527797f40b4678c4d7386a549c3f9f86de9bfaccaa175760a8759",
        "client_uuid": "2f42de8a806a5ae7bec74c680e9143443099805d9e23d1597b68ea6751c5ed43",
        "provider_id": "6610bac9341ac398f615a19389244ca1a8ef89008f4a7b593b6c3043ad9a5575",
        "transaction_id": "12345678",
        "bank_properties": {}
    }
    return validateT


def debitWallet():
    debitWal = {
        "access_key": "f002fc4bd99527797f40b4678c4d7386a549c3f9f86de9bfaccaa175760a8759",
        "client_id": "2f42de8a806a5ae7bec74c680e9143443099805d9e23d1597b68ea6751c5ed43",
        "provider_id": "6610bac9341ac398f615a19389244ca1a8ef89008f4a7b593b6c3043ad9a5575",
        "provider_route_id": "",
        "provider_properties": {"product_code": "GBPT"},
        "debit_account_number": "",
        "credit_account_number": "",
        "amount": "1.00",
        "narration": "Test",
        "transaction_id": "12345678",
        "notify_receiver": 0,
        "notify_sender": 0,
        "receiver_details": {"email": "wendy.dua@misika247.com", "msisdn": "0200313710"},
        "sender_details": {"email": "elikem.kuadey@misika247.com", "msisdn": "0208365428"},
    }
    return debitWal


def creditWallet():
    creditWal = {
        "access_key": "f002fc4bd99527797f40b4678c4d7386a549c3f9f86de9bfaccaa175760a8759",
        "client_id": "2f42de8a806a5ae7bec74c680e9143443099805d9e23d1597b68ea6751c5ed43",
        "provider_id": "6610bac9341ac398f615a19389244ca1a8ef89008f4a7b593b6c3043ad9a5575",
        "provider_route_id": "",
        "provider_properties": {"product_code": "GBPT"},
        "debit_account_number": "",
        "credit_account_number": "",
        "amount": "1.00",
        "narration": "Test",
        "transaction_id": "12345678",
        "notify_receiver": 0,
        "notify_sender": 0,
        "receiver_details": {"email": "wendy.dua@misika247.com", "msisdn": "0200313710"},
        "sender_details": {"email": "elikem.kuadey@misika247.com", "msisdn": "0208365428"},
    }
    return creditWal


def bankWalletBalance():
    bankWalBal = {
        "access_key": "f002fc4bd99527797f40b4678c4d7386a549c3f9f86de9bfaccaa175760a8759",
        "client_uuid": "2f42de8a806a5ae7bec74c680e9143443099805d9e23d1597b68ea6751c5ed43",
        "provider_id": "6610bac9341ac398f615a19389244ca1a8ef89008f4a7b593b6c3043ad9a5575",
        "transaction_id": "12345678",
        "bank_properties": {}
    }
    return bankWalBal


def providerWalletBalance():
    providerWalBal = {
        "access_key": "f002fc4bd99527797f40b4678c4d7386a549c3f9f86de9bfaccaa175760a8759",
        "client_uuid": "2f42de8a806a5ae7bec74c680e9143443099805d9e23d1597b68ea6751c5ed43",
        "provider_id": "6610bac9341ac398f615a19389244ca1a8ef89008f4a7b593b6c3043ad9a5575",
        "transaction_id": "12345678",
        "bank_properties": {}
    }
    return providerWalBal


# BEIGE FUNCTIONS
def miniStatement():
    minSta = {
        "access_key": "bfba4f8f392fc501d2eca028f3900df1802d0ada982f2f6fe8039e01b3b984a5",
        "client_uuid": "e7ea135abe23d14b8e768aee0735474515ffb547a9d5d0a3596d824135c13292",
        "provider_id": "b4ac717d34174eac936b9d013945da8b",
        "account_number": "100002441987",  # "021129682141",
        "misika247_transaction_id": "105521661"
    }
    return minSta


def accountDetails():
    accDet = {
        "access_key": "bfba4f8f392fc501d2eca028f3900df1802d0ada982f2f6fe8039e01b3b984a5",
        "client_uuid": "e7ea135abe23d14b8e768aee0735474515ffb547a9d5d0a3596d824135c13292",
        "provider_id": "b4ac717d34174eac936b9d013945da8b",
        "account_number": "100000650298",
        "misika247_transaction_id": "1062211661"
    }
    return accDet


def verifyAccount():
    vefAcc = {
        "access_key": "bfba4f8f392fc501d2eca028f3900df1802d0ada982f2f6fe8039e01b3b984a5",
        "client_uuid": "e7ea135abe23d14b8e768aee0735474515ffb547a9d5d0a3596d824135c13292",
        "provider_id": "b4ac717d34174eac936b9d013945da8b",
        "account_number": "0041453794061",
        "misika247_transaction_id": "1062211661"
    }
    return vefAcc


def onboardCustomer():
    onBCust = {
        "misika247_transaction_id": "5252111",
        "short_name": "YD",
        "name1": "Yaw",
        "name2": "Dua",
        "date_of_birth": "19520911",
        "gender": "MALE",
        "account_officer": "1224",
        "other_officer": "",
        "sector": "9000",
        "nationality": "GH",
        "customer_type": "ACTIVE",
        "residence_region": "GH01",
        "place_of_birth": "Dwinase",
        "mnemonic": "YA5DU3",
        "marital_status": "MARRIED",
        "industry": "8070",
        "residence": "GH",
        "language": "1",
        "address": "Dome North Accra",
        "country": "GH",
        "sms1": "233271004649",
        "legal_id": "2546713656",
        "legal_doc_name": "",
        "legal_holder_name": "Justin Dy",
        "legal_iss_auth": "GHANA",
        "legal_iss_date": "20161009",
        "legal_exp_date": "201891113",
        "employment_status": "EMPLOYED",
        "net_monthly_in": "7000",
        "contact_date": "20170625",
        "aml_check": "",
        "aml_result": "",
        "kyc_complete": "",
        "account_type": "6511",
        "branch_code": "090",
        "target": "1",
        "street": "DOME, ACCRA",
        "customer_status": "1"
    }
    return onBCust


def agentCollection():
    agCol = {
        "account_number": "0301453754121",
        "amount": "10",
        "misika247_transaction_id": "22120",
        "agent_code": "1224"
    }
    return agCol


def getTransferReceivingBanks():
    getTRB= {
    }



if __name__ == "__main__":
    print("UUID: " + create_uuid())

    #getTRB= getTransferReceivingBanks()
    #call_sr_interface(getTRB, "cowrycourier", "getTransferReceivingBanks")
    

    #getCBSConfs=getCBSConfigs()
    #call_sr_interface(getCBSConfs, "cowrycourier", "getCBSConfigs")

    balEnq=balanceEnquiry()
    call_sr_interface(balEnq, "cowrycourier", "BalanceEnquiry")

    # dbBalEnq = dbBalanceEnquiry()
    # call_sr_interface(dbBalEnq, "cowrycourier", "DBBalanceEnquiry")

    # accEnq=accountEnquiry()
    # call_sr_interface(accEnq, "cowrycourier", "AccountEnquiry")

    # fundsT=fundsTransfer()
    # call_sr_interface(fundsT, "cowrycourier", "FundsTransfer")

    # verifyANum=verifyAccountNumber()
    # call_sr_interface(verifyANum, "cowrycourier", "VerifyAccountNumber")

    # forx=forex()
    # call_sr_interface(forx, "cowrycourier", "Forex")

    # checkAccNum=checkAccountNumber()
    # call_sr_interface(checkAccNum, "cowrycourier", "CheckAccountNumber")

    # accState=accountStatement()
    # call_sr_interface(accState, "cowrycourier", "AccountStatement")

    # validateT=validateTransfer()
    # call_sr_interface(validateT, "cowrycourier", "ValidateTransfer")

    # debitWal=debitWallet()
    # call_sr_interface(debitWal, "cowrycourier", "DebitWallet")

    # creditWal=creditWallet()
    # call_sr_interface(creditWal, "cowrycourier", "CreditWallet")

    # bankWalbal=bankWalletBalance()
    # call_sr_interface(bankWalbal, "cowrycourier", "BankWalletBalance")

    # providerWalBal=providerWalletBalance()
    # call_sr_interface(providerWalBal, "cowrycourier", "ProviderWalletBalance")



    # minSta=miniStatement()
    # call_sr_interface(minSta, "cowrycourier", "MiniStatement")

    #accDet = accountDetails()
    #call_sr_interface(accDet, "cowrycourier", "AccountDetails")

    vefAcc = verifyAccount()
    call_sr_interface(vefAcc, "cowrycourier", "VerifyAccount")

    # onBSuct = onboardCustomer()
    # call_sr_interface(onBSuct, "cowrycourier", "OnboardCustomer")

    #agCol = agentCollection()
    #call_sr_interface(agCol, "cowrycourier", "AgentCollection")
