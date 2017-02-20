import requests
import sys

from datetime import datetime
from .PLAID_Constants import *
from .PLAID_User_Settings import *
from .getCredentials import *
from .plaidPaylods import *


def getFile(name, verb=False):
    newExt = \
        datetime.now().strftime('%Y%m%d%H%M%S') + \
        '.json'
    if verb:
        print(name)
        print(newExt)
    try:
        if verb:
            print(name)
            print(newExt)
        if '.txt' in name:
            name.replace(
                old='.txt',
                new=newExt
            )
        else:
            if '.json' in name:
                name.replace(
                    old='.json',
                    new=newExt
                )
            else:
                name = name + newExt
        if verb:
            print(name)
            print(newExt)
        data = open(name, 'w')
    except:
        print(sys.exc_info()[0])
        print('Error naming')
        name = 'stdout'
        data = sys.stdout
    return name, data


def getStream(idx):
    if(len(sys.argv) > idx):
        name = sys.argv[idx]
        name, data = getFile(name)
    else:
        name = 'stdout'
        data = sys.stdout
    return name, data


def evalResult(r: requests.Response, fs):
    print(
        r.request.method + '\n' +
        r.request.url + '\n' +
        r.request.body + '\n' +
        '%d' % r.status_code)
    if r.status_code == 200:
        print("Success\n")
        print(
            r.text,
            file=fs)
    else:
        print('failed!!\n')
        print(
            r.text,
            file=fs
        )


def runthis():
    fsName1, fsData1 = getStream(1)
    fsName2, fsData2 = getStream(2)
    fsName3, fsData3 = getStream(3)
    fsName4, fsData4 = getStream(4)

    print(
        'fs1: %s\nfs2: %s\nfs3: %s\nfs4: %s\n' %
        (
            fsName1,
            fsName2,
            fsName3,
            fsName4)
    )

    # Prepare Payloads to send
    r1 = requests.post(
        url=PLAID_URL_DEV + PLAID_END_CONNECT,
        data=payloadLoginTest
    )

    r2 = requests.delete(
        url=PLAID_URL_DEV + PLAID_END_CONNECT,
        data=payloadDel1
    )

    r3 = requests.delete(
        url=PLAID_URL_DEV + PLAID_END_CONNECT,
        data=payloadDel2
    )

    r4 = requests.delete(
        url=PLAID_URL_DEV + PLAID_END_CONNECT,
        data=payloadDel3
    )

    evalResult(r1, fsData1)
    evalResult(r2, fsData2)
    evalResult(r3, fsData3)
    evalResult(r4, fsData4)


def runGetChase(filename):
    fs, fsData = getFile(filename, True)

    print('File: %s' % fs)

    r = requests.post(
        url=PLAID_URL_DEV + PLAID_END_CONNECT,
        data=payloadLoginTest
    )
    evalResult(r, fsData)
    print(fs)

    if (fs != 'stdout'):
        print('return ok')
        return fs
    else:
        return None


if __name__ == '__main__':
    runthis()
