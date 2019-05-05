from .base import Base
from .settings import TRANSACTIONURL


class Transactions(Base):


	def __init__(self):
		super(Transactions, self).__init__()
		self.baseurl = TRANSACTIONURL


	def initialize(reference='', amount=0, email=''):


		'''
		PAYSTACK TRANSACTION API

		Initialize Transaction
		curl https://api.paystack.co/transaction/initialize \
		-H "Authorization: Bearer SECRET_KEY" \
		-H "Content-Type: application/json" \
		-d '{"reference": "7PVGX8MEk85tgeEpVDtD", "amount": 500000, "email": "customer@email.com"}' \
		-X POST
		'''



		raise NotImplementedError('You have not done this yet')




	def charge_auth(self, auth_code='', email='', amount=0):

		'''
		Charge Authorization
		curl https://api.paystack.co/transaction/charge_authorization \
		-H "Authorization: Bearer SECRET_KEY" \
		-H "Content-Type: application/json" \
		-d '{"authorization_code": "AUTH_72btv547", "email": "bojack@horsinaround.com", "amount": 500000}' \
		-X POST
		'''

		raise NotImplementedError('You have not done this yet')



	def re_auth(self):

		'''
		Request Reauthorization
		curl https://api.paystack.co/transaction/request_reauthorization \
		-H "Authorization: Bearer SECRET_KEY" \
		-H "Content-Type: application/json" \
		-d '{"authorization_code": "AUTH_72btv547", "email": "bojack@horsinaround.com", "amount": 500000}' \
		-X POST
		'''
	
		return ''





	def check_auth(self, auth_code='', email='', amount=0):

		'''
			Check Authorization
			curl https://api.paystack.co/transaction/check_authorization \
			-H "Authorization: Bearer SECRET_KEY" \
			-H "Content-Type: application/json" \
			-d '{"authorization_code": "AUTH_72btv547", "email": "bojack@horsinaround.com", "amount": 500000}' \
			-X POST
		'''
	
		return ''





	def verify(self, reference_code):
		'''
		Verify transaction
		curl https://api.paystack.co/transaction/verify/DG4uishudoq90LD \
		-H "Authorization: Bearer SECRET_KEY"
		'''
		return self.execute(endpoint = ('/verify/' + reference_code))



	def verify_by_customer(self, plan_code=None, reference_code=None, email=None, customer_id=None, customer_code=None):
		data = self.verify(reference_code)
		if customer_id: ver_measure =  customer_id
		elif customer_code: ver_measure =  customer_code
		elif email: ver_measure =  email
		else:
			raise TypeError('email or customer_detail cannot be null')


		# if (plan_code == data['plan'] ) and (email==  data['customer']['email'])  : pass
		
		cus = data['customer']
		auth = data['authorization']
		plan = data['plan']

		if ((cus['email'] == email) and (data['plan'] == plan_code)):
			return True
		return False

	def get_auth(self):
		return self.payload['authorization']

	def get_customer(self):
		return self.payload['authorization']

	def get_plan(self):
		return self.payload['plan']


	def fetch(self, id=0):

		'''
		Fetch Transaction
		curl "https://api.paystack.co/transaction/2091" \
		-H "Authorization: Bearer SECRET_KEY" 
		-X GET

		'''


		return ''




	def timeline(self, id=0):

		'''
			View transaction Timeline
		curl https://api.paystack.co/transaction/timeline/21002R319U5139 \
		-H "Authorization: Bearer SECRET_KEY"
		'''
	
		return ''





	def totals(self, user=None):

		'''
		
		Transaction Totals
		curl "https://api.paystack.co/transaction/totals" \
		-H "Authorization: Bearer SECRET_KEY" 
		-X GET
		'''
	
		return ''

	def user_totals(self, customer_id):
		self.data = {'customer': customer_id, 'status': 'success'}
		self.execute()
		rmeta = self.payload['meta']
		# f = open('data.json', 'w+')
		# f.write(str(self.payload))
		# f.close()
		print(self.payload)
		amount = 0
		# for item in self.payload['data']:
		# 	amount += item['amount']
		return rmeta["total_volume"]
		# return amount


	def export(self):

		'''
		
		Export Transaction
		curl "https://api.paystack.co/transaction/export" \
		-H "Authorization: Bearer SECRET_KEY" 
		-X GET

		'''
	
		return ''


	def verify_transaction(ref_code='', email='', plan_code = ''):
		transaction_url = 'https://api.paystack.co/transaction/verify/'
		if ref_code == '':
			raise ValueError('please provide a referece code')
		transaction_url += ref_code
		r = self.requests.get(transaction_url, headers=self.header)
		r = r.json() 
		print(r)

		if r['status']:
			data = r['data']
			cus = data['customer']
			auth = data['authorization']
			plan = data['plan']
			print(cus['email'],email,data['plan'], plan_code)
			print(type(cus['email']),type(email),type(data['plan']), type(plan_code))
			print('True0 True0')
			if ((cus['email'] == email) and (data['plan'] == plan_code)):
				print('True')
				return True
		print('False')
		return False

