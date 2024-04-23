class Displayer():
	def __init__(self, config):
		self.__logger = config.getLogger()

	def displayWords(self, words, end="\n"):
		line = ""
		for word in words:
			line += f"{word} "
		self.displayLine(line[:-1], end)

	def displayLine(self, message, end="\n"):
		print(message, end=end)
		self.log(message)

	def displayError(self, error):
		print(error)
		self.logError([[error]])

	def log(self, message):
		self.__logger.write(f"[DISPLAYER] : Displayed '{message}'")

	def logError(self, error):
		self.__logger.write(f"[ERROR] : {error}")
