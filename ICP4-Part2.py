### Hieu Trinh
### ICP 4 - Task 2
### 09/20/18

import numpy as np

vectorNum = np.random.randint(0,21,15)
for x in range (0, len(vectorNum)):
    print vectorNum[x]

def mostFrequent(numArray):
    numFrequent = []
    numDict = {}
    numDictCounter = -1
    
    for i in range(0,len(numArray)):
        if numArray[i] in numDict:
            continue
        else:
            numDict[numArray[i]] = np.count_nonzero(numArray == numArray[i])
    
    print("\n")
    
    for k in numDict:
        print (str(k) + " " + str(numDict[k]))

    for k in numDict:
        maxNum = max(numDict)
        if numDict[k] == max:
            numFrequent.append(k)
    
    return numFrequent

print("\n" + str(mostFrequent(vectorNum)))

### END ###