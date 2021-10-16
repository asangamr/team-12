import fileinput
import datetime
from prettytable import PrettyTable
lIne=[]
age=0
i=0
identity=[]
name=[]
gender=[]
birthday=[]
age=[]
alive=[]
death=[]
child=[]
spouse=[]
cond1="BIRT"
cond2="DEAT"
cond3="FAMS"
cond4="MARR"
l="NA"
identity1=[]
married=[]
divorced=[]
husband_id=[]
husband_name=[]
wife_id=[]
wife_name=[]
children=[]
columns = ["Identity", "Name", "Gender", "Birthday","Age","Alive","Death","Child","Spouse"]
from datetime import date
d2 = date.today()

  
# Using fileinput.input() method

for line in fileinput.input(files ='/Users/kiranmaigudiyella/Downloads/My-family.txt'):
    lIne.append(line)
x=len(lIne)
#print(x)
while(x>0):
    j=lIne[i]
    m=j.split(" ",2)
    y=len(m)
    #while(y>0):
    if(m[1].startswith('@I')):
        identity.append(m[1])
            #print(identity)
    elif m[1]=="NAME" and m[0]=="1":
        name.append(m[2])
    elif m[1]=="SEX":
        gender.append(m[2])
            #print(name)
        #y=y-1
    """if(m[1]=="DEAT"):
        death.append("YES")
    else:
        death.append("NO")
    if cond3 in j:
        z=i
        y=lIne[z+1]
        m=y.split()
        while(not cond3 in m[1]):
            k=lIne[z]
            m=k.split()
            m[1]=D
            if()"""
    if cond1 in j:
        y=lIne[i+1]
        m=y.split()
        #print(m)
        if m[3]=="JAN":
            month=1
        elif m[3]=="FEB":
            month=2
        elif m[3]=="MAR":
            month=3
        elif m[3]=="APR":
            month=4
        elif m[3]=="MAY":
            month=5
        elif m[3]=="JUN":
            month=6
        elif m[3]=="JUL":
            month=7
        elif m[3]=="AUG":
            month=8
        elif m[3]=="SEP":
            month=9
        elif m[3]=="OCT":
            month=10
        elif m[3]=="NOV":
            month=11
        else:
            month=12
        d1 = datetime.date(int(m[4]),month,int(m[2]))
        b=str(d1)
        birthday.append(b)
        if(d1<d2):
            age.append(str(d2.year - d1.year))
    
    if cond1 in j:
        q=lIne[i+2]
        #print(q+"\n")
        #n=q.split()
        if cond2 in q:
            y=lIne[i+3]
            m=y.split()
            #print(m)
            if m[3]=="JAN":
                month=1
            elif m[3]=="FEB":
                month=2
            elif m[3]=="MAR":
                month=3
            elif m[3]=="APR":
                month=4
            elif m[3]=="MAY":
                month=5
            elif m[3]=="JUN":
                month=6
            elif m[3]=="JUL":
                month=7
            elif m[3]=="AUG":
                month=8
            elif m[3]=="SEP":
                month=9
            elif m[3]=="OCT":
                month=10
            elif m[3]=="NOV":
                month=11
            else:
                month=12
            d3 = datetime.date(int(m[4]),month,int(m[2]))
            b=str(d3)
            death.append(b)
            child.append(l)
            spouse.append(l)
        else:
            death.append(l)
            child.append(l)
            spouse.append(l)
    if m[1]=="CHIL":
        p=m[2].replace("@","")
        pnew=p.lstrip("I")
        p1=int(pnew)
        #p=m[2].lstrip("I")
        #print(pnew)
        z=i
        y=lIne[z]
        m1=y.split()
        while(not m1[2]=="FAM"):
            z=z-1
            y=lIne[z]
            m1=y.split()
        
        if "FAM" in y:
            p1=p1-1
            child[p1]= m1[1]
    if m[1]=="HUSB" or m[1]=="WIFE":
        p=m[2].replace("@","")
        pnew=p.lstrip("I")
        p1=int(pnew)
        #p=m[2].lstrip("I")
        #print(pnew)
        z=i
        y=lIne[z]
        m1=y.split()
        while(not m1[2]=="FAM"):
            z=z-1
            y=lIne[z]
            m1=y.split()
        
        if "FAM" in y:
            p1=p1-1
            spouse[p1]= m1[1]
