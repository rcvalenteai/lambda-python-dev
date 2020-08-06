import json

print('loading function')


def lambda_handler(event, context):
    """
    echos the transaction fields with a new static message attached
    :param event:
    :param context:
    :return: http response object
    """
    # 1. Parse out query string params
    transaction_id = event['queryStringParameters']['transaction_id']
    transaction_type = event['queryStringParameters']['type']
    transaction_amount = event['queryStringParameters']['amount']

    print('transaction_id=' + transaction_id)
    print('transaction_type=' + transaction_type)
    print('transaction_amount=' + transaction_amount)

    # 2. Construct the body of the response object
    transaction_response = dict()
    transaction_response['transaction_id'] = transaction_id
    transaction_response['type'] = transaction_type
    transaction_response['amount'] = transaction_amount
    transaction_response['message'] = "Hello from Lambda"

    # 3. Construct http response object
    response_object = dict()
    response_object['statusCode'] = 200
    response_object['headers'] = dict()
    response_object['headers']['Content-Type'] = 'application/json'
    response_object['body'] = json.dumps(transaction_response)

    # 4. Return the response object
    return response_object


