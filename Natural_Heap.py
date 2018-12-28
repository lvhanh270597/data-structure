#!/usr/bin/env python
# coding: utf-8

# In[113]:


import random

lst_nodes = []
# Heap Min
def bigger(a, b):
    return lst_nodes[a].get_cur() > lst_nodes[b].get_cur()
class Heap:
    def __init__(self):
        self.elements = []
        self.size = 0    
    def insert(self, index):
        self.elements.append(index)
        self.size += 1
        i = self.size - 1
        val_i = index
        while i > 0:
            j = (i - 1) // 2
            if bigger(self.elements[j], val_i):
                self.elements[i] = self.elements[j]
                i = j
            else: break
        self.elements[i] = val_i            
    def get_top(self):
        return lst_nodes[self.elements[0]].get_cur()
    def pop_top(self):
        if self.size == 0: return 
        if self.size == 1:
            del self.elements[0]
            self.size = 0
            return 
        first_id = self.elements[0]
        lst_nodes[first_id].next_to()
        if lst_nodes[first_id].check_finish():        
            self.elements[0] = self.elements[-1]
            del self.elements[-1]        
            self.size -= 1    
        i = 0
        j_1, j_2 = i*2+1, i*2+2
        j = j_2 if (j_2 < self.size) and bigger(self.elements[j_1], self.elements[j_2]) else j_1
        val_i = self.elements[0]        
        while j < self.size:
            if bigger(val_i, self.elements[j]):
                self.elements[i] = self.elements[j]                
                i = j
            else: break
            j_1, j_2 = i*2+1, i*2+2
            j = j_2 if (j_2 < self.size) and bigger(self.elements[j_1], self.elements[j_2]) else j_1        
        self.elements[i] = val_i
            
def generate(n_size):
    left, right = 1, 100
    return [random.randint(left, right) for i in range(n_size)]

def smaller_or_equal(a, b):
    return a <= b
def bigger_or_equal(a, b):
    return a >= b

def separate_inscrement(arr):
    size = len(arr)
    if size == 1: return arr
    total = []
    cur = [arr[0]]
    cmps = [smaller_or_equal, bigger_or_equal]
    cmp_id = (arr[0] <= arr[1]) #random.randint(0, 1)    
    for i in range(1, size):
        if cmps[cmp_id](arr[i], cur[-1]):
            cur.append(arr[i])
        else:
            total.append((cur, cmp_id))
            cur = [arr[i]]
            cmp_id = (i < size-1) and (arr[i] <= arr[i + 1]) #random.randint(0, 1)
    if len(cur) > 0:
        total.append((cur, cmp_id))
    return total
    
class Node:
    def __init__(self, lst):
        self.lst = lst[:]
        self.index = 0
        self.size = len(self.lst)
    def get_cur(self):
        if self.check_finish():
            return None
        a = self.lst[self.index]
        return a
    def next_to(self):        
        if not self.check_finish():
            self.index += 1        
    def check_finish(self):
        return self.index == self.size
    
def main():
    a = generate(100000)
    #print(a)
    
    lst = separate_inscrement(a)
    new_l = []
    for (l, label) in lst:
        if not label: l = l[::-1]
        new_l.append(l)
    
    for lst in new_l:
        lst_nodes.append(Node(lst))

    n_lst = len(new_l)
    H = Heap()
    for i in range(n_lst): H.insert(i)
    
    b = []
    while H.size:
        b.append(H.get_top())
        H.pop_top()
    print(sorted(a) == b)
main()


# In[35]:


a = [74, 47, 96, 21, 98]
print(a)
del a[-1]
print(a)
del a[-1]
print(a)


# In[ ]:





# In[ ]:




