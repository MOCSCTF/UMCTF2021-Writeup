# UMCTF2021 - what-cipher-is-this

- Write-Up Author: bluebear \[[MOCTF](https://www.facebook.com/MOCSCTF)\]

- Flag:MOCSCTF{RE_Pyth0n_byt3_c0d3}

## **Question:**
what-cipher-is-this

[orzCipher.txt](./orzCipher.txt)

## Write up

---
* Given a ciphertext and XOR cipher.
* Disassemble the pythod bype code, we found it's XOR cipher.
* Perform XOR operation of ciphertext to get plaintext directly.
```
def XOR(input): 
    xorKey = 'A'
    length = len(input)
    for i in range(length):
        input = (input[:i] + chr(ord(input[i]) ^ ord(xorKey)) + input[i + 1:])
    return input
print(repr(XOR("\x0c\x0e\x02\x12\x02\x15\x07:\x13\x04\x1e\x1185)q/\x1e#85r\x1e\"q%r<")))
```
* You will get the flag **MOCSCTF{RE_Pyth0n_byt3_c0d3}**