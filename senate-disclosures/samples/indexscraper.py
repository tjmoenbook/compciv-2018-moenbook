from pathlib import Path
from bs4 import BeautifulSoup

html_filepath = Path('samples', 'ca-senate-disclosures-index.html')
html = html_filepath.read_text()
