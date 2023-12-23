class RailwayForm:
    formType = "RailwayForm"
    def printData(self):
        print(f"Name is {self.Name}")
        print(f"Train is {self.Train}")

raghvsApplication = RailwayForm()
raghvsApplication.Name = "raghav"
raghvsApplication.Train = "Rajdhani express"
raghvsApplication.printData()