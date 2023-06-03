contains_a = lambda word: 'a' in word

print(contains_a("banana"))
print(contains_a("apple"))
print(contains_a("cherry"))


long_string = lambda str: len(str) > 12

print(long_string("short"))
print(long_string("photosynthesis"))


ends_in_a = lambda str: str.endswith('a')
# ends_in_a = lambda str: str[-1] is 'a'

print(ends_in_a("data"))
print(ends_in_a("aardvark"))
