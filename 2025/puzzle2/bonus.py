# Goal: detect ID ranges, separated by commas. Invalid IDs either:
#   have repeated digits (11, 1010, 18851885, etc) or
#   start with a 0
# Example input: 11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
# 1698522-1698528,446443-446449,38593856-38593862,565653-565659,
# 824824821-824824827,2121212118-2121212124

def checkForRepeat(strToCheck):
    segmentsSame = True
    for divs in range(2, (len(strToCheck) + 1)): # subdivides to string length, +1 to include max
        # print("Testing length " + str(divs))
        if (len(strToCheck) % divs) == 0: # if we can split this properly
            segmentsSame = True

            strOffset = int(len(strToCheck)/divs)

            # print("Itinerary " + str(divs) + 
            #       "\nstrOffset: " + str(strOffset))
            
            segmentPersist = strToCheck[0:strOffset]
            # print("Persist Segment: " + segmentPersist)

            for d in range(1, divs):
                segment = strToCheck[d*strOffset:d*strOffset + strOffset]
                # print("Compare segment: " + segment)
                if segment != segmentPersist:
                    segmentsSame = False
            
            if segmentsSame:
                return True
    
    return False

    #     segmentPersist = strToCheck[0:strMiddleIndex]
    #     counter = 0 # add to each segment so no overlap
    #     for d in range(divs):
    #         segment = strToCheck[d*divs + counter:(d*divs) + strMiddleIndex + counter]
    #         print("SegmentPersist: " + segmentPersist)
    #         print("Segment: " + segment)
    #         if segment != segmentPersist:
    #             segmentsSame = False
    #         counter += 1
    #     if segmentsSame: # pattern repeated--there is repeat!
    #         return True
    #     else:
    #         segmentsSame = True # restart for another itinerary
    # return True

invalidIDs = 0

# if checkForRepeat("123123"):
#     print("123123 REPEAT!")


# if checkForRepeat("123123123"):
#     print("123123123 REPEAT!")


# if checkForRepeat("12931263123"):
#     print("1231231535323 REPEAT!")

print(checkForRepeat("1212121212"))

# split ranges
inp = input()
splitCommas = inp.split(',') # array of ranges
for idRange in splitCommas:
    splitHyphens = idRange.split('-')
    rangeMin = int(splitHyphens[0])
    rangeMax = int(splitHyphens[1])
    for id in range(rangeMin, rangeMax + 1): # +1 so we hit Max
        strId = str(id)
        if (checkForRepeat(str(id))):
            invalidIDs += id
            print("Invalid IDs: " + str(invalidIDs))
    