import numpy as np
sin, cos, pi = np.sin, np.cos, np.pi
import matplotlib.pyplot as plt

def scaletest():
    xys = np.array([(1,1),(2,3),(5,2)]).T
    scale = np.array([[2,0],[0,0.5]])
    print(np.dot(scale, xys))

def rotate(a):
    xys = np.array([(1,0),(2,0)]).T
    M = np.array([[cos(a), -sin(a)],[sin(a), cos(a)]])
    print(np.dot(M, xys))
    
def ellipse(a, b, thi):
    angs = np.linspace(0, np.pi*2, 100)
    xs = np.cos(angs) * 1
    ys = np.sin(angs) * 1
    pts = np.array([xs, ys])
    scale = np.array([[a,0],[0,b]])
    M = np.array([[cos(thi), -sin(thi)],[sin(thi), cos(thi)]])
    pts = np.dot(M, np.dot(scale, pts))
    plt.gca().set_aspect('equal')
    plt.plot(pts[0], pts[1])
    plt.show()

ellipse(6,3,pi/6)
    
