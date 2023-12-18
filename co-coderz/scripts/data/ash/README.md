# HyprSol ASH (Awesome Self-Hosted)

## Overview

HyprSol ASH is a project that automates the retrieval and management of self-hosted software information from the Awesome Self-Hosted GitHub repository. It fetches YAML files containing details about various self-hosted platforms, software, and tags, converts the content to JSON, and stores it in a MongoDB database. The project is modular, organized into separate files for better clarity and maintainability.

## Project Structure

The project is structured into three main components:

1. **mongodb_manager.py**: Manages MongoDB operations, including connecting to the database and inserting or updating data.

2. **github_fetcher.py**: Fetches YAML content from GitHub using the GitHub API.

3. **update_checker.py**: The main script that checks for updates, converts YAML to JSON, and stores the data in MongoDB.

## Setup

1. Install required Python packages:

   ```bash
   pip install pymongo requests pyyaml
   ```

2. Set up MongoDB: Update the `MONGO_URI` variable in `mongodb_manager.py` with your MongoDB URI.

3. Run the `update_checker.py` script:

   ```bash
   python update_checker.py
   ```

   This script continuously checks for updates, fetches new data from GitHub, and updates the MongoDB database.

## Notes

- The project is designed to be modular and can be extended to handle additional functionalities or categories.

- Make sure to customize the MongoDB connection parameters and update intervals based on your preferences.

- For more information about the Awesome Self-Hosted repository, visit [https://github.com/awesome-selfhosted/awesome-selfhosted](https://github.com/awesome-selfhosted/awesome-selfhosted).

Feel free to explore and adapt the project to suit your specific requirements!