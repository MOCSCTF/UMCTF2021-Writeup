# UMCTF2021 - signin

- Write-Up Author: James \[[Merak天璇 20级](https://we.buptmerak.cn/)\]

- Flag:mocsctf{4hanks_supp0rt@Merak}

## **Question:**
signin  
[signin.exe](./signin.exe)
## Write up

---

exe后缀名是假的，放进exeinfope便知道并不是exe是elf64位，放进linux虚拟机运⾏会出现⼀个⼆维码  
![img](./img/1.png)  
⽤linux虚拟机运⾏⼀下，同路径下会⽣成图⽚flag.png  
![img](./img/2.png)  
打开flag.png，扫描关注MOCSCTF facebook并发消息即可获得flag
![img](./img/flag.png)  