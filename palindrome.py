import unittest

def is_palindrome(mystring):
    for indice in range(0, len(mystring)):
        print(mystring[indice] + " --> " + mystring[-(indice +1)])
        if mystring[indice] !=  mystring[-(indice+1)]:
            print("no es")
            return False
    return True

class Testpalindorme(unittest.TestCase):
    def test_a(self):
        result = is_palindrome('a')
        self.assertEqual(result, True)
    
    def test_aa(self):
        result = is_palindrome('aa')
        self.assertEqual(result, True)

    def test_ab(self):
        result = is_palindrome('ab')
        self.assertEqual(result, False)  

    def test_aCa(self):
        result = is_palindrome('aCa')
        self.assertEqual(result, True)  

    def test_aCs(self):
        result = is_palindrome('aCs')
        self.assertEqual(result, False)  

    def test_aBBa(self):
        result = is_palindrome('aBBa')
        self.assertEqual(result, True)  
         
    def test_aBCBa(self):
        result = is_palindrome('aBCBa')
        self.assertEqual(result, True)
    
    def test_aBCCBa(self):
        result = is_palindrome('aBCCBa')
        self.assertEqual(result, True)
    
    def test_ZaBCCBa(self):
        result = is_palindrome('ZaBCCBa')
        self.assertEqual(result, False)

    def test_neuquen(self):
        result = is_palindrome('neuquen')
        self.assertEqual(result, True)
    
    def test_neuqenM(self):
        result = is_palindrome('neuquenM')
        self.assertEqual(result, False)

unittest.main()






