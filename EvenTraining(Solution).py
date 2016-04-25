#!/bin/python

import sys


n = int(raw_input().strip())
a = map(int,raw_input().strip().split(' '))
sum = 0
for i in a:
    if i==1:
        sum = sum+1
if sum%2 == 0:
    print 'Yes ' + str(sum)
else:
    print 'No ' + str(sum)
  