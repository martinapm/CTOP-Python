from random import choice, sample

my_list = [x for x in range(20)]

ganadores = ['C', 'M', 'A']

ganadores_list = sample(my_list, 3)


for g in ganadores_list:
    print(ganadores[0] +': ' + str(ganadores_list[0]))
    print(ganadores[1] +': ' + str(ganadores_list[1]))
    print(ganadores[2] +': ' + str(ganadores_list[2]))

