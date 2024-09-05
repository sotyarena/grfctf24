import base64
from cryptography.fernet import Fernet

FLAG = "grfctf24{s0m3_of_p7ogr4m_us3_ar9v_t0_run_9f56xs}"

key = b"veryveryveryveryveryverySafeKeyy"

f = Fernet(base64.urlsafe_b64encode(key))

cipher_text = f.encrypt(FLAG.encode())

print(key.hex())
print()
print(cipher_text)