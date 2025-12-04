# TODO: make this code allow for the top 12 inputs

joltage = 0
rankAmount = 12

while 1==1:
    inp = input()
    # determine highest num, then work from there
    highest = [] # append 12 items

    # fill up highest
    for i in range(rankAmount):
        highest.append(0)

    highest[0] = int(inp[0]) # so we can get first number

    highIndex = 0 # what high score we are on
    lastIndex = 0 # so we continue from last high (keeps them in order)
    for high in range(rankAmount):
        index = 0
        for battery in inp:
            power = int(battery)
            # print("highIndex: " + str(highIndex) +
            #       "\nNo go past index " + str((len(inp) - rankAmount) + highIndex))
            #                                         stay 12 or less away from end
            if power > highest[highIndex] and (index <= ((len(inp) - rankAmount) + highIndex)) and index > lastIndex:
                highest[highIndex] = power
                lastIndex = index
                # print("Appending " + str(power) + " at index " + str(index))
            index += 1
        highIndex += 1


    # highest = int(inp[0])
    # # keep track of index
    # index = 0
    # highestIndex = 0
    # for battery in inp:
    #     power = int(battery)
    #     if power > highest and index != (len(inp) - 1):
    #         highest = power
    #         highestIndex = index
    #     index += 1

    # secondHighest = 0
    # # determine second highest
    # index = 0
    # for battery in inp:
    #     power = int(battery)
    #     if power > secondHighest and index > highestIndex:
    #         secondHighest = power
    #     index += 1
    
    
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

    print(highest)

    combinedNumberStr = ""
    for high in highest:
        combinedNumberStr += str(high)
    combinedNumberInt = int(combinedNumberStr)


    joltage += combinedNumberInt
    print("Joltage: " + str(joltage))
