import math
class Vector:
    def __init__(self, *numbers):
        self.numbers = numbers

    def __str__(self):
        return f"Vector{self.numbers}"

    def __add__(self, other):
        if len(self.numbers) != len(other.numbers):
            raise ValueError("Two vectors are not of the same dimension!")
        return Vector(*(a + b for a, b in zip(self.numbers, other.numbers)))

    def __sub__(self, other):
        if len(self.numbers) != len(other.numbers):
            raise ValueError("Two vectors are not of the same dimension!")
        return Vector(*(a - b for a, b in zip(self.numbers, other.numbers)))

    def __mul__(self, other):
        if isinstance(other, int):
            return Vector(*(a * other for a in self.numbers))
        elif isinstance(other, Vector):
            if len(self.numbers) != len(other.numbers):
                raise ValueError("Two vectors are not of the same dimension!")
            list1 = list(a * b for a, b in zip(self.numbers, other.numbers))
            return sum(list1)
        else:
            raise TypeError("Unsupported operand type(s) for *: 'Vector' and '{}'".format(type(other).__name__))

    def __rmul__(self, other):
        return self.__mul__(other)
    
    def magnitude(self):
        mylist = list(a**2 for a in self.numbers)
        result = math.sqrt(sum(mylist))
        return result
    
    def normalize(self):
        mag = self.magnitude()
        if mag == 0:
            raise ValueError("Cannot normalize a zero vector.")
        return Vector(*(round(a / mag, 3) for a in self.numbers))

vec1 = Vector(1,2,5,4,6)
vec2 = Vector(2,1,4,1,1)
vec3 = vec2-vec1
vec4 = 3 * vec1
print(vec3)
print(vec1+vec2)
print(vec4)
print(vec1.magnitude())
print(vec1.normalize())