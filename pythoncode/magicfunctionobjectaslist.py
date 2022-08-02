class A:
    def __init__(self, item):
        self.item = item
    def __getitem__(self, index):
        return self.item[index]
a = A([1, 2, 3])
print(f"First item: {a[0]}")
print(f"Second item: {a[1]}")
print(f"Third item: {a[2]}")
