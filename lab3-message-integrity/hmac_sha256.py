import hashlib
import hmac
from base64 import b64encode

def hmacSha256(msg, key):
    # Python 2
    message = bytes(msg).encode('utf-8')
    secret = bytes(key).encode('utf-8')

    # Python 3
    # message = bytes(msg, 'utf-8')
    # secret = bytes(key, 'utf-8')
    
    print("Message:\t{message}\nKey:\t\t{key}".format(message=message, key=key))
    print("HMAC:\t\t{}".format(hmac.new(secret, message, digestmod=hashlib.sha256).hexdigest()))
    print("HMAC encoded:\t{}".format(b64encode(hmac.new(secret, message, digestmod=hashlib.sha256).digest())))
    print("\n")

hmacSha256('Cifrado de informacion seccion 10', 'CC3078')
# >> gGxuGFVOcKSrisiMn2RFZvrukuCvALr2Pl4pM/psqc0=
# Encoded
# >> 806c6e18554e70a4ab8ac88c9f644566faee92e0af00baf63e5e2933fa6ca9cd

hmacSha256('La implementacion de este ejercicio fue sencilla', 'MAC')
# >> Zlc36/M+z15ItsFPusomEsC/m/k9JAv9Lauf5mmQBUE=
# Encoded
# >> 665737ebf33ecf5e48b6c14fbaca2612c0bf9bf93d240bfd2dab9fe669900541



# Implementacion del timing attack extraida de
# https://github.com/sqreen/DevelopersSecurityBestPractices/tree/master/_practices/timing-attack/_python

# To run
# pip install -r requirements.txt
# gunicorn -w 1 app:app
# python hack.py
