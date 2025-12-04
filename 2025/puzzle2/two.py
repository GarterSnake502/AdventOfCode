# Goal: detect ID ranges, separated by commas. Invalid IDs either:
#   have repeated digits (11, 1010, 18851885, etc) or
#   start with a 0
# Example input: 11-22,95-115,998-1012,1188511880-1188511890,222220-222224,
# 1698522-1698528,446443-446449,38593856-38593862,565653-565659,
# 824824821-824824827,2121212118-2121212124

def checkForRepeat(strToCheck):
    strMiddleIndex = int(len(strToCheck)/2)
    strFirst = strToCheck[0:(strMiddleIndex)]
    strEnd = strToCheck[strMiddleIndex:]
    return (strFirst == strEnd)

invalidIDs = 0

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
    