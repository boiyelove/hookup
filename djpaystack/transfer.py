class Transfer:

	def __init__():

	return ''




	def initialize(reference='', amount=0, email=''):

		'''

		Initiate Transfer
		curl https://api.paystack.co/transfer \
		-H "Authorization: Bearer SECRET_KEY" \
		-H "Content-Type: application/json" \
		-d '{"source": "balance", "reason": "Calm down", "amount":3794800, "recipient": "RCP_gx2wn530m0i3w3m"}' \
		-X POST


		'''

	return ''



	def list():
		'''

		List Transfers
		curl -X GET -H "Authorization: Bearer SECRET_KEY" "https://api.paystack.co/transfer"

		'''
	return ''


	def fetch():
		'''

		Fetch Transfers
		curl "https://api.paystack.co/transfer/TRF_2x5j67tnnw1t98k" \
		-H "Authorization: Bearer SECRET_KEY" 
		-X GET

		'''
	return ''



	def finalize():
		'''

	curl https://api.paystack.co/transfer/finalize_transfer \
	-H "Authorization: Bearer SECRET_KEY" \
	-H "Content-Type: application/json" \
	-d '{"transfer_code": "TRF_vsyqdmlzble3uii", "otp": "928783"}' \
	-X POST

		'''
	return ''



	def initiate_bulk():
		'''

		Initiate Bulk Transfer
		curl https://api.paystack.co/transfer \
		-H "Authorization: Bearer SECRET_KEY" \
		-H "Content-Type: application/json" \
		-d '{
			"currency": "NGN",
			"source": "balance",
			"transfers": [
			{
			"amount": 50000,
			"recipient": "RCP_db342dvqvz9qcrn"
			},
			{
			"amount": 50000,
			"recipient": "RCP_db342dvqvz9qcrn"
			}
			]
		}' \
		-X POST


		'''
	return ''



	def create_receipt():
				'''

		Create Transfer Receipt
		curl -X POST -H "Authorization: Bearer SECRET_KEY" -H "Content-Type: application/json" -d '{ 
		   "type": "nuban",
		   "name": "Zombie",
		   "description": "Zombier",
		   "account_number": "01000000010",
		   "bank_code": "044",
		   "currency": "NGN",
		   "metadata": {
		      "job": "Flesh Eater"
		    }
		 }' "https://api.paystack.co/transferrecipient"



		'''
	return ''





	def check_balance():
				'''
		Check Balance
		curl -X GET -H "Authorization: Bearer SECRET_KEY" "https://api.paystack.co/balance"



		'''
	return ''






	def resend_otp():
				'''

		Resend OTP for Transfer
		curl https://api.paystack.co/transfer/resend_otp \
		-H "Authorization: Bearer SECRET_KEY" \
		-H "Content-Type: application/json" \
		-d '{"transfer_code": "TRF_vsyqdmlzble3uii"}' \
		-X POST



		'''
	return ''






	def list_recipients():
				'''



		List Tranfer Recipients
		curl "https://api.paystack.co/transferrecipient" \
		-H "Authorization: Bearer SECRET_KEY" 
		-X GET

		'''
	return ''





	def disable_otp():
				'''


		Disable  OTP Requirement for Transfer
		curl https://api.paystack.co/transfer/disable_otp \
		-H "Authorization: Bearer SECRET_KEY" \
		-X POST

		'''
	return ''






	def enable_otp():
		
		'''

		Enable OTP requirement for Transfers
		curl https://api.paystack.co/transfer/enable_otp \
		-H "Authorization: Bearer SECRET_KEY" \
		-X POST

		'''
	return ''





	def finalize_disable_otp():
				'''



		Finalize Disabling of OTP requirement for Transfers
		curl https://api.paystack.co/transfer/disable_otp_finalize \
		-H "Authorization: Bearer SECRET_KEY" \
		-H "Content-Type: application/json" \
		-d '{"otp": "928783"}' \
		-X POST

		'''
	return ''