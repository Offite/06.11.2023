class RectTriangle:

    def init(self, a, b):
        self.a = a
        self.b = b

    def increase_side(self, percent):
        new_a = (self.a * (100 + percent)) // 100
        new_b = (self.b * (100 + percent)) // 100
        return RectTriangle(new_a, new_b)

    def decrease_side(self, percent):
        new_a = self.a - (self.a * percent) // 100
        new_b = self.b - (self.b * percent) // 100
        if new_a < 0 or new_b < 0:
            raise ValueError("Side cannot become negative.")
        return RectTriangle(new_a, new_b)

    def calc_circumcircle_radius(self):
        a, b = self.a, self.b