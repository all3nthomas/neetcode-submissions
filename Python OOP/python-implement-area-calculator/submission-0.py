import math

class AreaCalc:
    # TODO: Implement calculate method
    def __init__(self):
        pass

    def calculate(self, length, width = None):
        if width == None:
            area = math.pi * length * length
            arear = round(area, 2)
            return arear

        else:
            return length * width



    
# Don't modify the following code
calc = AreaCalc()
print(calc.calculate(5))    
print(calc.calculate(4, 6))
