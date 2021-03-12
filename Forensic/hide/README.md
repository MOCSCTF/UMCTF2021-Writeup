# UMCTF2021 - Hide

- Write-Up Author: TeruLei \[[MOCTF](https://www.facebook.com/MOCSCTF)\]

- Flag:mocsctf{c@n_y0u_f1nd_0ur_53cr3t?!}

## **Question:**
Hide

[hide](./hide.zip)

## Write up
**below tool required in this article.**  

[binwalk](https://tools.kali.org/forensics/binwalk) - Binwalk is a tool for searching a given binary image for embedded files and executable code.  
[exiftool](https://github.com/exiftool/exiftool) - ExifTool meta information reader/writer.  
[zsteg](https://github.com/zed-0xff/zsteg) - detect stegano-hidden data in PNG & BMP  

---

Here are the steps to get the flag:

A. Information Gathering:
1. In Kali Linux, use binwalk command, find there is another file hidden in the png file.
2. Use extract two png files with binwalk: "binwalk -e --dd='.*' ./hide.png", then you will see two png image (0 and pic2.png) in _hide.png.extracted folder.

B. Get the flag from hidden information:
1. use exiftool to get flag 1 (Comment: mocsctf{c@n_y0u_f1nd)from metadata for the image which is a safe (pic2.png).
2. use zsteg (Need to install, not included in Kali Linux by default,  to get flag 2 from the other image ("zsteg ./0") -- (b1,rgb,lsb,xy       .. text: "_0ur_53cr3t?!}")
