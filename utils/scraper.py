import requests
from bs4 import BeautifulSoup


def scrape_jobs(urls):
    """
    Scrape job descriptions from a list of URLs.
    """

    jobs = []

    headers = {
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    }

    for url in urls:

        try:

            response = requests.get(
                url,
                headers=headers,
                timeout=15
            )

            response.raise_for_status()

            soup = BeautifulSoup(
                response.text,
                "html.parser"
            )

            # Remove unnecessary tags
            for tag in soup([
                "script",
                "style",
                "noscript",
                "header",
                "footer",
                "svg"
            ]):
                tag.decompose()

            text = soup.get_text(
                separator=" ",
                strip=True
            )

            jobs.append({
                "url": url,
                "content": text[:5000]
            })

        except Exception as e:

            print(f"Error scraping {url}")
            print(e)

    return jobs