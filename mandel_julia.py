#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
import pylab as py

__author__ = 'Dominik Krzeminski'


def mandel(n=500, m=500, itermax=80, x_lim=[-2,2], y_lim=[-2,2]):
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
    p = julia(-0.10+0.65*1j,x_lim=[0.3,0.6], y_lim=[0.3,0.6])
    py.imshow(p,cmap=py.get_cmap('gist_rainbow'))
    py.show()
