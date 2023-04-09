
def list_comparison(collection1, collection2):

    if collection1 and collection2:
        collection1 = list(collection1)
        collection2 = list(collection2)

        if collection1 == collection2:
            print('Collections have the exact same elements.')
        else:
            print('Collections have different elements.')

    return (collection1, collection2)


print(list_comparison({1, 2, 3}, (1, 2, 3)))
print(list_comparison({1, 2, 3}, (1, 2, 3, 4)))
print(list_comparison({1, 2, 3}, {1:1, 2:2, 3:3}))
