from googleapiclient.discovery import build
import wikipediaapi

# Replace 'YOUR_GOOGLE_API_KEY' with your actual API key
GOOGLE_API_KEY = 'AIzaSyA7E5AGbjL43yiGfuMMsO69Mp6b1RyIrwY'


def search_google(query, num_results=5):
    results = []
    service = build('customsearch', 'v1', developerKey=GOOGLE_API_KEY)
    res = service.cse().list(q=query, cx='YOUR_CUSTOM_SEARCH_ENGINE_ID', num=num_results).execute()
    items = res.get('items', [])
    for item in items:
        results.append(item['link'])
    return results


def search_wikipedia(query):
    wiki_wiki = wikipediaapi.Wikipedia('en')
    page_py = wiki_wiki.page(query)
    return page_py.text[:500]  # Limiting to the first 500 characters for brevity


def main():
    print("Hello! I'm your searching assistant. Ask me anything.")

    while True:
        user_query = input("You: ")

        if user_query.lower() in ['exit', 'quit', 'bye']:
            print("Goodbye!")
            break

        print("\nSearching on Google...")
        google_results = search_google(user_query)
        print("\nGoogle Results:")
        for result in google_results:
            print(result)

        print("\nSearching on Wikipedia...")
        wikipedia_result = search_wikipedia(user_query)
        print("\nWikipedia Result:")
        print(wikipedia_result)


if __name__ == "__main__":
    main()
