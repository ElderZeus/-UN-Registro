class node:
    def __init__ (self,data):
        self.data = data
        self.left = None
        self.rigth = None
        
class BinaryTree:
    def __init__ (self, data):
        self.raiz = node(data)
        
    def _add(self,node,data):
        if data < node.data:
            if node.left == None:
                node.left = node(data)
            else:
                self.add(node.left, data)
        else:
            if node.rigth == None:
                node.rigth = node(data)
            else:
                self.add(node.rigth, data)
                
    def _preOrder(self, node):
        if node != None:
            print(node.data, end=" ")            
            self.inOrder(node.left)
            self.inOrder(node.rigth)                       
            
    def _inOrder(self, node):
        if node != None:
            self.inOrder(node.left)
            print(node.data, end=" ")
            self.inOrder(node.rigth)
            
    def _postOrder(self, node):
        if node != None:
            self.inOrder(node.left)
            self.inOrder(node.rigth)             
            print(node.data, end=" ")
 
    def _search(self, node, temp):
        if node == None:
            return None
        if node.data == temp:
            return node
        if temp < node.data:
            return self.search(node.left, temp)
        if temp > node.data:
            return self.search(node.rigth, temp)    
        
    def add(self,data):
        self._add(self.raiz,data)

    def preOrder(self,data):
        self._preOrder(self.raiz,data)
        
    def inOrder(self,data):
        self._inOrder(self.raiz,data)
        
    def postOrder(self,data):
        self._postOrder(self.raiz,data)
        
    def search(self,temp):
        return self._search(self.raiz, temp)
    
                