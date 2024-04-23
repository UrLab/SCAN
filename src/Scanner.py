class Scanner():
	def __init__(self, config):
		self.__logger = config.getLogger()
		self.__exit_entry = config.getExitEntry()

	def getScan(self):
		scan = input()
		self.log(scan)
		if scan == self.__exit_entry:
			 exit(0)
		return scan

	def log(self, message):
		self.__logger.write(f"[SCANNER] : Scanned '{message}'")

