from django.http import HttpResponse
from django.shortcuts import render


def aboutus (request):
    return HttpResponse("hello world")

def Homepage (request):
    import requests

    def search_with_keyword(keyword):
        # Define the API endpoint
        endpoint = "https://www.googleapis.com/customsearch/v1"

        # Define the API key and the search engine ID
        api_key = "AIzaSyCZ13asugXqVmK5_Sz7WUDgEoqyZpd8nkM"
        cx = "12b0a58e323bc402c"

        # Define the parameters for the API request
        params = {
            "key": api_key,
            "cx": cx,
            "q": keyword
        }

        # Make the API request
        response = requests.get(endpoint, params=params)

        # Check the response status code
        if response.status_code != 200:
            raise Exception("Failed to search with keyword")

        # Extract the list of websites from the API response
        websites = []
        for item in response.json().get("items", []):
            websites.append(item["link"])

        return websites

    # Define a list of keywords
    keywords = [
        "html"

    ]

    # Create a list of websites for each keyword
    websites_by_keyword = {}
    web=[]
    for keyword in keywords:
        websites = search_with_keyword(keyword)
        websites_by_keyword[keyword] = websites

    # Print the list of websites for each keyword
    for keyword, websites in websites_by_keyword.items():
        print("Websites related to '%s':" % keyword)
        # for website in websites:
        web.append(websites)
        # print(websites)
        # print(type(websites))
   



    return render(request,"index.html",websites)
