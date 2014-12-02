#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import pylab as py

__author__ = 'Dominik Krzeminski'


def koch_iter(x,y):
    """
    One iteration of Koch curve. From two lists of lengths 2 (x and y
    coordinates) it gives two lists of lengths 5.
    """
    h_x = (x[1]-x[0])*1./3
    h_y = (y[1]-y[0])*1./3
    nx = []
    ny = []
    alph = np.pi/3
    for i in xrange(4):
        px = x[0]+h_x*i
        py = y[0]+h_y*i
        if i==2:
            nx.append((h_x)*np.cos(alph)-(h_y)*np.sin(alph)+(px-h_x))
            ny.append((h_x)*np.sin(alph)+(h_y)*np.cos(alph)+(py-h_y))
            nx.append(px)
            ny.append(py)
        else:
            nx.append(px)
            ny.append(py)
    return nx,ny

def koch_curve(n, bord = [0,3]):
    """
    Koch curve algorithm.
    Parameters: n - number of iterations, bord = [0,3] - x 
                coordinates of initial line.
    """
    left,right = bord
    n_x = [left,right]
    n_y = [0 , 0]
    for i in xrange(n):
        p_x, p_y = list(n_x), list(n_y)
        n_x, n_y = [],[]
        while len(p_x)>=2:
            x_,y_ = koch_iter(p_x[0:2],p_y[0:2])
            n_x.extend(x_[:-1])
            n_y.extend(y_[:-1])
            p_x.pop(0)
            p_y.pop(0)
        n_x.append(x_[-1])
        n_y.append(y_[-1])
    return n_x,n_y

def plot(data_x,data_y,title = ""):
    "Helper function to plot results of koch curve"
    py.title(title)
    py.plot(data_x,data_y,'r',lw=2)
    py.tick_params(axis='both', which='both', bottom=0, top=0,
                   left=0, right=0, labelbottom=0, labelleft =0) 
    py.xlim([0,3])
    py.ylim([0,1])

if __name__=="__main__":
    fig = py.figure()
    fig.subplots_adjust(hspace=0.25,top=0.93,bottom=0.05)
    for i in xrange(4):
        kx,ky = koch_curve(i)
        py.subplot(4,1,i+1)
        plot(kx,ky,title='iter = %i'%i)
    py.show()
