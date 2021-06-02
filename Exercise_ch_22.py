class Distance:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return "Distance[{}]".format(self.value)

    def __add__(self, other):
        new_value = self.value + other.value
        return Distance(new_value)

    def __sub__(self, other):
        new_value = self.value - other.value
        return Distance(new_value)

    def __mul__(self, other):
        if isinstance(other, Distance):
            new_value = self.value * other.value
            return Distance(new_value)
        elif isinstance(other, int):
            new_value = self.value * other
            return Distance(new_value)
        else:
            raise ValueError

    def __truediv__(self, other):
        if isinstance(other, Distance):
            new_value = self.value / other.value
            return Distance(new_value)
        elif isinstance(other, int):
            new_value = self.value / other
            return Distance(new_value)
        else:
            raise ValueError

    def __floordiv__(self, other):
        if isinstance(other, Distance):
            new_value = self.value // other.value
            return Distance(new_value)
        elif isinstance(other, int):
            new_value = self.value // other
            return Distance(new_value)
        else:
            raise ValueError


if __name__ == "__main__":
    d1 = Distance(6)
    d2 = Distance(3)
    print(d1 + d2)
    print(d1 - d2)
    print(d1 / 2)
    print(d2 // 2)
    print(d2 * 2)