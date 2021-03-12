# UMCTF2021 - momo's IOT 1&2

- Write-Up Author: RB916120 \[[MOCTF](https://www.facebook.com/MOCSCTF)\]

- Flag:MOCSCTF{you_can_digging_more_deeper!?!??} && MOCSCTF{345yf0ry0u?!#}

## **Question:**
omo's IOT 1&2

[xiaofang_MomoEdition.bin](./xiaofang_MomoEdition.bin)

## Write up
** writeup will enrich soon..
---

binwalk -e xiaofang_MomoEdition.bin  
in /home/Momo/Desktop/..secret  
flag1:MOCSCTF{you_can_digging_more_deeper!?!??}

when momo login will lacunh a script in /bin/mosh  
only when $USER=Momo
flag2:MOCSCTF{345yf0ry0u?!#}