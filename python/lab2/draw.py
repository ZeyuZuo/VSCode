import csv
import matplotlib.pyplot as plt

File = open('temper.csv')  # 打开csv文件
Reader = csv.reader(File)  # 读取csv文件
Data = list(Reader)  # csv数据转换为列表
length_zu = len(Data)  # 得到数据行数
length_yuan = len(Data[0])  # 得到每行长度

for i in range(1,length_zu):
    print(Data[i])

x = list()
y = list()

for i in range(1, length_zu):  # 从第二行开始读取
    x.append(int(Data[i][1]))  # 将第一列数据从第二行读取到最后一行赋给列表x
    y.append(int(Data[i][2]))  # 将第二列数据从第二行读取到最后一行赋给列表

plt.plot(x,y)  # 绘制x,y的折线图
plt.xlabel('time')
plt.ylabel('temperature')
plt.show()  # 显示折线图

