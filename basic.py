###
# There are 5 types of data structures (Tuples, set , list ,dictionaries, string)
#Tuples
# Tuples can have all data types which can be enclosed by paranthesis but seperated by commas

t=(1,2,3,"hello",3.14)
print(type(t))
t

#Tuples are immutable(i.e cannot alter a single element or change the element)
#eg : del t[1] we will get type error
#indexing (0th ,1st,2nd,3rd,4th...) 
t[0]
t[1]
### unpacking (assigning variables to elements in tuple and then calling each variable)
a,b,c,d,e=t
a

#slicing (start : stop :step)
t[1:4]
t[::1]
t[-1] # from last
t[::-1]# reverse

# methods performed in tuple
#t.count(3)
#index()

#Built in functions
#min(t), max(),len(),sorted(),sum(),tuple()(to convert dictionaries or other structures to tuple)
#max(t) # type error :since this tuple has all data types
#creation , repition (t*2), concatenation 

b1=(1,34,5,6,7,8)
b1.count(34)
# Tuple membership
print(2 in b1)
#we can iterate using tuple
for name in ("Sharm", "Sharu"):
    print("hello,", name)

# List are mutable (ie , single element can be accessed or changed)
#methods:
# append(), extend(), reverse(),index(), pop()
#l1.append(4)---adds 5 to last place
#li.insert(1,2)---adds 1 to the 2nd position
#l1.remove('p')---removes particular element
#l1.pop(1)---removes element in the particular position 1 and returns the element
#l1.reverse()---reverse
l1=[1,2,4,5,6]
l1.pop(2)
#