#!/usr/bin/env python3.9
import os
from aws_cdk import App
from cdk_python_lambda_dynamodb.cdk_python_lambda_dynamodb_stack import CdkPythonLambdaDynamodbStack

app = App()
CdkPythonLambdaDynamodbStack(app, "CdkPythonLambdaDynamodbStack")
app.synth()