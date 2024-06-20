from aws_cdk import Stack
from constructs import Construct
from my_construct import MyLambdaDynamoDBConstruct

class CdkPythonLambdaDynamodbStack(Stack):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        # Use the construct
        MyLambdaDynamoDBConstruct(self, "MyLambdaDynamoDBConstruct")