from fpdf import FPDF

title ='20,000 Leagues Under the Sea'

class PDF(FPDF):
    def header(self):
        pdf.set_font('helvetica','B',15)

        # calculate the width of title position
        title_w = self.get_string_width(title)+6
        doc_w = self.w
        self.set_x((doc_w-title_w)/2)

        
        self.cell(30,10,'Title',border=True,ln=1,align='C')
        self.ln(20)

    def footer(self):
        self.set_y(-15)
        self.set_font('helvetica','I',10)
        self.cell(0,10,f'Page {self.page_no()}/{{nb}}',align='C')



#create pdf object
pdf = PDF('P','mm','A4')

# auto page break
pdf.set_auto_page_break(auto=True,margin=15)

# get total page numbers
pdf.alias_nb_pages()

# add a page
pdf.add_page()

# specify font 
pdf.set_font('helvetica','',16)

for i in range(1,41):
    pdf.cell(0,10,f'This is line {i}',ln=True)


pdf.output('pdf_1.pdf')