
def main():

    """
    Call a few functions to demonstrate basic complex number handling.
    """

    print("---------------------------------")
    print("| codedrome.com                 |")
    print("| Complex Numbers: Introduction |")
    print("---------------------------------")

    ccreation()

    caddition()
    csubtraction()
    cmultiplication()
    cdivision()

    cconjugate()
    cmagnitude()


def ccreation():

    """
    Demonstrate ways of creating complex numbers, also print the type.
    """

    print("\nCreation\n--------")

    z1 = 7 + 12j
    z2 = complex(14, 24)

    print(z1)
    print(z2)

    print(type(z1))


def caddition():

    """
    Demonstrate addition of complex numbers.
    """

    print("\nAddition\n--------")

    z1 = 7 + 12j
    z2 = 14 + 24j

    print("{} + {} = {}".format(z1, z2, z1+z2))

    print("({:g}+{:g}) + ({:g}j+{:g}j) = {}".format(z1.real, z2.real, z1.imag, z2.imag, complex(z1.real+z2.real, z1.imag+z2.imag)))


def csubtraction():

    """
    Demonstrate subtraction of complex numbers.
    """

    print("\nSubtraction\n----------")

    z1 = 10 + 6j
    z2 = 5 + 3j

    print("{} - {} = {}".format(z1, z2, z1-z2))

    print("({:g}-{:g}) + ({:g}j-{:g}j) = {}".format(z1.real, z2.real, z1.imag, z2.imag, complex(z1.real-z2.real, z1.imag-z2.imag)))


def cmultiplication():

    """
    Demonstrate multiplication of complex numbers.
    """

    print("\nMultiplication\n--------------")

    z1 = 3 + 2j
    z2 = 4 + 5j

    print("{} * {} = {}".format(z1, z2, z1*z2))

    print("({:g}*{:g} - {:g}*{:g}) + ({:g}*{:g} + {:g}*{:g})j = {}".format(z1.real, z2.real, z1.imag, z2.imag,
                                                                   z1.real, z2.imag, z1.imag, z2.real,
                                                                   complex(z1.real *z2.real - z1.imag * z2.imag, z1.real * z2.imag + z1.imag * z2.real)))


def cdivision():

    """
    Demonstrate division of complex numbers.
    """

    print("\nDivision\n--------")

    z1 = 4 + 7j
    z2 = 1 - 3j

    print("{} / {} = {}".format(z1, z2, z1/z2))

    numerator = z1*z2.conjugate()
    denominator = z2*z2.conjugate()
    quotientreal = numerator.real / denominator.real
    quotientimag = numerator.imag / denominator.real
    quotient = complex(quotientreal, quotientimag)

    print("({}{}) / ({}{})".format(z1, z2.conjugate(), z2, z2.conjugate()), end="")
    print(" = ({}/{}) + ({}/{})j".format(numerator.real, denominator.real, numerator.imag, denominator.real), end="")
    print(" = {}".format(quotient))


def cconjugate():

    """
    Demonstrate complex conjugate using the conjugate method and by reversing imaginary part.
    """

    print("\nConjugate\n---------")

    z = 44 + 22j

    print(z)
    print(z.conjugate())
    print(complex(z.real, z.imag * -1))


def cmagnitude():

    """
    Demonstrate magnitude using abs method and by calculation.
    """

    print("\nMagnitude\n---------")

    z = 9 + 12j

    print(z)
    print(abs(z))
    print((z.real ** 2 + z.imag ** 2) ** 0.5)


main()
