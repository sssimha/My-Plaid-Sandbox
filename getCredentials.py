from getpass import getpass


def getUNPwd():
    un = input("Enter Username: ")
    pw = getpass(prompt="Enter Password: ")
    return un, pw


def getInitUNPwd():
    un = input("Enter Username: ")
    p1, p2 = pPrompt()

    while p1 != p2:
        print('Passwords did not match. Please try again.')
        p1, p2 = pPrompt()
    return un, p1


def pPrompt():
    return getpass("Password: "), getpass("Re-type Password: ")
