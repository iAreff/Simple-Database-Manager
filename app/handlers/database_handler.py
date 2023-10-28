import sqlite3

class database_handler:
	def __init__(self, db_name):
		main_path = "app/db/"
		self.conn = sqlite3.connect(main_path+db_name)
		self.cursor = self.conn.cursor()

	def create_table(self, table_name, columns):
		create_table_sql = f"CREATE TABLE IF NOT EXISTS {table_name} ({columns})"
		self.cursor.execute(create_table_sql)
		self.conn.commit()

	def insert_data(self, table_name, values, columns=""):
		insert_sql = f"INSERT INTO {table_name}{columns} VALUES {values}"
		self.cursor.execute(insert_sql)
		self.conn.commit()

	def delete_data(self, table_name, condition):
		delete_sql = f"DELETE FROM {table_name} {condition}"
		self.cursor.execute(delete_sql)
		self.conn.commit()

	def fetch_data(self, table_name, condition=""):
		select_sql = f"SELECT * FROM {table_name} {condition}"
		self.cursor.execute(select_sql)
		return self.cursor.fetchall()

	def close_connection(self):
		self.conn.close()

