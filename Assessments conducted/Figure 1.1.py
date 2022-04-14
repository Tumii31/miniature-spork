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
    root = TreeNode("Groceries")

    pastries = TreeNode("Pastries")
    pastries.add_child(TreeNode("Bread"))
    pastries.add_child(TreeNode("Cake"))
    pastries.add_child(TreeNode("Cheese Griller"))
    pastries.add_child(TreeNode("Meat Pie"))

    fruits = TreeNode("Fruits")
    fruits.add_child(TreeNode("Apples"))
    fruits.add_child(TreeNode("Oranges"))
    fruits.add_child(TreeNode("Mangoes"))
    fruits.add_child(TreeNode("Pawpaw"))

    vegetables = TreeNode("Vegetables")
    vegetables.add_child(TreeNode("Broccoli"))
    vegetables.add_child(TreeNode("Carrots"))
    vegetables.add_child(TreeNode("Potatoes"))
    vegetables.add_child(TreeNode("Okra"))

    meat = TreeNode("Meat")
    meat.add_child(TreeNode("Beef"))
    meat.add_child(TreeNode("Chicken"))
    meat.add_child(TreeNode("Turkey"))
    meat.add_child(TreeNode("Pork"))

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
