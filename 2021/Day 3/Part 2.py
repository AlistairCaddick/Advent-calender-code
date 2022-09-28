def readfile ():
    file = open("Input.txt","r")
    binary = []
    line = file.readline()
    line = line.strip('\n')
    while line:
        line = list(line)
        binary.append(line)
        line = file.readline()
        line = line.strip('\n')

    
    return binary



            
def calculate(binary,i):
    if len(binary) == 1:
        print(binary)
        return binary[0]
    one = []
    zero = []
    for x in binary:
        if int(x[i]) == 1:
            one.append(x)
                
        elif int(x[i]) ==0:
            zero.append(x)
    if len(one) < len(zero):
        i+=1
        calculate(zero,i)
        
    else:
        i+=1 
        calculate(one,i)

            

test= readfile()
calculate(test,0)
