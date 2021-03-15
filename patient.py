# Patient.py

class Patient:

    # These may need to be set in the constructor
    fitness = None
    weightClass = None

    def __init__(self):
        self.name
        self.dateOfBirth
        self.height
        self.weight
        self.smokes
        self.asthmatic
        self.ntjNtr
        self.hypertension
        self.renalRT
        self.ileostomyColostomy
        self.parenteral
        self.nutrition # No data

    def calculateBMI(self):
        return self.weight / (self.height ** 2)

    def classifyPatientByWeight(self):

        # Patient weighs less than 18.5 kg, underweight
        if (self.calculateBMI < 18.5): return "underweight" # could return 1
        
        # Patient weighs 18.5kg or more and 25kg or less, normal
        elif (self.calculateBMI >= 18.5 and self.calculateBMI <= 25): return "normal" # 2
  
        if (self.fitness == "slim"):

            # Patient weighs more than 25kg and 28kg or less, overweight
            if (self.calculateBMI > 25 and self.calculateBMI <= 28 ): return "overweight" # 3
            
            # Patient weighs more than 28kg, obese
            elif (self.calculateBMI > 28): return "obese" # 4

        elif (self.fitness == "regular"):

            # Patient weighs more than 25kg and 28kg or less, overweight
            if (self.calculateBMI > 25 and self.calculateBMI <= 29 ): return "overweight" # 3
            
            # Patient weighs more than 28kg, obese
            elif (self.calculateBMI > 29): return "obese" # 4
        
        elif (self.fitness == "athletic"):

            # Patient weighs more than 25kg and 28kg or less, overweight
            if (self.calculateBMI > 25 and self.calculateBMI <= 30 ): return "overweight" # 3
            
            # Patient weighs more than 28kg, obese
            elif (self.calculateBMI > 30): return "obese" # 4
        