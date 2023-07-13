def pascalTriangle(n : int) -> List[List[int]]:
    # Write your code here.
    tri = [[] for _ in range(n)]
    
    for i in range(n):
        tri[i] = [0 for _ in range(i+1)]

        tri[i][0] = 1
        tri[i][i] = 1
        
        for j in range(1,i):
            tri[i][j] = tri[i-1][j-1] + tri[i-1][j]

    return tri

    
