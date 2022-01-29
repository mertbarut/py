class Date :
	# ctor
	def __init__(self, day, month, year):
		self.julianDay = 0
		assert self._isValidGregorian(day, month, year), "Invalid Gregorian date."

		tmp = 0
		if month < 3:
			tmp = -1
		self._julianDay = day - 32075 + \
			(1461 * (year + 4800 + tmp) // 4) + \
			(367 * (month - 2 - tmp * 12) // 12) - \
			(3 * ((year + 4900 + tmp) // 100) // 4)

	# some accessors
	def day(self):
		return (self._toGregorian())[0]

	def month(self):
		return (self._toGregorian())[1]

	def year(self):
		return (self._toGregorian())[2]
		
	def dayOfWeek(self) -> int:
		day, month, year = self._toGregorian()
		if month < 3 :
			month = month + 12
			year = year - 1
		return ((13 * month + 3) // 5 + day + \
			year + year // 4 - year // 100 + year // 400) % 7	

	def __str__(self) -> str:
		day, month, year = self._toGregorian()
		return "%02d-%02d-%04d" % (day, month, year)
	
	# comparison operator overloading
	def __eq__(self, otherDate: object) -> bool:
		return self._julianDay == otherDate._julianDay

	def __lt__(self, otherDate: object) -> bool:
		return self._julianDay < otherDate._julianDay
		
	def __le__(self, otherDate: object) -> bool:
		return self._julianDay <= otherDate._julianDay

	def _toGregorian(self) -> tuple:
		A = self._julianDay + 68569
		B = 4 * A // 146097
		A = A - (146097 * B + 3) // 4
		year = 4000 * (A + 1) // 1461001
		A = A - (1461 * year // 4) + 31
		month = 80 * A // 2447
		day = A - (2447 * month // 80)
		A = month // 11
		month = month + 2 - (12 * A)
		year = 100 * (B - 49) + year + A
		return (day, month, year)

	def _isValidGregorian(self, day, month, year) -> bool:
		if day < 0 or month < 0:
			return False
		if month < 13:
			if month < 8:
				if month % 2 == 1:
					if day < 32:
						return True
				else:
					if month == 2:
						if year % 4 == 0:
							if day < 30:
								return True
						else:
							if day < 29:
								return True
					else:
						if day < 31:
							return True
			else:
				if month % 2 == 1:
					if day < 31:
						return True
				else:
					if day < 32:
						return True
		return False
