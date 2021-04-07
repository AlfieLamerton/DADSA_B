# Main.py

# Task 1 DONE
# Task 2:

# Extra:
# 1. Make outputby10 work
# 2. Add 'press any key functionality' to make output nicer

# Questions
# 1. Fitness/build is asked to be included in the spec, but it is never given to us in the form of data
# 2. By conditions, does it mean only the cells which can be ticked 'Y'? Or does weight class count too? Does anything else count?

import csv
import datetime
from datetime import date
from typing import final

#----------------------------------------------------------------------------------------------------------------------------
# Patient class
# Objects of this class represent each patient in the file
# The attributes store all the data needed for classification
#----------------------------------------------------------------------------------------------------------------------------

class Patient:
    
    #Store these attributes as booleans
    smokes = False
    asthmatic = False
    ntjNtr = False
    hypertension = False
    renalRT = False
    ileostomyColostomy = False
    parenteral = False
    nutrition = False

    # fitness = # Fitness/build is asked to be included in the spec, but it is never given to us in the form of data
    weightClass = ""
    # needsReferring = False
    topPriority = False

    # Old constructor required all attributes be SET in call, new one only does so for fields guaranteed to be present (first 5)
    # The rest are set to false unless the file specifies otherwise
    def __init__(self, name, dateOfBirth, sex, height, weight):

        # Store these attributes as strings
        self.name = name
        self.dateOfBirth = dateOfBirth
        self.sex = sex
        # Store height and weight as integers
        self.height = float(height)
        self.weight = float(weight)
        # Calculate BMI according to above attributes as integers
        self.BMI = self.weight / (self.height ** 2)
        # Calculate age according to date of birth
        self.age = calculateAge(dateOfBirth)
    
    def getName(self): return self.name
    def getAge(self): return self.age # Need to calculate age before using this
    def getBMI(self): return self.BMI
    def getWeightClass(self): return self.weightClass # Need to make sure objects have this attribute

    # setWeightClass in method form
        # def setWeightClass(self):
        
        #     # Patient weighs less than 18.5 kg, underweight
        #     if (self.calculateBMI < 18.5): self.weightClass = "underweight" # could return 1
            
        #     # Patient weighs 18.5kg or more and 25kg or less, normal
        #     elif (self.calculateBMI >= 18.5 and self.calculateBMI <= 25): self.weightClass = "normal" # 2

        #     # Patient weighs more than 25kg and 28kg or less, overweight
        #     if (self.calculateBMI > 25 and self.calculateBMI <= 28): self.weightClass = "overweight" # 3
            
        #     # Patient weighs more than 28kg, obese
        #     elif (self.calculateBMI > 28): self.weightClass = "obese" # 4

        # The following if statement is commented because there is nothing that defines whether a patient is slim, regular or athletic.
        # The next section of the program rely on the weight classes being set, and this can't happen if they're not being set properly because of this.
        # COMMENTED CODE

            # if (self.fitness == "slim"):

            #     # Patient weighs more than 25kg and 28kg or less, overweight
            #     if (self.calculateBMI > 25 and self.calculateBMI <= 28): self.weightClass = "overweight" # 3
                
            #     # Patient weighs more than 28kg, obese
            #     elif (self.calculateBMI > 28): self.weightClass = "obese" # 4

            # elif (self.fitness == "regular"):

            #     # Patient weighs more than 25kg and 28kg or less, overweight
            #     if (self.calculateBMI > 25 and self.calculateBMI <= 29): self.weightClass = "overweight" # 3
                
            #     # Patient weighs more than 28kg, obese
            #     elif (self.calculateBMI > 29): self.weightClass = "obese" # 4
            
            # elif (self.fitness == "athletic"):

            #     # Patient weighs more than 25kg and 28kg or less, overweight
            #     if (self.calculateBMI > 25 and self.calculateBMI <= 30): self.weightClass = "overweight" # 3
                
            #     # Patient weighs more than 28kg, obese
            #     elif (self.calculateBMI > 30): self.weightClass = "obese" #l 4
    
    # Currently not used
        # def displayFields(self):
        #     print(self.name)
        #     print(self.age)
        #     print(self.BMI)
        #     print(self.weightClass)

#----------------------------------------------------------------------------------------------------------------------------
# Function to calculate age based on the date of birth passed
# Input: patient's dateOfBirth attribute in string form e.g. "11/12/2002"
# Output: age calculated by subtracting the patient's date of birth from today's date
#----------------------------------------------------------------------------------------------------------------------------

