class Date :
	def __init__(self, day, month, year):
		self.julianDay = 0
		assert self._isValidGregorian(day, month, year), \
			"Invalid Gregorian date."

		tmp = 0
		if month < 3:
			tmp = -1
		self._julianDay = day - 32075 + \
			(1461 * (year + 4800 + tmp) // 4) + \
			(367 * (month - 2 - tmp * 12) // 12) - \
			(3 * ((year + 4900 + tmp) // 100) // 4)

		def day(self):
			return (self._toGregorian())[0]

		def month(self):
			return (self._toGregorian())[1]

		def year(self):
			return (self._toGregorian())[2]
		
		def dayOfWeek(self):
			day, month, year = self._toGregorian()
			if month < 3 :
				month = month + 12
				year = year - 1
				return ((13 * month + 3) // 5 + day + \
					year + year // 4 - year // 100 + year // 400) % 7
				 