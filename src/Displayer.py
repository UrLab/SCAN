class Displayer():
	def __init__(self, config):
		self.__logger = config.getLogger()

	def display(self, message_matrix):
		for line in message_matrix:
			for word in line:
				print(word, end=" ")
			print()
		self.log(message_matrix)

	def log(self, message_matrix):
		for line in message_matrix:
			self.__logger.write(f"[DISPLAYER] : Displayed '{line}'")

