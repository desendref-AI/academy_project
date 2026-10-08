from dotenv import load_dotenv
import os
load_dotenv()

print("malumotlar hafsiz saqlandi")
maxfiy_data = os.getenv("data")
print(maxfiy_data)