def calculateAge(dateOfBirth):
    # List containing each value in a patient object's dateOfBirth attribute
    dobElementList = dateOfBirth.split("/")
    # Day, month and year of patient's birthday put into separate integer values
    day =   int(dobElementList[0])
    month = int(dobElementList[1])
    year =  int(dobElementList[2])
    # Patient date of birth stored in date variable
    dateOfBirth = datetime.date(year, month, day)
    # Today's date stored to check dates of birth against
    todaysDate = date.today()
    # Patient's age calculated and returned
    return ((todaysDate - dateOfBirth) / 365).days

#----------------------------------------------------------------------------------------------------------------------------
# Function to set the weight class for each patient depending on their BMI and (in theory) their build
#----------------------------------------------------------------------------------------------------------------------------

def setWeightClass(patient):

    # for patient in patientList:
    
        # Patient weighs less than 18.5 kg, underweight
        if (patient.BMI < 18.5): patient.weightClass = "Underweight" # could return 1
        
        # Patient weighs 18.5kg or more and 25kg or less, normal
        elif (patient.BMI >= 18.5 and patient.BMI <= 25): patient.weightClass = "Normal" # 2

        # Patient weighs more than 25kg and 28kg or less, overweight
        if (patient.BMI > 25 and patient.BMI <= 28): patient.weightClass = "Overweight" # 3
        
        # Patient weighs more than 28kg, obese
        elif (patient.BMI > 28): patient.weightClass = "Obese" # 4

#----------------------------------------------------------------------------------------------------------------------------
# Function to read the CSV file
# Once this is executed, all the data in the CSV file is organised into patient objects, and these objects added to an array
# Using that array, we can start to classify patients
#----------------------------------------------------------------------------------------------------------------------------

def readFileSavePatients(fileName):

    patientList = []

    with open(fileName, newline = '') as patientData:

        reader = csv.reader(patientData)
        next(reader)
        # Iterate through each row in the file i.e. each patient
        for row in reader:
            # New Patient object is instantiated and all guaranteed data set by its constructor
            patient = Patient(row[0], row[1], row[2], row[3], row[4])
            
            # Extract data from file into Patient object
            if row[5] != '': patient.smokes = True
            if row[6] != '': patient.asthmatic = True
            if row[7] != '': patient.ntjNtr = True
            if row[8] != '': patient.hypertension = True
            if row[9] != '': patient.renalRT = True
            if row[10] != '': patient.ileostomyColostomy = True
            if row[11] != '': patient.parenteral = True
            # Ignoring nutrition because there's no data

            # Add patient to list of patients
            patientList.append(patient)
            
    patientData.close()
    return patientList

#-----------------------------------------------------------------------------------------------------------
# Function that prints each of the attributes needed for the output section
# Input: patient object
# Output: name, age, BMI and weightClass attributes, in a readable format
# Something extra I could add here is something that checks the number of digits in the float BMI, and changes
# the number of spaces that come after it so that the output aligns better
#-----------------------------------------------------------------------------------------------------------

def displayFields(patient):
    print("Name:", patient.name, " Age: ", patient.age, "BMI:", patient.BMI, "   Weight class:", patient.weightClass)

# For some reason I need to make these two things separate functions, when I try and iterate over the patient object directly from the list, it says 'Patient' is not iterable
def displayFieldsTask2(patient):
    print("Name:", patient.name, "Age: ", patient.age, "Top priority: ", patient.topPriority)

def displayFieldsTask2Loop(patientList): #Remove age
    for patient in patientList:
        displayFieldsTask2(patient)

#% Try and get this to work when finished

# def displayFieldsTask2(patientList):
#     for i in len(patientList):
#         print("Name:", i.name, "Age: ", i.age, "Top priority: ", i.topPriority)

def displayFieldsForTest(thing):
    print("First value: ", thing.attribute1, "Second value: ", thing.attribute2)

#-----------------------------------------------------------------------------------------------------------
# Function outputPer10
# In theory will stop me needing to reuse the count += 1 code
# Doesn't work yet
#-----------------------------------------------------------------------------------------------------------

    # def outputPer10(list, count):
    #     for patient in list:
    #         displayFields(patient)
    #         count += 1
    #         if count % 10 == 0:
    #             print("\n\n")
    #     return count

#-----------------------------------------------------------------------------------------------------------
# Function displayPatients
# Input: 4 patient lists stratified by weight class
# Output: Attribute of each patient required by the specification, with a line break every 10 patients
#-----------------------------------------------------------------------------------------------------------

