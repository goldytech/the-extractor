#!/usr/bin/env bash
echo "Debug starting..."
serverless invoke local --function $1 --path data.json