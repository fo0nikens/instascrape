from __future__ import annotations

from .insta_scraper import StaticInstaScraper
from .jsontools import ProfileJSON


class Profile(StaticInstaScraper):
    """
    Representation of an Instagram profile page.

    Attribues
    ---------
    url : str
        Full URL to an existing Instagram profile

    Methods
    -------
    static_load(session=requests.Session())
        Makes request to URL, instantiates BeautifulSoup, finds JSON data,
        then parses JSON data.
    """

    def __init__(self, url):
        """
        Parameters
        ----------
        url : str
            Full URL to an existing Instagram profile
        """
        super().__init__(url)

    def _scrape_json(self, json_data: dict):
        self.data = ProfileJSON(json_data)
        self.data.parse_json()

    @classmethod
    def from_username(cls, username: str):
        """
        Factory method for convenience to create Profile instance given
        just a username instead of a full URL.

        Parameters
        ----------
        username : str
            Username of the Profile for scraping

        Returns
        -------
        Profile(url)
            Instance of Profile with URL at the given username

        Example
        -------
        >>>Profile.from_username('gvanrossum')
        <https://www.instagram.com/gvanrossum/: Profile>
        """

        url = f"https://www.instagram.com/{username}/"
        return cls(url)


if __name__ == "__main__":
    url = r"https://www.instagram.com/chris_greening/"
    profile = Profile(url)
    profile.static_load()