#merge k sorted lists

# import heapq
# def merge_k_sorted_lists(lists: list[list[int]]) -> list[int]:

#     min_heap=[]
#     res=[]

#     for i in range(len(lists)):
#         if lists[i]:
#             heapq.heappush(min_heap,(lists[i][0],i,0))


#     while min_heap:
#         val,l_idx,e_idx=heapq.heappop(min_heap)
#         res.append(val)

#         if e_idx+1 < len(lists[l_idx]):
#             nxt_val=lists[l_idx][e_idx+1]
#             heapq.heappush(min_heap,(nxt_val,l_idx,e_idx+1))


#     return res


# print(merge_k_sorted_lists(lists=[[1,4,5],[1,3,4],[2,6]]))        



import heapq
def merge_k_sorted_lists(lists: list[list[int]]) -> list[int]:

    min_heap=[]
    res=[]
    
    #push first elements of all lists
    for i in range(len(lists)):
        if lists[i]:
            heapq.heappush(min_heap,(lists[i][0],i,0))

    #pop min heap and store it and then append it to result
    while min_heap:
        val,l_idx,e_idx=heapq.heappop(min_heap)
        res.append(val)
        

        #if more elements in same lists then do this
        if e_idx+1<len(lists[l_idx]):
            nxt_val=lists[l_idx][e_idx+1]
            heapq.heappush(min_heap,(nxt_val,l_idx,e_idx+1))  

    return res   

print(merge_k_sorted_lists(lists=[[1,4,5],[1,3,4],[2,6]]))                



#copy list with random pointer
from typing import Optional
def copy_list_with_random_pointer(nodes: list[tuple[int, Optional[int]]]) -> list[tuple[int, Optional[int]]]:

    if not nodes:
        return []
    
    new_nodes=[(val,None) for val,_ in nodes]

    for i in range(len(nodes)):
        val,ran_idx=nodes[i]
        new_nodes[i]=(val,ran_idx)


    return new_nodes

print(copy_list_with_random_pointer(nodes=[(7,None),(13,0),(11,4),(10,2),(1,0)]))    


