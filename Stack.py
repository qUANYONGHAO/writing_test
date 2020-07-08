# -*- coding: utf-8 -*-
"""
Created on Wed Jul  8 19:58:08 2020

@author: Quan
"""

class Stack(object):
    def __init__(self):
        self.array = [[], []]
 
    def push_a(self, data):
        self.array[0].append(data)
 
    def pop_a(self):
        if len(self.array[0]) == 0:
            print('Stack a is empty')
        else:
            self.array[0].pop()
 
    def push_b(self, data):
        self.array[1].append(data)
 
    def pop_b(self):
        if len(self.array[1]) == 0:
            print('Stack b is empty')
        else:
            self.array[1].pop()
 
    def show(self):
        if len(self.array[0]) == 0:
            print('Stack a is empty')
        else:
            print('Stack a:', self.array[0])
        if len(self.array[1]) == 0:
            print('Stack b is empty')
        else:
            print('Stack b:',self.array[1])
            

