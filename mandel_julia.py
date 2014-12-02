#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import pylab as py

__author__ = 'Dominik Krzeminski'


def mandel(n=500, m=500, itermax=80, x_lim=[-2,2], y_lim=[-2,2]):
    """
    Function for calculating Mandelbrot set.
    Parameters: n,m - plot size, itermax - number of iterations,
                x_lim, y_lim - borders of the complex plane
    """
    x, y = np.mgrid[0:n, 0:m]
    x_ = np.linspace(x_lim[0], x_lim[1], n)[x]
    y_ = np.linspace(y_lim[0], y_lim[1], m)[y]
    c = x_+1j*y_
    z = np.zeros(c.shape)
    pict = np.zeros(c.shape, dtype=int)
    for i in xrange(itermax):
        bord = np.abs(z)<2
        z = np.multiply(z,z)
        z = np.add(z,c)
        pict[x[bord], y[bord]] = i+1
    return pict.T

def julia(c, n=500, m=500, itermax=80, x_lim=[-2,2], y_lim=[-2,2]):
    """
    Function for calculating Julia's sets.
    Parameters: c - parameter, n,m - plot size, itermax - number of 
                iterations, x_lim, y_lim - borders of the complex plane
    """
    x, y = np.mgrid[0:n, 0:m]
    x_ = np.linspace(x_lim[0], x_lim[1], n)[x]
    y_ = np.linspace(y_lim[0], y_lim[1], m)[y]
    z = x_+1j*y_
    pict = np.zeros(z.shape)
    for i in xrange(itermax):
        bord = np.abs(z)<2
        z = np.multiply(z,z)
        z = np.add(z,c)
        pict[x[bord], y[bord]] = i+1
    return pict.T
    
if __name__=="__main__":
    p = mandel()
    py.imshow(p)
    py.axis('off')
    py.figure()
    p = julia(-0.10+0.65*1j,x_lim=[-1,1], y_lim=[-1,1])
    py.imshow(p,cmap=py.get_cmap('Set1'))
    py.axis('off')
    py.figure()
    p = julia(-0.73+0.19*1j)
    py.imshow(p,cmap=py.get_cmap('RdPu'))
    py.axis('off')
    py.show()
