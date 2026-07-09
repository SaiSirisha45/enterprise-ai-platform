#!/bin/bash

echo "Running Smoke Tests..."

curl http://localhost:8000/

curl http://localhost:8000/docs

curl http://localhost:8000/metrics

echo "Smoke Tests Passed" 