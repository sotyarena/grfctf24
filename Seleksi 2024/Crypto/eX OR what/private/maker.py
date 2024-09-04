from pwn import xor

FLAG = "grfctf24{s3ben4rnya_gK_ada_y9_n4many4_17azah_s0ftFile_jad1_c3r1ta_in1_H0Ak528}"

open('ijazah.txt', 'wb').write(xor(FLAG, b"CWK"))