#----------------------------------------FAMILY TABLE---------------------------------------------#
    if(m[1].startswith('@F')):
        identity1.append(m[1])
        married.append(l)
        divorced.append(l)
        z=i+1
        y=lIne[z]
        m=y.split()
        while(not m[1].startswith('@F')):
        #identity1.append(m[1])
            #print(m[1])
            #print(not m[1].startswith('@F'))
            if cond4 in y:
                y=lIne[z+1]
                m=y.split()
                if m[1]=="DATE":
                #print(m)
                    if m[3]=="JAN":
                        month=1
                    elif m[3]=="FEB":
                        month=2
                    elif m[3]=="MAR":
                        month=3
                    elif m[3]=="APR":
                        month=4
                    elif m[3]=="MAY":
                        month=5
                    elif m[3]=="JUN":
                        month=6
                    elif m[3]=="JUL":
                        month=7
                    elif m[3]=="AUG":
                        month=8
                    elif m[3]=="SEP":
                        month=9
                    elif m[3]=="OCT":
                        month=10
                    elif m[3]=="NOV":
                        month=11
                    else:
                        month=12
                    d1 = datetime.date(int(m[4]),month,int(m[2]))
                    b=str(d1)
                    v=len(married)-1
                    married[v]=b
            elif m[1]=="DIV":
                y=lIne[z+1]
                m=y.split()
                if m[1]=="DATE":
                #print(m)
                    if m[3]=="JAN":
                        month=1
                    elif m[3]=="FEB":
                        month=2
                    elif m[3]=="MAR":
                        month=3
                    elif m[3]=="APR":
                        month=4
                    elif m[3]=="MAY":
                        month=5
                    elif m[3]=="JUN":
                        month=6
                    elif m[3]=="JUL":
                        month=7
                    elif m[3]=="AUG":
                        month=8
                    elif m[3]=="SEP":
                        month=9
                    elif m[3]=="OCT":
                        month=10
                    elif m[3]=="NOV":
                        month=11
                    else:
                        month=12
                    d1 = datetime.date(int(m[4]),month,int(m[2]))
                    b=str(d1)
                    v=len(married)-1
                    divorced[v]=b
            elif(m[1]=="HUSB"):
                p=m[2].replace("@","")
                husband_id.append(p)
                p=p.replace("I","")
                p=int(p)
                #print(type(p))
                husband_name.append(name[p-1])
                #husband_id.append(m[2])
            elif(m[1]=="WIFE"):
                p=m[2].replace("@","")
                wife_id.append(p)
                p=p.replace("I","")
                p=int(p)
                #print(type(p))
                wife_name.append(name[p-1])
                #husband_id.append(m[2])
            '''elif(m[1]=="CHIL"):
                chil=[]
                string=""
                while(m[1]=="CHIL"):
                    p=m[2].replace("@","")
                    chil.append(p)
                    y=lIne[i+1]
                    m=y.split()
                string=(','.join(chil))
                e=0
                while(e<len(chil)):
                    string=" "+chil[e]
                    e=e+1
                #print(string)
                children.append(chil)
                chil.clear()'''
                
                
            
            if(m[1]=="TRLR"):
                break
                
            z=z+1
            y=lIne[z]
            m=y.split()
        
            
        
        
    x=x-1
    i=i+1
#print(children)
'''print(identity1)
print(married)
print(divorced)
print(husband_id)
print(husband_name)
print(wife_id)
print(wife_name)
print(children)'''
'''print(identity)
print(name)
print(gender)
print(birthday)
print(age)
print(death)
print(child)
print(spouse)
print(len(identity))
print(len(name))
print(len(gender))
print(len(birthday))
print(len(age))
print(len(death))
print(len(child))
print(len(spouse))'''
print("--------------------------INDIVIDUAL TABLE--------------------------------")
columns = ["Identity", "Name", "Gender", "Birthday","Age","Death","Child","Spouse"]
individuals = PrettyTable()
len_column=len(columns)
individuals.add_column(columns[0],identity)
individuals.add_column(columns[1],name)
individuals.add_column(columns[2],gender)
individuals.add_column(columns[3],birthday)
individuals.add_column(columns[4],age)
individuals.add_column(columns[5],death)
individuals.add_column(columns[6],child)
individuals.add_column(columns[7],spouse)
print(individuals)
print("--------------------------FAMILY TABLE--------------------------------")
columns_1=["ID","Married","Divorced","Husband_id","Husband_name","Wife_id","Wife_name"]
family=PrettyTable()
family.add_column(columns_1[0],identity1)
family.add_column(columns_1[1],married)
family.add_column(columns_1[2],divorced)
family.add_column(columns_1[3],husband_id)
family.add_column(columns_1[4],husband_name)
family.add_column(columns_1[5],wife_id)
family.add_column(columns_1[6],wife_name)

print(family)

#i1,i13,i2,i6,i10,i14,i15,i8,i9
