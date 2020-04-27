list_priyanshu1 = [{},{},{}]
list_priyanshu2 = [{123,2345},{},{}]
print(all(not d for d in list_priyanshu1))
print(all(not d for d in list_priyanshu2))


#output:
#
#True
#False
#
