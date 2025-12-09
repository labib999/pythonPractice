import datetime
def question(a):
    match a:
        case 0: 
            return input("write your ugly name: ")
        case 1: 
            return int(input("which year were u born in?: ")) 
        case 2:
            return input("university name?: ")
        case 3:
            return int(input("which semester?: "))
        case 4:
            return float(input("u knew it was coming...write the insignificant cg of urs: "))
def ask():
    var = [] 
    for i in range(5):
        while True:
            try:
                var.append(question(i))
                break
            except:
                match i:
                    case 1:
                        print("age needs to be integer year")
                    case 3:
                        print("semester should be in integer eg: 5,6,9")
                    case 4:
                        print("cgpa should be in float")
    intro(var[0],var[1],var[2],var[3],var[4])

def intro(name,age,uni,semester,cgpa):
    print(f"hi my name is {name.upper()}. I am {datetime.datetime.now().year - age} years old. I am currently studying in {uni.upper()} and in {semester}th semester. Even tho I didnt wanted to say it but my cgpa is {cgpa}. Thanks")

def main():
    ask()
    while True:
        umm = input("keep going?: y = yes...n = no ")
        if umm == "n":
            print("nice one ngga")
            break
        else:
            ask()

main()
