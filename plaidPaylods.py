from .PLAID_Constants import *
from .PLAID_User_Settings import *


chaseInstType = 'chase'

atChase = ''

at1 = '23c6ff7515b9656c0a9d3d4a52caebf6ca9cdac49' +\
    '89df2f48127ecfb0334d78a7dcbeae5feb6e30205' +\
    '676e0a449216a639602714d095a3a3e121a1d6c30' +\
    'b5fc0b39460c0c559d352a799443b6b138860'

at2 = '23c6ff7515b9656c0a9d3d4a52caebf6ca9cdac49' +\
    '89df2f48127ecfb0334d78a7dcbeae5feb6e30205' +\
    '676e0a449216a60e465b77bcb981818cc9a61f32c' +\
    'bf28750ee600a9f3cd98c24f8efd0ef86388a'

at3 = '23c6ff7515b9656c0a9d3d4a52caebf6ca9cdac49' +\
    '89df2f48127ecfb0334d78a7dcbeae5feb6e30205' +\
    '676e0a449216a6d448d3a5ac8ebfcd664e849d30d' +\
    '6c3a926ba9016c768cd92263c9a85c0586f40'

atChase = '23c6ff7515b9656c0a9d3d4a52caebf6ca9cdac49' +\
    '89df2f48127ecfb0334d78a7dcbeae5feb6e30205' +\
    '676e0a449216a608a11dc6b102561fa092fbc48b3' +\
    '03d12b118ee8cf3160ad28dec17617fae9061'

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
    Pr_at: at3
}
