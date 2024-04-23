from Database import Database
from Displayer import Displayer
from Scanner import Scanner
from Config import Config

CONFIG_FILE = "CONFIG.py"

def main(scanner, displayer, database, config):
	while 1:
		username = scanner.getScan()
		balance = database.getBalance(username)
		displayer.display([[username, balance]])
		product_code = scanner.getScan()
		product_name = database.getName(product_code)
		price = database.getPrice(product_name)
		displayer.display([[username, balance], [product_name, price], [username, balance - price]])
		#WaitForValidation
		validation = scanner.getScan()
		if validation == "no":
			continue
		database.writeTransaction(username, product_name, price, balance, balance - price)
		displayer.display([[config.getThanksMessage()]])


if __name__ == "__main__":
	config = Config()
	main(Scanner(config), Displayer(config), Database(config), config)

