import numpy as np
from matplotlib import pyplot as plt

def dataScraper(dataFile):

    importantList = []

    count = 0

    for i in dataFile:

        count += 1

        if (count == 1):
            continue

        importantList.append(i.split(","))

    return importantList
    

dataFile = open("Student Mental health.csv", "r")

importantList = dataScraper(dataFile)

dataFile.close()

selectDepressionRates = []
selectAnxietyRates = []
selectPanicRates = []

overallDepressionRates = []
overallAnxietyRates = []
overallPanicRates = []

for i in importantList:

    score = 0

    count = -1

    for x in i:

        count += 1

        if (x == 'Male'):
            score += 1

        elif (count == 2 and x != ''):
            if (int(x) >= 18 and int(x) <= 21):
                score += 1

        elif (x == 'Engineering'):
            score += 2

        elif (x == 'year 1' or x == 'year 2'):
            score += 1

        elif (count == 5 and x == '2.50 - 2.99' or x == '0 - 1.99' or x == '2.00 - 2.49' or x == '3.00 - 3.49' or x == '3.50 - 4.00'):
            score += 1
        
        elif (count == 6 and x == 'Yes'):
            score += 1

        elif (count == 7 and score > 4):
            if (x == 'Yes'):
                selectDepressionRates.append(1)
            else:
                selectDepressionRates.append(0)
        
        elif (count == 8 and score > 4):
            if (x == 'Yes'):
                selectAnxietyRates.append(1)
            else:
                selectAnxietyRates.append(0)

        elif (count == 9 and score > 4):
            if (x == 'Yes'):
                selectPanicRates.append(1)
            else:
                selectPanicRates.append(0)

    if (i[7] == 'Yes'):
        overallDepressionRates.append(1)
    elif (i[7] == 'No'):
        overallDepressionRates.append(0)
    if (i[8] == 'Yes'):
        overallAnxietyRates.append(1)
    elif (i[8] == 'No'):
        overallAnxietyRates.append(0)
    if (i[9] == 'Yes'):
        overallPanicRates.append(1)
    elif (i[9] == 'No'):
        overallPanicRates.append(0)

npSelectDepression = np.array(selectDepressionRates)
npSelectAnxiety = np.array(selectAnxietyRates)
npSelectPanic = np.array(selectPanicRates)

npOverallDepression = np.array(overallDepressionRates)
npOverallAnxiety = np.array(overallAnxietyRates)
npOverallPanic = np.array(overallPanicRates)


print("Select Depression Rates Average: " + str(round(np.mean(npSelectDepression), 2)))
print("Select Anxiety Rates: " + str(round(np.mean(npSelectAnxiety), 2)))
print("Select Panic Rates: " + str(round(np.mean(npSelectPanic), 2)))

print("\n")

print("Overall Depression Rates Average: " + str(round(np.mean(npOverallDepression), 2)))
print("Overall Anxiety Rates Average: " + str(round(np.mean(npOverallAnxiety), 2)))
print("Overall Panic Rates Average: " + str(round(np.mean(npOverallPanic), 2)))
        
anxietyBinomial = np.random.binomial(len(selectAnxietyRates), 0.4, size=10000) / float(len(selectAnxietyRates))

plt.hist(anxietyBinomial, range=(0,1), bins=20)
plt.show()

importantPrediction = np.mean(anxietyBinomial >= 0.2)
print("\nChances of having anxiety: " + str(importantPrediction))