import pdfkit

if __name__ == "__main__":
    # Test
    body = """
        <html>
          <head>
            <meta name="pdfkit-page-size" content="Legal"/>
            <meta name="pdfkit-orientation" content="Landscape"/>
          </head>
          Hello World!
          </html>
        """
    config = pdfkit.configuration(wkhtmltopdf='/bin/wkhtmltopdf')
    pdfkit.from_string(body, 'out.pdf', configuration=config)