def displayPatients(obesePatients, underweightPatients, overweightPatients, normalweightPatients):

    # Patients displayed in this order: obese, underweight, overweight, normal
    count = 0

        # This is here from me trying to condense the functionality
        # outputPer10(obesePatients, count)
        # outputPer10(underweightPatients, count)
        # outputPer10(overweightPatients, count)
        # outputPer10(normalweightPatients, count)

    for patient in obesePatients:
        displayFields(patient)
        count += 1
        if count % 10 == 0:
            print("\n\n")

    for patient in underweightPatients:
        displayFields(patient)
        count += 1
        if count % 10 == 0:
            print("\n\n")

    for patient in overweightPatients:
        displayFields(patient)
        count += 1
        if count % 10 == 0:
            print("\n\n")

    for patient in normalweightPatients:
        displayFields(patient)
        count += 1
        if count % 10 == 0:
            print("\n\n")

#-----------------------------------------------------------------------------------------------------------
# Function displayFiveWorst
#-----------------------------------------------------------------------------------------------------------

def displayFiveWorst(underweightPatients, obesePatients):

    # 1. Stratify into subgroups

    underWeightMales = []
    underWeightFemales = []
    obeseMales = []
    obeseFemales = []

    # Underweight patients split into groups by sex
    for patient in underweightPatients:
        if (patient.sex == "M"): underWeightMales.append(patient)
        else: underWeightFemales.append(patient)
    # Obese patients split into groups by sex
    for patient in obesePatients:
        if (patient.sex == "M"): obeseMales.append(patient)
        else: obeseFemales.append(patient)
    
    # 2. Sort subgroups by BMI
    underWeightMales.sort(key = lambda patient: patient.BMI, reverse = False)
    underWeightFemales.sort(key = lambda patient: patient.BMI, reverse = False)
    obeseMales.sort(key = lambda patient: patient.BMI, reverse = True)
    obeseFemales.sort(key = lambda patient: patient.BMI, reverse = True)

    # Display section
    # Current code prints out all patients in the lists
    # Commented code would print out the worst 5, but there aren't enough patients in the file so
    # input out of range exception is raised

    print("Worst underweight males\n")
    for i in underWeightMales:
        displayFields(i)
    # for i in range(0, 4):
    #     displayFields(underWeightMales[i])
    print("\nWorst underweight females\n")
    for i in underWeightFemales:
        displayFields(i)
    # for i in range(0, 4):
    #     displayFields(underWeightFemales[i])
    
    print("\nWorst obese males\n")
    for i in obeseMales:
        displayFields(i)
    # for i in range(0, 4):
    #     displayFields(obeseMales[i])
    print("\nWorst obese females\n")
    for i in obeseFemales:
        displayFields(i)
    # for i in range(0, 4):
    #     displayFields(obeseFemales[i])

#-----------------------------------------------------------------------------------------------------------
# Function: referOrNot
# Input: patient object
# Process: calculates whether or not a given patient needs referral based on the spec,
# if so, that patient is added 
#-----------------------------------------------------------------------------------------------------------

def referOrNot(list):

    newList = []

    for patient in list:
    # First attempt, more brute force
        # if ((patient.weightClass == "Obese" or patient.weightClass == "Underweight")
        # or (patient.hypertension == True)
        # or (patient.asthmatic == True or patient.smokes == True)
        # or (patient.ntjNtr == True)
        # or (patient.renalRT == True)
        # or (patient.ileostomyColostomy == True)
        # or (patient.parenteral == True)):
        #     patient.needsReferring = True
    
    # Second attempt, more streamlined, but going off assumption that inclusive ors can be layered like this
        if ( (patient.weightClass == "Obese" or patient.weightClass == "Underweight")
            or (patient.hypertension 
            or patient.asthmatic
            or patient.smokes
            or patient.ntjNtr
            or patient.renalRT
            or patient.ileostomyColostomy
            or patient.parenteral == True) ): newList.append(patient)

    return newList

#-----------------------------------------------------------------------------------------------------------
# Function: calculatePriority
# Input: patient object
#-----------------------------------------------------------------------------------------------------------

