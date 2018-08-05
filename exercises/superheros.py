# Write your solutions for 1.5 here!

class superheroes :
    def __init__(self,name,superpower,streangth):
        self.name=name
        self.superpower=superpower
        self.streangth=streangth
    def superid(self):
        print(self.name,self.streangth)
dr_strange=superheroes("dr.strange","magic", 9001)
dr_strange.superid()