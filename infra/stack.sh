#!/usr/bin/env bash

# Usage:
# ./stack.sh create server
# ./stack.sh update server

AWS_PROFILE="gofore-crew"
STACK_NAME="sc2-spectator"
COMMAND=$1
TEMPLATE=$2

if [[ $COMMAND == "create" ]]; then
  echo "Creating stack"
  aws cloudformation create-stack --stack-name $STACK_NAME --template-body file://$TEMPLATE.yml --profile $AWS_PROFILE
elif [[ $COMMAND == "update" ]]; then
  echo "Updating stack"
  aws cloudformation update-stack --stack-name $STACK_NAME --template-body file://$TEMPLATE.yml --profile $AWS_PROFILE
fi
