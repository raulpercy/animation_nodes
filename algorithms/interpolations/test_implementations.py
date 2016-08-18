from unittest import TestCase
from . implementations import (Linear,
                               PowerIn, PowerOut, PowerInOut,
                               ExponentialIn, ExponentialOut, ExponentialInOut,
                               CircularIn, CircularOut, CircularInOut,
                               ElasticIn, ElasticOut, ElasticInOut)

class TestLinear(TestCase):
    def testNormal(self):
        f = Linear()
        self.assertEqual(f(0.00), 0)
        self.assertEqual(f(0.25), 0.25)
        self.assertEqual(f(0.50), 0.5)
        self.assertEqual(f(0.75), 0.75)
        self.assertEqual(f(1.00), 1)

    def testBelowZero(self):
        f = Linear()
        self.assertEqual(f(-1), 0)

    def testAboveOne(self):
        f = Linear()
        self.assertEqual(f(2), 1)

class TestPower(TestCase):
    def testPowerOut(self):
        f = PowerOut(exponent = 2)
        self.assertEqual(f(0.00), 0)
        self.assertEqual(f(0.25), 0.4375)
        self.assertEqual(f(0.50), 0.75)
        self.assertEqual(f(0.75), 0.9375)
        self.assertEqual(f(1.00), 1)

    def testPowerIn(self):
        f = PowerIn(exponent = 3)
        self.assertEqual(f(0.00), 0)
        self.assertEqual(f(0.25), 0.015625)
        self.assertEqual(f(0.50), 0.125)
        self.assertEqual(f(0.75), 0.421875)
        self.assertEqual(f(1.00), 1)

    def testPowerInOut(self):
        f = PowerInOut(exponent = 2)
        self.assertEqual(f(0.00), 0)
        self.assertEqual(f(0.25), 0.125)
        self.assertEqual(f(0.50), 0.5)
        self.assertEqual(f(0.75), 0.875)
        self.assertEqual(f(1.00), 1)

class TestExponential(TestCase):
    def testExponentialIn(self):
        f = ExponentialIn(base = 3, exponent = 4)
        self.assertAlmostEqual(f(0.00), 0)
        self.assertAlmostEqual(f(0.25), 0.025)
        self.assertAlmostEqual(f(0.50), 0.1)
        self.assertAlmostEqual(f(0.75), 0.325)
        self.assertAlmostEqual(f(1.00), 1)

    def testExponentialOut(self):
        f = ExponentialIn(base = 2, exponent = 3)
        self.assertAlmostEqual(f(0.00), 0)
        self.assertAlmostEqual(f(0.25), 0.097399)
        self.assertAlmostEqual(f(0.50), 0.2612039)
        self.assertAlmostEqual(f(0.75), 0.5366898)
        self.assertAlmostEqual(f(1.00), 1)

    def testExponentialInOut(self):
        f = ExponentialInOut(base = 3, exponent = 3)
        self.assertAlmostEqual(f(0.00), 0)
        self.assertAlmostEqual(f(0.25), 0.0806952)
        self.assertAlmostEqual(f(0.50), 0.5)
        self.assertAlmostEqual(f(0.75), 0.9193048)
        self.assertAlmostEqual(f(1.00), 1)

class TestCircular(TestCase):
    def testCircularIn(self):
        f = CircularIn()
        self.assertAlmostEqual(f(0.00), 0)
        self.assertAlmostEqual(f(0.25), 0.0317542)
        self.assertAlmostEqual(f(0.50), 0.1339746)
        self.assertAlmostEqual(f(0.75), 0.3385622)
        self.assertAlmostEqual(f(1.00), 1)

    def testCircularOut(self):
        f = CircularOut()
        self.assertAlmostEqual(f(0.00), 0)
        self.assertAlmostEqual(f(0.25), 0.6614378)
        self.assertAlmostEqual(f(0.50), 0.8660254)
        self.assertAlmostEqual(f(0.75), 0.9682458)
        self.assertAlmostEqual(f(1.00), 1)

    def testCircularInOut(self):
        f = CircularInOut()
        self.assertAlmostEqual(f(0.00), 0)
        self.assertAlmostEqual(f(0.25), 0.0669873)
        self.assertAlmostEqual(f(0.50), 0.5)
        self.assertAlmostEqual(f(0.75), 0.9330127)
        self.assertAlmostEqual(f(1.00), 1)

class TestElastic(TestCase):
    def testElasticIn(self):
        f = ElasticIn(bounces = 4, base = 3, exponent = 2)
        self.assertAlmostEqual(f(0.00), 0)
        self.assertAlmostEqual(f(0.25), -0.0736475)
        self.assertAlmostEqual(f(0.50), 0.2357023)
        self.assertAlmostEqual(f(0.75), -0.5334021)
        self.assertAlmostEqual(f(1.00), 1)

    def testElasticOut(self):
        f = ElasticOut(bounces = 3, base = 2, exponent = 3)
        self.assertAlmostEqual(f(0.00), 0)
        self.assertAlmostEqual(f(0.25), 1.5493421)
        self.assertAlmostEqual(f(0.50), 0.75)
        self.assertAlmostEqual(f(0.75), 1.0804493)
        self.assertAlmostEqual(f(1.00), 1)

    def testElasticInOut(self):
        f = ElasticInOut(bounces = 3, base = 2, exponent = 3)
        self.assertAlmostEqual(f(0.00), 0)
        self.assertAlmostEqual(f(0.25), 0.125)
        self.assertAlmostEqual(f(0.50), 0.5)
        self.assertAlmostEqual(f(0.75), 0.875)
        self.assertAlmostEqual(f(1.00), 1)