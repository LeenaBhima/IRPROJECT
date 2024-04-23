import scrapy
import os

class WebDocumentSpider(scrapy.Spider):
    name = 'webdocuments'

    start_urls = [
        'https://en.wikipedia.org/wiki/Barack_Obama',
        'https://en.wikipedia.org/wiki/William_Shakespeare',
        'https://en.wikipedia.org/wiki/Marie_Curie',
        'https://en.wikipedia.org/wiki/Google',
        'https://en.wikipedia.org/wiki/Renaissance'
    ]

    def start_requests(self):
        for url in self.start_urls:
            yield scrapy.Request(url=url, callback=self.parse)

    def parse(self, response):
        # Extracting the content of the web page
        content = response.body

        # Get the page title
        page_title = response.css('title::text').get()

        if page_title:
            # Create the output folder if it doesn't exist
            output_folder = 'output'
            os.makedirs(output_folder, exist_ok=True)

            # Save the content to a file with the page title as the filename
            filename = f'{output_folder}/{page_title}.html'
            with open(filename, 'wb') as f:
                f.write(content)
            self.log(f'Saved file {filename}')
