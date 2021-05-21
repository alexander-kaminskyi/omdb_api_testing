from rest.OmdbBase import OmdbBase
import requests
"""
sdsdsdd
"""

class OmdbClient(OmdbBase):

    def search(self, title):
        """
        Method returns a list of all results that matched that search string.
        """

        result_search = []
        page = 1
        movies_on_page = True
        while movies_on_page:
            """Get movie data from specific page"""
            self.log.warning(f"\nGetting response for title {title} on {page} page")
            result = requests.get(self.url + f'&{"s=" + title}' + f'&page={page}').json()
            self.log.warning(f"{result}\n")
            """Verify there are movies data on the page by key 'Search'"""
            if "Search" in result:
                for item in range(len(result["Search"]) - 1):
                    """Append movie data from all pages to new list"""
                    result_search.append(result["Search"][item])
                page += 1
            else:
                movies_on_page = False
        return result_search

    def get_by_id(self, imdb):
        """
        Method returns the result based on the input id.
        """
        self.log.warning(f"\nGetting response for ID {imdb} = ")
        response = requests.get(self.url + f"&i={imdb}")  # Sends a GET request
        self.log.warning(f"{response.json()}\n")
        return response.json()

    def get_by_title(self, title):
        """
        Method returns the result based on input string as title name.
        """

        self.log.warning(f"\nGetting response for title {title} = ")
        response = requests.get(self.url + f"&t={title}")
        self.log.warning(f"{response.json()}\n")
        return response.json()
