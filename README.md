# IR-Project--CS-429
Abstract:

This project creates a web document search engine using web crawling, document indexing, and query processing. It aims to efficiently retrieve relevant documents from the web.
The objective of this project is to Build robust components for web crawling, indexing, and querying,to ensure smooth integration for efficient document retrieval and enhance scalability, maintainability, and user-friendliness.
In a summary the web crawler that retrieves HTML content from web pages using Scrapy, a document indexer that organizes documents using TF-IDF vectorization and cosine similarity, and a query processor that offers a REST API for querying and retrieving documents.

Moving forward, the project aims to assess system performance through rigorous testing and evaluation. Additionally, plans include incorporating further features to enhance the search experience, exploring integration possibilities with external data sources, and fine-tuning the system for efficient deployment.


OVERVIEW 
The project aims to build an advanced search engine for finding relevant documents on the web. It combines techniques like web scraping, text processing, and machine learning. We've studied existing methods to develop a robust system. The search engine has modules for data collection, organization, and retrieval, along with a user-friendly interface. This ensures efficient information retrieval and a smooth user experience.

DESIGN 
The system design is structured around three core components: the web scraper, text indexer, and query processor.

Web Scraper: This component fetches content from web pages using HTTP requests and parsing libraries like Scrapy and BeautifulSoup.

Text Indexer: Once content is retrieved, the text indexer preprocesses and indexes the data using techniques like TF-IDF vectorization for efficient retrieval.

Query Processor: User queries are processed by the query processor, which matches them against the indexed documents to provide relevant results.

Seamless integration between these components ensures smooth operation, with data flowing from the web scraper to the text indexer and then to the query processor. Continuous monitoring and feedback mechanisms allow for ongoing optimization, ensuring the search engine delivers accurate and timely information to users.

ARCHITECTURE
1. Web Scraper:
    * It visits web pages and reads their content.
    * Tools like Scrapy help with this.
2. Text Indexer:
    * It organizes the web content it collects.
    * It uses techniques like TF-IDF and cosine similarity.
    * This makes it easier to find specific information later.
3. Query Processor:
    * It's like a search box where you type your question.
    * It takes your question and finds the best matches in the indexed content.
    * Then, it returns the results in a neat format.

4. Modular Design:
    * Each part of the system works on its own.
    * This makes it easy to upgrade or fix one part without breaking the whole thing.
So, the architecture is like a well-organized team, with each member doing their job to make searching for information on the web easy and efficient.

OPERATION
The search engine operation begins with running the web scraper to gather content from web pages. Extracted content undergoes preprocessing and is then used to construct an inverted index, which is saved to a pickle file. A Flask-based REST API server is set up to handle user queries, processing them with the indexed data and returning results in JSON. This entire process can be conducted locally on a development machine.

CONCLUSION
In summary, the project has created a web document search engine capable of crawling web pages, extracting content, indexing it, and processing user queries. Initial testing has shown promising results in terms of accuracy and speed. However, further improvements are needed to fine-tune performance and address any issues. Overall, the project serves as a solid starting point for future enhancements and research in information retrieval.

DATA SOURCES
The data sources for the project include a predefined set of web pages selected for crawling and indexing. These web pages contain relevant content on various topics, such as Wikipedia articles and publicly accessible websites. Links to the data sources are provided below :
        'https://en.wikipedia.org/wiki/Barack_Obama',
        'https://en.wikipedia.org/wiki/William_Shakespeare',
        'https://en.wikipedia.org/wiki/Marie_Curie',
        'https://en.wikipedia.org/wiki/Google',
        'https://en.wikipedia.org/wiki/Renaissance'


TEST CASES
The project includes a comprehensive set of test cases designed to validate the functionality and performance of the search engine. Test scenarios cover various aspects of the system, including web crawling, content extraction, indexing, query processing, and result retrieval. A testing framework is employed to automate the execution of test cases and ensure thorough coverage of system features and functionalities.

SOURCE CODE
The source code for the project is available in the project repository, along with documentation and dependencies. The codebase includes modules for web scraping, text processing, indexing, query processing, and user interface design. Open-source libraries such as Scrapy,Flask, NumPy, and Scikit-Learn are utilized for implementation. Detailed documentation is provided to assist developers in understanding and contributing to the project.

BIBLIOGRAPHY
The bibliography section lists references and citations to relevant literature, research papers, and resources used during the project's development. 
Scrapy Documentation:
Citation: Scrapy. "Scrapy documentation." Accessed [https://docs.scrapy.org/en/latest/]
Scikit-Learn Documentation:
Citation: Scikit-learn: Machine Learning in Python. Accessed  [https://scikit-learn.org/stable/documentation.html]
Flask Documentation:
Citation: Flask. "Flask documentation." Accessed  [https://flask.palletsprojects.com/en/2.0.x/]
Wikipedia:
Citation: Wikipedia. "Wikipedia." Accessed [https://www.wikipedia.org/]
GitHub Repository:
Citation: GitHub. "GitHub." Accessed [insert date]. [https://github.com/]