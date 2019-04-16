from lib.Config import Config
import MySQLdb
from warnings import filterwarnings

class Database:
	filterwarnings('ignore', category = MySQLdb.Warning)

	def __init__(self):
		self.config = Config().getConfig()

	def connect(self):
		conn = MySQLdb.connect(
			host=self.config['mysql']['host'],
			port=self.config['mysql']['port'],
			user=self.config['mysql']['username'],
			passwd=self.config['mysql']['password'],
			db=self.config['mysql']['db']
			)
		conn.autocommit(True)
		conn.set_character_set('utf8')
		return conn

	def query(self, sql, args=None):
		conn = self.connect()
		cursor = conn.cursor()
		cursor.execute(sql,args)

		conn.close()
		return cursor

	def queryMany(self, sql, args=None):
		conn = self.connect()
		cursor = conn.cursor()
		cursor.executemany(sql,args)
		
		conn.close()
		return cursor