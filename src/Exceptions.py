from CONFIG import USER_NOT_FOUND_ERROR_MESSAGE, PRODUCT_CODE_NOT_FOUND_ERROR_MESSAGE, PRODUCT_NOT_FOUND_ERROR_MESSAGE

class ProductNotFound(Exception):
	def __init__(self):
		self.message = PRODUCT_NOT_FOUND_ERROR_MESSAGE

	def __str__(self):
		return self.message

class UserNotFound(Exception):
	def __init__(self):
		self.message = USER_NOT_FOUND_ERROR_MESSAGE

	def __str__(self):
		return self.message

class ProductCodeNotFound(Exception):
	def __init__(self):
		self.message = PRODUCT_CODE_NOT_FOUND_ERROR_MESSAGE

	def __str__(self):
		return self.message

