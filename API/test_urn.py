import unittest
import urn
import urlparse


#TODO: 

class SchoolDataSourceUriTests(unittest.TestCase):
    #    self.a = "A"
    #    self.b = 2
    def setUp(self):
        #def __init__(self, baseuri, description, uriconstructor):
        self.thisTestClass = urn.SchoolDataSourceUri("http://www.ofsted.gov.uk/inspection-reports/find-inspection-report/provider/ELS/", 
                                                     "OFSTED Inspection Reports", "http://www.ofsted.gov.uk/inspection-reports/find-inspection-report/provider/ELS/<>")
        self.returnedURI = self.thisTestClass.result(138825)
                                                     
    def testConstructedURIInsertsExpectedURN(self):
        self.assertEquals(self.returnedURI, "http://www.ofsted.gov.uk/inspection-reports/find-inspection-report/provider/ELS/138825")

    def testConstructedURIIsValidURI(self):
        #Based on http://stackoverflow.com/questions/12565098/python-how-to-check-if-a-string-is-a-valid-iri
        parts = urlparse.urlsplit(self.returnedURI)  
        self.failIf( not parts.scheme or not parts.netloc) #'''apparently not an url'''
            

        
        

class demoForTestTests(unittest.TestCase):
    #    self.a = "A"
    #    self.b = 2
    def setUp(self):
        self.thisTestClass = urn.demoForTest()
    
    def testOne(self):
        self.failUnless(self.thisTestClass.a == "A")
    
    def testTwo(self):
        self.failIf(self.thisTestClass.b == "A")
    
    def testThree(self):
        self.failUnless(self.thisTestClass.b == 2)

        
        
def main():
    unittest.main()

if __name__ == '__main__':
    #Based on http://stackoverflow.com/questions/9202772/tests-succeed-still-get-traceback
    # ...response from Remi, to handle error when used in IDE.
    try:
        unittest.main()
    except SystemExit as inst:
        if inst.args[0] is True: # raised by sys.exit(True) when tests failed
            raise
