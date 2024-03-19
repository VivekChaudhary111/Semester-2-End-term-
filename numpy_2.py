class array:
    def __init__(self, lst):
        self.lst = lst

    def __str__(self):
        st  = str(self.lst).replace(',', '')
        return st
    def __add__(self, other):
        first = self.lst
        second = other.lst
        adder = []
        if len(first) == len(second):
            for i in range(len(first)):
                adder.append(first[i] + second[i])
            return array(adder)
        else:
            return "Invalid data format"
    
    def reshape(self, m, n):
        pass



arr1 = array([2, 4, 6, 8, 9])
arr2 = array([4, 6, 8, 9, 10, 34])
arr1.reshape(2, 3)
out = arr1 + arr2
print(out, type(out))



