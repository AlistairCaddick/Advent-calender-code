def readfile ():
    file = open("Input.txt","r")
    binary = []
    for line in file:
        binary.append(line)
    
    return binary



            
def calculate(binary):
    most = []
    least = []
    for i in range(0,12):
        one = 0
        zero = 0
        for x in binary:
            if int(x[i]) == 1:
                one += 1
            elif int(x[i]) ==0:
                zero += 1
        if one > zero:
            most.append(1)
            least.append(0)
        else:
            most.append(0)
            least.append(1)

    print(most)
    print(least)
            

test= readfile()
calculate(test)
