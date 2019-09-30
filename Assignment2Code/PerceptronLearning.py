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



if __name__ == "__main__":
    main()
