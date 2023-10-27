def top_three(input_list):
    input_list.sort()
    tops=input_list[-1:]
    q=sorted(tops, reverse=True)
    return q

list1 = top_three([2,3,5,6,8,4,20,1,12,15,16])
print (list1)