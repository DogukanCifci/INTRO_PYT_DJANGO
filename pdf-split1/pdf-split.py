from PyPDF4 import PdfFileReader, PdfFileWriter

pdf_oku = PdfFileReader('/Users/dogukan/Desktop/CLARUSWAY/Full Stack Developer BEG Brochure ClaruswayDE.pdf')

pdf_yaz = PdfFileWriter()

pages = [0,3]

for p in pages :
    pdf_yaz.addPage(pdf_oku.getPage(p-1))

    with open('/Users/dogukan/Desktop/pdf-split-new-files/new_pdf.pdf', 'wb') as wf :
        pdf_yaz.write(wf)
        print(f'Yeni dosya : {wf.name} olusturuldu')

        #Güzel calisiyor sikinti yok.