import unittest
from Register import Register

class testReg(unittest.TestCase):  
    def setUp(self):
        self.reg = Register()

    def  test_creation(self):
        reg = Register()
        self.assertIsInstance(self.reg,Register)

    def test_password_firstletter(self):
        reg = Register()
        self.assertTrue(self.reg.password_firstletter("Sack01"),"First character should be uppercase")

    def test_password_len(self):         
        reg = Register()
        self.assertGreaterEqual(self.reg.password_len("Sack01"),4,msg="password should not 4 charaters less")
        
    def test_password_Characters(self):         
        reg = Register()
        self.assertRegexpMatches(self.reg.password("SacK01"),"1234567890#$%^&sjbtsvgjg--_","password should contain lowercase, numbers and special characters")

    def test_password_Characters(self):         
        reg = Register()
        self.assertIn(self.reg.Useremail("johndoe@gmail.com"),"johndoe@gmail.com","should be valid email")

        #self.assertEqual(self.reg.Useremail("johndoe@gmail.com"),"*@gmail.com","should be valid email")