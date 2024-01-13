"""
File: main.py
Author: Luffy
Date: 13th January 2024
Description: Package Prediction Using The Linear Regerssion Model with 92% Accuracy.

"""



import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

df = pd.read_csv('./placement.csv')
	
xb=df.iloc[:,0]
yb=df.iloc[:,1]
	
	
x_train, x_test, y_train, y_test = train_test_split(xb, yb, test_size=0.05, random_state=0)
 
def LR(X):
	 
	x=x_train
	y=y_train
	point=[]
	xy=[]
	x2=[]
	y2=[]
	for i in range(len(x)):
		point.append([x.iloc[i],y.iloc[i]])
		xy.append(x.iloc[i]*y.iloc[i])
		x2.append(x.iloc[i]*x.iloc[i])
	zx=sum(x)
	zy=sum(y)
	zxy=sum(xy)
	zxozy=zx*zy
	zx2=sum(x2)
	zxo2=zx*zx
	n=len(x)
	a=((zy*zx2)-(zx*zxy))/((n*zx2)-zxo2)
	b=((n*zxy)-zxozy)/((n*zx2)-zxo2)
	y=[]
	for i in x:
		y.append(a+b*i)
	return (a+b*X)

def Test():
	
	pt=[]
	for i in range(len(x_test)):
		a=LR(x_test.iloc[i])
		b=y_test.iloc[i]
		if a>b:
			pt.append((b/a)*100)
		elif a<=b:
			pt.append((a/b)*100)
	
	print("Accuracy : ",round(sum(pt)/len(pt)))
	


def User():
	
	x=float(input("Enter Your CGPA : "))
	print("Your Package Was ",round(LR(x),3)," LPA")
	
Test()
User()