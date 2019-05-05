import json
import requests
from .base import Base
from .settings import CUSTOMERURL

class Customer(Base):

	def __init__(self, id=None):
		super(Customer, self).__init__()
		self.baseurl = CUSTOMERURL
		if id:
			self.payload = self.fetch(id)



	def create(self, email, firstname=None, lastname=None, phone=None):

		'''

		Create Customer
		curl "https://api.paystack.co/customer" \
		-H "Authorization: Bearer SECRET_KEY" \
		-H "Content-Type: application/json" \
		-d '{"email": "bojack@horsinaround.com"}' \ 
		-X POST

		QUERY 
			email
			string
			REQUIRED
			Customer's email address


			first_name
			string
			Customer's first name


			last_name
			string
			Customer's last name


			phone
			string
			Customer's phone number


			metadata
			object
			A set of key/value pairs that you can attach to the customer. It can be used to store additional information in a structured format.

			 
			 

		RETURN DATA

		{
		  "status": true,
		  "message": "Customer created",
		  "data": {
		    "email": "bojack@horsinaround.com",
		    "integration": 100032,
		    "domain": "test",
		    "customer_code": "CUS_xnxdt6s1zg1f4nx",
		    "id": 1173,
		    "createdAt": "2016-03-29T20:03:09.584Z",
		    "updatedAt": "2016-03-29T20:03:09.584Z"
		  }
		}

		'''

		if '@' not in email:
			raise ValueError('Provide a valid email address')
		self.data = {
				'email': email,
				'first_name' : firstname,
				'last_name': lastname,
				'phone':phone,
				}
		r = self.execute(1)
		if r:
			return [r['id'], r['customer_code']]
		return r



	def list(self):

		'''


		List Customer
		curl "https://api.paystack.co/customer" \
		-H "Authorization: Bearer SECRET_KEY" 
		-X GET


		'''
		raise NotImplementedError("method not yet implemented")





	def fetch(self, id):

		'''


		Fetch Customer
		curl "https://api.paystack.co/customer/1173" \
		-H "Authorization: Bearer SECRET_KEY" 
		-X GET

		https://api.paystack.co/customer/:id_or_customer_code
		CUS_tiyf5lbhz9fc3hf



		'''
		return self.execute(endpoint = ("/" + str(id)))




	def update(self):

		'''


		Update Customer
		curl "https://api.paystack.co/customer/CUS_xnxdt6s1zg1f4nx" \
		-H "Authorization: Bearer SECRET_KEY" \
		-H "Content-Type: application/json" \
		-d '{"first_name": "BoJack"}' \ 
		-X PUT




		'''
		raise NotImplementedError("method not yet implemented")





	def set_risk_action(self, ccode=''):

		'''




		Whitelist/Backlist Customer
		curl https://api.paystack.co/customer/set_risk_action \
		-H "Authorization: Bearer SECRET_KEY" \
		-H "Content-Type: application/json" \
		-d '{"customer": "CUS_xr58yrr2ujlft9k", "risk_action": "allow"}' \
		-X POST




		'''
		raise NotImplementedError("method not yet implemented")






	def whitelist(self, ccode=''):
		return self.set_risk_action(allow=True, ccode=ccode)

	def whitelist(self, ccode=''):
		return self.set_risk_action(allow=False, ccode=ccode)



	def deactivate_auth(self):


		'''
		Deactivate Authorization
		curl -X POST -H "Authorization: Bearer SECRET_KEY" -H "Content-Type: application/json" -d '{"authorization_code": "AUTH_au6hc0de"}' "https://api.paystack.co/customer/deactivate_authorization"

		'''

		raise NotImplementedError("method not yet implemented")


	def get_subscriptions(self, customer=None):
		if not customer:
			if self.payload:
				data = self.payload
			else:
				raise NotImplementedError('customer id or code not provided')
		else:
			data = self.fetch(customer)
		return data['subscriptions']


	def charge(self, amount):
		pass