import sys
import base64
from cryptography.fernet import Fernet

if len(sys.argv) == 1:
    print("Huh, I think you miss the reverse things, don't you?")

else:
    argv = sys.argv[1].encode()

    if argv == bytes.fromhex("766572797665727976657279766572797665727976657279536166654b657979"):
        f = Fernet(base64.urlsafe_b64encode(argv))
        print(f.decrypt(b"gAAAAABmvG2ibuPTaxAz4YNbFZ7ZI0FVRPjVm0bV2bDsQqIfj1FA_yz0EPm8n_-tJJcQlWDi1NjX2X6djTddKklPWAwqgCOdeaCEgFiqyf-6DBBe9AmuaUk1AWNGmUIzOgw6KNKuIYnx").decode())
    else:
        print("Wrong lmao:p")