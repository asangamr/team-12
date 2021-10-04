#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 19:57:21 2021

@author: Sahithh Kumar
"""

# import fileinput
import fileinput
lIne=[]
i=0
  
# Using fileinput.input() method

for line in fileinput.input(files ='/Users/kiranmaigudiyella/Downloads/fam.txt'):
    print("-->"+line)
    outLine=line
    lIne.append(line)
    output=(outLine.replace(" ", "| ",1))
    outLineSplit=output.split()
    outLineSplit.pop(0)
    for i in outLineSplit:
        #print(i)
        if(i=="NOTE"):
            output=(output.replace(i,"NOTE|Y|"))
            break
        elif(i=="HEAD"):
            output=(output.replace(i,"HEAD|Y|"))
            break
        elif(i=="TRLR"):
            output=(output.replace(i,"TRLR|Y|"))
            break
        elif(i=="DATE"):
            output=(output.replace(i,"DATE|Y|"))
            break
        elif(i=="DIV"):
            output=(output.replace(i,"DIV|Y|"))
            break
        elif(i=="CHIL"):
            output=(output.replace(i,"CHIL|Y|"))
            break
        elif(i=="WIFE"):
            output=(output.replace(i,"WIFE|Y|"))
            break
        elif(i=="HUSB"):
            output=(output.replace(i,"HUSB|Y|"))
            break
        elif(i=="MARR"):
            output=(output.replace(i,"MARR|Y|"))
            break
        elif(i=="FAMS"):
            output=(output.replace(i,"FAMS|Y|"))
            break
        elif(i=="FAMC"):
            output=(output.replace(i,"FAMC|Y|"))
            break
        elif(i=="DEAT"):
            output=(output.replace(i,"DEAT|Y|"))
            break
        elif(i=="BIRT"):
            output=(output.replace(i,"BIRT|Y|"))
            break
        elif(i=="SOUR"):
            output=(output.replace(i,"SOUR|Y|"))
            break
        elif(i=="DEST"):
            output=(output.replace(i,"DEST|Y|"))
            break
        elif(i=="NAME"):
            output=(output.replace(i,"NAME|Y|"))
            break
        else:
            output=(output.replace(outLineSplit[0],outLineSplit[0]+"|N|"))
            break
    outLineSplit2=output.split()
    if(outLineSplit2[1].startswith('@') and outLineSplit2[2]=="INDI"):
        output=(output.replace(outLineSplit2[1],outLineSplit[0]))
        output=(output.replace(outLineSplit2[2],"|"+outLineSplit2[2]+"|Y|"))
    if(outLineSplit2[1].startswith('@') and outLineSplit2[2]=="FAM"):
        output=(output.replace(outLineSplit2[1],outLineSplit[0]))
        output=(output.replace(outLineSplit2[2],"|"+outLineSplit2[2]+"|Y|"))        
    print("<--"+output)
    
    