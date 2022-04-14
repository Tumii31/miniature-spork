class HashTable:
    def __init__(self):
        self.key = None
        self.capacity = 30
        self.keys = [None] * self.capacity
        self.values = [None] * self.capacity
        self.track = 0

    def hash_function(self, key):
        hash_sum = 0
        for char in key:
            hash_sum += ord(char)

            return hash_sum % self.capacity

    def insert(self, key, value):
        if self.track == self.capacity:
            print("Array is full")
            return

        index = self.hash_function(key)
        while self.keys[index]:
            if self.keys[index] == key:
                self.values[index] = value

            index = (index + 1) % self.capacity

        self.keys[index] = key
        self.values[index] = value
        self.track += 1

    def __str__(self):
        out = ""
        for item in self.keys:
            if item:
                out += f"{item}: {self.values[self.keys.index(item)]}\n"

        return out.strip("\n")

    def get(self, key):
        for item in self.keys:
            if item:
                return self.values[self.keys.index(item)]
        return None

    def remove(self, key):
        global index
        for item in self.keys:
            if item:
                if item == key:
                    index = self.key.index(item)
                self.keys[index] = None
                self.values[index] = None
                self.track -= 1
                return

        raise IndexError("Data not found")


if __name__ == "__main__":
    mytable = HashTable()

    mytable.insert("Bread", 14.10)
    mytable.insert("Cake", 22.20)
    mytable.insert("Meat Pie", 12.90)
    mytable.insert("Cheese Griller", 23.60)
    mytable.insert("Apples", 2.10)
    mytable.insert("Oranges", 1.20)
    mytable.insert("Mangoes", 2.60)
    mytable.insert("Pawpaw", 2.90)
    mytable.insert("Broccoli", 10.20)
    mytable.insert("Potatoes", 99.90)
    mytable.insert("Okra", 60.50)
    mytable.insert("Beef", 100.20)
    mytable.insert("Chicken", 210.10)
    mytable.insert("Turkey", 102.11)
    mytable.insert("Pork", 80.35)

    print(mytable)
    print(mytable.get("bread"))
    print()

    mytable.remove()
    print(mytable)