from date import Date
from linearbag import Bag
from studentfile import StudentFileReader, printReport

if __name__ == "__main__":
	birth = Date(1, 9, 2006)
	print(birth)
	print(birth.day())
	print(birth.month())
	print(birth.year())
	print(birth.dayOfWeek())

	print(Date(23, 11, 4999) < Date(31, 1, 7839))
	print(Date(1, 1, 4242) == Date(1, 1, 4242))

	bag = Bag()
	bag.add(Date(27, 2, 2033))
	bag.add(Date(19, 9, 2009))
	bag.add(Date(11, 2, 2011))
	bag.add(Date(12, 6, 2012))
	bag.add(Date(31, 3, 2022))

	iterator = bag.__iter__()

	while True:
		try:
			item = iterator.__next__()
			print(item)
		except StopIteration:
			break
	
	reader = StudentFileReader("students.txt")
	reader.open()
	studentList = reader.fetchAll()
	reader.close()

	studentList.sort(key = lambda rec: rec.id)
	printReport(studentList)


