from hashlib import new
from config import enum

class QueryFactory:

	def activate_product(product_id):
		if type(product_id) is list:
			print('list')
		return f'''
		update products set product_status_id=(select id from product_statuses where name='active')
    	where id in {tuple(product_id) if type(product_id) is list else f"('{product_id}')"}
		'''
	
	def inactivate_product(product_id):
		return f'''
		update products set product_status_id=(select id from product_statuses where name='inactive')
    	where id in {tuple(product_id) if type(product_id) is list else f"('{product_id}')"}
		'''
	def set_product_breakable(product_id):
		return f'''
		update products set breakable=false
    	where id in {tuple(product_id) if type(product_id) is list else f"('{product_id}')"}
		'''

	def set_product_unbreakable(product_id):
		return f'''
		update products set breakable=false
    	where id in {tuple(product_id) if type(product_id) is list else f"('{product_id}')"}
		'''

	def update_product_price(product_id, price):
		return f'''
		update pricing_base set pricing_per_unit={price}
    	where id = '{product_id}'
		'''

	def get_blocked_affilates(product_id):
		if not product_id: return
		return f'''SELECT product_id, string_agg(a.name, ', ') as blacklisted
				FROM product_affiliation_blacklists pab join affiliations a on pab.affiliation_id=a.id 
				WHERE product_id='{product_id}'
				GROUP BY product_id;'''
	
	def add_affiliate_to_blacklist(product_id, affiliation_name):
		affiliation_id = enum.AffiliationID(affiliation_name)
		if not (product_id and affiliation_id) : return
		return f'''
				INSERT INTO PRODUCT_AFFILIATION_BLACKLISTS(PRODUCT_ID,AFFILIATION_ID,ACTIVATION_DATE,CREATED_AT,UPDATED_AT)
				VALUES('{product_id}','{affiliation_id}',NOW(),NOW(),NOW())
			'''
	
	def affilitae_blaclist_caprx_proudct(product_id):
		'''
		Blacklist all the affilates except caprx
		Arguments:
			product_id: Product ID
		Returns:
			Query
		'''
		new_row = []
		for i in list(enum.AffiliationID):
			new_row.append(f"('{product_id}','{i.value}',NOW(),NOW(),NOW())")
		return f'''INSERT INTO PRODUCT_AFFILIATION_BLACKLISTS(PRODUCT_ID,AFFILIATION_ID,ACTIVATION_DATE,CREATED_AT,UPDATED_AT)
				VALUES {",".join(new_row)}
				'''