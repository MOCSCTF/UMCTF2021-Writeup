# UMCTF2021 - hardhead

- Write-Up Author: danniel@Boardware

- Flag:MOCSCTF{Boardware_15_6r347_:D!!}

## **Question:**
hardhead

## Write up

---

目錄下會有index.php, secret.php  
![img](./img/1.png)  
讓參賽者訪問 / 會跳轉到secret.php 
![img](./img/2.png)  
真正的flag在index.php的cookie內, 參賽者只要在訪問 / 時capture request即可找到flag
![img](./img/3.png)  
MOCSCTF{Boardware_15_6r347_:D!!}
