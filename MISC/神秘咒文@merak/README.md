# UMCTF2021 - 神秘咒文

- Write-Up Author: 茯苓 \[[Merak天璇 20级](https://we.buptmerak.cn/)\]

- Flag:MOCSCTF{pl@y_ωith_turtl3}

## **Question:**
trutle leave this path to us, can you track him?

>PD 海龟放下画笔 PU 海龟提起画笔 LT 海龟向左（逆时针）转指定的角度 RT 海龟向右（顺时针）转指定的角度 FD 海龟前进指定的步数 BK 海龟后退指定的步数

[mantra](./mantra.txt)
## Write up
**below tool required in this article.**  

[Logo (programming language)](https://en.wikipedia.org/wiki/Logo_(programming_language)) - Logo is an educational programming language, designed in 1967 by Wally Feurzeig, Seymour Papert, and Cynthia Solomon.


---

打开附件看到一堆字母和数字的神秘组合 根据题面中的“龟之国”很容易可以联想到logo语言  

>logo语言简介: 20世纪60年代，美国麻省理工学院人工智能实验室的西摩尔·帕伯特专为孩子们 设计了一种叫LOGO的计算机语言，是一种易学、易懂、易于掌握的结构化程序设计语言，出发 点是将原本较为枯燥的程序设计形象化，希望学生不要机械地记忆事实，使学生在掌握了为数不 多的LOGO原始命令后，能在发现和探索中学习，通过操纵屏幕上的海龟来学习编写程序，强调 创造性的探索能给学生严密的计算思维和有趣的学习体验。  
附件中正是一份可以操控海龟画出图案的代码  

基本用到了以下的操作:  
>命令 作用  
PD 海龟放下画笔  
PU 海龟提起画笔  
LT 海龟向左(逆时针)转指定的角度 RT 海龟向右(顺时针)转指定的角度 FD 海龟前进指定的步数  
BK 海龟后退指定的步数    

在网上可以找到这个海龟画图软件，输入txt中的代码可以画出一个残缺的二维码 画图过程中可能会遇到以下问题: 找不到可以用的软件/画出来的二维码太小/命令不能一次输入
用MSWlogo来画效果最好，既可以放大缩小图像，右下角的Edall功能也可以一次性输入所有命令(但 是小网站下的mswlogo可能会带些奇怪的东西......)請用官方軟件

画好后的二维码如下图所示  
![img](./img/1.png)
 
这个二维码缺少了左下和右上两个定位角 可以尝试自己用海龟画出来(doge)或者用ps之类的软件补全
扫描补全后的二维码得到flag MOCSCTF{pl@y_ωith_turtl3}  
![img](./img/2.png)