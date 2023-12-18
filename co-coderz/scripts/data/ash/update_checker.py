# update_checker.py

import time
from mongodb_manager import connect_to_mongodb, insert_or_update_data
from github_fetcher import fetch_yaml_content, convert_yaml_to_json

def check_for_updates(client):
    while True:
        try:
            # Iterate through specified categories
            categories = ["software", "platforms", "tags"]
            for category_name in categories:
                # Fetch YAML file names
                api_url = f"{REPO_URL}/{category_name}"
                response = requests.get(api_url)
                response.raise_for_status()  # Check for HTTP errors
                yaml_files = response.json()

                # Iterate through YAML files in the folder
                for yaml_file in yaml_files:
                    file_name = yaml_file["name"]
                    yaml_content = fetch_yaml_content(category_name, file_name)

                    if yaml_content:
                        json_content = convert_yaml_to_json(yaml_content)
                        insert_or_update_data(client, category_name, json_content)

            # Wait for some time before the next iteration (e.g., 24 hours)
            time.sleep(24 * 60 * 60)

        except Exception as e:
            print(f"Error during the update check: {e}")

def main():
    # Connect to MongoDB
    client = connect_to_mongodb()
    if not client:
        return

    try:
        # Start the loop for checking updates
        check_for_updates(client)

    finally:
        # Close the MongoDB connection
        client.close()

if __name__ == "__main__":
    main()
