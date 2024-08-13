# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 19:12:49 2024

@author:Phạm Tuyết Nhung-23707091
"""
a=float(input("Nhập vào số a:"))
b=float(input("Nhập vào số b:"))
if a==0 and b==0:
    print("Phương trình vô số nghiệm")
elif a==0 and b!=0:
        print("Phương trình vô nghiệm")
else:
    x= -b/a
    print("Nghiệm của phương trình là: x=", x)
    
    
