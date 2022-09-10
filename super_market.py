import csv
def create():
    print("------------------------------------------------------------------------------------------------------------------------------------------------")
    f=open("super market.csv","w")
    c=csv.writer(f,lineterminator='\n')
    list=[]
    a=int(input("Enter number of items="))
    h=["ID","NAME","TYPE","PRICE","GST PRICE","FINAL PRICE"]
    for i in range(0,a):
        iid=int(input("ENTER PRODUCT ID:"))
        n=input("ENTER PRODUCT NAME:")
        t=input("ENTER PRODUCT TYPE:")
        p=int(input("ENTER PRICE:"))
        gp=int(input("ENTER GST PERCENTAGE:"))
        g=(p*gp)/100
        ne=p+g
        list.append([iid,n,t,p,int(g),int(ne)])
    c.writerow(h)
    c.writerows(list)
    f.close()
    print("------------------------------------------------------------------------------------------------------------------------------------------------")



def add():
    print("------------------------------------------------------------------------------------------------------------------------------------------------")
    f=open("super market.csv","a")
    c=csv.writer(f,lineterminator='\n')
    list=[]
    a=int(input("Enter number of items to be added="))
    for i in range(0,a):
        iid=int(input("ENTER PRODUCT ID:"))
        n=input("ENTER PRODUCT NAME:")
        t=input("ENTER PRODUCT TYPE:")
        p=int(input("ENTER PRICE:"))
        gp=int(input("ENTER GST PERCENTAGE:"))
        g=(p*gp)/100
        ne=p+g
        list.append([iid,n,t,p,g,ne])
    c.writerows(list)
    f.close()
    print("------------------------------------------------------------------------------------------------------------------------------------------------")




def search():
    print("------------------------------------------------------------------------------------------------------------------------------------------------")
    f=open("super market.csv","r")
    list=csv.reader(f)
    p=int(input("enter id of product to be searched:"))
    next(f)
    found=0
    for i in list:
        if int(i[0])==p:
            found=1
    if found==1:
        print(i[0].ljust(10),i[1].ljust(10),i[2].ljust(10),i[3].rjust(10),i[4].rjust(10),i[5].rjust(20))
    else:
        print("ITEM NOT FOUND")
    print("------------------------------------------------------------------------------------------------------------------------------------------------")

            

def sum():
    print("------------------------------------------------------------------------------------------------------------------------------------------------")
    f=open("super market.csv","r")
    list=csv.reader(f)
    print("1.calculate total price:")
    print("2.calculate gst price:")
    print("3.calcutale final total price:")
    a=int(input("your choice:"))
    s=0
    next(f)

    if a==1:
          for i in list:
              b=i[3]
              b=int(b)
              s+=b
          print("total price:",int(s))
    elif a==2:
        for i in list:
              b=i[4]
              b=int(b)
              s+=b
        print("total  gst price:",s)
              
    elif a==3:
        for i in list:
              b=int(i[5])
              s+=b
        print("total final price:",s)
    print("------------------------------------------------------------------------------------------------------------------------------------------------")

    

def display():
    print("------------------------------------------------------------------------------------------------------------------------------------------------")
    f=open("super market.csv","r")
    itlist=csv.reader(f)
    print("\t\t\t\tITEM LIST")
    for i in itlist:
        print(i[0].ljust(10),i[1].ljust(10),i[2].ljust(10),i[3].rjust(10),i[4].rjust(10),i[5].rjust(20))
    print("------------------------------------------------------------------------------------------------------------------------------------------------")


def delete():
    f=open("super market.csv","r")
    l=csv.reader(f)
    l2=[]
    a=input("Enter item id to be deleted:")
    g=0
    for i in l:
        if i[0]==a:
            print("Deleting details of ",a)
            g=1
        else:
            l2.append(i)
    if g==0:
        print("no such id.....")
    f=open("super market.csv","w")
    c=csv.writer(f,lineterminator='\n')
    c.writerows(l2)
    f.close()
    print("file after deletion")
    display()


def conditionaldisplay():
    print("------------------------------------------------------------------------------------------------------------------------------------------------")
    f=open("super market.csv","r")
    itlist=csv.reader(f)
    a=int(input("enter the lower limit for final price:"))
    b=int(input("enter th upper limit for final price:"))
    print("\t\t\t\tITEM LIST")
    next(f)
    for i in itlist:
        if int(i[5])<b and int(i[5])>a:
            print(i[0].ljust(10),i[1].ljust(10),i[2].ljust(10),i[3].rjust(10),i[4].rjust(10),i[5].rjust(20))

    print("------------------------------------------------------------------------------------------------------------------------------------------------")


def gst():
    print('''
      5%
      ----------
      packaged foods
      paneer
      coffee
      tea
      agarbatti

      12%
      ----------
      butter
      ghee
      fruit juices
      note books
      frozen meat products
      dry fruits
      sauses
      cutlery items
      board games
      playing cards

      18%
      -----------
      biscuits
      pasta
      jams
      soups
      ice creams
      tampons
      salad dressing

      28%
      -----------
      shaving items
      elecrtonic items
      ''')




print('''\t\t\t\tFRESHMART SUPER MARKET
      \t\t\t\t----------------------''')
print("WELCOME TO FRESHMART!!!!!")
print(" ")
while True:
    print("1.create")
    print(" ")
    print("2.add")
    print(" ")
    print("3.display")
    print(" ")
    print("4.sum")
    print(" ")
    print("5.delete")
    print(" ")
    print("6.search")
    print(" ")
    print("7.conditional display")
    print(" ")
    print("8.current gst values")
    print(" ")
    print("-----------------------------------------------------------------------------------------------------------------------------------------------")
    n=int(input("enter your choice:"))
    if n==1:
        create()
    elif n==2:
        add()
    elif n==3:
        display()
    elif n==4:
        sum()
    elif n==5:
        delete()
    elif n==6:
        search()
    elif n==7:
        conditionaldisplay()
    elif n==8:
        gst()
    else:
        print("invalid choice")

    print(" ")
    a=input("do you want to continue(yes/no):")
    print("------------------------------------------------------------------------------------------------------------------------------------------------")
    if a=="yes":
        pass
    elif a=="no":
        print("FINAL BILL")
        print(" ")
        print("------------------------------------------------------------------------------------------------------------------------------------------------")
        f=open("super market.csv","r")
        itlist=csv.reader(f)
        print("\t\t\t\tITEM LIST")
        for i in itlist:
            print(i[0].ljust(10),i[1].ljust(10),i[2].ljust(10),i[3].rjust(10),i[4].rjust(10),i[5].rjust(20))
            print(" ")
        print("------------------------------------------------------------------------------------------------------------------------------------------------")
        next(f)
        s=0
        for i in f:
           s=s+int(i[5])
           print("total price:",s)
        break
    else:
        break
