import pdfkit
import requests
import tempfile
from bs4 import BeautifulSoup
from pypdf import PdfMerger

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
    with tempfile.TemporaryDirectory() as tmpdir:
        merger = PdfMerger()
        for i in range(1, 50):
            url = f"https://truyenyy.pro/truyen/bat-dau-danh-dau-hoang-co-thanh-the-ban-dich/chuong-{i}.html"
            contents = get_content(url)
            file_path = f"{tmpdir}/chap_{i}.pdf"
            # TODO: Error format
            pdfkit.from_string(contents, file_path)
            merger.append(file_path)
        merger.write("result.pdf")
        merger.close()
        


if __name__ == "__main__":
    main()