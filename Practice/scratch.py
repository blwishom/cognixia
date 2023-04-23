#KEY WORD ARGUMENTS
def keyword_arguments(element1, element2, element3, element4):
    print(f'This is element1: {element1}, element2: {element2}, element3: {element3}, element4: {element4}')

# keyword_arguments(element3 = 1, element1 = 8, element4 = 78, element2 = 400)
# keyword_arguments(element3 = 'orange', element1 = 8, element4 = 'after orange', element2 = 'before orange')


# ARGUMENT LISTS (*args) and (*kwargs)
def argument_list(*args):
        print(f'These are the args: {args} auto saved into a tuple.')

# argument_list('arg1', 2, 'arg3', 4)

def kwarg_list(**kwargs):
        print(f'These are the kwargs: {kwargs} auto saved into a dictionary.')

# kwarg_list(kwarg1 = 2, kwarg2 = 4)

# PRINT FUNCTIONS
print(1, 2, 3, sep = ' + ')
print(4, 5, 6, sep = ' + ', end='\t')
print('print after t')
print(3, 2, 1, sep = ' + ', end='\n')
print('print after n')
print(3, 2, 1, sep = ' + ', end='\n\n')
print('print after nn')


# LAMBDA FUNCTIONS
def my_map(sequence, mapper):
 res = []
 for elm in sequence:
    res.append(mapper(elm))
 return res

print(my_map([1,2,3], lambda x: x * 10))
print(my_map([1,2,3], lambda x: f"{x}!"))
