import unittest
from package1.TC_logingTest import LoginTest
from package1.TC_singuptest import SignUpTest

from package2.TC_paymentRertrunsTest import PaymentReturntest
from package2.TC_paymentTest import PaymentTest
#get all the testcases in the classes
tc1=unittest.TestLoader().loadTestsFromTestCase(LoginTest)
tc2=unittest.TestLoader().loadTestsFromTestCase(SignUpTest)
tc3=unittest.TestLoader().loadTestsFromTestCase(PaymentReturntest)
tc4=unittest.TestLoader().loadTestsFromTestCase(PaymentTest)



#creating test suites
santlyTEst=unittest.TestSuite([tc1,tc2])
unittest.TextTestRunner().run(santlyTEst)
fuctiontestsu=unittest.TestSuite([tc3,tc4])
unittest.TextTestRunner().run(fuctiontestsu)
mastertest=unittest.TestSuite([tc1,tc2,tc3,tc4])
unittest.TextTestRunner().run(mastertest)
