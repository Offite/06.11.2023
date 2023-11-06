class Vector3D:

    def init(self, x, y, z):
        self.coords = (x, y, z)

    def display(self):
        print(f"Vector3D: {self.coords}")

class method:

    def read(cls):
        x, y, z = map(int, input("Введите координаты: ").split())
        return cls(x, y, z)

    def __add__(self, other):
      if isinstance(other, Vector3D):
        return Vector3D(self.coords[0] + other.coords[0], self.coords[1] + other.coords[1], self.coords[2] + other.coords[2])
      else:
        raise TypeError("Можно добавить только два экземпляра Vector3D или экземпляры с совместимыми координатами.")

    def __sub__(self, other):
        return self + (-other)

def __mul__(self, factor):
    if factor == 0:
        raise ZeroDivisionError("Невозможно разделить на ноль")