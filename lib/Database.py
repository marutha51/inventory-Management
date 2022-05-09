import psycopg2
import config


class DB:
	def __init__(self, env='local', is_auto_commit=False):
		self.conn = DB.get_db_conn(env)
		self.conn.autocommit = is_auto_commit
	
	def get_db_conn(env):
		conn_params = config.STAGE_DB_PARAMS
		if env == 'local':
			conn_params = config.LOCAL_DB_PARAMS
		if env == 'stage':
			conn_params = config.PROD_DB_PARAMS
		conn = psycopg2.connect(**conn_params)
		return conn

	def exec_query(self,query):
		cur = self.get_cursor()
		cur.execute(query=query)

	def get_cursor(self):
		return self.conn.cursor()
