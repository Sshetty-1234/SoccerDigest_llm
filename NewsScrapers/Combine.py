import re
from fpdf import FPDF
from apn_news_scraper import article_content as adp_info
from goal_com_scraper import article_content as goal_info
from transfermarket_scraper import article_content as transfermarket_info

pdf = FPDF()


pdf.add_page()

pdf.set_font("Arial", size=12)

adp_info = adp_info.strip()
adp_info = re.sub(r'\s+', ' ', adp_info)
adp_info = adp_info.encode('latin1', 'replace').decode('latin1')


text = goal_info + transfermarket_info + adp_info

pdf.multi_cell(0, 10, text)

pdf_output = "data/news_information.pdf"
pdf.output(pdf_output)
