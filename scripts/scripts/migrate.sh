#!/bin/bash

echo "Running Database Migration..."

alembic upgrade head

echo "Migration Completed" 