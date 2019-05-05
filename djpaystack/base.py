import requests
import json
from .settings import PLANURL, PAYSTACK_AUTH

class Base:

	CONTENT_TYPE = "application/json"
	baseurl = ''

	@classmethod
	def __init__(self, auth=None):

		self.requests = requests
		self.json = json
		self.data = {}
		if auth:
			self.header = {'Authorization': auth,'content-type': 'application/json'}
		elif PAYSTACK_AUTH:
			self.header = {'Authorization': PAYSTACK_AUTH,'content-type': 'application/json'}
		else:
			raise NotImplementedError('Missing authorization Key')


	def load(self):
		return self.json.loads(self.data)

	def dump(self):
		return self.json.dumps(self.data)

	def execute(self, method=0, endpoint=''):
		if method == 0:
			r = self.requests.get(self.baseurl + endpoint, params=self.data, headers=self.header)
		elif method == 1:
			r = self.requests.post(self.baseurl + endpoint, data=self.dump(), headers=self.header)
		elif method == 2:
			r = self.requests.put(self.baseurl + endpoint, data=self.dump(), headers=self.header)
		else: raise ValueError('Please specify a valid method')

		self.payload = r.json()
		if self.payload['status'] == True:
			try:
				return self.payload['data']
			except KeyError:
				return self.payload['status']
		else:
			print(self.payload)
			print(self.payload['message'])


	def list_all(self):
		return self.execute()

	def get_one(self, id):
		if type(id) is not str: id=str(id)
		endpoint = '/' + id
		return self.execute(endpoint=endpoint)

	def get_data(self):
		return self.payload