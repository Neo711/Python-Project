import patient as p
import os

#Menu
def menu():
    print(" Patient Menu  \n 0 - Return to Main Menu \n 1 - Display patient's list \n 2 - Search for patient by ID \n 3 - Add patient \n 4 - Edit patient info")


#searchPatientByID
def searchPatientByID():
    aaa = False
    patientID = str(input("Enter patient ID: "))
    file = open("txt/patients.txt", "r")

    for line in file:
        if patientID in line:
            print(line)
            aaa = True


#edirPatientInfo
def editPatientInfo():
    file = open("txt/patients.txt", "r")
    filecopy = open("txt/copypatients.txt", "w")

    print("\n")
    p.patient.ID = (input("Enter the patient ID: "))
    print("\n")

    lines = ' '
    while (lines):
        lines = file.readline()
        line = lines.replace ("_", " ")
        area = lines.split("_")
        if len(lines)>0:
            if(area[0]) == p.patient.ID:
                print(line)
                p.patient.Name = input("Enter new Name: ")
                p.patient.Diagnosis = input("Enter new Diagnosis: ")
                p.patient.Gender = input("Enter new Gender: ")
                p.patient.Age = input("Enter new Age: ")
                filecopy.write(p.patient.ID+"_"+p.patient.Name+"_"+p.patient.Diagnosis+"_"+p.patient.Gender+"_"+p.patient.Age+"\n")
            else:
                filecopy.write(lines)
    
    file.close()
    filecopy.close()
    os.remove("txt/patients.txt")
    os.rename("txt/copypatients.txt", "patients.txt")


#readPatientsFile
def readPatientsFile():
    with open("txt/patients.txt",'r') as file:
        for line in file:
            grade_data = line.strip().split(',')
            print(grade_data)


def addPatientToList():
    ID = str(input("Enter patient ID: "))
    Name = str(input("Enter patient Name: "))
    Diagnosis = str(input("Enter patient Diagnosis: "))
    Gender = str("Enter patient Gender: ")
    Age = str(input("Enter patient Age: "))

    writePatientListToFile(p.patient(ID, Name, Diagnosis, Gender, Age))

def writePatientListToFile(patient):
    lines = [patient.ID , "_", patient.Name, "_", patient.Diagnosis, "_", patient.Gender, "_", patient.Age]
    with open("txt/patients.txt", "a") as f:
        f.writeline(lines)

def displayPatientList():
    file = open("txt/patients.txt")
    for lines in file:
        lines = lines.replace("_", " ")
        print(lines)
    file.close()

menu()
option = int(input(" Enter your option: "))

while option != 0:
    if option == 1:
        readPatientsFile()

    elif option == 2:
        searchPatientByID()
        
    elif option == 3:
        addPatientToList()
        writePatientListToFile()
        displayPatientList()

    elif option == 4:
        editPatientInfo()
        
    else:
        print("Invalid Option")
    
    print()
    menu()
    option = int(input(" Enter your option: "))





