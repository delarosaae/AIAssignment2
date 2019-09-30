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

    lengthOfWeight = len(heightArray)
    lengthOfHeight = len(weightArray)

    # lists that will include the normalized values and all values will initially be 0
    normalizedHeightArray = []
    normalizedWeightArray = [0] * lengthOfWeight
    normalizedGenderArray = []

    for i in range(0, lengthOfWeight):
        zi = (weightArray[i] - minWeight) / (maxWeight - minWeight)
        normalizedWeightArray[i] = zi
    for y in normalizedWeightArray:
        print(y)



if __name__ == "__main__":
    main()
