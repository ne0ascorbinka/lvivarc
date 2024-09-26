import os
import json
from bs4 import BeautifulSoup

# Path to your project root and HTML files
PROJECT_ROOT = 'pages/'
IMAGES_FOLDER = 'Images/'

# Initialize data structures
data = []
groups = {}

# Function to process each HTML file
def process_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        soup = BeautifulSoup(file, 'html.parser')

        # 1. Extract group details from the navbar
        navbar = soup.find('a', class_='navbar-brand')
        if navbar:
            group_href = navbar['href'].replace('.html', '')  # Extract slug (e.g., 'churchs')
            group_slug = group_href
            group_title = soup.find('strong').text.strip()  # Extract title (e.g., 'Церкви та монастирі')

            # Check if this group is already in the groups dictionary
            if group_slug not in groups:
                # Create and add the group to the list
                group = {
                    "table": "arcgroup",
                    "name": group_slug,
                    "title": group_title,
                    "slug": group_slug
                }
                groups[group_slug] = group  # Add to dictionary to avoid duplicates
                data.append(group)  # Add group to final data list

        # 2. Extract the place details (architecture object)
        title = soup.find('h1').text.strip()

        paragraphs = soup.find_all('p', class_="text-justify")
        article_text = "\n".join([p.text.strip() for p in paragraphs])

        address = soup.find_all('p')[-1].text.split("Сучасна адреса:")[-1].strip()[:-1]

        image_tag = soup.find('img')
        image = image_tag['src'] if image_tag else None

        # Create a new architecture object
        place = {
            "table": "arcobject",
            "title": title,
            "text": article_text,
            "address": address,
            "group": group_slug,  # Link to the group using the slug
            "image": os.path.join(IMAGES_FOLDER, os.path.basename(image)) if image else None
        }

        data.append(place)


def main() -> None:
    # Example processing for a single file  
    # process_html(os.path.join(PROJECT_ROOT, 'Assumption Church.html'))

    for root, dirs, files in os.walk(PROJECT_ROOT):
        for file in files:
            if file.endswith('.html'):
                file_path = os.path.join(root, file)
                process_html(file_path)

    # Save to a JSON file
    with open('output_data.json', 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, ensure_ascii=False, indent=4)

    print("Data extracted and saved to output_data.json")
    

if __name__ == '__main__':
    main()
