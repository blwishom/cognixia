# CREATE DF
df1 = pd.DataFrame({
  'Product ID': [1, 2, 3, 4],
  'Product Name': ['t-shirt', 't-shirt', 'skirt', 'skirt'],
  'Color': ['blue', 'green', 'red', 'black']
})

print(df1)

# ADD ROWS 3-4 and ADD COLUMN NAMES
df2 = pd.DataFrame([
  [1, 'San Diego', 100],
  [2, 'Los Angeles', 120],
  [3, 'San Francisco', 90],
  [4, 'Sacramento', 115]
],
  columns=[
    'Store ID',
    'Location',
    'Number of Employees'
  ])

print(df2)


# TRANSFORM DF TO CSV FORMAT
''' name,cake_flavor,frosting_flavor,topping
Chocolate Cake,chocolate,chocolate,chocolate shavings,
Birthday Cake,vanilla,vanilla,rainbow sprinkles,
Carrot Cake,carrot,cream cheese,almonds '''


# READ CSV and CONVERT TO DF
df = pd.read_csv('sample.csv')
print(df)
