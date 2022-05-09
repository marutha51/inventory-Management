import sys
sys.path.append('..') #go to root dir
import lib
import pandas as pd

def main():
	try:
		errors = []
		db = lib.DB('local')
		qf = lib.QueryFactory
		data = pd.read_csv('../files/ScheduleII-Price_req.csv')
		product_id_list = list(data.get('product_id', str))
		product_id_dict = data.to_dict('records')
		with db.get_cursor() as cur:
			for id in product_id_list:
				cur.execute(query=qf.activate_product(id))
				if not cur.rowcount:
					print(id)
		db.conn.commit()
		all

	except Exception as e:
		print(e)









if __name__ == '__main__':
	main()