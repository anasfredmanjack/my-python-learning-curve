ninjas = ['emma', 'fred', 'yoshi']

# for ninja in ninjas:
#  print(ninja)

#how to print just a portion of the list
# for ninja in ninjas[1:2]:
#     print(ninja)

for ninja in ninjas:
    if ninja =='fred':
        print(f'{ninja} -- black ninja')
        #how to break out of a loop
        break
    else:
        print(ninja)
