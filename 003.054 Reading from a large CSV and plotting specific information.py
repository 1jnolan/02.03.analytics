import pandas as pd

from matplotlib import pyplot

def breaker():
    print("\n**********************\n")

#READING DATA FROM A CSV WITH PANDAS
    
#1. READ THE FILE & CREATE DATAFRAME
df=pd.read_csv('sample.csv')

#2. Test 01 - CHECK THE TYPE OF DATA STORED IN THE DATAFRAME
print(type(df))
breaker()
#3. Test 02 - Print the data.
print(df)
breaker()

#4. Calculating Mean age of people under 24
#Solution 1:
print("Mean weight of people under 24=", df.loc[(df["Age"]<24)]['Weight'].mean())
breaker()

#Solution 2:
"""create a new dataframe "df_under24" which reads in the data for those only under 24 from the first dataframe using loc"""
df_under24=df.loc[(df['Age']<24)]

"""From this new table called: "df_under24" get the mean of the data spec"""
print("Mean weight of people under 24:", df_under24['Weight'].mean())
print(df_under24)
breaker()


#People's average weight grouped by age
"""To group data by a specific catagory use the "groupby" function on the dataframe, you can then get the mean of other data for
that data"""
df2=df.groupby('Age')['Weight'].mean()
print("You can now see the mean weight for each age in the data")
print(df2)

#Plot the data
"""This shows how to plot the data for mean weight of each age group"""
pyplot.title("Average Weight vs Average Height")
pyplot.xlabel("Age")
pyplot.ylabel("Weight")
pyplot.plot(df2)
pyplot.show()