import requests
from bs4 import BeautifulSoup

url = "https://www.tpointtech.com/python-tutorial"  # or any website you want
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# Extract all class attributes from all tags
all_classes = set()
for tag in soup.find_all(True):  # True finds all tags
    classes = tag.get("class")
    if classes:
        for cls in classes:
            all_classes.add(cls)

# Print all unique class names
for cls in sorted(all_classes):
    print(cls)
