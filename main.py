import requests
from bs4 import BeautifulSoup
import json

# Step 1: Fetch HTML content from URL
url = 'https://sunnah.com/hisn'  # Replace with actual URL
response = requests.get(url)
html_content = response.content

# Step 2: Parse HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')
sorted_hadiths = {}

# Step 3: Extract chapters and Hadiths
chapters = soup.find_all('div', class_='chapter')
for chapter in chapters:
    chapter_number = chapter.find('div', class_='echapno').text.strip()
    chapter_title = chapter.find('div', class_='englishchapter').text.strip()
    arabic_chapter = chapter.find('div', class_='arabicchapter').text.strip()

    if chapter_number not in sorted_hadiths:
        sorted_hadiths[chapter_number] = {
            'chapter_title': chapter_title,
            'arabic_chapter': arabic_chapter,
            'hadiths': []
        }

    hadith_containers = chapter.find_next_siblings('div', class_='actualHadithContainer')
    for hadith in hadith_containers:
        english_hadith = hadith.find('div', class_='english_hadith_full')
        arabic_hadith = hadith.find('div', class_='arabic_hadith_full arabic')
        transliteration = hadith.find('span', class_='transliteration')
        reference = hadith.find('span', class_='hisn_english_reference')

        # Safely extract text if element exists
        english_text = english_hadith.find('span', class_='translation').text.strip() if english_hadith and english_hadith.find('span', class_='translation') else None
        arabic_text = arabic_hadith.find('span', class_='arabic_text_details arabic').text.strip() if arabic_hadith and arabic_hadith.find('span', class_='arabic_text_details arabic') else None
        transliteration_text = transliteration.text.strip() if transliteration else None
        reference_text = reference.text.strip() if reference else None

        if english_text and arabic_text and transliteration_text and reference_text:
            sorted_hadiths[chapter_number]['hadiths'].append({
                'arabic_hadith': arabic_text,
                'english_hadith': english_text,
                'transliteration': transliteration_text,
                'reference': reference_text
            })

# Step 4: Save sorted Hadiths to JSON
with open('hisn_ul_muslim.json', 'w', encoding='utf-8') as f:
    json.dump(sorted_hadiths, f, ensure_ascii=False, indent=4)

print("Hadiths sorted by chapter with transliteration saved to sorted_hadiths_by_chapter_with_transliteration.json")



















# from bs4 import BeautifulSoup
# import json
# import requests

# # Fetch HTML content from the URL
# url = "https://sunnah.com/hisn"
# response = requests.get(url)
# html_content = response.content

# soup = BeautifulSoup(html_content, 'html.parser')
# duas = {}

# # Extract chapter data
# chapter_data = []
# chapter_containers = soup.find_all('div', class_='chapter')
# for chapter in chapter_containers:
#     chapter_number = chapter.find('div', class_='echapno').text.strip()
#     english_chapter_title = chapter.find('div', class_='englishchapter').text.strip()
#     arabic_chapter_title = chapter.find('div', class_='arabicchapter arabic').text.strip()

#     chapter_data.append({
#         'chapter_number': chapter_number,
#         'english_title': english_chapter_title,
#         'arabic_title': arabic_chapter_title
#     })

# # Extract hadith data
# hadiths = []
# hadith_containers = soup.find_all('div', class_='actualHadithContainer')

# for hadith in hadith_containers:
#     english_hadith = hadith.find('div', class_='english_hadith_full')
#     arabic_hadith = hadith.find('div', class_='arabic_hadith_full')
#     reference = hadith.find('span', class_='hisn_english_reference')
#     transliteration = english_hadith.find('span', class_='transliteration') if english_hadith else None

#     if english_hadith:
#         english_text = english_hadith.find('span', class_='translation').text.strip()

#         # Check if arabic_hadith is found and then extract the text
#         if arabic_hadith:
#             arabic_text = arabic_hadith.find('span', class_='arabic_text_details arabic').text.strip() if arabic_hadith.find('span', class_='arabic_text_details arabic') else "No Arabic text available"
#         else:
#             arabic_text = "No Arabic text available"

#         transliteration_text = transliteration.text.strip() if transliteration else "No transliteration available"
#         reference_text = reference.text.strip() if reference else "No reference available"

#         hadiths.append({
#             'transliteration': transliteration_text,
#             'arabic': arabic_text,
#             'english': english_text,
#             'reference': reference_text
#         })

# # Wrap the extracted chapters and hadiths into a dictionary =>>>>> 'duas'
# duas['chapters'] = chapter_data
# duas['hadiths'] = hadiths

# # Save to JSON file
# with open('duas.json', 'w', encoding='utf-8') as f:
#     json.dump(duas, f, ensure_ascii=False, indent=4)

# print("Chapters and Duas extracted and saved to duas.json")






# import requests
# from bs4 import BeautifulSoup
# import json

# url = 'https://sunnah.com/hisn'  # Replace with actual URL
# response = requests.get(url)
# soup = BeautifulSoup(response.content, 'html.parser')

# # all chapter links
# chapters = soup.find_all('div', class_='chapter_link title')

# # Extraction of  relevant data
# data = []
# for chapter in chapters:
#     chapter_number = chapter.find('div', class_='chapter_number').text.strip()
#     english_chapter_name = chapter.find('div', class_='english_chapter_name').text.strip()
#     arabic_chapter_name = chapter.find('div', class_='arabic_chapter_name').text.strip()

#     data.append({
#         'chapter_number': chapter_number,
#         'english_name': english_chapter_name,
#         'arabic_name': arabic_chapter_name
#     })

# # Save to JSON file
# with open('chapters.json', 'w', encoding='utf-8') as f:
#     json.dump(data, f, ensure_ascii=False, indent=4)

# print("Data saved to chapters.json")




# from bs4 import BeautifulSoup
# import json
# import requests

# url = 'https://sunnah.com/hisn'  # URL of the webpage to scrape
# response = requests.get(url)
# html_content = response.content

# soup = BeautifulSoup(html_content, 'html.parser')
# hadiths = []

# # Find all hadith containers
# hadith_containers = soup.find_all('div', class_='actualHadithContainer')

# for hadith in hadith_containers:
#     english_hadith = hadith.find('div', class_='english_hadith_full')
#     arabic_hadith = hadith.find('div', class_='arabic_hadith_full')
#     reference = hadith.find('span', class_='hisn_english_reference')
#     transliteration = english_hadith.find('span', class_='transliteration') if english_hadith else None

#     # null safety 
#     try:
#         english_text = english_hadith.find('span', class_='translation').text.strip() if english_hadith else "No English text available"
#         arabic_text = arabic_hadith.find('span', class_='arabic_text_details').text.strip() if arabic_hadith else "No Arabic text available"
#         transliteration_text = transliteration.text.strip() if transliteration else "No transliteration available"
#         reference_text = reference.text.strip() if reference else "No reference available"

#         hadiths.append({
#             'transliteration': transliteration_text,
#             'arabic': arabic_text,
#             'english': english_text,
#             'reference': reference_text
#         })
#     except AttributeError as e:
#         print(f"Error extracting hadith: {e}")

# # Save to JSON file
# with open('hadiths.json', 'w', encoding='utf-8') as f:
#     json.dump(hadiths, f, ensure_ascii=False, indent=4)

# print("Hadiths extracted and saved to hadiths.json")
