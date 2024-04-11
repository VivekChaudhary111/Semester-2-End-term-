import pandas as pd

student_scores = {'ID':[1,2,3,4],'Name':['Alice','Bob','Charlie', 'Dana'], 'Math_score':[85, 75, 90, 80], 'Science_score':[90,85,80,95]}
df = pd.DataFrame(student_scores)
# print(df)

# part a
average_math_score = df.Math_score.mean()
# print(average_math_score)

# part b
highest_science_score = df.Science_score.max()
# print(highest_science_score)

# part c
df['Total_score'] = df['Math_score'] + df['Science_score']
# print(df)

# part d
highest_total_score = df.loc[df['Total_score']==df['Total_score'].value_counts().idxmax()]
print(highest_total_score['Name'])

# part e
diff =df['Math_score'].mean() - df['Science_score'].mean()
print(diff)