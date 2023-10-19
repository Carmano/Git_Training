import math


class Fraction:
    def __init__(self, *args):
        if len(args) != 2:  # if the argument is received in the form string. We return it separately
            args = self._transformation(args[0])
        self.num, self.den = self._reduce_fraction(*args)
        self._check_negative()

    def numerator(self, change=0):
        if change == 0:
            return self.num
        self.num, self.den = self._reduce_fraction(change, self.den)
        self._check_negative()

    def denominator(self, change=0):
        if change == 0:
            return self.den
        self.num, self.den = self._reduce_fraction(self.num, change)
        self._check_negative()

    def __str__(self):
        return f'{self.num}/{self.den}'

    def __repr__(self):
        return f'Fraction(\'{self.num}/{self.den}\')'

    def __mul__(self, other):
        pass

    def __neg__(self):
        return Fraction(-self.num, self.den)

    @staticmethod
    def _reduce_fraction(num, den):
        return num // math.gcd(num, den), den // math.gcd(num, den)

    @staticmethod
    def _transformation(args):
        num, den = args.split('/')
        return int(num), int(den)

    def _check_negative(self):
        if self.num and self.den < 0:
            self.num *= (-1)
            self.den *= (-1)


def main():
    a = Fraction('-1/2')
    b = -a
    print(a, b, a is b)
    b.numerator(-b.numerator())
    a.denominator(-3)
    print(a, b)
    print(a.numerator(), a.denominator())
    print(b.numerator(), b.denominator())


if __name__ == '__main__':
    main()
