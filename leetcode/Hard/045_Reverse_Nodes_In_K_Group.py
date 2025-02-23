# THIS SOLUTION CURRENTLY IS NOT WORKING
from Node_Lib import Node
def reverse_node_in_k_group(n: Node, k: int) -> Node:
    recnst_arr = []
    m = n
    inx = 0
    while n is not None:
        if inx % k == 0:
            prev, curr = None, m 
            while curr != n:
                next = curr.next 
                curr.next = prev 
                prev = curr 
                curr = next 
            recnst_arr.append(prev)
            m = n 
        inx += 1 
        n = n.next 
    
    if m is not None:
        recnst_arr.append(m)
                
            
