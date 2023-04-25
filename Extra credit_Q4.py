import csv

file = open("riskfactors.csv" , "r")
file1 = open("best_and_worst.txt" , "w")

def analyzef1(file):
    data = {}
    csvReader = csv.reader(file)

    stateLineNumber = 0
    Line1 = 0
    Line2 = 0
    Line3 = 0
    Line4 = 0
    Line5 = 0
    Line6 = 0

    for lines in csvReader:              
        if("State" in lines):
            stateLineNumber = stateLineNumber
            Header = 0
            for headers in lines:
                while(Header != len(lines)):
                    if("Heart Disease Death Rate" in lines[Header]):
                        Line2 = Header
                    elif("Motor Vehicle Death Rate" in lines[Header]):
                        Line3 = Header
                    elif("Teen Birth Rate" in lines[Header]):
                        Line4 = Header
                    elif("Adult Smoking" in lines[Header]):
                        Line5 = Header
                    elif("Adult Obesity" in lines[Header]):
                        Line6 = Header
                    Header = Header + 1
                    
        elif(Line1 > stateLineNumber):
            data[lines[0]] = lines[1:]
        else:
            stateLineNumber = stateLineNumber + 1
        
        Line1 = Line1 + 1
    
    return data, Line2, Line3, Line4, Line5, Line6


        
def analyze_data(infile, data, f1 , f2 , f3 , f4, f5):
    
    heart = []
    motorData = []
    birthData = []
    smokingData = []
    obesityData = []
    
    infile.write("Indicator {0:>30}{1:>30}\n".format("Min" , "Max"))

    for keys in data:
        heart.append(data[keys][f1])
        maxHeart = max(heart)
        if(maxHeart in data[keys]):
            maxHeartState = keys
        minHeart = min(heart)
        if(minHeart in data[keys]):
            minHeartState = keys

        motorData.append(data[keys][f2])
        maxMotor = max(motorData)
        if(maxMotor in data[keys]):
            maxMotorState = keys
        minMotor = min(motorData)
        if(minMotor in data[keys]):
            minMotorState = keys

        birthData.append(data[keys][f3])
        maxBirth = max(birthData)
        if(maxBirth in data[keys]):
            maxBirthState = keys
        minBirth = min(birthData)
        if(minBirth in data[keys]):
            minBirthState = keys

        smokingData.append(data[keys][f4])
        maxSmoking = max(smokingData)
        if(maxSmoking in data[keys]):
            maxSmokingState = keys
        minSmoking = min(smokingData)
        if(minSmoking in data[keys]):
            minSmokingState = keys

        obesityData.append(data[keys][f5])
        maxObesity = max(obesityData)
        if(maxObesity in data[keys]):
            maxObesityState = keys
        minObesity = min(obesityData)
        if(minObesity in data[keys]):
            minObesityState = keys

    infile.write("{0:<35}{1:<20}{2:<10}{3:<20}{4:<10}\n".format("Heart Disease Death Rate (2007):", minHeartState , float(minHeart), maxHeartState, float(maxHeart)))
    infile.write("{0:<35}{1:<20}{2:<10}{3:<20}{4:<10}\n".format("Motor Vehicle Death Rate (2009):", minMotorState , float(minMotor), maxMotorState, float(maxMotor)))
    infile.write("{0:<35}{1:<20}{2:<10}{3:<20}{4:<10}\n".format("Teen Birth Rate (2009):", minBirthState , float(minBirth), maxBirthState, float(maxBirth)))
    infile.write("{0:<35}{1:<20}{2:<10}{3:<20}{4:<10}\n".format("Adult Smoking (2010):", minSmokingState , float(minSmoking.strip("%")), maxSmokingState, float(maxSmoking.strip("%"))))
    infile.write("{0:<35}{1:<20}{2:<10}{3:<20}{4:<10}\n".format("Adult Obesity (2010):",minObesityState , float(minObesity.strip("%")), maxObesityState, float(maxObesity.strip("%"))))
    
    

analyzeFile = analyzef1(file)

data = analyzeFile[0]
f1 = analyzeFile[1] - 1
f2 = analyzeFile[2] - 1
f3 = analyzeFile[3] - 1
f4 = analyzeFile[4] - 1
f5 = analyzeFile[5] - 1

analyzeData = analyze_data(file1 , data, f1, f2, f3, f4, f5)

file.close()
file1.close()
