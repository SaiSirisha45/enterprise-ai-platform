#!/bin/bash

echo "Creating Backup..."

mkdir -p backups

TIMESTAMP=$(date +"%Y%m%d_%H%M%S")

cp enterprise_ai.db backups/database_$TIMESTAMP.db

echo "Backup Completed" 