import websocket
import simplejson as json
import time
import ssl

from params import *
    
ws = websocket.WebSocket(sslopt={"cert_reqs": ssl.CERT_NONE})
ws.connect("wss://websockets.financialmodelingprep.com")

login = {
    'event':'login',
    'data': {
        'apiKey': FINANCE_API_KEY,
    }
}
    
subscribe = {
    'event':'subscribe',
    'data': {
        'ticker': ["aapl", "msft"] ,
    }
}

unsubscribe = {
    'event':'unsubscribe',
    'data': {
        'ticker': "aapl",
    }
}
    
ws.send(json.dumps(login))
     
time.sleep(1)
     
ws.send(json.dumps(subscribe))
     
time.sleep(1)
     
#ws.send(json.dumps(unsubscribe))
    
while True:
    print(ws.recv())
