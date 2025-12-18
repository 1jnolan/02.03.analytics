#creating a CSV file
file=open("myCSV.csv", "w")

#inserting data into the file.
file.write("1,19,27,8,5,9")
file.close()


#**************************************************
#reading from any csv file
file=open("myCSV.csv", "r")
#put the data into a variable
dataIn=file.read()
print(dataIn)

#***********************************************
#DIVIDE UP WHAT YOU HAVE READ IN AND PUT IN A NEW VARIABLE
myList=dataIn.split(",")
#We can 
myList=[int(item) for item in myList]
print(myList)

#Sort the list in order
myList.sort()
print("The list in ascending order", myList)

#Sorting the list in reverse order requires boolean logic. We assign the sort tool with the conditions that
#will reverse the solution
myList.sort(reverse=True)
print("The list in descending order", myList)

#*******************************************************
#REMOVING DATA
#Sometimes there is data that is out of the range. let us assume that any number greater than 20
#should not be in this list.
for item in range(len(myList)):
    for items in myList:
        if items < 10:
            myList.remove(items)
print(myList)
#to keep all items greater than a value:
myList = [item for item in myList if item > 19]
print(myList)
