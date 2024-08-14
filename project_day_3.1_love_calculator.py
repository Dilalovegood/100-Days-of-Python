your_name = input("what's ur name: ").lower()
their_name = input("what's ur gf/bf name: ").lower()


name_combine = your_name + their_name
print(f"Your name combination is: {name_combine}")
t = name_combine.count("t")
r = name_combine.count("r")
u = name_combine.count("u")
e = name_combine.count("e")

true = t+r+u+e
# print(type(true))

l = name_combine.count("l")
o = name_combine.count("o")
v = name_combine.count("v")
e = name_combine.count("e")

love = l+o+v+e
# print(type(love))

# switch the data type from int to str and reverse
love_score = str(true) + str(love)
fix_love_score = int(love_score)

if fix_love_score >= 85:
    print(f"Your love score is {love_score}, you guys are grean couple")
elif fix_love_score >= 50 or fix_love_score <= 84:
    print(f"Your love score is {love_score}, you guys are yellow couple")
elif fix_love_score >= 10 or fix_love_score <= 49:
    print(f"Your love score is {love_score}, you guys are red couple")
else:
    ("You love has no score")
