
# coding: utf-8

# In[6]:

import csv
f= open("1121.csv","r",encoding="utf-8")
data=[]
for row in csv.reader(f):
    data.append(row)
out=[]
for j in range(1,len(data[0])-1):
    for i in range(5,len(data)):
        if 61<=i<=74 or 76<=i<=105:
            continue
        #print(i,j)
        #print(data[i][j])
        if data[i][j] != "":
            #print(i,j)
            #print(data[i][j])
            out.append([data[k][j] for k in [0,2,3,4]])
            out[-1].append(data[i][0])
            out[-1].append(data[i][j])
f.close()
head=['報告日期','批號','產地','檢測項目','種類','數值']
#macos不須加入nweline
o=open("out_put.csv","w",newline=(""))
f_csv = csv.writer(o)
f_csv.writerow(head)
#macos可接受二維list引入
for row in out:
    f_csv.writerow(row)
#macos不嚴格檢查是否有檔案
o.close()


# In[ ]:



