class Glass:
    capacity = 250

    def __init__(self):
        self.content = 0
        self.capacity = 250
        self.space_left = 250 - 0

    def fill(self, ml):
        if ml + self.content > self.capacity:
            return f"Cannot add {ml} ml"
        self.content += ml
        return f"Glass filled with {ml} ml"

    def empty(self):
        self.content = 0
        return "Glass is now empty"

    def info(self):
        self.space_left = self.capacity - self.content
        return f"{self.space_left} ml left"


glass = Glass()
print(glass.fill(100))
print(glass.fill(200))
print(glass.empty())
print(glass.fill(200))
print(glass.info())
