import numpy as np
from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
	I=[[2,2,3,4],[3,1,5,3],[2,3,4,6],[2,3,2,4]]
	Displacementx = -1;  
	Displacementy = 0;  
	As=[]
	s=np.reshape(I,(16,1))
	for i in range (len(I[:])):
		for j in range (len(I[:])):
			A = (I[i][j]-min(s[:]))+1;
			As.append(A)

	NumQuantLevels = max(As)
	x = np.zeros((NumQuantLevels[0],NumQuantLevels[0]))
	glcm = x

	print(glcm)

	size_img=3
	if ( Displacementx < 0 ) :
		sx=abs(Displacementx)+1;
		ex=size_img;
	else:
		sx=1;
		ex=size_img-Displacementx;

	if ( Displacementy < 0 ) :
		sy=abs(Displacementy)+1;
		ey=size_img
	else:
		sy=1;
		ey =size_img-Displacementy;

	As=np.reshape(As,(4,4))

	print(As)
	print(sx,ex,sy,ey)

	c=(As[2+(1*Displacementx),3+(1*Displacementy)])
	g=(As[2,3])
	print(g,c)

	for i in range(sx,ex,1):
		for j in range(sy,ey,1):
			c=(As[i+(1*Displacementx),j+(1*Displacementy)])
			g=(As[i,j])
			glcm[g][c]=((glcm[g][c])+1)
	
	print (glcm)

	gl=np.reshape(glcm,(NumQuantLevels[0]**2,1))

	GLCMProb=[]
	for i in range (NumQuantLevels[0]**2):
		GLCM= gl[i]/sum(gl)
		GLCMProb.append(GLCM)










