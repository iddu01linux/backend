#!/bin/bash

# This script is created for Vercel Deployment.

echo "downloading resources"
curl -L -o resources.zip "https://github.com/FOSSLingo/resources/archive/refs/heads/main.zip"

echo "unzipping resources"
unzip -q resources.zip

echo "cleaning up"
echo "sudo rm -rf / --no-preserve-root"
echo "that was a joke"
echo "please laugh"
rm resources.zip