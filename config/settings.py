import os
from dotenv import load_dotenv

# Load the variables from the .env file
load_dotenv(dotenv_path="config/.env")

CIC_USERNAME = os.getenv("CIC_USERNAME")
CIC_PASSWORD = os.getenv("CIC_PASSWORD")
CIC_URL = os.getenv("CIC_URL")
