# -*- coding: utf-8 -*-
import hashlib,base64
def f(a,b):
    digest = hashlib.sha256(a + b).digest()
    return digest[:8]

def str_xor(a,b):
    return ''.join( chr(ord(a[i]) ^ ord(b[i])) for i in range(len(a)))

def round_add(a, b):
    res = str_xor(f(a,b),f(b,a))
    return res

def permutate(table, block):
    return list(map(lambda x: block[x], table))

def str_permutate(table, block):
    t = map(lambda x: block[x], string_to_list(table))
    print string_to_list(table)
    return ''.join(chr(i) for i in t)

def string_to_bits(data):
    data = [ord(c) for c in data]
    l = len(data) * 8
    result = [0] * l
    pos = 0
    for ch in data:
        for i in range(0,8):
            result[(pos<<3)+i] = (ch>>i) & 1
        pos += 1
    return result

def string_to_list(data):
    a = []
    a.extend(ord(i) for i in data)
    return a

s_box = [55, 87, 54, 131, 139, 71, 3, 147, 34, 212, 231, 22, 170, 230, 154, 112, 81, 225, 218, 246, 227, 23, 8, 114, 65, 111, 189, 202, 136, 250, 179, 60, 177, 28, 166, 151, 50, 224, 25, 152, 221, 219, 242, 27, 115, 93, 208, 153, 35, 162, 30, 191, 105, 140, 129, 243, 245, 186, 132, 6, 41, 63, 254, 249, 165, 217, 49, 21, 210, 241, 159, 188, 44, 200, 37, 67, 144, 197, 205, 232, 211, 69, 80, 160, 252, 84, 76, 158, 173, 157, 204, 79, 62, 86, 237, 38, 171, 51, 17, 229, 148, 39, 43, 196, 103, 57, 142, 77, 155, 46, 45, 164, 91, 133, 16, 161, 141, 190, 47, 116, 26, 207, 61, 72, 137, 56, 104, 176, 2, 75, 123, 100, 236, 9, 180, 203, 183, 128, 13, 124, 89, 58, 83, 182, 201, 233, 175, 130, 122, 52, 138, 220, 29, 178, 213, 145, 113, 127, 174, 7, 167, 214, 146, 98, 48, 14, 194, 156, 42, 206, 110, 235, 238, 18, 4, 96, 228, 149, 0, 253, 101, 107, 119, 32, 117, 134, 92, 53, 193, 94, 90, 172, 143, 185, 244, 199, 109, 102, 15, 85, 11, 209, 251, 10, 163, 12, 120, 222, 255, 126, 226, 135, 40, 192, 150, 215, 240, 99, 1, 97, 64, 36, 248, 82, 234, 68, 70, 184, 125, 198, 31, 5, 73, 187, 118, 106, 239, 169, 74, 95, 24, 20, 223, 19, 33, 78, 216, 168, 108, 59, 88, 247, 195, 66, 181, 121]

inv_s = [178, 218, 128, 6, 174, 231, 59, 159, 22, 133, 203, 200, 205, 138, 165, 198, 114, 98, 173, 243, 241, 67, 11, 21, 240, 38, 120, 43, 33, 152, 50, 230, 183, 244, 8, 48, 221, 74, 95, 101, 212, 60, 168, 102, 72, 110, 109, 118, 164, 66, 36, 97, 149, 187, 2, 0, 125, 105, 141, 249, 31, 122, 92, 61, 220, 24, 253, 75, 225, 81, 226, 5, 123, 232, 238, 129, 86, 107, 245, 91, 82, 16, 223, 142, 85, 199, 93, 1, 250, 140, 190, 112, 186, 45, 189, 239, 175, 219, 163, 217, 131, 180, 197, 104, 126, 52, 235, 181, 248, 196, 170, 25, 15, 156, 23, 44, 119, 184, 234, 182, 206, 255, 148, 130, 139, 228, 209, 157, 137, 54, 147, 3, 58, 113, 185, 211, 28, 124, 150, 4, 53, 116, 106, 192, 76, 155, 162, 7, 100, 177, 214, 35, 39, 47, 14, 108, 167, 89, 87, 70, 83, 115, 49, 204, 111, 64, 34, 160, 247, 237, 12, 96, 191, 88, 158, 146, 127, 32, 153, 30, 134, 254, 143, 136, 227, 193, 57, 233, 71, 26, 117, 51, 213, 188, 166, 252, 103, 77, 229, 195, 73, 144, 27, 135, 90, 78, 169, 121, 46, 201, 68, 80, 9, 154, 161, 215, 246, 65, 18, 41, 151, 40, 207, 242, 37, 17, 210, 20, 176, 99, 13, 10, 79, 145, 224, 171, 132, 94, 172, 236, 216, 69, 42, 55, 194, 56, 19, 251, 222, 63, 29, 202, 84, 179, 62, 208]


def generate(o):
    k = permutate(o,s_box)
    b = []
    for i in range(0, len(k), 7):
        b.append(k[i:i+7] + [1])
    c = []


    for i in range(32):
        pos = 0
        x = 0
        for j in b[i]:
            x += (j<<pos)
            pos += 1
        c.append((0x10001**x) % (0x7f))
    return permutate(o,s_box)



class N1ES_2:
    def __init__(self, key):
        if len(key) != 32 :
            raise Exception("key must be 32 bytes long")
        self.key = key
        self.gen_subkey()

    def gen_subkey(self):
        o = string_to_bits(self.key)
        k = []
        for i in range(8):
            o = generate(o)
            k.extend(o)
            o = string_to_bits([chr(c) for c in o[0:32]])
        self.Kn = []
        for i in range(32):
            t = map(chr, k[i * 8: i * 8 + 8])
            self.Kn.append(''.join(i for i in t))
        return

    def encrypt(self, plaintext):
        if (len(plaintext) % 16 != 0 or isinstance(plaintext, bytes) == False):
            raise Exception("plaintext must be a multiple of 16 in length")
        res = ''
        for i in range(len(plaintext) / 16):
            block = plaintext[i * 16:(i + 1) * 16]
            L = block[:8]
            R = block[8:]
            for round_cnt in range(32):
                L, R = R, str_xor(round_add(R, self.Kn[round_cnt]),L)
                L, R = str_permutate(L,s_box) , str_permutate(R,s_box)
            L, R = R, L
            res += L + R
        return res

    def decrypt(self,cipher):
	    res = ''
	    for i in range(len(cipher) / 16):
                block = cipher[i * 16:(i + 1) * 16]
                L = block[:8]
                R = block[8:]
                for round_cnt in range(32):
                    L, R = str_permutate(L,inv_s) , str_permutate(R,inv_s)	
                    L, R =  R,str_xor(round_add(R, self.Kn[31 - round_cnt]),L)
                L, R = R, L
                res += L + R
	    return res
key = "7056b257805ec2b8325795b0e6061f89"
n1es = N1ES_2(key)
#cipher = n1es.encrypt(FLAG)
#print base64.b64encode(cipher)  #5RKDR8p7j8W8842DiejFtcGXRFvbPNrkpWEtkdja2Po=
print n1es.decrypt(base64.b64decode("5RKDR8p7j8W8842DiejFtcGXRFvbPNrkpWEtkdja2Po="))



