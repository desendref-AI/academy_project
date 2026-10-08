from dotenv import load_dotenv
import os
load_dotenv()

maxfiy_data = os.getenv("data")
print(maxfiy_data)