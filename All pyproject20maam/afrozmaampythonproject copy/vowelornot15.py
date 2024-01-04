#Write a program to determine whether the character entered is a Vowel or not
n=input(" enter a word ")
vowels=("a","e","i","o","u")

if n.lower() in vowels:
    print("It is a vowel")
else:
    print("not a vowel")

