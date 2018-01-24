#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Created on Sun Oct 19 16:29:09 2014

@author: vinayakumar R
"""

import numpy as np
import os
from hpelm import ELM
import hpelm

curdir = os.path.dirname(__file__)
pX = os.path.join(curdir, "../dataset_tests/iris/NOkdd.txt")
pY = os.path.join(curdir, "../dataset_tests/iris/foo.txt")

X = np.loadtxt(pX)
Y = np.loadtxt(pY)

print "sigmoid with multi class error"
elm = ELM(41,24)
elm.add_neurons(15, "sigm")
elm.train(X, Y, "c")
Yh = elm.predict(X)
print Yh
acc = float(np.sum(Y.argmax(1) == Yh.argmax(1))) / Y.shape[0]
print "kdd dataset training error: %.1f%%" % (100-acc*100)

print "sigmoid with MSE"
elm = hpelm.ELM(41, 24)
elm.add_neurons(10, "sigm")
elm.train(X, Y)
Y1 = elm.predict(X)
err = elm.error(Y1, Y)
print err

print "rbf_12 with multi class error"
elm = hpelm.ELM(41, 24)
elm.add_neurons(10, "rbf_l2")
elm.train(X, Y, 'c')
Y1 = elm.predict(X)
err = elm.error(Y1, Y)
print err


print "rbf_11 with multi class error"
elm = hpelm.ELM(41, 24)
elm.add_neurons(5, "rbf_l1")
elm.train(X, Y, 'c')
Y1 = elm.predict(X)
err = elm.error(Y1, Y)
print err
print(str(elm))

print "rbf_linf with multi class error"
elm = hpelm.ELM(41, 24)
elm.add_neurons(10, "rbf_linf")
elm.add_neurons(5, "rbf_l1")
elm.train(X, Y, 'c')
Y1 = elm.predict(X)
err = elm.error(Y1, Y)
print err


print "tanh with multi class error"
elm = hpelm.ELM(41, 24)
elm.add_neurons(10, "tanh")
elm.train(X, Y, 'c')
Y1 = elm.predict(X)
err = elm.error(Y1, Y)
print err

print "lin with multi class error"
elm = hpelm.ELM(41, 24)
elm.add_neurons(10, "lin")
elm.train(X, Y, 'c')
Y1 = elm.predict(X)
err = elm.error(Y1, Y)
print err






