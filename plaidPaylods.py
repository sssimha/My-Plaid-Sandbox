from .PLAID_Constants import *
from .PLAID_User_Settings import *


chaseInstType = 'chase'

atChase = ''

at1 = ''

at2 = ''

at3 = ''

atChase = ''

payloadChaseLogin = {
    Pr_cid: PLAID_KEYS_CLIENT_ID,
    Pr_sec: PLAID_KEYS_SECRET,
    Pr_uname: 'sssimha86',
    Pr_pwd: 'Hebbar86',
    Pr_type: chaseInstType
}

payloadLoginTest = {
    Pr_cid: PLAID_KEYS_TEST_CLIENT_ID,
    Pr_sec: PLAID_KEYS_TEST_SECRET,
    Pr_uname: PLAID_TEST_Username,
    Pr_pwd: PLAID_TEST_Password,
    Pr_type: PLAID_TEST_Wells
}

payloadChaseSairam = {
    Pr_cid: PLAID_KEYS_CLIENT_ID,
    Pr_sec: PLAID_KEYS_SECRET,
    Pr_uname: 'sssimha86',
    Pr_pwd: 'Hebbar86',
    Pr_type: PLAID_TEST_Wells
}

payloadGetAllInst = {
    Pr_cid: PLAID_KEYS_CLIENT_ID,
    Pr_sec: PLAID_KEYS_SECRET,
    Pr_cnt: 250,
    Pr_ofst: 0
}

payloadDel1 = {
    Pr_cid: PLAID_KEYS_CLIENT_ID,
    Pr_sec: PLAID_KEYS_SECRET,
    Pr_at: at1
}

payloadDel2 = {
    Pr_cid: PLAID_KEYS_CLIENT_ID,
    Pr_sec: PLAID_KEYS_SECRET,
    Pr_at: at2
}

payloadDel3 = {
    Pr_cid: PLAID_KEYS_CLIENT_ID,
    Pr_sec: PLAID_KEYS_SECRET,
    Pr_at: atChase
}
