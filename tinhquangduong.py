# -*- coding: utf-8 -*-
"""
Created on Tue Aug 13 14:30:23 2024

@author: Pham Tuyet Nhung-23707091
"""

s=float(input("Nhập quãng đường đi được(km):")) 
if s<=1:
    print("Tổng tiền phải trả là 20000 ")
elif 1<s<4:
    print("Tổng tiền phải trả là:",(20000+(s-1)*13000 ))
elif 4<=s<=8:
    print("Tổng tiền phải trả là:",(3*13000+(s-3)*12000))
elif  (3*13000+5*12000+(s-8)*10)>100000:
    print("Tổng tiền phải trả là:",(3*13000+5*12000+(s-8)*10000)*0.92  )
else:
    print("Tổng tiền phải trả là:",(3*13000+5*12000+(s-8)*10000 ))
          

        


    
    
    


