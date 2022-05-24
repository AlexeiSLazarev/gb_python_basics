src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [23, 1, 3, 10, 4, 11]

from collections import Counter                                                                                                                                                                                                                                                   

c = Counter(src)    
print([i for i,j in c.items() if j==1])

