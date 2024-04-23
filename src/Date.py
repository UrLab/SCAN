from datetime import datetime

class Date():
	@classmethod
	def now(cls):
		return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

