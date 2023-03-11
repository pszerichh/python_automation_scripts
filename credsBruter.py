import requests, queue, os
# from bs4 import BeautifulSoup as bs
from datetime import datetime as dt

# key:value pairs of usernames and passwords that will be sent to the login page
credsBody = {
    'username': '',
    'password': ''
}


# the output file
outFile = ''
# the dicitionary for username field
unameWordlist = '/home/sam/Shop/python_automation_scripts/resources/username_mini.txt'
# the dictionary for the password field
passWordlist = '/home/sam/Shop/python_automation_scripts/resources/passwords_mini.txt'
# url to the login page
loginUrl = ''
# queue consisting of usernames to be used
unameQueue = queue.Queue()
# queue consisting of passwords to be used
passQueue = queue.Queue()

# this dictionary builds both the dictionaries
def makeDictionary(uname, passwd):
    if uname:
        fd = open(unameWordlist, 'r')
        rawWords = fd.readlines()
        fd.close()
        for line in rawWords:
            unameQueue.put(line.rstrip())

    if passwd:
        fd = open(passWordlist, 'r')
        rawWords = fd.readlines()
        fd.close()
        for line in rawWords:
            passQueue.put(line.rstrip())


def launchAttack():
    for uname in unameQueue.queue:
        for passwd in passQueue.queue:
            print(F'request: username = {uname} & password = {passwd}')



def setStage():
    # CRED = '\033[91m'
    # CEND = '\033[0m'
    # print(CRED+'Hello, there'+CEND)

    global loginUrl, passWordlist, unameWordlist, outFile
    makeUname, makePasswd = True, True
    loginUrl = input('Enter url to the login page: ')
    chPass = input(F'Currently dictionary for passowrds\n\t {passWordlist}\n\nChange? (y/N): ')
    if(chPass=='y' or chPass=='Y'):
        pldOp = int(input('[1] Use single payload\n[2] Use multiple payloads\n\nYour choice?: '))
        if pldOp==1:
            sinPass = input('Enter password: ')
            passQueue.put(sinPass)
            makePasswd=False
        else:
            newPassFile = input('Enter path to new password dictionary: ')
            if os.path.exists(newPassFile):
                passWordlist = newPassFile
                print('wordlist for password changed\n')
            else:
                print('Supplied file does not exist')
                print(F'Continuing with file at\n\t{passWordlist}\n')

    chUser = input(F'Currntly dictionary for usernames\n\t {unameWordlist}\n\nchange? (y/N): ')
    if chUser=='y' or chUser=='Y':
        pldOp = int(input('[1] Use single payload\n[2] Use multiple payloads\n\nYour choice?: '))
        if pldOp==1:
            sinUser = input('Enter username: ')
            unameQueue.put(sinUser)
            makeUname=False
        else:
            newUserFile = input('Enter path to new username dictionary: ')
            if(os.path.exists(newUserFile)):
                unameWordlist = newUserFile
                print('Wordlist for username changed\n')
            else:
                print('Supplied file does not exist')
                print(F'Countinuing with file at\n\t${unameWordlist}\n')

    makeDictionary(makeUname, makePasswd)

    name = dt.isoformat(dt.now())
    outFile = "outputs/CredStuffer/"+name+".txt"


setStage()

# def getHandler():
#     makeDictionary()
#     # res = requests.get(loginUrl)
#     # soupObj = bs(res.text, 'lxml')
#     # print(res.text)
#     # with :
#     #     credsBody['password'] = password
#     #     print(F'requesting with username: {credsBody["username"]} & password: {credsBody["password"]}')
#     #     res = requests.post(url=loginUrl, data=credsBody)
#     #     print(res.headers['Content-Length'])

# it does the setup for the whole attack