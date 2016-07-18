# This is an example of analysing a database using pandas
# The data is from the historic survey of housing in San Francisco
import pandas

# Read in the database
df = pandas.read_csv('Historic_Secured_Property_Tax_Rolls.csv')

# Number of entries
numentry = len(df)

# Descending list of number of properties with specific codes
a = df['Property Class Code'].value_counts()

# Answer the first question of the most common class fraction
print("The fraction of the most common class is: ", a[0]/len(df))

# Answer the second question.
#   1. take only the non-zero improvement values
#   2. Sort by date
#   3. Remove old entries for duplicated property listed
b = df[df['Closed Roll Assessed Improvement Value']>0].sort('Current Sales Date',ascending=False).groupby('Block and Lot Number').head(1)

#   4. Find the average

print("The average assessed improvement value, for non-zero, is: ", b['Closed Roll Assessed Improvement Value'].mean())

# All of the values of neighborhood codes
b['Neighborhood Code'].unique()