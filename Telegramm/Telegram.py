############# Imports
import requests


############# Settings
# Bot API Token
Token ="994221020:AAGh-2TABWpEkJdGG6q72oOr7j1B1A38OYM"
# Chat ID
ID = "1088557135"

############# Defs
#- Senden der nachrichten
def SendTelegram(Message):
    params = {"chat_id":ID, "text":Message}
    url = f"https://api.telegram.org/bot{Token}/sendMessage"
    message = requests.post(url, params=params)
    return(message)