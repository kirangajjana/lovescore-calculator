name1=input("enter your boyfriend name")
name2=input("enter your girlfriend name")

couple=name1+name2
new=couple.lower()
#finding the truelove percentage

#True Love percentage based on your names
#true
t=new.count('t')
r=new.count('r')
U=new.count('u')
e=new.count('e')
true=t+r+U+e
#lover
l=new.count('l')
o=new.count('o')
v=new.count('v')
e=new.count('e')
love=l+o+v+e
lovescore=str(true)+str(love)
new=int(lovescore)
#love percentage
if new>=10 or new<=90:
    print(f"your love score between {name1} and {name2} is {lovescore}")