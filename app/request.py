import requests

def getquotes():
    url = "http://www.quoteland.com/random.asp"
    call = requests.get(url)
    quote = call.json()
    return quote