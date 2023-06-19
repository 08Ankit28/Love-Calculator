#Print Greeting for the user.
print("Welcome to the Love Calculator!")
#Take input both the names from the user.
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
#Concatenate both the names as one.
string=name1+name2
#Convert the string into lowercase or uppercase.
str1=string.lower()
#Check for the letters 't','r','u','e' and 'l','o','v','e' within the string.
t=str1.count("t")
r=str1.count('r')
u=str1.count('u')
e=str1.count('e')
true=t+r+u+e
l=str1.count('l')
o=str1.count('o')
v=str1.count('v')
e=str1.count('e')
love=l+o+v+e
#join both the counts as a string
love_score= str(true) + str(love)
score=int(love_score)
if score<10 or score>90:
    print("Your score is **",score,"**, you go together like coke and mentos.")
elif score>=40 and score<=50:
    print("Your score is **",score,"**, you are alright together.")
else:
    print("Your score is **",score,"**.")