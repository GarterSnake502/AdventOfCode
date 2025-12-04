joltage = 0

while 1==1:
    inp = input()
    # determine highest num, then work from there
    highest = int(inp[0])
    # keep track of index
    index = 0
    highestIndex = 0
    for battery in inp:
        power = int(battery)
        if power > highest and index != (len(inp) - 1):
            highest = power
            highestIndex = index
        index += 1

    secondHighest = 0
    # determine second highest
    index = 0
    for battery in inp:
        power = int(battery)
        if power > secondHighest and index > highestIndex:
            secondHighest = power
        index += 1
    
    
    # order them
    # firstOrder = 0
    # secondOrder = 0
    # for battery in inp:
    #     power = int(battery)
    #     if power == highest:
    #         firstOrder = highest
    #         secondOrder = secondHighest
    #         break
    #     elif power == secondHighest:
    #         firstOrder = secondHighest
    #         secondOrder = highest
    #         break

    combinedNumberStr = str(highest) + str(secondHighest)
    combinedNumberInt = int(combinedNumberStr)


    joltage += combinedNumberInt
    print("Joltage: " + str(joltage))
