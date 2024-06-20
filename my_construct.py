from aws_cdk import (
    aws_lambda as _lambda,
    aws_dynamodb as dynamodb,
    aws_iam as iam,
    aws_apigateway as apigateway,
    Stack
)
from constructs import Construct
class MyLambdaDynamoDBConstruct(Construct):

    def __init__(self, scope: Construct, id: str, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)

        table = dynamodb.Table(
            self, "RavaliTestTable",
            partition_key={"name": "id", "type": dynamodb.AttributeType.STRING},
            table_name="ravali-test"
        )

        lambda_function = _lambda.Function(
            self, "MyLambdaFunction",
            runtime=_lambda.Runtime.PYTHON_3_8,
            handler="lambda_handler.handler",
            code=_lambda.Code.from_asset("lambda")
        )

        table.grant_read_write_data(lambda_function)

        lambda_role = iam.Role(
            self, "LambdaExecutionRole",
            assumed_by=iam.ServicePrincipal("lambda.amazonaws.com"),
            managed_policies=[
                iam.ManagedPolicy.from_aws_managed_policy_name("service-role/AWSLambdaBasicExecutionRole")
            ]
        )

        lambda_function.add_to_role_policy(
            iam.PolicyStatement(
                actions=["dynamodb:*"],
                resources=[table.table_arn]
            )
        )

        api = apigateway.LambdaRestApi(
            self, "MyApiGateway",
            handler=lambda_function,
            proxy=False
        )

        items = api.root.add_resource("items")
        items.add_method("POST") 