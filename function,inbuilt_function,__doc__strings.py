# def name():
#    print("hi shainaz")
# name()

# def name(s):
#    print("hi shainaz")
# name("shn")

# def name(s):
#     print("hi shainaz "+s)
# name("hw r u")
# name("wr r u")

# def names(*colours):
#     print(" colours are :",colours[:])
#     print(" colours are :",colours[1:])
#     print(" colours are :",colours[0])
#     print(" colours are :",colours[-1])
#     print(" colours are :",colours[::-1])
# names("white","pink","black")

# def details(name,age):
#     print("name is "+name+" and age is "+str(age))
# details("shn",21)
# details("vahid","49")
# details(name='shn',age=21)
# details(age=49 ,name='vahid')
# name=input("enter u rname :")
# age=input("enter u r age is :")
# details(name,age)

# def r(x,y):
#     print("sum is",x+y)
#     print('product is ',x*y)
#     print("reminder is ",x%y)
# r(2,3)
# r(8,2)
# r(10,2)

# def z(p,q):
#     return p*q,p+q
# a=z(6,9)
# b=z(5.8,6.8)
# print(a)
# print(b)

        # " " "pre defined functions" " "
# print(sorted({2,4,1,3.6}))
# print(sorted((9,6,4,7,2,1)))
# print(sorted([3,6.4,9,2,8.8]))

# print(all((False,True,1,0)))
# print(all((True,True,1,0)))
# print(all((True,True,1,)))
# print(all((False,True)))
# print(all((False,True,None)))
# print(all((True,True,None)))
# print(all((True,1)))
# print(all((True,False)))


# print(any((False,0)))
# print(any((True,True,1,0)))
# print(any((True,True,1,)))
# print(any((False,False)))
# print(any((False,True,None)))
# print(any((True,True,None)))
# print(any((True,1)))
# print(any((True,False)))

# print(bool(False))
# print(bool(True))
# print(bool(None))
# print(bool(1))
# print(bool(0))
# print(bool(bool))

# print('eval=',eval('2+6.6-4'))
# print(eval('4.4*6-8'))
# a=eval('9.9+6*5')
# print(a)

# print(sum((1,3,6,8,4)))
# print(sum([1,3,6,8,4]))

# for i in reversed((8,5,3,8.5,2)):
#    print(i,end=",\n")
# for i in reversed([3,4,1,6,7.7,9]):
#    print(i,end=",")

# a=['yellow','pink','white']
# b=enumerate(a)
# print(b,type(b))
# c=list(b)
# print(c,type(c))

# a=['yellow','pink','white']
# c=enumerate(a,8)
# print(list(c))

                  # '''__doc__'''

# def s():
#     '''hi shainaz 
#         '''
# print(s.__doc__)   
            # '''default argument'''
# def info(name="shn",age=21):
#     print("name:",name)
#     print("age:",age)
# info()  
# info('thassu') 
# info(age=20)
# print("thassu",21)
