from consolemenu import *
from consolemenu.items import *

class dbconfig:
	def __init__(self, arguments: list, switches: list) -> None:
		self.arguments = arguments
		self.switches = switches

#===========================================
	def run(self) -> str:
		if len(self.arguments) < 2:
			self.menu()
			return ""
		return ""

# menu function
	def menu(self) -> None :
		main_menu = ConsoleMenu("Database config", "Supported databases (mysql,sqlite)")

		manage_menu = ConsoleMenu("Manage databases")
		for i in range(10):
			manage_menu.append_item(FunctionItem("Add new sqlite database", self.add_sqlite))

		add_sqlite_databse = FunctionItem("Add new sqlite database", self.add_sqlite)
		main_menu.append_item(add_sqlite_databse)
		add_mysql_database = FunctionItem("Add new mysql database", self.add_mysql)
		main_menu.append_item(add_mysql_database)
		add_mysql_database = SubmenuItem("Manage databases", manage_menu,main_menu)
		main_menu.append_item(add_mysql_database)

		main_menu.show()

# add/manage databse function
	def add_sqlite(self):
		print("""
	Now you can add a new sqlite database
	======================================
	HELP :: you can use 'dbconfig sqlite -n "NAME" -p "SQLITE PATH"'
	for adding new database.
				""")
		name= input("Database name : ")
		path = input("Database file path (full path) : ")
		if name == "" and path == "" :
			input("(ENTER) return to main menu")
			return


	def add_mysql(self):
		print("""
	Now you can add a new mysql database
	======================================
	HELP :: you can use 
	'dbconfig mysql -n "NAME" -u "USER" -p "PASSWORD" -h "HOST" -db "DATABASE NAME"'
	for adding new database.
				""")
		host = input("Database host : ")
		user = input("Database user : ")
		password = input("Database password : ")
		db_name = input("Database name : ")
		if db_name == "" and host == "" and password == "" and user == "" :
			input("(ENTER) return to main menu")
			return


	def database_management(self):
		print("database_management")
		input()
		
