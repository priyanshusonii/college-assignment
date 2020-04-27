def common_data(list1, list2):
    result = False
    for x in list1:
        for y in list2:
            if x == y:
                result = True
                return result
print(common_data([121,222,332,432,125], [125,236,457,678,779]))
print(common_data([1,2,3,4,5], [6,7,8,9]))

#output

#
#True
#None
#
