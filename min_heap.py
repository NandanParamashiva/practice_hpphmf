#!/usr/bin/python

class min_heap:
    def __init__(self):
        self.data = []

    def get_left_child_index(self,index):
        return ((2*index) + 1)

    def get_right_child_index(self, index):
        return ((2*index) + 2)

    def get_parent_index(self, index):
        return ((index - 1) / 2 )

    def swap(self, i,j):
        tmp = self.data[i]
        self.data[i] = self.data[j]
        self.data[j] = tmp

    def heapify_up(self):
        if len(self.data) == 0:
            return
        cur = len(self.data) - 1
        while cur >= 0:
            p = self.get_parent_index(cur)
            if p < 0 :
                return
            if self.data[p] > self.data[cur]:
                self.swap(p,cur)
                cur = p
            else:
                break

    def minimum(self, lc, rc):
        if (self.data[lc] < self.data[rc]):
            return lc
        else:
            return rc


    def heapify_down(self):
        if len(self.data) == 0:
            return
        cur = 0
        while cur < len(self.data)-1:
            lc = self.get_left_child_index(cur)
            rc = self.get_right_child_index(cur)
            if lc >= len(self.data) and rc >= len(self.data):
                break
            if lc <= len(self.data) and rc >= len(self.data):
                min_idx =  lc
            else:
                min_idx = self.minimum(lc,rc)
            if self.data[min_idx] < self.data[cur]:
                self.swap(min_idx,cur)
            else:
                break

        return min_return



    def insert(self, num):
        self.data.append(num)
        self.heapify_up()

    def extract_min(self):
        min_return = self.data[0]
        self.data[0] = self.data[len(self.data) - 1]
        del self.data[-1]
        self.heapify_down()
        return min_return

    def display(self,index):
        if index < 0 or index > (len(self.data) - 1):
            return
        print '%d, ' %(self.data[index]) ,
        self.display(self.get_left_child_index(index))
        self.display(self.get_right_child_index(index))

def main():
    test = min_heap()
    test.insert(10)
    test.insert(20)
    test.display(0)
    print'\n'
    test.insert(5)
    test.display(0)
    print'\n'
    test.insert(2)
    test.display(0)
    print'\n'
    test.insert(1)
    test.display(0)
    print'\n'
    test.insert(15)
    test.display(0)

if __name__ == "__main__":
    main()