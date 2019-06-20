#! /usr/bin/env python3
n=2
for s,d in[('',int(input()))]*35:
 while d:s=chr(48+39*(d%n>9)+d%n)+s;d//=n
 print(s);n+=1

# python2
'''
n=2
for s,d in[('',input())]*35:
 while d:s=chr(48+39*(d%n>9)+d%n)+s;d/=n
 print s;n+=1
'''