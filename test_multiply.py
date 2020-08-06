import unittest
import json

from multiply import lambda_handler, MissingError


class TransactionTest(unittest.TestCase):
    def test_transaction(self):
        # Test properly parses input and creates response object
        event = dict()
        context = dict()
        event.setdefault('queryStringParameters', dict())
        event['queryStringParameters']['transaction_id'] = 1
        event['queryStringParameters']['type'] = "PURCHASE"
        event['queryStringParameters']['amount'] = 500

        response_object = dict()
        response_object['statusCode'] = 200
        response_object['headers'] = dict()
        response_object['headers']['Content-Type'] = 'application/json'
        response_object['body'] = json.dumps({'transaction_id': 1,
                                              "type": "PURCHASE",
                                              "amount": 500,
                                              "message": "Hello from Lambda"})

        self.assertEqual(lambda_handler(event, context), response_object)

    def test_missing(self):
        # Test properly parses input and creates response object
        event = dict()
        context = dict()
        event.setdefault('queryStringParameters', dict())
        event['queryStringParameters']['transaction_id'] = 1
        # event['queryStringParameters']['type'] = "PURCHASE"
        event['queryStringParameters']['amount'] = 500

        response_object = dict()
        response_object['statusCode'] = 200
        response_object['headers'] = dict()
        response_object['headers']['Content-Type'] = 'application/json'
        response_object['body'] = json.dumps({'transaction_id': 1,
                                              "type": "PURCHASE",
                                              "amount": 500,
                                              "message": "Hello from Lambda"})

        with self.assertRaises(MissingError):
            lambda_handler(event, context)


if __name__ == '__main__':
    unittest.main()
