from PyPDF2 import PdfReader
reader = PdfReader('Saurabh_Resume_final.pdf')
print(len(reader.pages))

page = reader.pages[0]

text = page.extract_text()

print(text)


