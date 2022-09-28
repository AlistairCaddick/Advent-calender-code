def readfile ():
    f = open("input.txt")
    inputs = []
    line = f.readline()
    line = line.strip('\n')
    while line:
        line = int(line)
        inputs.append(line)
        if line == 10526:
            break
        line = f.readline()
        line = line.strip('\n')
        line = int(line)
    return inputs

def compare(inputs):
    count = 0
    for i in range(0,len(inputs)-1):
        if inputs[i+1] > inputs[i]:
            count += 1

        i += 1
    print(count)
    return count



def compress(inputs):
    compressed = []
    for i in range(0,len(inputs)-1):
        if i == len(inputs)-3:
            first = inputs[i]
            second = inputs[i+1]
            third = inputs[i+2]
            total = first + second + third
            compressed.append(total)
            break
        first = inputs[i]
        second = inputs[i+1]
        third = inputs[i+2]
        total = first + second + third
        compressed.append(total)
        i+=1
    return compressed


answer = readfile()
sums = compress(answer)
test = compare(sums)



