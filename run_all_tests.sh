#!/bin/bash

if [ -z "$OPENAI_TOKEN" ]; then
    echo "Environment variable OPENAI_TOKEN is not set. Please set it before proceeding."
    echo "Example: export OPENAI_TOKEN=<your_token>"
    exit 1
fi

pip install -r ./requirements.txt
python -m spacy download en_core_web_sm

python -m unittest discover
