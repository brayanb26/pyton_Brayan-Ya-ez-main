def countKdivParis (a , n , k ):
    count = 0
    for i in range (0 , n):
        for j in range (i+1, n):
            if ((a[i] + a[j]  % k==0)):
                count += 1
    return count
a=[2 ,2 ,1 ,7 ,5 ,3]
n = len(a) 
k = 4
print(countKdivParis(a, n,k))           