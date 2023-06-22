#!/bin/bash

if [ -z "$OPENAI_TOKEN" ]; then
    echo "Environment variable OPENAI_TOKEN is not set. Please set it before proceeding."
    echo "Example: export OPENAI_TOKEN=<your_token>"
    exit 1
fi

# Test secrets
export aws_credentials='{"aws_access_key_id": "test","aws_secret_access_key": "test","aws_region_name": "test"}'

pip install -r ./requirements.txt
python -m spacy download en_core_web_sm

python -m unittest discover
