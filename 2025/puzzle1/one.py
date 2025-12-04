maxNum = 99
minNum = 0
num = 50
totalZeroes = 0

def moveDirection(dir, amt):
    global num
    if dir == 'L':
        for i in range(amt):
            num -= 1
            if num < minNum:
                num = maxNum
    else:
        for i in range(amt):
            num += 1
            if num > maxNum:
                num = minNum

while 1==1:
    inp = input()
    inpDir = inp[0]
    inpAmt = inp[1:]
    moveDirection(inpDir, int(inpAmt))

    if num == 0:
        totalZeroes += 1
        print("TotalZero incremented to " + str(totalZeroes))
    else:
        print("TotalZeroes is " + str(totalZeroes)
              + "\nNum is " + str(num))
