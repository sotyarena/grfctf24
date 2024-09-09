import sys
import base64
from cryptography.fernet import Fernet

FLAG = b'gAAAAABm3rqEPOcpPuJgksDgaTjUgs490kQt4pfyfbM6NWM5CSV2CxxVsaVgZSYhyuHCRiqDuYqfQq2CUdIU3C30N2uzip4QDAAn_3m55yUuX6Rn-e47uAHTRf4-FhicxDjwXkrOUXCb_uMWNvzs4DsNrbwV9dL2Aw=='

if len(sys.argv) == 1:
    print("Huh, I think you miss the reverse things, don't you?")

else:
    argv = sys.argv[1].encode()

    if argv == bytes.fromhex("766572797665727976657279766572797665727976657279536166654b657979"):
        f = Fernet(base64.urlsafe_b64encode(argv))
        print(f.decrypt(FLAG).decode())
    else:
        print("Wrong lmao:p")