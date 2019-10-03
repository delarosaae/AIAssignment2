import numpy as np
import math
import matplotlib.pyplot as plt

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


    percent = .75
    #percent = .25
    trainArray, testArray = percentData(normalizedHeightArray, normalizedWeightArray, normalizedGenderArray, percent)

    ep = .00001
    #ep = 100
    #ep = 1450
    train(trainArray, ep, lengthOfHeight, genderArray, normalizedHeightArray, normalizedWeightArray)


def train(trainArray, epsilon, numberOfInputs, normGender, height, weight):
    f = open("ASoft.txt", "w+")
    tc = 5000
    np = numberOfInputs
    ni = 3
    alpha = .1
    weights = [0, 0, 0]
    dOut = normGender
    num = random.uniform(-.5, .5)
    num1 = random.uniform(-.5, .5)
    num2 = random.uniform(-.5, .5)
    weights[0] = num
    weights[1] = num1
    weights[2] = num2

    trainIt = trainArray
    # dout = [-.5, .5]
    sentianl = False
    totalTE = 0
    ou = [0.0] * len(normGender)
    err = 0
    learn = 0

    for i in range(0, tc):
        for j in range(0, np):
            net = 0
            for k in range(0, ni -1):
                net = net + weights[k] * trainIt[j][k]
            ou[j] = sign(net)
            # ou = sign(net)
            err = dOut[j] - ou[j]
            te = err * err
            totalTE = totalTE + te
            learn = alpha * err
            #print(i, j, net, err, learn, weights, f, totalTE)
            #f.write("ite= " + str(i) + "  p=" + str(j) + " net= " + str(net) + " err= " + str(err) + " lrn= " + str(learn) + " wei= " + str(weights[0]) +" , " + str(weights[1]) + " , " + str(weights[2]) + "\n")
            for b in range(0, ni):
                weights[b] = weights[b] + learn*trainIt[j][b]
            #print(totalTE)
        if totalTE < epsilon:
            break
        #print(totalTE)
    print(err)
    print(learn)
    print(weights)
    print(totalTE)


    #plt.scatter(height, weights)
    #plt.plot()
    #plt.show()




    #f.write("total error = " + str(totalTE))
    #f.close()


def printArr(i, j, net, err, learn, weights, f, te):
    print("ite= " + i + "  p=" + j + " net= " + net + " err= " + err + " lrn= " + learn + " wei= " + weights + "   TE= " +te)


# hard activation
#def sign(net):
#    number = net
#    y = .5
#    if number > 0:
#        y = .5
#    else:
#        y = -.5
#    return y

# soft activation
def sign(net):
    k = 3
    o = (1) / (1 + math.exp(k * net * (-1)))
    return o


# this method will return to use the training and testing data
def percentData(height, weight, gender, percent):

    # all the lists with all the original values
    fullWeight = weight
    fullHeight = height
    fullGender = gender

    menWeight = fullWeight[:2000]
    menHeight = fullHeight[:2000]
    menGender = fullGender[:2000]
    womenWeight = fullWeight[2000:]
    womenHeight = fullHeight[2000:]
    womenGender = fullGender[2000:]

    # get the percent, then get where to find the first index where we will split
    # our data into both sets. From 0 to indexToGetPercent is our training and from index + 1 to end is testing
    value = percent
    lengthOfArray = len(fullWeight)
    indexToGetPercent = int(value * lengthOfArray)



    menWeightTraining = menWeight[:indexToGetPercent]
    menWeightTesting = menWeight[indexToGetPercent:]
    menHeightTraining = menHeight[:indexToGetPercent]
    menHeightTesting = menHeight[indexToGetPercent:]
    menGenderTraining = menGender[:indexToGetPercent]
    menGenderTesting = menGender[indexToGetPercent:]

    womenWeightTraining = womenWeight[:indexToGetPercent]
    womenWeightTesting = womenWeight[indexToGetPercent:]
    womenHeightTraining = womenHeight[:indexToGetPercent]
    womenHeightTesting = womenHeight[indexToGetPercent:]
    womenGenderTraining = womenGender[:indexToGetPercent]
    womenGenderTesting = womenGender[indexToGetPercent:]

    weightTraining = menWeightTraining + womenWeightTraining
    weightTesting = menWeightTesting + womenWeightTesting
    heightTraining = menHeightTraining + womenHeightTraining
    heightTesting = menHeightTesting + womenHeightTesting
    genderTraining = menGenderTraining + womenGenderTraining
    genderTesting = menGenderTesting + womenGenderTesting

    trainArray = list(zip(weightTraining, heightTraining, genderTraining))
    testArray = list(zip(weightTesting, heightTesting, genderTesting))

    return trainArray, testArray




if __name__ == "__main__":
    main()
