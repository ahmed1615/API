import unittest
class PaymentTest(unittest.TestCase):
    def test_paymentInDollar(self):
        print("this is payment in dollar")
        self.assertTrue(True)

    def test_Paymentinbeso(self):
        print("this is payment in beso")
        self.assertTrue(True)
if __name__ == '__main__':
    unittest.main()