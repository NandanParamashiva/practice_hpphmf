
import math

class Node:
    def __init__(self, data=0):
        self.left = None
        self.right = None
        self.data = data

def add(root, data):
    if root == None:
        return Node(data)
    if data < root.data:
        root.left = add(root.left, data)
    elif data > root.data:
        root.right = add(root.right, data)
    else:
        print 'No equal elems allowed at this point'
    return root

def show(root):
    if root == None:
        return
    show(root.left)
    print root.data ,
    show(root.right)

def check_BST(root):
    if not root:
        print 'root is None'
        return
    return isBST(root, None, None)


def isBST(root, mini, maxi):
    if root == None:
        return True

    print root.data, mini, maxi

    if mini:
        if root.data < mini:
            print 'root.data < mini; False'
            return False
    if maxi:
        if root.data > maxi:
            print 'root.data > maxi; False'
            return False

    if False == isBST(root.left, mini, root.data):
        return False
    if False == isBST(root.right, root.data, maxi):
        return False
    print "returning True"
    return True

    #return (isBST(root.left, mini, root.data) and isBST(root.right, root.data, maxi))

def main():
    root = None
    test_data = [50, 30, 60, 20, 70, 35, 55]
    for data in test_data:
        root = add(root, data)
    show(root)
    print
    print
    if check_BST(root) == True:
        print "\n True: It is BST"
    else:
        print '\n False: It is not BST'


if __name__ == "__main__":
    main()