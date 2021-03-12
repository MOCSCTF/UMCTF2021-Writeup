# UMCTF2021 - Break my shield

- Write-Up Author: TeruLei \[[MOCTF](https://www.facebook.com/MOCSCTF)\]

- Flag:mocsctf{y0u_w1n_ch33r5!}

## **Question:**
Break my shield

[shield.zip](./shield.zip)

## Write up

**will enrich the writeup soon

---

1. After inspecting the shield.zip file, the file is just to change the encrypion bit of the file (e.g. the hex that after 504B03041400,504B01023F001400), change the encryption bit to "0". The file can be opened. You can get shield.jpg and shield1.zip.
(Notes: for step 1, you can use hexeditor to do the trick)
2. Shield1.zip is a real password protected zip file. It has 2 x encrypted file shield.jpg and flag.txt. After checking (you can check the CRC of the shield.jpg file in step1, and according to zip file format, check the CRC of shield.jpg in shield1.zip), the shield.jpg from step 1 and shield.jpg in shield1.zip are binary the sanme. 
(Notes: you can crc32 and hexeditor to do the trick)
3. Use ARCHPR with the unzipped file shield.jpg from step 1, you can decrypt shield1.zip file (according the zip file structure to get the key position then decrypt the file) with plaintext attack, then you can get the flag.
