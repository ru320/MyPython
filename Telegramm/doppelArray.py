############# Imports
import collections
import requests


############# Settings
myAccounts = collections.defaultdict(dict)
# Bot API Token
# Chat ID
#- RF 
myAccounts['RF']['Token'] = "994221020:AAGh-2TABWpEkJdGG6q72oOr7j1B1A38OYM"
myAccounts['RF']['ID'] = "1088557135"
#- BF
myAccounts['BF']['Token'] = "1066076427:AAEuY_zrcAnYmACuX4WdQExGtMqe1GhwxTY"
myAccounts['BF']['ID'] = "1090297721"



############# Defs
#- Senden der Nachriten
def SendTelegram(Message,myAccount):
    ID = myAccounts[myAccount]['ID']
    Token = myAccounts[myAccount]['Token']
    params = {"chat_id":ID, "text":Message}
    url = f"https://api.telegram.org/bot{Token}/sendMessage"
    message = requests.post(url, params=params)
    return(message)

#- Sende Mult Nachriten
def SendMultTelegram(Message):
    for myAccount in myAccounts:
        print()
        ID = myAccounts[myAccount]['ID']
        Token = myAccounts[myAccount]['Token']
        params = {"chat_id":ID, "text":Message}
        url = f"https://api.telegram.org/bot{Token}/sendMessage"
        message = requests.post(url, params=params)
        return(message)

SendMultTelegram('Test')
SendTelegram('Test2','RF')
