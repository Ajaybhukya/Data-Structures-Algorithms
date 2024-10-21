class TreeNode:
    def __init__(self,data):
        self.data=data
        self.parent=None
        self.children=[]
    def add_child(self,child):
        child.parent=self
        self.children.append(child)
    def get_level(self):
        level=0
        p=self.parent
        while p:
            level+=1
            p=p.parent
        return level
    def print_tree(self):
        prefix=' '*self.get_level()*3
        prefix=prefix+'|__' if self.parent else ""
        print(prefix+self.data)
        if len(self.children)>0:
            for child in self.children:
                child.print_tree()
def built_tree():
    root=TreeNode("Electronic")

    laptop=TreeNode("Laptop")
    laptop.add_child(TreeNode("Mac"))
    laptop.add_child(TreeNode("Windows"))
    laptop.add_child(TreeNode("Linux"))
    root.add_child(laptop)

    TV=TreeNode("TV")
    TV.add_child(TreeNode("Samsung"))
    TV.add_child(TreeNode("Sony"))
    TV.add_child(TreeNode("LG"))

    root.add_child(TV)

    return root
if __name__ == '__main__':
    root=built_tree()
    root.print_tree()
    print(root.get_level())
'''
OUTPUT:
Electronic
   |__Laptop
      |__Mac
      |__Windows
      |__Linux
   |__TV
      |__Samsung
      |__Sony
      |__LG
0
'''
