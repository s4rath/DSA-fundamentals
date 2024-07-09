# Greedy Algorithm
# Largest Permutation problem 

#Given an integer array A of size N consisting of unique integers from 1 to N. 
# You can swap any two integers atmost B times.

# if A=[8,1,9,6,2] and B=3

# then it should return [9, 8, 6, 1, 2]

def solve(A, B):
        temp=0
        ideal=sorted(A,reverse=True)
        i=0
        j=0
        while i<B:
            while True:
        
                if ideal[j]==A[i]:
                    break
                else:
                    temp=A[i]
                    ind=A.index(ideal[j])
            
                    A[i]=A[ind]
            
                    A[ind]=temp
                    break
            j+=1
            i+=1

        return A

A=[8,1,9,6,2]
B=3
print(solve(A,B))