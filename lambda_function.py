import json

def lambda_handler(event, context):
	postdata = event['body']
	usercredentials = json.loads(postdata)
	username = usercredentials['username']
	password = usercredentials['password']
	if username == 'admin' and password == '123456':
		print("success")
		return {
	        'statusCode': 200,
	        'body': json.dumps('success')
    	}
	else:
		print("invalid")
		return {
	        'statusCode': 200,
	        'body': json.dumps('invalid user credentials')
    	}