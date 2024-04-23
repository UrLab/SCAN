from Database import Database
from Displayer import Displayer
from Scanner import Scanner
from Config import Config
from Exceptions import UserNotFound, ProductCodeNotFound, ProductNotFound


def main(scanner, displayer, database, config):
	while 1:
		displayer.displayLine(config.getWelcomeMessage())
		displayer.displayLine(config.getGetUsernameMessage(), "")
		username = scanner.getScan()
		try:
			balance = database.getBalance(username)
		except UserNotFound as error:
			displayer.displayError(error)
			continue
		displayer.displayWords([username, balance])

		displayer.displayLine(config.getGetProductCodeMessage(), "")
		product_code = scanner.getScan()
		try:
			product_name = database.getName(product_code)
			price = database.getPrice(product_name)
		except ProductCodeNotFound as error:
			displayer.displayError(error)
			continue
		except ProductNotFound as error:
			displayer.displayError(error)
			continue
		new_balance = round(balance - price, 2)
		displayer.displayWords([username, balance])
		displayer.displayWords([product_name, price])
		displayer.displayWords([username, new_balance])

		validation = None
		while validation not in [config.getYes(), config.getNo()]:
			displayer.displayLine(config.getGetValidationMessage(), "")
			validation = scanner.getScan()
		if validation == config.getNo():
			continue
		database.writeTransaction(username, product_name, price, balance, new_balance)
		displayer.displayLine(config.getThanksMessage())


if __name__ == "__main__":
	config = Config()
	main(Scanner(config), Displayer(config), Database(config), config)

