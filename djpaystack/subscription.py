from .base import Base
from.settings import SUBSCRIPTIONURL

class Subscription(Base):


	def __init__(self, id=None, code=None, plan_code=None, email=None, customer_id=None):
		super(Subscription, self).__init__()
		self.baseurl = SUBSCRIPTIONURL
		if email and plan_code:
			self.create(email=email, plan_code=plan_code)
		if code:
			self.get(code)

		



	def get(self, code):
		return self.execute(endpoint = "/" + code)



	#Create New Subscriber
	def create(self, plan_code=None, email=None, customer_code=None, start_date=None, invoice_limit=2):

		if plan_code and (email or customer_code):
			self.data = {
			'customer': email or customer_code,
			'plan': plan_code,
			'start_date': start_date,
			'invoice_limit': invoice_limit,
			}
			return self.execute(1)
		raise TypeError('plan_code and email or customer_code cannot be None')
		# return  self.execute(endpoint = "/SUB_vsyqdmlzble3uii")


	#Enable User SUbscription
	def enable(self, mode=1, code=None, token=None):
		if mode == 1:
			endpoint = "/enable"
		elif mode == 0:
			endpoint = "/disable"
		self.data = {
		'code': code,
		'token': token
		}
		return  self.execute(1, endpoint = endpoint)


	#Disable User Subscription
	def disable(self, code=None, token=None):
		return self.enable(mode = 0, code=code, token=token)

	def get_for_customer(self, customer_id):
		endpoint = "/" + str(customer_id)
		return self.execute(endpoint=endpoint)
