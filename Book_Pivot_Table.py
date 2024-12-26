# -*- coding: utf-8 -*-
"""Book_Pivot_Table.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1MrkSsWaKRFlqPfWbQFbRdsmtLV0v0Dcf
"""

import pandas as pd
uri = 'sale_quarterly1.xlsx'
cols = 'b:e' #เลือกคอลัมน์ B:E
df = pd.read_excel(uri,sheet_name='Sheet1',usecols=cols,header=2) #เลือกข้าม 2 แถวบน
df.head(4) #ดู 4 แถวแรก
df.shape #ดูจำนวนแถว และจำนวนคอลัมน์
df.dtypes #ดูประเภทของข้อมูลแต่ละคอลัมน์
df.describe() #ดูข้อมูลสถิติที่เป็นเชิงปริมาณของ df
df.Quarter = df.Quarter.astype('category') #เปลี่ยนประเภทข้อมูลเป็น Category เพื่อให้ describe แล้วไม่ถูกคำนวณ
df.Sales.sum() #หาผลรวมของคอลัมน์ที่ต้องการ

pvt = df[['Sales','Quarter']] #เลือกคอลัมน์ที่ต้องการใช้
pvt = pvt.pivot_table(index='Quarter') #เลือกคอลัมน์ที่ต้องการเป็น Index ของ Pivot table และถ้าไม่กำหนด Agg ระบบจะเลือกเป็นค่าเฉลี่ยให้
pvt = pvt.pivot_table(index='Quarter',margins=True) #มีแถวสรุปผลเพิ่มเติมให้
pvt

pvt = df[['Sales','Quarter','Employee']]
# pvt = pvt.pivot_table(index=['Quarter','Employee'],margins=True) สามารถปรับเปลี่ยน Index โดยเรียงก่อนหลังได้
# pvt
pvt = pvt.pivot_table(index=['Employee','Quarter'],margins=True) 
pvt

pvt = df[['Sales','Quarter']] #เลือกคอลัมน์ที่ต้องการใช้
pvt = pvt.pivot_table(index=['Quarter'],values='Sales',aggfunc='sum') #ค่ารวม
pvt = pvt.pivot_table(index=['Quarter'],values='Sales',aggfunc='mean',margins=True) #ค่าเฉลี่ย
pvt = pvt.applymap('{0:,}'.format) #กำหนดรูปแบบ Comma
pvt

import numpy as np
pvt = df.pivot_table(index=['Quarter'],values='Sales',aggfunc=np.sum,margins=True)
pvt.style.format({'Sales':'{:,.2f}'}) #กำหนดคอมม่าเฉพาะคอลัมน์ Sales
pvt.applymap('${0:,.2f}'.format) #กำหนดรูปแบบ $ และมีทศนิยม เช่น $3,000.00

pvt = df.pivot_table(index=['Quarter'],values=['Sales'],aggfunc=['sum','min','mean','max'],margins=True)
pvt
