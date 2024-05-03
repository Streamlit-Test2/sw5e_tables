import nltk
from nltk.corpus import words
nltk.download('words')
import requests
from tqdm import tqdm

def find_words_by_clue(length=None, letters=None):
    # 'letters' should be a dict with {position: char}, positions are 0-based
    word_list = set(words.words())
    filtered_words = [
        word for word in word_list
        if len(word) <= length
    ]
    return filtered_words

base_url = 'https://sw5eapi.azurewebsites.net/api/'


# Example usage
# Find 5-letter words where the third letter is 'a' and the last is 'e'
matches = find_words_by_clue(length=9)
# Loop through each endpoint guess
for _, endpoint in tqdm(enumerate(matches), total=len(matches)):
    url = f"{base_url}{endpoint}"
    #print(url)
    response = requests.get(url)
    if response.status_code == 200:
        print(f"Success: {endpoint}") #feature, feat, monster, archetype, equipment, class, species
    else:
        #print(f"Failed: {url} - Status Code: {response.status_code}")
        pass


