#!/usr/bin/env python
# coding: utf-8

# In[53]:


import random
# Heap Min
def bigger(a, b):
    return a > b
class Heap:
    def __init__(self):
        self.elements = []
        self.size = 0    
    def insert(self, val):
        self.elements.append(val)
        self.size += 1
        i = self.size - 1
        val_i = val
        while i > 0:
            j = (i - 1) // 2
            if bigger(self.elements[j], val_i):
                self.elements[i] = self.elements[j]
                i = j
            else: break
        self.elements[i] = val_i            
    def get_top(self):
        return self.elements[0]
    def pop_top(self):
        if self.size == 0: return 
        if self.size == 1:
            del self.elements[0]
            self.size = 0
            return 
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
def main():
    a = generate(20)
    print(a)
    H = Heap()
    for x in a: H.insert(x)
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




