import os, sys, time, random
from sys import exit as keluar
from time import sleep as waktu
from random import random as acak
from random import choice as pilih
from sys import stdout
from os import system


os.system("clear")
m = '\x1b[1;91m'
h = '\x1b[1;92m'
k = '\x1b[1;93m'
b = '\x1b[1;94m'
u = '\x1b[1;95m'
c = '\x1b[1;96m'
p = '\x1b[0m'
i = '\x1b[1;90m'
v = '\x1b[1;38;5;198m'
j = '\x1b[1;38;5;208m'
w = (m, v, j, p, k, b, u, c)
W = pilih(w)
blen=raw_input("\x1b[1;93mInput pict Doi Lu : ")
time.sleep(2)
print ("\x1b[1;92mPict Doi Lu",blen)
time.sleep(2)
print ("\x1b[1;92mScann dulu ya boss :)")
 
def load():
    l = 'S '
    a = 'C'
    g = 'A '
    i = 'N '
    n = 'N '
    P = '  '
    r = ' I '
    h = 'N '
    w = 'G '
    u = '. '
    o = '. '
    s = '. '
    e = '. '
    S = '. '
    for z in range(90):
        waktu(0.1)
        stdout.write('\r  [\x1b[1;36m' + l[z % len(l)] + a[z % len(a)] + g[z % len(g)] + i[z % len(i)] + n[z % len(n)] + P[z % len(P)] + r[z % len(r)] + o[z % len(o)] + s[z % len(s)] + e[z % len(e)] + S[z % len(S)] + P[z % len(P)] + r[z % len(r)] + S[z % len(S)] + u[z % len(u)] + w[z % len(w)] + h[z % len(h)] + '\x1b[1;37m]')
        stdout.flush()
        
load()
print
time.sleep(3)
print ("\x1b[1;91mMundur Bos!!!, Dia Dah Punya Pasangan!!!")
time.sleep(2)
print ("Do You Want Remove Love?")
back=raw_input("Y/N=> ")
if back =='Y': 
      print ("Removing....")       
def load():
    l = 'R '
    a = 'E'
    g = 'M '
    i = 'O '
    n = 'V '
    P = ' . '
    r = ' I '
    h = 'N '
    w = 'G '
    u = '. '
    o = '. '
    s = '. '
    e = '. '
    S = '. '
    for z in range(90):
        waktu(0.1)
        stdout.write('\r  [\x1b[1;36m' + l[z % len(l)] + a[z % len(a)] + g[z % len(g)] + i[z % len(i)] + n[z % len(n)] + P[z % len(P)] + r[z % len(r)] + o[z % len(o)] + s[z % len(s)] + e[z % len(e)] + S[z % len(S)] + P[z % len(P)] + r[z % len(r)] + S[z % len(S)] + u[z % len(u)] + w[z % len(w)] + h[z % len(h)] + '\x1b[1;37m]')
        stdout.flush()
        
load()
time.sleep(1)
print
print ("\x1b[1;93mERROR!!!!!!!");
