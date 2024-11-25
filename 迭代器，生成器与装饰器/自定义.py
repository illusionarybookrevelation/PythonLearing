class MyIterator:
    def __init__(self,x,xmax):
        self._mul,self._x = x,x
        self._xmax = xmax

    def __iter__(self):
        return self

    def __next__(self):
        if self._mul and self._x != 1:
            self._mul *= self._x
            if self._mul <= self._xmax:
                return self._mul
            else:
                raise StopIteration
        else:
            raise StopIteration
if __name__ == '__main__':
    myiter = MyIterator(3,300)
    for i in myiter:
        print("迭代的元素为: ",i)