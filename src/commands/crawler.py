import pdfkit
import requests
import tempfile
from bs4 import BeautifulSoup

def get_content(url):
    jar = requests.cookies.RequestsCookieJar()
    jar.set('truyenyyid', 'bpffhnjzukasyt2rgmj7oqvslqspc8d6', domain='truyenyy.pro', path='/')
    response = requests.get(url, cookies=jar)
    soup = BeautifulSoup(response.content, "html.parser")
    contents = soup.find(id='inner_chap_content_1').get_text()
    return contents

def main():
    # Test
    # https://truyenyy.pro/truyen/bat-dau-danh-dau-hoang-co-thanh-the-ban-dich/chuong-1.html
    url = "https://truyenyy.pro/truyen/bat-dau-danh-dau-hoang-co-thanh-the-ban-dich/chuong-1.html"
    contents = get_content(url)
    with tempfile.TemporaryDirectory() as tmpdir:
        file_path = f"{tmpdir}/out.pdf"
        pdfkit.from_string(contents, file_path)


if __name__ == "__main__":
    main()