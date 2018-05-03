import numpy as np
import operator
import random
import math
from graphics import *
from PIL import Image

######################SETUP#############################
def s(x):
	return 1/(1+math.e**(-x))
panel=GraphWin("jNet",1100,750,autoflush=False)
net=np.array([16,8,5,10])
l=len(net)
dictPos={}	#position dictionary
dictW={}	#weight dictionary
cost=0		#cost function

def dataSetup():
	rawData = np.genfromtxt('./optdigits.tra', delimiter=',')	#data import and slicing
	trainSet=rawData[:100,0:64]		#64 data points
	labels=rawData[:100,64]			#true values
	values=np.zeros([100,16])		#setup for image generation
	
	for i in range(100):
		for k in range(16):
			values[i,k]=(np.sum(trainSet[i,2*k:2*k+2])+np.sum(trainSet[i,2*k+8:2*k+10]))/4		#graphic pixel reduction 64->16
	
	for k in range(16):
			r=values[2,k]*15
			c=Circle(Point(30+(k%4)*20,100+math.floor(k/4)*20),10);c.setFill(color_rgb(r,r,r));c.draw(panel)	#graphing short set
	for k in range(64):
			r=trainSet[2,k]*15
	                c=Circle(Point(30+(k%8)*20,300+math.floor(k/8)*20),10);c.setFill(color_rgb(r,r,r));c.draw(panel)	#graphing long set
	input=trainSet[0,:]	#first entry of 64 points
	print input[2]

dataSetup()

for i in range(l):	#point and matrix creation
	w=[]
	list=[]
	for m in range(net[i]):list.append(m)	#weights and bias
	dictPos[i]=list

	for k in range(net[i]):
		w=[];b=[]
		for j in range(net[i-1]):
			g=random.randint(0,100);f=random.randint(0,10)
			w.append(g);b.append(f)
		p=Point(int(200+400/l+i*180),int(600-500*k/(net[i]-1)))
		dictPos[i][k]=[p,0,w,b,'+']	#actual dictionary
		c=Circle(p,6);c.draw(panel)

for i in range(1,l):	#weight graphing
	for k in range(net[i]):
		for r in range(len(dictPos[i][k][2])):
			t=dictPos[i][k][2][r]*255/100
			line=Line(dictPos[i][k][0],dictPos[i-1][r][0])
			line.setFill(color_rgb(t,t,t));line.draw(panel)

list=[]
print dictPos
for m in range(net[0]):list.append(m);dictPos[0]=list
for i in range(net[0]):dictPos[0][i][1]=3#input[i]/16.0
print dictPos

def frame():
	exp=np.zeros([l,1])
	for i in range (2,l):
		for k in range(net[i]):
        	        for r in range(len(dictPos[i][k][2])):
        	                t=dictPos[i][k][2][r]
        	                dictPos[i][k][1]+=round(dictPos[i][k][2][r]*dictPos[i-1][r][1]/100.000,3)
			dictPos[i][k][1]=round(s(dictPos[i][k][1]),3)
	for i in range (1,l):
        	for k in range(net[i]):
			p=Point(int(200+400/l+i*180),int(600-500*k/(net[i]-1)))
			c=Circle(p,6);c.setFill(color_rgb(dictPos[i][k][1]*255,dictPos[i][k][1]*255,dictPos[i][k][1]*255));c.draw(panel)
	print dictPos[l-1][:][1]
	#cost=(exp-dictPos[l-1][:][1])**2;print cost
	panel.update()
frame()

#for i in range (1,l):
#        for k in range(net[i]):
#                print dictPos[i][k][0]
#                c=Circle(dictPos[i][k][0],6);c.setFill(color_rgb(dictPos[i][k][1]*255,dictPos[i][k][1]*255,dictPos[i][k][1]*255));c.draw(panel)
