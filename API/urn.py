
class demoForTest():
    def __init__(self):
        self.a = "A"
        self.b = 2
    
    

class School():
    def __init__(self):
        #Could be defined by multiple constructors...
        pass
        #properties...
        #head, location, academic cohort snapshot, links.




class SchoolDataSourceUri():
    def __init__(self, baseuri, description, uriconstructor):
        # uses <> as placeholder in the uriconstructor to show urn position.
        # may need to generalise to non urn id numbers?
        #e.g. ("www.raiseonline.org", "Raise website provides summary and interactive analyses...", 
        #	   "www.raiseonline.org/demo?urnid=<>")
        self.baseuri = baseuri
        self.description = description
        self.uriconstructor = uriconstructor
    
    def result(self, urn):
        #Uses replaces the '<>' in uriconstructor to return uri. Returns false if '<>' not found.
        sBase = self.uriconstructor.replace("<>", str(urn))
        if sBase == self.uriconstructor:
            return false     
        else:
            return sBase



