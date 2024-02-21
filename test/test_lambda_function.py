from src.lambda_function import lambda_handler
from src.extra_utils import get_lambda_message
import json


def test_lambda_function():
    assert {
               'statusCode': 200,
               'body': json.dumps(get_lambda_message())
           } == lambda_handler({}, {})
