import unittest
from decimal import Decimal as dec


class ConversionNotPossible(Exception):
    pass

KCDIF = dec('273.15')
KFDIF = dec('459.67')
NDIVF = dec('9') / 5
FDIVN = dec('5') / 9


F1 = {'cel': {'kel': (KCDIF, 1, 0), 'fah': (0, NDIVF, 32)},
      'kel': {'cel': (-KCDIF, 1, 0), 'fah': (0, NDIVF, -KFDIF)},
      'fah': {'cel': (-32, FDIVN, 0), 'kel': (KFDIF, FDIVN, 0)},
      'mil': {'yar': (0, dec(1760), 0), 'met': (0, dec(1609.34), 0)},
      'yar': {'mil': (0, dec(.00056818), 0), 'met': (0, dec(.9144), 0)},
      'met': {'mil': (0, dec(.00062137), 0), 'yar': (0, dec(1.09361), 0)}
     }


def convert(fromUnit, toUnit, value):
    fu = fromUnit[:3].lower()
    tu = toUnit[:3].lower()
    value = dec(value)
    if fu == tu:
        return float(value)
    elif tu in F1[fu]:
        conversion = ((value + F1[fu][tu][0]) *
                      (F1[fu][tu][1]) +
                      (F1[fu][tu][2]))

        return round(float(conversion), 3)
    else:
        raise ConversionNotPossible


class ConverstionTests(unittest.TestCase):
    tvals = [('Celsius', 'Kelvin', 100, 373.15),
             ('Celsius', 'fahrenheit', 300, 572.0),
             ('Kelvin', 'Celsius', 273.15, 0),
             ('Kelvin', 'Fahrenheit', 573.15, 572.0),
             ('Fahrenheit', 'Celsius', 32, 0),
             ('Fahrenheit', 'Kelvin', 32, 273.15),
             ('Miles', 'Yards', 1, 1760),
             ('Miles', 'Meters', .5, 804.67),
             ('Yards', 'Miles', 5, .003),
             ('Yards', 'Meters', 10, 9.144),
             ('Meters', 'Yards', 5, 5.468),
             ('Meters', 'Miles', 1000, .621)]

    def testConversions(self):
        for i in self.tvals:
            self.assertEqual(convert(i[0], i[1], i[2]), i[3])

    def testSameUnit(self):

        for c in F1:
            self.assertEqual(convert(c, c, 1.0), 1.0)

    def testIncompatibleUnits(self):
        self.assertRaises(ConversionNotPossible, convert, 'Miles', 'Kelvin', 10)