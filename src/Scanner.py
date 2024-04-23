class Scanner():
	def __init__(self, config):
		self.__logger = config.getLogger()

	def getScan(self):
		scan = input()
		self.log(scan)
		return scan

	def log(self, message):
		self.__logger.write(f"[SCANNER] : Scanned '{message}'")

