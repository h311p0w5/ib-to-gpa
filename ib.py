import time

print('''
██╗██████╗░  ████████╗░█████╗░  ░██████╗░██████╗░░█████╗░
██║██╔══██╗  ╚══██╔══╝██╔══██╗  ██╔════╝░██╔══██╗██╔══██╗
██║██████╦╝  ░░░██║░░░██║░░██║  ██║░░██╗░██████╔╝███████║
██║██╔══██╗  ░░░██║░░░██║░░██║  ██║░░╚██╗██╔═══╝░██╔══██║
██║██████╦╝  ░░░██║░░░╚█████╔╝  ╚██████╔╝██║░░░░░██║░░██║
╚═╝╚═════╝░  ░░░╚═╝░░░░╚════╝░  ░╚═════╝░╚═╝░░░░░╚═╝░░╚═╝

░█████╗░░█████╗░██╗░░░░░░█████╗░██╗░░░██╗██╗░░░░░░█████╗░████████╗░█████╗░██████╗░
██╔══██╗██╔══██╗██║░░░░░██╔══██╗██║░░░██║██║░░░░░██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
██║░░╚═╝███████║██║░░░░░██║░░╚═╝██║░░░██║██║░░░░░███████║░░░██║░░░██║░░██║██████╔╝
██║░░██╗██╔══██║██║░░░░░██║░░██╗██║░░░██║██║░░░░░██╔══██║░░░██║░░░██║░░██║██╔══██╗
╚█████╔╝██║░░██║███████╗╚█████╔╝╚██████╔╝███████╗██║░░██║░░░██║░░░╚█████╔╝██║░░██║
░╚════╝░╚═╝░░╚═╝╚══════╝░╚════╝░░╚═════╝░╚══════╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝''')


print("\nMade by h311p0w5 - IB'23")

time.sleep(2)


def gpa(weight):
    gpa_sum = 0.0
    subjects = ["Language & Literature (G1)", "Language Acquisition (G2)", "Individuals and Societies (G3)",
                "Experimental Sciences (G4)", "Mathematics (G5)", "The Arts (G6)"]

    question = True
    while question:
        answr = str(input("\nWould you like to personalize your subjects? (Y/N only) ")).upper()

        if answr == "N":
            time.sleep(0.5)
            print("\nPlease remember that the following groups are only referential."+
                      "\nIf a group you don't take is mentioned, just put the grade of the subject you take as a replacement")
            time.sleep(1.5)
            question = False

        if answr == "Y":
                time.sleep(0.25)

                print("\nPlease remember that the following groups are only referential."+
                      "\nIf a group you don't take is mentioned, just put the name of the subject you take as a replacement")
                time.sleep(1.5)
                for i in range(0, 6):
                    subjects[i] = str(input("\nWhat subject do you take for " + subjects[i] + "? ")).upper()
                question = False


    for i in range(0,6):
        ib_grade = int(input("\nWhat is your grade/predicted for subject <" + subjects[i] +">, from 1 to 7...- "))
        if ib_grade == 7: gpa_sum += weight
        if ib_grade == 6: gpa_sum += 4.0
        if ib_grade == 5: gpa_sum += 3.0
        if ib_grade == 4: gpa_sum += 2.0
        if ib_grade == 3: gpa_sum += 1.0

    return gpa_sum/6


question = True
weight = 0

while question:
    q1 = str(input("\n\n\nDo you wish to get a WEIGHTED [1] or UNWEIGHTED [2] GPA (Weighted suggested)"
                    +"\nPlease enter [1] or [2] "))
    if q1 == "1":
        weight += 4.3
        q1 = "WEIGHTED"
        question = False

    if q1 == "2":
        weight += 4.0
        q1 = "UNWEIGHTED"
        question = False

print(f"\n\nYOUR GPA {q1} IS " + str(gpa(weight)))
print("\nPlease remember that this is unofficial" +
      "\nThis program was created using the estimates provided in: http://gg.gg/ib_gpa")

print("\n\nGood luck with this hellish bloodbath that IB is, fellas!")

input("\n\nPress ENTER to exit")
