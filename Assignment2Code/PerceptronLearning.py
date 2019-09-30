def main():
    # open the file that we are reading
    file = open("../groupA.txt", "r")
    # get each line
    fileContents = file.readlines()

    # arrays of each category
    heightArray = []
    weightArray = []
    genderArray = []

    # for each line we are going to split the text by the commas
    # we will then add each one to the array that it belongs in
    for x in fileContents:
        line = x.split(",")
        heightArray.append(float(line[0]))
        weightArray.append(float(line[1]))
        genderArray.append(float(line[2]))

    maxHeight = max(heightArray)
    minHeight = min(heightArray)
    maxWeight = max(weightArray)
    minWeight = min(weightArray)
    maxGender = max(genderArray)
    minGender = min(genderArray)

    lengthOfWeight = len(heightArray)
    lengthOfHeight = len(weightArray)
    lengthOfGender = len(genderArray)

    # lists that will include the normalized values and all values will initially be 0
    normalizedHeightArray = [0] * lengthOfHeight
    normalizedWeightArray = [0] * lengthOfWeight
    normalizedGenderArray = [0] * lengthOfGender

    normalMin = -.5
    normalMax = .5

    for i in range(0, lengthOfWeight):
        zi = (((weightArray[i] - minWeight) / (maxWeight - minWeight)) * (normalMax - normalMin)) + normalMin
        normalizedWeightArray[i] = zi

    for i in range(0, lengthOfHeight):
        zi = (((heightArray[i] - minHeight) / (maxHeight - minHeight)) * (normalMax - normalMin)) + normalMin
        normalizedHeightArray[i] = zi

    for i in range(0, lengthOfGender):
        zi = (((genderArray[i] - minGender) / (maxGender - minGender)) * (normalMax - normalMin)) + normalMin
        normalizedGenderArray[i] = zi
    

if __name__ == "__main__":
    main()
