import sys
import base64
from cryptography.fernet import Fernet

FLAG = b'gAAAAABm2JWmEc0ytyOKlDhNrYDSD_moZUYoi7e1J4c3TM7i8YiVeDtKowBqA-DSWZ6a1GogS1JmdD_WU1FzLcz7LCXWKUO7R1Y5jlysmAWOr5WfiINg4mFHJ0SCYASIBZmnRcXv6mG5lkMBo2Q81cgNxGrQS5VhLA=='

if len(sys.argv) == 1:
    print("Huh, I think you miss the reverse things, don't you?")

else:
    argv = sys.argv[1].encode()

    if argv == bytes.fromhex("766572797665727976657279766572797665727976657279536166654b657979"):
        f = Fernet(base64.urlsafe_b64encode(argv))
        print(f.decrypt(FLAG).decode())
    else:
        print("Wrong lmao:p")