from OpenGL.GL import *
from OpenGL.GLUT import *
import numpy as np
from math import *


def drawCircle(r, xc, yc, cl1, cl2, cl3):
    glBegin(GL_POLYGON)
    for theta in np.arange(0,2*pi,0.001):
        x = r*cos(theta)
        y = r*sin(theta)

        glColor3f(cl1, cl2, cl3)
        


        glVertex(x + xc ,y + yc)

    glEnd()


def drawEllipse(rx,yx,u, cl1,cl2,cl3):
    
    glBegin(GL_POLYGON)
    glColor3f(cl1,cl2,cl3)
    for i in np.arange(0,2*pi,0.001):
        x = rx*sin(i)
        y = yx*cos(i)
        glVertex(x ,y+u)
    glEnd()


    

    
def drawHead():
    glBegin(GL_POLYGON)
    glColor3f(0.5,0.5,0.5)
    glVertex(0.07,0.3)
    glVertex(-0.07,0.3)
    glVertex(-0.07,0.36)
    glVertex(0.07,0.36)
    glEnd()

    drawEllipse(0.5,0.35,0.7, 0.7, 0.7, 0.7)

    drawCircle(0.15,0.25,0.77,1,1,1)
    drawCircle(0.09,0.22,0.77,0,0,0)

    glTranslate(0.27,0.01,0)
    drawEllipse(0.019,0.04,0.8 , 1,1,1)
    glTranslate(-0.27,-0.01,0)



    glRotate(180,0,1,0)

    drawCircle(0.15,0.25,0.77,1,1,1)
    drawCircle(0.09,0.22,0.77,0,0,0)

    glTranslate(0.27,0.01,0)
    drawEllipse(0.019,0.04,0.8 , 1,1,1)
    glTranslate(-0.27,-0.01,0)

    glRotate(-180,0,1,0)


















    glTranslate(0,0.6,0)

    glBegin(GL_POLYGON)
    glColor3f(0.5,0.5,0.5)
    glVertex(0.14,-0.18)
    glVertex(0.14,-0.02 )
    glVertex(0.12,-0.02 )
    glVertex(0.12,-0.18)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0.5,0.5,0.5)
    glVertex(0.1,-0.18)
    glVertex(0.1,-0.02 )
    glVertex(0.08,-0.02 )
    glVertex(0.08,-0.18)
    glEnd()



    glBegin(GL_POLYGON)
    glColor3f(0.5,0.5,0.5)
    glVertex(0.06,-0.18 )
    glVertex(0.06,-0.02 )
    glVertex(0.04,-0.02)
    glVertex(0.04,-0.18)
    glEnd()


    glBegin(GL_POLYGON)
    glColor3f(0.5,0.5,0.5)
    glVertex(0.02,-0.18 )
    glVertex(0.02,-0.02 )
    glVertex(0,-0.02)
    glVertex(0,-0.18)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0.5,0.5,0.5)
    glVertex(-0.02,-0.18 )
    glVertex(-0.02,-0.02 )
    glVertex(-0.04,-0.02)
    glVertex(-0.04,-0.18)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0.5,0.5,0.5)
    glVertex(-0.06 ,-0.18)
    glVertex(-0.06,-0.02 )
    glVertex(-0.08,-0.02)
    glVertex(-0.08,-0.18)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0.5,0.5,0.5)
    glVertex(-0.1,-0.18)
    glVertex(-0.1,-0.02 )
    glVertex(-0.12,-0.02)
    glVertex(-0.12,-0.18)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0.5,0.5,0.5)
    glVertex(-0.14,-0.18)
    glVertex(-0.14,-0.02 )
    glVertex(-0.16,-0.02)
    glVertex(-0.16,-0.18)
    glEnd()

    glTranslate(0,-0.6,0)

    





def tower():
    glBegin(GL_POLYGON)
    glColor3f(0.7,0.7,0.7)
    glVertex(-0.43,0.6)
    glVertex(-0.4,0.6)
    glVertex(-0.4,0.87)
    glVertex(-0.43,0.87)
    glEnd()

    drawCircle(0.05,-0.415,0.87,0.9,0,0)


def drawLegs(xc, xy):
    glBegin(GL_POLYGON)
    glColor3f(0.5,0.5,0.5)
    glVertex(0.19,-0.3)
    glVertex(0.19,-0.6)
    glVertex(0.25,-0.6)
    glVertex(0.25,-0.3)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0.7,0.7,0.7)
    for i in np.arange(0,pi,0.001):
        x = 0.12*cos(i)
        y = 0.12*sin(i)

        glVertex(x + xc,y + xy)
    glEnd()




