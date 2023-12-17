#!/bin/bash

# Check if a URL is provided as an argument
if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

url="$1"

# Download the HTML content of the webpage
html=$(curl -s "$url")

# Use grep to extract content within <span style="color: #000000;">
# Adjust the pattern according to the actual structure of the HTML
content=$(echo "$html" | grep -o '<span style="color: #000000;">[^<]*</span>' | sed 's/<span style="color: #000000;">//;s/<\/span>//')

# Print the extracted content
echo "$content"
