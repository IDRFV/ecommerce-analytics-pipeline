import subprocess
import os

# Create data directory if not exists
os.makedirs("data/raw", exist_ok=True)

# Download dataset via Kaggle API
subprocess.run([
    "python", "-m", "kaggle", "datasets", "download",
    "-d", "mkechinov/ecommerce-behavior-data-from-multi-category-store",
    "-p", "data/raw",
    "--unzip"
])

print("Download complete. Files in data/raw:")
print(os.listdir("data/raw"))