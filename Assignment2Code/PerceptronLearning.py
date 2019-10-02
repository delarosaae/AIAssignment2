
import random

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


def train(trainArray, testArray):
    tc = 5000
    np = len(trainArray)
    ni = 3
    alpha = 0.1
    weights = [0,0,0]
    for i in range(0,2):
        num = random.uniform(-3, 3)
        weights[i] = round(num, 2)
    train = trainArray
    dout = [0, 1]

    sentinal = False
    for i in range(0, tc -1):
        for j in range(0, np - 1):
            net = 0
            for k in range(0, ni):
                net = net + weights[k] * train[j][k]
            ou = sign(net)
            err = dout[j] - ou
            learn = alpha * err
            for i in range(0, ni):
                weights[i] = weights[i] + learn*train[j][k]


# hard activation
def sign(array):
    number = array.pop(0)
    y = .5
    if number > 0:
        y = 1
    else:
        y = 0
    return y

# soft activation
def sign(net):
    k = 3
    o = (1) / (1 + 10**(k * net * (-1)))
    return o


# this method will return to use the training and testing data
def percentData(weight, height, gender, percent):

    # all the lists with all the original values
    fullWeight = weight
    fullHeight = height
    fullGender = gender

    # get the percent, then get where to find the first index where we will split
    # our data into both sets. From 0 to indexToGetPercent is our training and from index + 1 to end is testing
    value = percent
    lengthOfArray = len(fullWeight)
    indexToGetPercent = int(value * lengthOfArray)

    weightTraining = fullWeight[:indexToGetPercent]
    weightTesting = fullWeight[indexToGetPercent:]
    heightTraining = fullHeight[:indexToGetPercent]
    heightTesting = fullHeight
    genderTraining = fullGender[:indexToGetPercent]
    genderTesting = fullGender

    return weightTraining, weightTesting, heightTraining, heightTesting, genderTraining, genderTesting




if __name__ == "__main__":
    main()
