def merge(a, b, c, n, m):
    i=j=k=0
    while i<n and j<m:
        if a[i]<b[j]:
            c[k]=a[i]
            k=k+1
            i=i+1
        else:
            c[k]=b[j]
            k=k+1
            j=j+1
    while i<n:
        c[k]=a[i]
        k=k+1
        i=i+1
    while j<m:
        c[k]=b[j]
        k=k+1
        j=j+1


