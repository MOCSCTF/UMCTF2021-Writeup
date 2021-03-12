# UMCTF2021 - obfuscatedJS

- Write-Up Author: bluebear \[[MOCTF](https://www.facebook.com/MOCSCTF)\]

- Flag:MOCSCTF{RE_0bfusc@tlOn_J5}

## **Question:**
obfuscatedJS

[obfuscatedJS](./obfuscatedJS.html)

## Write up

---

* atob() function decodes a string of data which has been encoded using Base64 encoding.
```
NzcsNzksNjcsODMsNjcsODQsNzAsMTIzLDgyLDY5LDk1LDQ4LDk4LDEwMiwxMTcsMTE1LDk5LDY0LDExNiwxMDgsNzksMTEwLDk1LDc0LDUzLDEyNQ
```
* After base64 decoded, open browser console, use String.fromCharCode function to convert Decimal to ASCII.
```
String.fromCharCode(77,79,67,83,67,84,70,123,82,69,95,48,98,102,117,115,99,64,116,108,79,110,95,74,53,125)
```
* You will get the flag **MOCSCTF{RE_0bfusc@tlOn_J5}**
