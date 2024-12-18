# -*- coding: utf-8 -*-
"""Book_Pandas.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1VPwQ8kl8UrewprLBKgTa59uguYo9I4DH
"""

#สร้างข้อมูล Series จาก List
import pandas as pd
data1 = [15,12.5,'ksb',22,'Jim']
ps = pd.Series(data1)
ps

#สร้างข้อมูล Series จาก Tuple
data2 = (15,12.5,'ksb',22,'Jim')
ps = pd.Series(data2)
ps

#สร้างข้อมูล Series จาก Numpy
import pandas as pd
import numpy as np
data = [15,12.5,'Ksb',"Jim"]
ndata = np.array(data)
ps = pd.Series(ndata)
ps

#สร้างข้อมูล Series แบบกำหนด index
data = [15,12.5,18,22,17]
idx = ['A','B','C','D','E']
ps = pd.Series(data,index=idx)
ps

#สร้างข้อมูล Series ด้วย Numpy แบบกำหนด index
data = [15,12,20]
idx = ['A','B','C']
ps = pd.Series(np.array(data),index=idx)
ps

#สร้างข้อมูล Series จาก Dictionary
data = {'A':15,'B':8,'C':20}
ps = pd.Series(data)
ps

#การเข้าถึงข้อมูล
data = {'A':15,'B':8,'C':20}
ps = pd.Series(data)
ps['A']
ps['B']
ps['C']

#การเข้าถึงช่วงข้อมูล Slicing
data = {'A':15,'B':8,'C':20}
ps = pd.Series(data)
ps[:]
ps[2:]
ps[:2]
ps[1:3]

#สร้าง Dataframe จาก List
import pandas as pd
data = [12,15,20,25]
cols = ['Age']
df = pd.DataFrame(data,columns=cols)
df

#สร้าง DataFrame จาก List หลายมิติ
import pandas as pd
data = [[12,15,20],[5,6,7],[10,20,30]]
colms = ['A','B','C']
df = pd.DataFrame(data,columns=colms)
df

#สร้าง DataFrame จาก List หลายตัว โดยใช้ Zip
list1 = [1,2,3,4,5]
list2 = [5,6,7,8,9]
data = list(zip(list1,list2))
cols = ['A','B']
df = pd.DataFrame(data,columns=cols)
df

#สร้าง DataFrame แบบกำหนดชื่อคอลัมน์ และเลือก Index จากคอลัมน์
import pandas as pd
import numpy as np
data = [['A',1,2],['B',1,2],['C',1,2]]
cols = ['D','E','F']
df = pd.DataFrame(data,columns=cols)
df.set_index(['D'],inplace = True)
df

#สร้าง DataFrame จาก Dictionary
data = [{'Name':'A','Age':20},{'Name':'B','Age':25},{'Name':'C','Age':30}]
df = pd.DataFrame(data)
df

#สร้าง DataFrame จาก Series
name = ['A','B','C']
age = [10,20,30]
score = [70,80,90]
name_series = pd.Series(name)
age_series = pd.Series(age)
score_series = pd.Series(score)
frame = {'Name':name_series,'Age':age_series,'Score':score_series}
df = pd.DataFrame(frame)
df

#บันทึกไฟล์ในรูปแบบ CSV
cols = ['Name','Age']
df.to_csv('data.csv',index=False,columns=cols) #กรณีต้องการ Index ให้อเอาออก

#อ่านไฟล์ Excel ทั้งหมด ทุกคอลัมน์
import pandas as pd
uri = 'score_ageb.xlsx'
df = pd.read_excel(uri)
df

#อ่านไฟล์ Excel ทั้งหมด ทุกคอลัมน์ และใช้คอลัมน์อื่นเป็น Index
df = pd.read_excel(uri,index_col='Name')
df

#อ่าน Excel บางคอลัมน์ และข้าม Header
uri = 'score_ageb.xlsx'
cols = 'a,c:d'
df = pd.read_excel(uri,sheet_name='MySheet1',usecols=cols,header=3)
df.head()

#อ่าน Excel บางคอลัมน์ ข้าม Header และใช้คอลัมน์ Name เป็น Index
df = pd.read_excel(uri,sheet_name='MySheet1',usecols=cols,index_col='Name')
df
df.loc['Tim']
df.loc['Tim']['Score']
df.loc['Tim']['Section']
df.sort_index() #Sort แถวตาม Index

mycolumns = ['Student','Math','Comp','Year']
df = pd.read_excel(uri,names=mycolumns,index_col='Student')
df['Comp']['Tim']

uri = 'score_ageb.csv'
cols = ['Name','Score']
df = pd.read_csv(uri,usecols=cols,nrows=4,skiprows=[1,2]) #อ่านบางคอลัมน์ ข้ามแถว และกำหนดจำนวนแถว
df

uri = 'score_ageb.csv'
df = pd.read_csv(uri)
df.head()
df.head(10)
df.tail()
df.sample(3) #สุุ่มเลือกแถวตามจำนวนที่ต้องการ
