
# 
# This problem was asked by Google.
# 
# Given the root to a binary tree, implement serialize(root), 
# which serializes the tree into a string, and deserialize(s), 
# which deserializes the string back into the tree.
# 
# For example, given the following Node class
# 
# class Node:
#     def __init__(self, val, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
# 
# The following test should pass:
# 
# node = Node('root', Node('left', Node('left.left')), Node('right'))
# assert deserialize(serialize(node)).left.left.val == 'left.left'


class Node:
    def __init__(self, val , left=None , right=None):
        self.val = val 
        self.left = left 
        self.right = right 

def serialize(root):
    
    if(root.left == None and root.right == None):
        return 'Node(val='+root.val+')'
    
    if(root.left != None and root.right == None):
        return 'Node(val='+root.val+',left='+serialize(root.left)+')'
    
    if(root.left != None and root.right == None):
        return 'Node(val='+root.val+',right='+serialize(root.right)+')'
    
    
    return 'Node(val='+root.val+',left='+ serialize(root.left)+',right='+ serialize(root.right)+')' 


left_left = Node('left-left')
left = Node('left',left=left_left)
right = Node('right')
root = Node('root',left,right)

serialize(root)



# Output ->
# 'Node(val=root,left=Node(val=left,left=Node(val=left-left)),right=Node(val=right))'