def drawArm():
    glBegin(GL_LINE_STRIP)
    glColor3f(0.5,0.5,0.5)
    for x in np.arange(0.3,0.7,0.001):
        y = cos(x)
        glVertex(x,y - 0.67)
        for step in np.arange(0,0.03,0.001):
            y = cos(x + step) - step
            glVertex(x,y - 0.67 - step)

    glEnd()

   
    drawCircle(0.13,0.75,-0.03,0.7,0.7,0.7)

    glBegin(GL_TRIANGLE_STRIP)
    glColor3f(1,1,1)
    glVertex(0.75,-0.03)
    glVertex(0.78,-0.16)
    glVertex(0.88,-0.16)
    glEnd()

        
def drawBody():

    

    
    glBegin(GL_POLYGON)
    glColor3f(0.7,0.7,0.7)
    glVertex(-0.3,0.3)
    glVertex(0.3,0.3)
    glVertex(0.3,-0.3)
    glVertex(-0.3,-0.3)
    glEnd()


    glBegin(GL_POLYGON)
    glColor3f(0.9,0.9,0.9)
    glVertex(-0.2,0.2)
    glVertex(0,0.2)
    glVertex(0,-0.19)
    glVertex(-0.2,-0.19)
    glEnd()

    
    glBegin(GL_POLYGON)
    glColor3f(0.5,0.5,0.5)
    glVertex(-0.18,0.18)
    glVertex(-0.02,0.18 )
    glVertex(-0.02,0.16 )
    glVertex(-0.18,0.16)
    glEnd()


    glBegin(GL_POLYGON)
    glColor3f(0.5,0.5,0.5)
    glVertex(-0.18,0.14 )
    glVertex(-0.02,0.14 )
    glVertex(-0.02,0.12 )
    glVertex(-0.18,0.12)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0.5,0.5,0.5)
    glVertex(-0.18,0.1 )
    glVertex(-0.02,0.1 )
    glVertex(-0.02,0.08 )
    glVertex(-0.18,0.08)
    glEnd()



    glBegin(GL_POLYGON)
    glColor3f(0.5,0.5,0.5)
    glVertex(-0.18,0.06 )
    glVertex(-0.02,0.06 )
    glVertex(-0.02,0.04)
    glVertex(-0.18,0.04)
    glEnd()


    glBegin(GL_POLYGON)
    glColor3f(0.5,0.5,0.5)
    glVertex(-0.18,0.02 )
    glVertex(-0.02,0.02 )
    glVertex(-0.02,0)
    glVertex(-0.18,0)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0.5,0.5,0.5)
    glVertex(-0.18,-0.02 )
    glVertex(-0.02,-0.02 )
    glVertex(-0.02,-0.04)
    glVertex(-0.18,-0.04)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0.5,0.5,0.5)
    glVertex(-0.18,-0.06)
    glVertex(-0.02,-0.06 )
    glVertex(-0.02,-0.08)
    glVertex(-0.18,-0.08)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0.5,0.5,0.5)
    glVertex(-0.18,-0.1)
    glVertex(-0.02,-0.1 )
    glVertex(-0.02,-0.12)
    glVertex(-0.18,-0.12)
    glEnd()

    glBegin(GL_POLYGON)
    glColor3f(0.5,0.5,0.5)
    glVertex(-0.18,-0.14)
    glVertex(-0.02,-0.14 )
    glVertex(-0.02,-0.16)
    glVertex(-0.18,-0.16)
    glEnd()

    











    drawCircle(0.06, 0.193,0.12, 0.9,0.9,0.9)

    drawCircle(0.03, 0.193,0.12, 0.7,0.2,0.3)

    

    

def draw():
    glClearColor(1,1,1,1)

    glClear(GL_COLOR_BUFFER_BIT)
    
    

    glTranslate(0,-0.23,0)

    drawBody()
    drawLegs(0.25, -0.69)
    
    glTranslate(-0.45,0,0)
    drawLegs(0.25 - 0.06, -0.69)
    glTranslate(0.45,0,0)

    drawArm()

    glRotate(180,0,1,0)
    drawArm()
    glRotate(-180,0,1,0)



    drawHead()

    glTranslate(0,0.23,0)

    tower()





    glFlush()


glutInit()
glutInitDisplayMode(GLUT_SINGLE | GLUT_RGB)

glutInitWindowSize(500,500)
glutCreateWindow(b"robot")
glutDisplayFunc(draw)
glutMainLoop()

    
