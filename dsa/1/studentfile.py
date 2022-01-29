class StudentRecord:
	def __init__(self):
		self.id = 0
		self.firstName = None
		self.lastName = None
		self.classCode = 0
		self.gpa = 0.0

class StudentFileReader:
	def __init__(self, inputSrc):
		self._inputSrc = inputSrc
		self._inputFile = None

	def open(self):
		self._inputFile = open(self._inputSrc, "r")
	
	def close(self):
		self._inputFile.close()
		self._inputFile = None
	
	def fetchAll(self):
		theRecords = list()
		student = self.fetchRecord()
		while student != None:
			theRecords.append(student)
			student = self.fetchRecord()
		return theRecords

	def fetchRecord(self):
		line = self._inputFile.readline()
		if line == "" :
			return None
		
		student = StudentRecord()
		student.id = int(line)
		student.firstName = self._inputFile.readline().rstrip()
		student.lastName = self._inputFile.readline().rstrip()
		student.classCode = int(self._inputFile.readline())
		student.gpa = float(self._inputFile.readline())
		return student

def printReport(lst):
	classNames = (None, "Freshman", "Sophomore", "Junior", "Senior")

	print("LIST OF STUDENTS".center(50))
	print("")
	print("%-5s %-25s %-10s %-4s" % ('ID', 'NAME', 'CLASS', 'GPA'))
	print("%5s %25s %10s %4s" % ('-' * 5, '-' * 25, '-' * 10, '-' * 4))

	for record in lst:
		print ("%5d %25s %10s %4.2f" % (record.id, record.lastName + ', ' + record.firstName, classNames[record.classCode], record.gpa))
	
	print('-' * 48)
	print("Number of students:", len(lst))
