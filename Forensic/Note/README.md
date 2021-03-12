# MOCTF - Note

- Write-Up Author: Simon Leung \[[MOCTF](https://www.facebook.com/MOCSCTF)\]

- Flag:MOCSCTF{y0u_h@ve_f1nd_the_n0te!}

## **Question:**
> Note

[note](./note)

## Write up
**below tool required in this article.**  
[volatility](https://github.com/volatilityfoundation/volatility) - An advanced memory forensics framework. 

---
### 1. Identify the file:
![img](./img/note1.PNG)


### 2. Unzip the file:

![img](./img/note2.PNG)

### 3. Use Volatility Framework to analyze the file:
Use pslist to list the process


![img](./img/note3.PNG)

### 4. Found some interesting process:
Found notepad.exe


![img](./img/note4.PNG)

### 5. Found the flag in clipboard:
Suppose the user was editing via notepad, it is likely that the user has some info copied
and it should be found in the clipboard.

Try the clipboard parsing function of Volatility Framework to find the flag
![img](./img/note5.PNG)

Or use "notepad" option of Volatility Framework to reveal the content of the notepad process
![img](./img/note6.PNG)
