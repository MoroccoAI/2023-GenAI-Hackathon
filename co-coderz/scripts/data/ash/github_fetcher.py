# github_fetcher.py

import requests
import yaml

REPO_URL = "https://api.github.com/repos/awesome-selfhosted/awesome-selfhosted-data/contents"

def fetch_yaml_content(folder_name, file_name):
    try:
        raw_url = f"https://raw.githubusercontent.com/awesome-selfhosted/awesome-selfhosted-data/master/{folder_name}/{file_name}"
        response = requests.get(raw_url)
        response.raise_for_status()  # Check for HTTP errors
        yaml_content = response.text
        return yaml_content
    except requests.exceptions.RequestException as e:
        print(f"Error fetching YAML content: {e}")
        return None

def convert_yaml_to_json(yaml_content):
    try:
        json_content = yaml.safe_load(yaml_content)
        return json_content
    except yaml.YAMLError as e:
        print(f"Error converting YAML to JSON: {e}")
        return None
