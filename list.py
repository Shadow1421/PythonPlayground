# List example

studentNames = ["Neeraj", "Sanjoy", "Ayush", "Amol"]
physicsMarks = [35, 45, 99, 50]
scienceMarks = [55, 33, 55, 22]
englishMarks = [45, 65, 77, 98]
#append data in list
studentNames.append("Sanjay")
physicsMarks.append(79)
scienceMarks.append(43)
englishMarks.append(55)

for index in range(len(studentNames)):
    print(str(studentNames[index]) + " has got " + str(physicsMarks[index]) + " in Physics, " + str(scienceMarks[index]) + " in Science and " + str(englishMarks[index]) + " in English")