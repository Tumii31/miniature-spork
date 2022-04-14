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
    root = TreeNode("Groceries (Building 1)")

    pastries = TreeNode("Pastries (South)")
    pastries.add_child(TreeNode("Bread (South - Shelf 1)"))
    pastries.add_child(TreeNode("Cake (South - Shelf 2)"))
    pastries.add_child(TreeNode("Cheese Griller (South - Shelf 3)"))
    pastries.add_child(TreeNode("Meat Pie (South - Shelf 4)"))

    fruits = TreeNode("Fruits (East)")
    fruits.add_child(TreeNode("Apples (East - Shelf 1)"))
    fruits.add_child(TreeNode("Oranges (East - Shelf 2)"))
    fruits.add_child(TreeNode("Mangoes (East - Shelf 3)"))
    fruits.add_child(TreeNode("Pawpaw (East - Shelf 4)"))

    vegetables = TreeNode("Vegetables (West)")
    vegetables.add_child(TreeNode("Broccoli (West - Shelf 1)"))
    vegetables.add_child(TreeNode("Carrots (West - Shelf 2)"))
    vegetables.add_child(TreeNode("Potatoes (West - Shelf 3)"))
    vegetables.add_child(TreeNode("Okra (West - Shelf 4)"))

    meat = TreeNode("Meat (North)")
    meat.add_child(TreeNode("Beef (North - Shelf 1)"))
    meat.add_child(TreeNode("Chicken (North - Shelf 2)"))
    meat.add_child(TreeNode("Turkey (North - Shelf 3)"))
    meat.add_child(TreeNode("Pork (North - Shelf 4)"))

    root.add_child(pastries)
    root.add_child(fruits)
    root.add_child(vegetables)
    root.add_child(meat)

    return root


if __name__ == '__main__':
    root = build_product_tree()
    #print(root.get_levelO())
    root.print_tree()
    pass
