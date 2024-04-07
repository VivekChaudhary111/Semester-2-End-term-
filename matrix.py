# input->
# 1 2 3 4 5 6
# 3 2
# output->
# 3 3
# 1 2 4
# 3 4 5
# 5 6 6
#


class array:
    def __init__(self, lst, r=0, c=0):
        self.lst = lst
        self.r = r
        self.c = c
        if r != 0 and c != 0:
            M = []
            tmp = []
            for i in self.lst:
                tmp.append(i)
                if len(tmp) == c :
                    M.append(tmp)
                    tmp = []
            self.lst = M

    def __add__(self, other):
        if (self.r, self.c) == (other.r, other.c):
            M = [[0]*self.c] * self.r  # [[0, 0, 0], [0, 0, 0]]
            for i in range(self.r):
                for j in range(other.c):
                    M[i][j] = self.lst[i][j] + other.lst[i][j]
                return array(M)
        else:
            return "Not Compatible for Addition"
    
    def __sub__(self, other):
        if (self.r, self.c) == (other.r, other.c):
            M = [[0]*self.c] * self.r  # [[0, 0, 0], [0, 0, 0]]
            for i in range(self.tr):
                for j in range(other.c):
                    M[i][j] = self.lst[i][j] - other.lst[i][j]
                return array(M)
        else:
            return "Not Compatible for Subtraction"

    def __mul__(self, other):
        if (self.r, self.c) == (other.r, other.c):
            M = [[0]*self.c] * self.r  # [[0, 0, 0], [0, 0, 0]]
            for i in range(self.tr):
                for j in range(other.c):
                    M[i][j] = self.lst[i][j] * other.lst[i][j]
                return array(M)
        else:
            return "Not Compatible for Multiplication"

    def dot(self, other):
        if self.c == other.r:
            M = eval(str([[0]*self.r] * self.c))  # [[0, 0, 0], [0, 0, 0]]
            for i in range(self.r):
                for j in range(other.c):
                    for k in range(self.c):
                        M[i][j] += self.lst[i][k] * other.lst[k][j]
                return array(M)
        else:
            return "Not Compatible for dot product"
        
    def transpose(self):
        M = eval(str([[0]*self.r] * self.c))
        for i in range(self.c):
            for j in range(self.r):
                M[i][j] = self.lst[j][i]
        return array(M)

    def display(self):
        for i in self.lst:
            print(*i)


# driver code
lst1 = list(map(eval, input("Enter Matrix 1 Elements\n").split()))
r1, c1 = list(map(eval, input("R x C\n").split()))
arr1 = array(lst1, r1, c1)

lst2 = list(map(eval, input("Enter Matrix 2 Elements\n").split()))
r2, c2 = list(map(eval, input("R x C\n").split()))
arr2 = array(lst2, r2, c2)

print("\nMatrix 1")
arr1.display()
print("\nMatrix 2")
arr2.display()
out = arr1.dot(arr2)
print("\nMatrix multiplication")
out.display()
