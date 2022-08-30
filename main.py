import random
a1 = 1;
b1 = 2;
c1 = 3;
c2 = 4;
a2 = 5;
b2 = 6;
b3 = 7;
c3 = 8;
a3 = 9;

data = [a1,a2,a3,b1,b2,b3,c1,c2,c3]
print("nhap gia tri bat ky tu 1 den 9")
so1 = int(input())
so2 = int(input())
so3 = int(input())
tohop3 = [so1,so2,so3]
print(tohop3)
tohop1 = int(so2-so1)
tohop2 = int(so3-so2)
if tohop1 == 1 or -1 or 3 or -3:
    if tohop2 == 1 or -1 or 3 or -3:
        print("yes")
    else: print("no")
else:
    print("no")

