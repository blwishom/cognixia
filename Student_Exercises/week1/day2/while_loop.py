# while i < 10:
#     print(i)
#     i += 1
# print('End of loop')

# while i > 1:
#     if (i % 2 == 0):
#         print(i)
#     elif (i == 3):
#         break
#     i -= 1


# EXAMPLE OF CONTINUE
# i = 0
# while i < 5:
#     print('Before condition, i:', i)
#     i += 1
#     if (i % 2 == 0): continue
#     print('After condition, i:', i)

# EXAMPLE OF BREAK
i = 0
while i < 3:
    print('in whle loop i:', i)
    i += 1
    # if i == 3:
    #     break
else:
    print('in else i:', i)
print('outside of loop i:', i)
