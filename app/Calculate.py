class Calculate:
    # Constructor
    def __init__(self, v, v1):
        self.value = v
        self.value1 = v1

    # Get y Set
    def get_value(self):
        return self.value

    def set_value(self, v):
        self.value = v

    def get_value1(self):
        return self.value1

    def set_value1(self, v1):
        self.value1 = v1

    # Operator
    def sum(self):
        return self.value + self.value1

    def subtraction(self):
        return self.value - self.value1

    def divide(self):
        return self.value / self.value1

    def multiply(self):
        return self.value * self.value1
