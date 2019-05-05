import requests
from .base import Base
from .settings import PLANURL, PAYSTACK_AUTH


class Plan(Base):

    # _CONTENT_TYPE = "application/json"
    # _URL = PLANURL


	# def __init__(self, auth=None):
	# 	if auth:
	# 		self._header = {'Authorization': auth,'Content-Type': self._CONTENT_TYPE}
	# 	elif PAYSTACK_AUTH:
	# 		self._header = {'Authorization': PAYSTACK_AUTH,'Content-Type': 'application/json'}
	# 	else:
	# 		raise NotImplementedError('Missing authorization Key')

	def __init__(self, code=None, id=None):
		super(Plan, self).__init__()
		self.baseurl = PLANURL
		if code:
			self.get_one(code)

	def create(self, name=None, interval=None, amount=None, description=None):

		'''

		Create plan
		curl https://api.paystack.co/plan \
		-H "Authorization: Bearer SECRET_KEY" \
		-H "Content-Type: application/json" \
		-d '{"name": "Monthly retainer", "interval": "monthly", "amount": 500000}' \
		-X POST


		'''
		payload = {}
		if not (name and interval and amount):
			raise NotImplementedError('Plan requires a name, interval and amount')
		payload['name'] = name
		payload['interval'] = interval
		payload['amount'] = amount
		payload['description'] = description
		if payload:
			self.data = payload
			return self.execute(1)
		else:
			raise NotImplementedError('Missing plan creation payload')



	def get(self, plan_code=None):

		'''

				
		Fetch plan
		curl "https://api.paystack.co/plan/PLN_gx2wn530m0i3w3m" \
		-H "Authorization: Bearer SECRET_KEY" 
		-X GET


		'''

		if plan_code:
			plan_url += plan_cpde
			requests.get(plan_url, headers=header)
			print(r.status_code)
			er = r.json()
			return er['data']
		else:
			raise NotImplementedError('Missing plan code')


	def update(self,  plan_code = None, name=None, amount=None, description=None):

		'''

		
		Update plan
		curl "https://api.paystack.co/plan/PLN_gx2wn530m0i3w3m" \
		-H "Authorization: Bearer SECRET_KEY" \
		-H "Content-Type: application/json" \
		-d '{"name": "Monthly retainer (renamed)"}' \ 
		-X PUT



		'''
		if plan_code:
			plan_url += plan_id
			self.data= {'name': 'DSP-5000', 'description':'Daily Savings Plan 5000', 'amount': 500000}
			result = self.execute(2, endpoint=('/' + plan_code))
			if result:
				return result
		else:
			raise NotImplementedError('Missing plan code')


	def get_subscriptions(self, plan_code):
		plan = self.get(plan_code)
		return plan['subscriptions']