import pdfkit
import requests
import tempfile
from bs4 import BeautifulSoup

def get_content(url):
    jar = requests.cookies.RequestsCookieJar()
    jar.set('truyenyyid', 'bpffhnjzukasyt2rgmj7oqvslqspc8d6', domain='truyenyy.pro', path='/')
    response = requests.get(url, cookies=jar)
    soup = BeautifulSoup(response.content, "html.parser")
    contents = str(soup.find(id='inner_chap_content_1'))
    header = str(soup.find(class_='heading-font mt-2'))
    return contents, header

def main():
    # Test
    # https://truyenyy.pro/truyen/bat-dau-danh-dau-hoang-co-thanh-the-ban-dich/chuong-1.html
    with tempfile.TemporaryDirectory() as tmpdir:
        full_contents = "<h1 style='text-align: center'>Bắt Đầu Đánh Dấu Hoang Cổ Thánh Thể. ( Bản dịch. )</h1>"
        file_path = f"chap.pdf"
        # file_path = f"{tmpdir}/Crawler.pdf"
        for i in range(1, 200):
            url = f"https://truyenyy.pro/truyen/bat-dau-danh-dau-hoang-co-thanh-the-ban-dich/chuong-{i}.html"
            try:
                contents, header = get_content(url)
            except:
                print("Error or page not exit")
                continue
            options = {
                'encoding': "UTF-8",
            }
            if contents is not None:
                full_contents += header + contents + "<br>"
        pdfkit.from_string(full_contents, file_path, options=options)
        

if __name__ == "__main__":
    main()