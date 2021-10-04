import fileinput
count = 0
for myline in fileinput.input(files='/Users/anj/Desktop/My-Family.txt'):
    print("-->",myline)
    list=myline.split()
    label=list[0]
    myline = myline.replace(label, "")
    tag=list[1]
    print("<--",label,"|",end = '')
    print(tag,"|",end = '')
    def switch():
        option = tag

        if option == "INDI":
            
        
        
            res = "Y"
            print(res,"|",end = '')
 
        elif option == "NOTE":
        
            res = "Y"
            print(res,"|",end = '')
 
        elif option == "CHIL":
        
            res = "Y "
            print(res,"|",end = '')
        elif option == "SEX":
        
            res = "Y "
            print(res,"|",end = '')
        elif option == "BIRTH":
        
            res = "Y " 
            print(res,"|",end = '')
        elif option == "DEAT":
        
            res = "Y "
            print(res,"|",end = '')
        elif option == "FAMC":
        
            res = "Y "
            print(res,"|",end = '')
        elif option == "FAMS":
        
            res = "Y "
            print(res,"|",end = '')
        elif option == "FAM":
        
            res = "Y "
            print(res,"|",end = '')
        elif option == "MARR":
        
            res = "Y "
            print(res,"|",end = '')
        elif option == "HUSB":
        
            res = "Y "
            print(res,"|",end = '')
        elif option == "WIFE":
        
            res = "Y "
            print(res,"|", end = '')
        elif option == "DIV":
        
            res = "Y "
            print(res,"|",end = '')
        elif option == "DATE":
        
            res = "Y "
            print(res,"|",end = '')
        elif option == "HEAD":
        
            res = "Y "
            print(res,"|",end = '')
        elif option == "TRLR":
        
            res = "Y "
            print(res,"|",end = '')
        elif option == "BIRT":
            
            res = "Y "
            print(res,"|",end = '')
        elif option.startswith('@'):
            global count
            count = count + 1
            new=myline.split()
            if(new[1]=="INDI"):
                #new[1].replace("INDI","|INDI|Y|")
                print(new[1],"|","Y")
            if(new[1]=="FAM"):
                print(new[1],"|","Y")
              
                
                
        else:
            res = "N"
            print(res,"|",end='')
     
    switch()
    
    myline = myline.replace(tag,"")
 
    if(count==1):
        print("")
    else:
        print(myline)
    count=0




