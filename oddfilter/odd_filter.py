# Create a function that takes a list as a parameter,
# and returns a new list with every odd number from the orignal list
# example: [1, 2, 3, 4, 5] should produce [1, 3, 5]

old_list=[]
newlist = []

def odd_filter(old_list):
    for i in old_list:
        if i % 2 == 1:
            newlist.append(i)
    return(newlist)


print(odd_filter([1, 2, 3, 4, 5]))  # should print [1, 3, 5]