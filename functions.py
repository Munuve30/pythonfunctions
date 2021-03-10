#calling a function
def my_function():
    print("Wagwaan!")
my_function()

#calling a function
def my_name():
    print("Stop!")
my_name()

#calling a function
def st_tr():
    print("Kimeumana!")
st_tr()

#calling a function
def tr_tr():
    print("bOGAS!")
tr_tr()

#arguements
def sum(r,y):
    u=r+y
    print("The sum is", u)
sum(409,456)

#arguements
def sum(p,y):
    a=p+y
    return("The sum is",a)
print(sum(20,30))

#arguements
def product(r,t):
   b=r/t
   print("The product is", b)
   
product(7,5)

#arbitrary args using print
def courses(*args):
    for subject in args:
        print(subject)
courses("Big Data", "CCNA", "OOP2")

#arbitrary args using print
def courses(*units):
    for subjects in units:
        print(subjects)
courses("Database Management", "OOSAD", "Professional Ethics")



#arbitrary args using return
def courses(*args):
    for subject in args:
        return subject
print(courses("Big Data","CCNA"))

#arbitrary keyword arguements
def units(**turo):
    for key, value in turo.items():
        print("{}:{}". format (key,value))
units(first='Big data', second='CCNA', third='HCIA')

#default parameter value
def Africa(Country = "Kenya"):
    print("I am from "+ Country)
Africa()
Africa("South Africa")
Africa("Nigeria")
Africa("Egypt")

#passing a list as an arguement
def mimi_wewe(fruits):
    for c in fruits:
        print(c)
fruits = ["banana", "cherry", "apple"]
mimi_wewe(fruits)

#area of a rectangle  using functions

def area(l,w):
    a=l*w
    print("The area of the rectangle is ", a)
area(4,7)
    
#area of a cicrcle  using functions

def area(r):
    pi=3.142
    a=pi*(r*r);
    print("The area of the circle is ", a)
area(7)

#volume of a sphere  using functions

def volume(r):
    pi=3.142
    v= 4/3*pi*(r*r*r);
    print("The volume of the sphere is ", v)
volume(7)


#volume of a cylinder using functions

def volume_cylinder(r,h):
    pi=3.142
    v=pi*(r*r)*h;
    print("The volume is ", v)
volume_cylinder(7,12)

