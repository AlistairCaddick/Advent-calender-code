def readfile ():
    file = open("Inputs.txt","r")
    forward = []
    down = []
    up = []
    for line in file:
        line = list(line)
        if line[0] == "f":
            value = int(line[8])
            forward.append(value)
        elif line[0] == "d":
            value = int(line[5])
            down.append(value)
        elif line[0] == "u":
            value = int(line[3])
            up.append(value)
    return forward,down,up
            

    
        
readfile()


def calculate(f,u,d):

    if up > down:
        move = up - down
    else:
        move = down - up

    total = forward * move
    print(forward)
    print(move)
    print(total)
        


options = readfile()

calculate(options[0],options[2],options[1])
