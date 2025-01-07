# -*- coding: utf-8 -*-
"""Book_Visual1

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1MCGTpnGrzIre2kXYp-OxnCNMJyWQB6nQ
"""

# Commented out IPython magic to ensure Python compatibility.
# %matplotlib inline
import matplotlib.pyplot as plt
x = [1,2,3,4,5,6]
ydata = [1,2.8,2.1,4.3,3,3.5]
plt.bar(x,ydata)
plt.show()

import numpy as np
x = np.array([1,2,3,4,5,6])
ydata = np.array([1,2.8,2.1,4,3,3.5])
plt.bar(x,ydata) #กราฟแนวตั้ง
plt.show()
plt.barh(x,ydata) #กราฟแนวนอน ให้เติมเป็น barh
plt.show()

x = np.array([1,2,3,4,5,6])
ydata = np.array([1,2.8,2.1,4,3,3.5])
plt.bar(x,ydata)
plt.savefig('matplot1.png') #Save Image File
plt.show()
plt.savefig('matplot2.png',dpi = 50,transparent = True)

x = np.array([1,2,3,4,5,6])
ydata = np.array([1,2.8,2.1,4,3,3.5])
plt.plot(x,ydata)
plt.show()

x = [1,2,3,4,5,6]
ydata = [1,2.8,2.1,4,3,3.5]
ydata2 = [2.2,1.6,2.3,2,2.3,2.1]
#x,y ทุกชุด จะต้องมีจำนวนที่เท่ากัน

plt.plot(x,ydata)
plt.plot(x,ydata2)
plt.show() # Plot ข้อมูลเปรียเทียบกัน

months = ['Jan','Feb','Mar','Apr','May','Jun']
ydata = [1,2.8,2.1,4,3,3.5]
expl = (0,0.15,0,0,0,0.25) #แตกชิ้นข้อมูลที่ 2 และ 6 ให้แยกออกมา
plt.pie(ydata,explode=expl,labels=months,autopct='%.1f%%',shadow=True,startangle=90)
plt.show()

x = [1,2,3,4,5,6]
ydata = [1,2.8,2.1,4,3,3.5]
plt.scatter(x,ydata) # Scatter Plot
plt.show()

x = [1,2,3,4,5,6]
ydata = [1,2.8,2.1,4,3,3.5]
x2 = [1.1,2,3,3.9,5.1,6]
ydata2 = [2.2,1.6,2.3,2.0,2.3,2.1]
plt.scatter(x,ydata)
plt.scatter(x2,ydata2)
plt.show() #Plot Scatter ซ้อนกัน

age = [18,17,20,18,19,18,17,20,17,18,20,18,17,18,19,20]
plt.hist(age)
plt.show()
import pandas as pd
df = pd.DataFrame(age,columns=['Age'])
df.head() #ดูข้อมูล 5 แถวแรก
df.Age.value_counts() #นับความถี่

wt = np.random.normal(10,2.5,5000)
plt.hist(wt)
# plt.hist(wt,bins=50) Plot แบบแบ่งช่วงข้อมูลเป็น 50
plt.show()

age = [18,17,20,18,19,18,17,20,17,18,20,18,17,18,19,20]
# plt.grid()
plt.grid(linestyle='--',axis='y') #เขียนเส้นกริดตามแนวประ แกน Y
plt.boxplot(age)
plt.show()

import pandas as pd
import matplotlib as mpl
%matplotlib inline
mpl.__version__
!wget -q https://github.com/Phonbopit/sarabun-webfont/raw/master/fonts/thsarabunnew-webfont.ttf #Get Font Thai
#Add Font and Set up
mpl.font_manager.fontManager.addfont('thsarabunnew-webfont.ttf')
mpl.rc('font',family='TH Sarabun New', size=20)
xs = [1,2,3,4,5,6]
ydata = [1,2.8,2.1,4,3,3.5]
ydata2 = [2.2,1.6,2.3,2,2.3,2.1]
plt.figure(figsize=(6,4))
plt.grid(linestyle='--',axis='y') #แสดง Grid เฉพาะแกน Y
plt.bar(x,ydata,color='c',width=0.5,label='ในประเทศ')
plt.bar([x + 0.2 for x in xs], #ระยะขยับของกราฟแต่ละแท่ง
        ydata2,width=0.5,color='orange',alpha=0.8,label='ส่งออก')
plt.plot(x,ydata,color='b',marker='s',markersize=8) # b=blue
plt.plot(x,ydata2,color='r',marker='s',markersize=8) # r=red
plt.xlabel('เดือน')
plt.ylabel('ยอดขาย')
plt.title('รายงาน Sales Report')
plt.legend()
plt.ylim(0,4.5) #กำหนดค่าแกน Y
plt.show()
