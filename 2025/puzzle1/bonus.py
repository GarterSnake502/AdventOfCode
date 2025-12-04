maxNum = 99
minNum = 0
num = 50
totalZeroes = 0

def moveDirection(dir, amt):
    global num, totalZeroes
    if dir == 'L':
        for i in range(amt):
            num -= 1
            if num < minNum:
                num = maxNum
            if numZero():
                totalZeroes += 1
    else:
        for i in range(amt):
            num += 1
            if num > maxNum:
                num = minNum
            if numZero():
                totalZeroes += 1

def numZero():
    global num
    return (num == 0)

while 1==1:
    inp = input()
    inpDir = inp[0]
    inpAmt = inp[1:]
    moveDirection(inpDir, int(inpAmt))

    print("TotalZeroes is " + str(totalZeroes)
          + "\nNum is " + str(num))
