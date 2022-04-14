class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent

        return level

    def print_tree(self):
        spaces = '' * self.get_level() * 3
        prefix = spaces + "|__" if self.parent else ""

        print(prefix + self.data)
        if len(self.children) > 0:
            for child in self.children:
                child.print_tree()


def build_product_tree():
    root = TreeNode("Building 1")

    South = TreeNode("South")
    South.add_child(TreeNode("South - Shelf 1"))
    South.add_child(TreeNode("South - Shelf 2"))
    South.add_child(TreeNode("South - Shelf 3"))
    South.add_child(TreeNode("South - Shelf 4"))

    East = TreeNode("East")
    East.add_child(TreeNode("East - Shelf 1"))
    East.add_child(TreeNode("East - Shelf 2"))
    East.add_child(TreeNode("East - Shelf 3"))
    East.add_child(TreeNode("East - Shelf 4"))

    West = TreeNode("West")
    West.add_child(TreeNode("West - Shelf 1"))
    West.add_child(TreeNode("West - Shelf 2"))
    West.add_child(TreeNode("West - Shelf 3"))
    West.add_child(TreeNode("West - Shelf 4"))

    North = TreeNode("North")
    North.add_child(TreeNode("North - Shelf 1"))
    North.add_child(TreeNode("North - Shelf 2"))
    North.add_child(TreeNode("North - Shelf 3"))
    North.add_child(TreeNode("North - Shelf 4"))

    root.add_child(South)
    root.add_child(East)
    root.add_child(West)
    root.add_child(North)

    return root


if __name__ == '__main__':
    root = build_product_tree()
    #print(root.get_levelO())
    root.print_tree()
    pass
