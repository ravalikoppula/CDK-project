
# Serverless Application with AWS CDK

This project demonstrates the deployment of a serverless application using AWS CDK (Cloud Development Kit). It includes essential serverless components such as API Gateway, Lambda functions, DynamoDB, IAM roles, and more. Additionally, it includes a CDK construct and a wrapper that creates a CDK stack.
# Table of Contents
## Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Prerequisites](#prerequisites)
- [Setup and Deployment](#setup-and-deployment)
- [Best Practices](#best-practices)
- [Contributing](#contributing)
- [License](#license)

## Overview

This project aims to showcase proficiency in infrastructure as code and AWS services by deploying a serverless application using AWS CDK.

## Architecture

The application architecture includes the following components:

- **API Gateway**: To expose RESTful endpoints.
- **Lambda Functions**: To handle business logic.
- **DynamoDB**: As the data store.
- **IAM Roles**: For managing permissions.

## Prerequisites

- AWS CLI configured with appropriate permissions.
- Node.js (v14.x or later).
- Python (v3.7 or later).
- AWS CDK Toolkit installed.

## Setup and Deployment

### 1. Clone the Repository
Open your terminal and run the following commands:

```sh
git clone <repository-url>
cd <repository-directory>
```

### 2. Install AWS CDK
Ensure you have the necessary dependencies installed by running:

```sh
#install aws cdk
npm install -g aws-cdk
cdk --version
#Create new CDK project (if you are working on a new project)
mkdir cdk-python-lambda-dynamodb
cd cdk-python-lambda-dynamodb
cdk init app --language python
```
### 3. Create a Python Virtual Environment

The `cdk.json` file tells the CDK Toolkit how to execute your app.

This project is set up like a standard Python project.  The initialization
process also creates a virtualenv within this project, stored under the `.venv`
directory.  To create the virtualenv it assumes that there is a `python3`
(or `python` for Windows) executable in your path with access to the `venv`
package. If for any reason the automatic creation of the virtualenv fails,
you can create the virtualenv manually.


To manually create a virtualenv on MacOS and Linux:

```
$ python3.9 -m venv .venv
```

After the init process completes and the virtualenv is created, you can use the following
step to activate your virtualenv.

```
$ source .venv/bin/activate
```

If you are a Windows platform, you would activate the virtualenv like this:

```
% .venv\Scripts\activate.bat
```

Once the virtualenv is activated, you can install the required dependencies.

```
$ pip3.9 install -r requirements.txt
```

At this point you can now synthesize the CloudFormation template for this code.

```
$ cdk synth
```

To add additional dependencies, for example other CDK libraries, just add
them to your `setup.py` file and rerun the `pip install -r requirements.txt`
command.

## Useful commands

 * `cdk ls`          list all stacks in the app
 * `cdk synth`       emits the synthesized CloudFormation template
 * `cdk deploy`      deploy this stack to your default AWS account/region
 * `cdk diff`        compare deployed stack with current state
 * `cdk docs`        open CDK documentation
### 4. Bootstrap Your AWS Environment
Bootstrap the AWS environment if you haven't already:
```sh
$ cdk bootstrap
```
### 5. Deploy the CDK Stack
Deploy the stack to your AWS account:
```sh
$ cdk deploy
```

## Best Practices
- Use environment variables for configuration.
- Ensure least privilege for IAM roles.
- Use meaningful naming conventions.
- Write unit tests for Lambda functions.


## Contributing
Contributions are welcome! Please fork the repository and submit pull requests for review.

## Licence


