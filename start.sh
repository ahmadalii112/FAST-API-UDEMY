#!/bin/bash

source .venv/Scripts/activate

if [ -z "$1" ]; then
    echo "Usage: ./start.sh <module>"
    echo "Example: ./start.sh 05-FastApi.books"
    exit 1
fi

python -m uvicorn "$1:app" --reload