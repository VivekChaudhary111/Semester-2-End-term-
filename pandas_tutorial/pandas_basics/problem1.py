import pandas as pd

data = {'ID':[1,2,3,4],'Name':['Alice','Bob','Charlie', 'Dana'], 'Age':[25, 30, 28, 35], 'Gender':['Female','Male', 'Male', 'Female'], 'City':['New York', 'London', 'Paris', 'Berlin']}
df = pd.DataFrame(data)
# print(df)

# part a
unique_cities = df.City.unique()
# print(unique_cities)

# part b
average_age = df.Age.mean()
# print(average_age)

# part c
male_df = df.loc[df['Gender'] == 'Male']
# print(male_df.Gender.count())
female_df = df.loc[df['Gender'] == 'Female']
# print(female_df.Gender.count())

# part d
oldest_person = df.loc[df['Age'] == df.Age.max()]
# print(oldest_person.Name)

# part e
most_popular_city = df.City.mode()
print(most_popular_city)

