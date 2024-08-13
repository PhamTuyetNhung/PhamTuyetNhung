# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 18:44:41 2024

@author:Phạm Tuyết Nhung-23707091
"""
GPA=float(input("Nhập điểm trung bình(GPA):"))
if GPA < 3.5:
    print("Học lực Kém")
elif GPA >=3.5 and GPA < 5.0:
    print("Học lực Yếu")
elif GPA >=5.0 and GPA <7.0:
    print("Học lực Trung bình")
elif GPA >= 7.0 and GPA <8.0:
    print("Học lực Khá")
elif GPA >=8.0 and GPA <9.0:
    print("Học lực Giỏi")
else:
    print("Học lực Xuất sắc")
    
