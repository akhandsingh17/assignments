"""
Input:

X[] = { 1, 4, 7, 8, 10 }
Y[] = { 2, 3, 9 }

Output:

X[] = { 1, 2, 3, 4, 7 }
Y[] = { 8, 9, 10 }
The idea is simple. Consider each array element X[] and ignore it if it is already in the correct order
 (i.e., the element smallest among all remaining elements); otherwise, swap it with the smallest element, which happens
  to be the first element of Y[]. After swapping, move the element (now present at Y[0]) to its correct position in Y[]
   to maintain the sorted order.

"""

def merge(X, Y):
    m = len(X)
    n = len(Y)

    for i in range(m):
        if X[i] > Y[0]:
            temp = X[i]
            X[i] = Y[0]
            Y[0] = temp

            first = Y[0]
            k = 1
            while k < n and Y[k] < first:
                Y[k-1] = Y[k]
                k += 1
            Y[k-1] = first

if __name__ == '__main__':

    X = [1, 4, 7, 8, 10]
    Y = [2, 3, 9]
    merge(X, Y)
    print("X:", X)
    print("Y:", Y)