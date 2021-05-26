from fpdf import FPDF


#create pdf object
pdf = FPDF('P','mm','A4')
pdf.add_page()

pdf.set_font('helvetica','BU',16)
pdf.set_text_color(200,50,50)

pdf.cell(120,100,'Hello World',ln=True, border=True)


pdf.set_font('helvetica','',16)
pdf.cell(80,10,'good bye World!')

# pdf.set_font('times','',12)
# pdf.cell(80,10,'good bye')
pdf.output('pdf.pdf')