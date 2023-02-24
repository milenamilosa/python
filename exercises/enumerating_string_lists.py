alist = ["c", "v", "c"]

def indices(lst, item):
    return [i for i, x in enumerate(lst) if x == item]
 
print(indices(alist, "c"))