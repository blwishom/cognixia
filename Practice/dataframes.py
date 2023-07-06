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


# READ CSV and PRINT DF INFO
df = pd.read_csv('imdb.csv')
print(df.head())
print(df.info())


# EXTRACT DATA FROM DF
df = pd.DataFrame([
  ['January', 100, 100, 23, 100],
  ['February', 51, 45, 145, 45],
  ['March', 81, 96, 65, 96],
  ['April', 80, 80, 54, 180],
  ['May', 51, 54, 54, 154],
  ['June', 112, 109, 79, 129]],
  columns=['month', 'clinic_east',
           'clinic_north', 'clinic_south',
           'clinic_west']
)
clinic_north = df['clinic_north']
print(type(clinic_north))
print(type(df))

# CREATE NEW DF WITH COLUMNS FROM ORIGINAL DF
clinic_north_south = df[['clinic_north', 'clinic_south']]
print(type(clinic_north_south))
