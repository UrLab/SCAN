from Logger import Logger
from CONFIG import *
from Exceptions import UserNotFound, ProductCodeNotFound, ProductNotFound

class Config():
	def __init__(self):
		self.__exit_entry = EXIT_ENTRY
		self.__yes = YES
		self.__no = NO
		self.__welcome_message = WELCOME_MESSAGE
		self.__get_username_message = GET_USERNAME_MESSAGE
		self.__get_product_code_message = GET_PRODUCT_CODE_MESSAGE
		self.__get_validation_message = GET_VALIDATION_MESSAGE
		self.__thanks_message = THANKS_MESSAGE
		self.__database_folder = DATABASE_FOLDER
		self.__userbase_file = DATABASE_FOLDER + "/" + USERBASE_FILE
		self.__productbase_file = DATABASE_FOLDER + "/" + PRODUCTBASE_FILE
		self.__codebase_file = DATABASE_FOLDER + "/" + CODEBASE_FILE
		self.__transactionbase_file = DATABASE_FOLDER + "/" + TRANSACTIONBASE_FILE
		self.__log_file = LOG_FILE
		self.__logger = Logger(self.__log_file)
		self.__logger.write("Program Started")

	def getWelcomeMessage(self):
		return self.__welcome_message

	def getGetUsernameMessage(self):
		return self.__get_username_message

	def getGetProductCodeMessage(self):
		return self.__get_product_code_message

	def getGetValidationMessage(self):
		return self.__get_validation_message

	def getYes(self):
		return self.__yes

	def getNo(self):
		return self.__no

	def getLogger(self):
		return self.__logger

	def getThanksMessage(self):
		return self.__thanks_message

	def getExitEntry(self):
		return self.__exit_entry

	def getDatabaseFolder(self):
		return self.__database_folder

	def getUserbaseFile(self):
		return self.__userbase_file

	def getProductbaseFile(self):
		return self.__productbase_file

	def getCodebaseFile(self):
		return self.__codebase_file

	def getTransactionbaseFile(self):
		return self.__transactionbase_file

	def getLogFile(self):
		return self.__log_file

