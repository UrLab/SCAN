class Database():
	def __init__(self, config):
		self.__logger = config.getLogger()
		self.__transactionbase_file = config.getTransactionbaseFile();
		self.__userbase_file = config.getUserbaseFile()
		self.__codebase_file = config.getCodebaseFile()
		self.__productbase_file = config.getProductbaseFile()

	def getBalance(self, username):
		try:
			return float(self.getInfo(self.__userbase_file, username))
		except ValueError:
			self.addUser(username)
			return 0

	def getName(self, product_code):
		return self.getInfo(self.__codebase_file, product_code)

	def getPrice(self, product_name):
		return float(self.getInfo(self.__productbase_file, product_name))

	def getInfo(self, db_file, filter_):
		with open(db_file, 'r') as database:
			for line in database:
				line = line[:-1].split(",")
				if line[1] == filter_:
					return line[2]

		raise ValueError("Information not found")

	def getLastId(self, db_file):
		with open(db_file, 'r') as database:
			lines = database.readlines()
			if len(lines) == 0:
				return 0
			return int(lines[-1].split(",")[0])

	def addUser(self, username):
		with open(self.__userbase_file, 'a') as database:
			id_ = self.getLastId(self.__userbase_file) + 1
			database.write(f"{id_},{username},0\n")

		self.logUser(id_, username)

	def writeTransaction(self, username, product, price, balance, new_balance):
		with open(self.__transactionbase_file, 'a') as database:
			id_ = self.getLastId(self.__transactionbase_file) + 1
			database.write(f"{id_},{username},{product},{price},{balance},{new_balance}\n")

		self.logTransaction(username, product, price, balance, new_balance, id_)

	def logUser(self, id_, username):
		self.__logger.write(f"[DATABASE] : Added user '{id_}' '{username}'")

	def logTransaction(self, username, product, price, balance, new_balance, last_id):
		self.__logger.write(f"[DATABASE] : Wrote transaction '{username}' '{product}' '{price}' '{balance}' '{new_balance}' with id '{last_id+1}'")

