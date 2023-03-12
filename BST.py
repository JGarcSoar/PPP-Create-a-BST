#Part 1: Create a BSTNode class

class BSTNode:
    def __init__(self, data= None, left = None, right = None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)
    
    def __repr__(self):
        return str(self.data)
    
# node1 = BSTNode(3)
# print(node1)

# node2 = BSTNode(4, left=node1)
# print(node2)

# node3= BSTNode()
# print(node3)
# node3.data = 5
# print(node3)

#Part 2: Create a BST class

class BST:
    def __init__(self, root = None):
        self.root = root
        self.contents = []
    
    def __str__(self):
        if self.root == None:
            return "The tree is empy"
        else:
            self.output = ""
            self.print_tree(node=self.root)
            return self.output
        
    def __repr__(self):
        return BST.__str__(self)
    
    def print_tree(self, node, level=0):
        if node != None:
            self.print_tree(node.right, level + 1)
            self.output += " " * 4 * level + "-> " + str(node) + "\n"
            self.print_tree(node.left, level + 1)

#Part 3: Add functionality to your BST class

    def add(self, node):
        node_type = type(node)
        if node_type != int and node_type != BSTNode:
            raise ValueError("Error!")
        else:
            if node_type == int:
                node = BSTNode(node)

            if node.data in self.contents:
                return
            
            if self.root == None:
                self.root = node
                self.contents.append(node.data)
                return
            
            self.add_node(self.root, node)

    def add_node(self, cur_node, new_node):
        if new_node.data > cur_node.data:
            if cur_node.right == None:
                cur_node.right = new_node
                self.contents.append(new_node.data)
                return
            else:
                self.add_node(cur_node.right, new_node)
        
        else:
            if cur_node.left == None:
                cur_node.left = new_node
                self.contents.append(new_node.data)
                return
            else:
                self.add_node(cur_node.left, new_node)

    def remove(self, node):
        node_type = type(node)
        if node_type != int and node_type != BSTNode:
            raise ValueError("Error!")
        else:
            if node_type == BSTNode:
                node = node.data

            if node not in self.contents:
                raise ValueError("Bigger Error")
            
            self.remove_node(self.root, node)

    def remove_node(self, cur_node, rem_node, parent_node = None):
        if rem_node == cur_node.data:
            if cur_node.right == None and cur_node.left == None:
                if cur_node == parent_node.right:
                    parent_node.right = None
                    self.contents.remove(rem_node)
                else:
                    parent_node.left == None
                    self.contents.remove(rem_node)
            elif cur_node.right == None and cur_node.left != None:
                if cur_node == parent_node.right:
                    parent_node.right = cur_node.left
                    self.contents.remove(rem_node)
                else:
                    parent_node.left = cur_node.left
                    self.contents.remove(rem_node)
            elif cur_node.left == None and cur_node.right != None:
                if cur_node== parent_node.left:
                    parent_node.left = cur_node.right
                    self.contents.remove(rem_node)
                else:
                    parent_node.right = cur_node.right
                    self.contents.remove(rem_node)
            else:
                self.nodes = []
                self.traverse_tree(cur_node)

                self.nodes.remove(rem_node)
                self.contents.remove(rem_node)

                if cur_node == parent_node.right:
                    parent_node.right = None
                else:
                    parent_node.left = None

                for node in self.nodes:
                    self.add(node)
        elif rem_node > cur_node.data:
            self.remove_node(cur_node.right, rem_node, parent_node=cur_node)
        elif rem_node < cur_node.data:
            self.remove_node(cur_node.left, rem_node, parent_node=cur_node)



    def traverse_tree(self, node):
        if node != None:
            self.traverse_tree(node.right)
            self.nodes.append(node.data)
            self.traverse_tree(node.left)
            









bst = BST()
bst.add(8)
bst.add(14)
bst.add(3)
bst.add(13)
bst.add(17)
bst.add(158)
bst.add(33)
bst.add(81)
bst.add(142)
bst.add(135468)
bst.add(21)
bst.add(785)
bst.add(99)
bst.add(1)

print(bst)


bst.remove(81)
bst.remove(142)
bst.remove(33)

print(bst)


