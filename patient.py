class patient:
    def ___init___(self, ID, Name, Diagnosis, Gender, Age):
        self.ID = ID
        self.Name = Name
        self.Diagnosis = Diagnosis
        self.Gender = Gender
        self.Age = Age

    def formatPatientInfo(self):
        return f"{self.ID}_{self.Name}_{self.Diagnosis}_{self.Gender}_{self.Age}"

    def _str_(self):
        return f"{self.ID}_{self.Name}_{self.Diagnosis}_{self.Gender}_{self.Age}"