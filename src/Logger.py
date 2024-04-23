from Date import Date

class Logger():
	def __init__(self, log_file):
		self.__log_file = log_file

	def write(self, message):
		with open(self.__log_file, 'a') as log:
			log.write(f"[{Date.now()}] {message}\n")
