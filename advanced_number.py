class AdvancedNumber:
    def __init__(self, value):
        self.value = value

    def __str__(self):
        return f"Value: {self.value}"

    def __repr__(self):
        return f"AdvancedNumber({self.value})"

    # Arithmetic operators
    def __add__(self, other):
        if isinstance(other, AdvancedNumber):
            return AdvancedNumber(self.value + other.value)
        return AdvancedNumber(self.value + other)

    def __sub__(self, other):
        if isinstance(other, AdvancedNumber):
            return AdvancedNumber(self.value - other.value)
        return AdvancedNumber(self.value - other)

    def __mul__(self, other):
        if isinstance(other, AdvancedNumber):
            return AdvancedNumber(self.value * other.value)
        return AdvancedNumber(self.value * other)

    def __truediv__(self, other):
        if isinstance(other, AdvancedNumber):
            return AdvancedNumber(self.value / other.value)
        return AdvancedNumber(self.value / other)

    def __mod__(self, other):
        if isinstance(other, AdvancedNumber):
            return AdvancedNumber(self.value % other.value)
        return AdvancedNumber(self.value % other)

    # Comparison operators
    def __lt__(self, other):
        if isinstance(other, AdvancedNumber):
            return self.value < other.value
        return self.value < other

    def __le__(self, other):
        if isinstance(other, AdvancedNumber):
            return self.value <= other.value
        return self.value <= other

    def __gt__(self, other):
        if isinstance(other, AdvancedNumber):
            return self.value > other.value
        return self.value > other

    def __ge__(self, other):
        if isinstance(other, AdvancedNumber):
            return self.value >= other.value
        return self.value >= other

    def __eq__(self, other):
        if isinstance(other, AdvancedNumber):
            return self.value == other.value
        return self.value == other

    def __ne__(self, other):
        if isinstance(other, AdvancedNumber):
            return self.value != other.value
        return self.value != other

    # Hash and boolean conversion
    def __hash__(self):
        return hash(self.value)

    def __bool__(self):
        return bool(self.value)

    # Callable behavior
    def __call__(self):
        return self.value ** 2

    # Custom formatting
    def __format__(self, format_spec):
        if format_spec:
            return format(self.value, format_spec)
        return str(self.value)

    # Destructor
    def __del__(self):
        print(f"AdvancedNumber with value {self.value} is being destroyed") 