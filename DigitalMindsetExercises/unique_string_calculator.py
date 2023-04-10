
# SOLUTION 1
def unique_string_calculator(str):
    lowered = str.lower()
    split_str = lowered.split()
    print(split_str)

    for el in split_str:
        print(f'{el}:', split_str.count(el))

unique_string_calculator('hello this is a hello string')
unique_string_calculator('This that and that this')
unique_string_calculator('I am a hello string and I am saying HELLO hello Hello')
