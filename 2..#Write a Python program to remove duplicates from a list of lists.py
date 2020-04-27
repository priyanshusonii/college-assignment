import itertools
number = [[110, 120], [240], [330, 456, 425], [310, 220], [133], [240]]
print("Original List", number)
number.sort()
new_number = list(number for number,_ in itertools.groupby(number))
print("New List", new_number)

#output:

#
#Original List [[110, 120], [240], [330, 456, 425], [310, 220], [133], [240]]
#New List [[110, 120], [133], [240], [310, 220], [330, 456, 425]]
#
