import main
import os
import shutil
import pandas as pd
from fpdf import FPDF
import fpdf


def create_letterhead(pdf, WIDTH):
    pdf.image("/images/header.png)", 0, 0, WIDTH)


def create_title(title, pdf):
    # Add main title
    pdf.set_font('Helvetica', 'b', 20)
    pdf.ln(40)
    pdf.write(5, title)
    pdf.ln(10)

    # Add date of report
    pdf.set_font('Helvetica', '', 14)
    pdf.set_text_color(r=128, g=128, b=128)
    today = time.strftime("%d/%m/%Y")
    pdf.write(4, f'{today}')

    # Add line break
    pdf.ln(10)


def write_to_pdf(pdf, words):
    # Set text colour, font size, and font type
    pdf.set_text_color(r=0, g=0, b=0)
    pdf.set_font('Helvetica', '', 12)

    pdf.write(5, words)

class PDF(FPDF):

    def footer(self):
        self.set_y(-15)
        self.set_font('Helvetica', 'I', 8)
        self.set_text_color(128)
        self.cell(0, 10, 'Page ' + str(self.page_no()), 0, 0, 'C')

try:
    shutil.rmtree("plot/")
    os.mkdir("plot/")
except FileNotFoundError:
    os.mkdir("plot/")


df = main.read("https://raw.githubusercontent.com/buzzCraft/RobTek-prosjekt/main/StepRespons%2003032022_2.csv")
navn = {
    "SB401": "Ventilåpning til bygg E",
    "RT503": "Retur radiator",
}
df = main.rename(df, navn)
steps_done = [[50, 40], [40, 60], [60, 50]]
single_step = []
list_of_steps = []
for step in steps_done:
    single_step.append(main.step_analytics(main.find_step(df, step), 60, step, 0.3))

i = 1
single_step[i].measured_value = "RT503"
single_step[i].gain = "SB401"
single_step[i].calculate()
single_step[i].plot_detailed(False)
single_step[i].detailed_plot.savefig("plot/test.png", dpi=300, bbox_inches='tight', pad_inches=0)

# Global Variables
TITLE = "Monthly Business Report"
WIDTH = 210
HEIGHT = 297

# Create PDF
pdf = PDF() # A4 (210 by 297 mm)


'''
First Page of PDF
'''
# Add Page
pdf.add_page()

# Add lettterhead and title
create_letterhead(pdf, WIDTH)
create_title(TITLE, pdf)

# Add some words to PDF
write_to_pdf(pdf, "1. The table below illustrates the annual sales of Heicoders Academy:")
pdf.ln(15)

# Add table
pdf.image("plot/test.png", w=170)
pdf.ln(10)

# Add some words to PDF
write_to_pdf(pdf, "2. The visualisations below shows the trend of total sales for Heicoders Academy and the breakdown of revenue for year 2016:")

# Add the generated visualisations to the PDF
pdf.image("plot/test.png", 5, 200, WIDTH/2-10)
pdf.image("plot/test.png", WIDTH/2, 200, WIDTH/2-10)
pdf.ln(10)


'''
Second Page of PDF
'''

# Add Page
pdf.add_page()

# Add lettterhead
create_letterhead(pdf, WIDTH)

# Add some words to PDF
pdf.ln(40)
write_to_pdf(pdf, "3. In conclusion, the year-on-year sales of Heicoders Academy continue to show a healthy upward trend. Majority of the sales could be attributed to the global sales which accounts for 58.0% of sales in 2016.")
pdf.ln(15)

# Generate the PDF
pdf.output("annual_performance_report.pdf", 'F')