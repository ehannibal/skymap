#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 12:21:13 2017

@author: Elsa Forberger
"""
        
class Point(object):
    def __init__(self,dec, ra, err):
        self.err = err
        self.ra = ra
        self.dec = dec
        if float(self.err) > 50:
            self.eventType = "Shower"
        else:
            self.eventType = "Track"
    def toString(self):
        return "dec " + str(self.dec) +" ra "+ str(self.ra)+ " err " + str(self.err) + " type " + self.eventType
points = []
out = open("/Users/Patron/Documents/output.txt", "w")
data = open('/Users/Patron/Documents/upgoing_events.txt', "r+")
datalist = data.readlines()
for item in datalist:
    words = item.split()
    if words[0] != "MDJ" and words[2] != "ang_err":
    	points.append({'dec': words[4], 'ra': words[3], 'type': 'Track'}
       # out.write(Point(words[4], words[3], words[2]).toString() + "\n")
    #print(str(words))
    #dec, ra, err, type OUTPUT
    #mdj, log, err, ra, dec INPUT
    #print ("MADE IT TO 26")
data.close()
out.close()
        
