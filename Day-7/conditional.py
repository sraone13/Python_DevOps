import sys

type = sys.argv[1]

if type == "t2.micro":
    print("it charges the 2 dollers")

elif type == "t2.medium":
    print("it charges the 4 dollers")

elif type == "t2.large":
    print("it charges the 6 dollers")

else:
    print("please provide the valid type")
