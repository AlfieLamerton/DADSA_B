# Main.py

# 1. Import the data into a data structure that you will create DONE
# 2. Calculate the BMI for each patient and classify these patients as underweight, normal, overweight, or obese. DONE
# 3. Update the data structure adding the BMI DONE
# 4. Display / Print on screen the patient name, age, BMI, and weight classification. Sort the display so that those classed as obese are shown at the top of the screen , followed by those classed as underweight, then those that are overweight with the list completed by those that are classed as normal body mass. Insert breaks every 10 patients to allow the user of the system to study the results.
# 5. Display / Print on screen the worst 5 underweight and the worst 5 obese patients in two groupings, male and female.

import csv
# Module 1
# Read the file and save data
# 1. Create patient class DONE
# 2. Create function that takes data and saves to another data structure

# This array holds all patients
patientList = {}

underweightPatients = {}
normalweightPatients = {}
overweightPatients = {}
obesePatients = {}

# Patient class
# Objects of this class represent each patient in the file
# The attributes store all the data needed for classification
class Patient:


    # Old constructor required all attributes be SET in call, new one only does so for fields guaranteed to be present (first 5)
    #def __init__(self, name, dateOfBirth, sex, height, weight, smokes, asthmatic, ntjNtr, hyperTension, renalRT, ileostomyColostomy, parenteral):
    def __init__(self, name, dateOfBirth, sex, height, weight):
        self.name = name
        self.dateOfBirth = dateOfBirth
        self.sex = sex
        self.height = height
        self.weight = weight

        # Attribute assignment omitted for now
        # self.smokes = smokes
        # self.asthmatic = asthmatic
        # self.ntjNtr = ntjNtr
        # self.hypertension = hyperTension
        # self.renalRT = renalRT
        # self.ileostomyColostomy = ileostomyColostomy
        # self.parenteral = parenteral

        self.nutrition = None
        self.BMI = self.weight / (self.height ** 2)
        self.fitness = None
        self.weightClass = None

    def classifyPatientByWeight(self):

        # Patient weighs less than 18.5 kg, underweight
        if (self.calculateBMI < 18.5): self.weightClass = "underweight" # could return 1
        
        # Patient weighs 18.5kg or more and 25kg or less, normal
        elif (self.calculateBMI >= 18.5 and self.calculateBMI <= 25): self.weightClass = "normal" # 2
  
        if (self.fitness == "slim"):

            # Patient weighs more than 25kg and 28kg or less, overweight
            if (self.calculateBMI > 25 and self.calculateBMI <= 28): self.weightClass = "overweight" # 3
            
            # Patient weighs more than 28kg, obese
            elif (self.calculateBMI > 28): self.weightClass = "obese" # 4

        elif (self.fitness == "regular"):

            # Patient weighs more than 25kg and 28kg or less, overweight
            if (self.calculateBMI > 25 and self.calculateBMI <= 29): self.weightClass = "overweight" # 3
            
            # Patient weighs more than 28kg, obese
            elif (self.calculateBMI > 29): self.weightClass = "obese" # 4
        
        elif (self.fitness == "athletic"):

            # Patient weighs more than 25kg and 28kg or less, overweight
            if (self.calculateBMI > 25 and self.calculateBMI <= 30): self.weightClass = "overweight" # 3
            
            # Patient weighs more than 28kg, obese
            elif (self.calculateBMI > 30): self.weightClass = "obese" # 4
    
    def patientDisplay(self):
        print(self.name)
        print(self.age)
        print(self.BMI)
        print(self.weightClass)


# Function to read the CSV file
# Once this is executed, all the data in the CSV file is organised into patient objects, and these objects added to an array
# Using that array, we can start to classify patients
def readFileSavePatients(fileName):

    with open(fileName, newline = '') as patientData:
        reader = csv.reader(patientData)
        next(reader)

        # Iterate through each row in the file i.e. each patient
        for row in reader:

            # We run into a problem here!
            # When there is a blank cell (''), it still adds the next cell's value to the patient object.
            # Not only does this mean that not all the data is being collected, but it also means the data that is being collected will be wrong in most cases
            # Come up with a brute force approach then condense
            # First 5 cells are guaranteed, the rest are not

            # Instantiate a new patient object
            patient = Patient(row[1], row[2], row[3], row[4], row[5])
            

            # Extract data from file into Patient object

            patient.name = row[1] 
            patient.DateOfBirth = row[2]
            patient.sex = row[3]
            patient.height = row[4]
            patient.weight = row[5]
            patient.smokes = row[6]
            patient.asthmatic = row[7]
            patient.ntjNtr = row[8]
            patient.hypertension = row[9]
            patient.renalRT = row[10]
            patient.ileostomyColostomy = row[11]
            patient.parenteral = row[12]
            patient.nutrition = row[13] # There's no data in this field

            # Add patient to list of patients
            patientList.append(patient)

    patientData.close()

# Function to split the original patient list into 4 separate lists based on weightClass attribute
def orderPatientsByWeightClass(patientList):

    underweightPatients = {}
    normalweightPatients = {}
    overweightPatients = {}
    obesePatients = {}

    for i in patientList:
        # Set weightclass attribute for each patient according to their BMI
        patientList[i].assignWeightClass;
        # Put patients into arrays based on their weight class
        # This extra classification might not be needed since the patients are already classified by the attribute
        if (patientList[i].weightClass == "underweight"): underweightPatients.append(patientList[i])
        elif (patientList[i].weightClass == "normalWeight"): normalweightPatients.append(patientList[i])
        elif (patientList[i].weightClass == "overWeight"): overweightPatients.append(patientList[i])
        elif (patientList[i].weightClass == "obese"): obesePatients.append(patientList[i])

    return underweightPatients, normalweightPatients, overweightPatients, obesePatients

#-----------------------------------------------------------------------------------------------------------
# Function to print out patient data
# Input: patientList (array containing Patient objects)
# Output: result of patientDisplay method for each element in input array
# Iterates through the  passed to it (it should only ever be passed the global array patientList - 15/03/21)
#-----------------------------------------------------------------------------------------------------------

def printPatientData(patientList):
    for patient in patientList:
        # Display method is called on each object
        patientList[patient].patientDisplay()
        # New line for every 10 prints (as spec asks)
        if (patient % 10 == 0): print("\n")


#-----------------------#
# - Execution section - #
#-----------------------#

readFileSavePatients("DADSA 2021 CWK B DATA COLLECTION.csv")

for i in patientList:
        # Set weightclass attribute for each patient according to their BMI
        patientList[i].assignWeightClass;
        # Put patients into arrays based on their weight class
        # This extra classification might not be needed since the patients are already classified by the attribute
        if (patientList[i].weightClass == "underweight"): underweightPatients.append(patientList[i])
        elif (patientList[i].weightClass == "normalWeight"): normalweightPatients.append(patientList[i])
        elif (patientList[i].weightClass == "overWeight"): overweightPatients.append(patientList[i])
        elif (patientList[i].weightClass == "obese"): obesePatients.append(patientList[i])

printPatientData(underweightPatients)
printPatientData(normalweightPatients)
printPatientData(overweightPatients)
printPatientData(obesePatients)



# TODO
# Find out what's left to do from this module
# Do that and move onto next module
# Consult spec to make sure you're staying on track