# If we pass this function a list of patients that need to be referred, it won't have to
# deal with extraneous patients
def calculatePriority(newList):

    # Set topPriority to True for patients who are top priority
    for patient in newList:
        count = 0
        # First sentence in rules
        if ( ((patient.asthmatic == True or patient.smokes == True) and patient.age > 55)
        or (patient.weightClass == "Obese" and patient.hypertension == True) ): count += 3

        # Second sentence
        # Adds 1 to a counter for every condition the patient has
        if (patient.smokes == True): count += 1
        if (patient.asthmatic == True): count += 1
        if (patient.ntjNtr == True): count += 1
        if (patient.hypertension == True): count += 1
        if (patient.renalRT == True): count += 1
        if (patient.ileostomyColostomy == True): count += 1
        if (patient.parenteral == True): count += 1
        # By conditions, does it mean only the cells which can be ticked 'Y'? Or does weight class count too?
        if (count > 3): patient.topPriority = True

    # Return new and improved list
    return newList


#-----------------------------------------------------------------------------------------------------------
# stratifyByWeightAndDisplay
# Input: csv file
# Reads file into patient objects, categorises those into arrays, and outputs the contents of those arrays 
# Output: 4 arrays with patient objects, with a line break every 10 patients
#-----------------------------------------------------------------------------------------------------------

def stratifyByWeightAndDisplay(file):

    underweightPatients = []
    normalweightPatients = []
    overweightPatients = []
    obesePatients = []

    # Call readFileSavePatients here to create a list data structure containing objects of the patient class
    patientList = readFileSavePatients(file)
    
    # Patients stratified into subsets by weight class
    for patient in patientList:
        setWeightClass(patient)
        if (patient.weightClass == "Underweight"): underweightPatients.append(patient)
        elif (patient.weightClass == "Normal"): normalweightPatients.append(patient)
        elif (patient.weightClass == "Overweight"): overweightPatients.append(patient)
        elif (patient.weightClass == "Obese"): obesePatients.append(patient)
    
    displayPatients(obesePatients, underweightPatients, overweightPatients, normalweightPatients)
    displayFiveWorst(underweightPatients, obesePatients)

#-----------------------------------------------------------------------------------------------------------
# Function: displayReferralPriority
#-----------------------------------------------------------------------------------------------------------

# This needs sorting out
# I think, in the print section, it should be outputting the top priority patients first. It is printing one
# low priority patient near the top and one high priority patient near the bottom

def displayByPriority(file):

    patientList = readFileSavePatients(file)
    
    for patient in patientList: # For some reason I can't execute a function here for the entire list, I need to adress each object individually
        setWeightClass(patient)
    

    # # { Does some stuff to lists
    # # referralList contains only the patients who need referring. I.e. the ones who will be included in the output
    # referralList = referOrNot(patientList)
    # # topPriorityList builds on referralList by setting each patient's priority attribute
    # topPriorityList = calculatePriority(referralList)
    # # }

    patientList = calculatePriority(patientList) # For all patients considered top priority, their topPriority attribute is assigned here

    #% Now we need to split patientList into two lists: one for topPriority and one for lower priority
    
    topPriorityPatientList = []

    #% This doesn't quite work yet. Not all top priority patients are being removed from patientList
    for patient in patientList:
        if patient.topPriority == True:
            # Remove from patientList
            patientList.remove(patient)
            # Add to new list
            topPriorityPatientList.append(patient)

    
    # # Both lists sorted by age
    patientList.sort(reverse = True, key = lambda patient: patient.age)
    topPriorityPatientList.sort(reverse = True, key = lambda patient: patient.age)

    #% Now we need to concatenate both lists. When finished, work out which of these is faster. Explaining this will get marks

    # topPriorityPatientList.extend(patientList)
    newList = topPriorityPatientList + patientList
    
    # Old thing I may still use
        # topPriorityList and referralList are turned into sets. Each value is compared with the inclusive OR operator, thus removing shared objects. The sets are then turned back into a list.
        #% This list holds all of the patients we are bothered with
        # tempList = list(set(topPriorityList) | set(referralList))
    
    # for patient in newList:
    #     displayFieldsTask2(patient)

    count = 0
    for patient in newList:
        displayFieldsTask2(patient)
        count += 1
        if count % 10 == 0:
            print("\n")


    


#-----------------------#
# - Execution section - #
#-----------------------#

# Task 1
# stratifyByWeightAndDisplay("DADSA 2021 CWK B DATA COLLECTION.csv")

# Task 2
displayByPriority("DADSA 2021 CWK B DATA COLLECTION.csv")

#% Patients with top priority showing up in low priority list: ABD444, DDF333, ABD721
#% There are duplicates!? Could it be the symbol? I'm not using that code anymore! What could it be?
#% The output is different every time I run it