#!/usr/bin/env python
# -*- coding: utf-8 -*-
#S = "OZONETOWER"
#S = "ETHER"
#S = "WEIGHFOXTOURIST"
#S = "OURNEONFOE"
#S = ""
S = "RTEERTEVRHEEEHTSEEHNEIGHT"
ZERO = "ZERO"
ONE = "ONE"
TWO = "TWO"
THREE = "THREE"
FOUR = "FOUR"
FIVE = "FIVE"
SIX = "SIX"
SEVEN = "SEVEN"
EIGHT = "EIGHT"
NINE = "NINE"

numbers = ''#this is the phone numbers

temp = ""#this is the stack temp variable, it has the push and pop opreatores
i = 0
i_temp = 0

count = 0#count the string

S_buffer = S

while 1:
    #print numbers
    #print S
    #print temp
    lens = len(S)
    if lens == 0:
        break
    temp = temp + S[i % lens]#this is the push opreator
    l = len(temp)
    if temp == ONE[0:l] or temp == TWO[0:l] or temp == THREE[0:l] or temp == FOUR[0:l] or temp == FIVE[0:l] or temp == SIX[0:l] or temp == SEVEN[0:l] or temp == EIGHT[0:l] or temp == NINE[0:l] or temp == ZERO[0:l]:
        S = S[0:i % lens] + S[i % lens + 1:]
        if l == 1:
            i_temp = i
        count = 0
        if temp == ONE:
            numbers = numbers + '1'
            temp = ""
            S_buffer = S
            i = 0
        elif temp == TWO:
            numbers = numbers + '2'
            temp = ""
            i = 0
            S_buffer = S
        elif temp == THREE:
            numbers = numbers + '3'
            temp = ""
            S_buffer = S
            i = 0
        elif temp == FOUR:
            numbers = numbers + '4'
            temp = ""
            S_buffer = S
            i = 0
        elif temp == FIVE:
            numbers = numbers + '5'
            temp = ""
            S_buffer = S
            i = 0
        elif temp == SIX:
            numbers = numbers + '6'
            temp = ""
            S_buffer = S
            i = 0
        elif temp == SEVEN:
            numbers = numbers + '7'
            temp = ""
            S_buffer = S
            i = 0
        elif temp == EIGHT:
            numbers = numbers + '8'
            temp = ""
            S_buffer = S
            i = 0
        elif temp == NINE:
            numbers = numbers + '9'
            temp = ""
            S_buffer = S
            i = 0
        elif temp == ZERO:
            numbers = numbers + '0'
            temp = ""
            S_buffer = S
            i = 0
    else:
        temp = temp[0:len(temp)-1]#this is the pop opreator
        i = i + 1
        count = count + 1
        if count >= len(S):
            S = S_buffer
            i = i_temp+1
            temp = ""
            count = 0
print numbers
print S
print temp
