def MaximoMontana(x):
    if len(x)== 2:
        if x[0]>x[1]:
            return x[0]
        if x[1]>x[0]:
            return x[1]
    mid = len(x)//2
    if x[mid]>x[mid+1] and x[mid]<x[mid-1]:
        return MaximoMontana(x[:mid])
    if x[mid]>x[mid-1] and x[mid]<x[mid+1]:    
        return MaximoMontana(x[mid:])
    if x[mid]>x[mid-1] and x[mid]>x[mid+1]:
        return x[mid]

print(MaximoMontana([1, 3, 8, 14, 16, 13, 8, 4, 2, 1]) )