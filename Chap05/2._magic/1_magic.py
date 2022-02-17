class Length:
    __metric = {"mm" : 0.001, "cm" : 0.01, "m" : 1, "km" : 1000,
                "in" : 0.0254, "ft" : 0.3048, "yd" : 0.9144,
                "mi" : 1609.344 }
    def __init__(self, value, unit = "m" ):
        self.value = value
        self.unit = unit
    def Converse2Metres(self):
        return self.value * Length.__metric[self.unit]

    def __add__(self, other):
        if type(other) == int or type(other) == float:
            l = self.Converse2Metres() + other
        else:
            l = self.Converse2Metres() + other.Converse2Metres()
        return Length(l / Length.__metric[self.unit], self.unit)

    def __radd__(self, other):
        if type(other) == int or type(other) == float:
            l = self.Converse2Metres() + other
        else:
            l = self.Converse2Metres() + other.Converse2Metres()
        return Length(l / Length.__metric[self.unit], self.unit)

    def __str__(self):
        return str(self.Converse2Metres())
    def __repr__(self):
        return "Length(" + str(self.value) + ", '" + self.unit + "')"



# x = Length(4)
# print(x)
# z = Length(4.5, "yd") + Length(1)
# print(repr(z))
# print(z)

x = 1
x  += Length(1)

x += Length(4, "yd")
print(x)