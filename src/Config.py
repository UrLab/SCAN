from Logger import Logger
from CONFIG import *

class Config():
	def __init__(self):
		self.__thanks_message = THANKS_MESSAGE
		self.__database_folder = DATABASE_FOLDER
		self.__userbase_file = DATABASE_FOLDER + "/" + USERBASE_FILE
		self.__productbase_file = DATABASE_FOLDER + "/" + PRODUCTBASE_FILE
		self.__codebase_file = DATABASE_FOLDER + "/" + CODEBASE_FILE
		self.__transactionbase_file = DATABASE_FOLDER + "/" + TRANSACTIONBASE_FILE
		self.__log_file = LOG_FILE
		self.__logger = Logger(self.__log_file)

	def getLogger(self):
		return self.__logger

	def getThanksMessage(self):
		return self.__thanks_message

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

