import pandas as pd
cancerdb = pd.read_csv('/home/blair/cognixia/kaggle_cancerdb.csv')

# print(cancerdb['tissue'])

cancerDataFrame = pd.DataFrame({
    'Title:': cancerdb['title'][:20],
    'Tissue:': cancerdb['tissue'][:20],
    'Location:': cancerdb['city'][:20],
    'Description:': cancerdb['description'][:20]
})

print(cancerDataFrame)
