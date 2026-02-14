from fpdf import FPDF
pdf = FPDF()

pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, text="Hello, Kekeli!", ln=True)
pdf.output("example.pdf")