class Matrix:
    def __init__(self, arr):
        self.arr = arr

    def validity(self, m, n):
        return len(self.arr) == m*n
    
    def create(self, m, n):
        self.matrix = []
        for i in range(m):
            self.ap = []
            for j in range(n):           
                self.ap.append(self.arr[j+n*i])
            self.matrix.append(self.ap)
        return self.matrix

    def display(self):
        for i in self.matrix:
            print(*i)

if __name__ == '__main__':
    arr = list(map(int, input().split()))
    m, n = map(int, input().split())
    object1 = Matrix(arr)
    if object1.validity(m, n):
        object1.create()
        object1.display()
    else:
        print("Invalid Dimensions")
