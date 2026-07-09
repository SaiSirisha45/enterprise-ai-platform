#!/bin/bash

echo "Rolling Back..."

kubectl rollout undo deployment/enterprise-ai-backend

echo "Rollback Completed" 