import decimal


def convertCelsiusToKelvin(degrees):
    degrees = str(degrees)
    convert = (decimal.Decimal(degrees) + decimal.Decimal('273.1'))
    return float(convert)


def convertCelsiusToFahrenheit(degrees):
    degrees = str(degrees)
    convert = (decimal.Decimal(degrees) / decimal.Decimal('5') * 9) + 32
    return float(convert)


def convertFahrenheitToCelsius(degrees):
    degrees = str(degrees)
    convert = ((decimal.Decimal(degrees) - 32) * 5) / decimal.Decimal('9')
    return float(convert)


def convertFahrenheitToKelvin(degrees):
    degrees = str(degrees)
    convert = (((decimal.Decimal(degrees) + decimal.Decimal('459.67')) * 5) /
               decimal.Decimal('9'))
    return float(convert)


def convertKelvinToCelsius(degrees):

    degrees = str(degrees)
    convert = (decimal.Decimal(degrees) - decimal.Decimal('273.15'))
    return float(convert)


def convertKelvinToFahrenheit(degrees):
    degrees = str(degrees)
    convert = (((decimal.Decimal(degrees) * 9) / decimal.Decimal('5'))
               - decimal.Decimal('459.67'))
    return float(convert)