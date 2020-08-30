# python3
import numpy as np

def edit_distance(first_string, second_string):
    a=len(first_string)
    b=len(second_string)

    d=np.zeros((a+1,b+1), dtype=int)
    d[0]=list(range(b+1))
    d[:,0]=list(range(a+1))
    for i in range(1,a+1):
        for j in range(1,b+1):
            match=d[i-1,j-1]
            mismatch = match+1
            insertion = d[i-1,j]+1
            deletion = d[i,j-1]+1
            if first_string[i-1]==second_string[j-1]:
                d[i,j]=min(match, insertion, deletion)
            else:
                d[i,j]=min(mismatch, insertion, deletion)
    return d



if __name__ == "__main__":
    print(edit_distance(input(), input()))
