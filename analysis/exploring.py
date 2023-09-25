
# importing required modules
import PyPDF2
import time
import enchant
d = enchant.Dict("en_US")

start_time = time.time()

# Abra o arquivo PDF
with open('dataset/books/humanaction_body.pdf', 'rb') as pdf_file:
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)

    # Inicialize uma lista para armazenar todas as words
    all_words = []

    # Itere pelas páginas do PDF
    for page_number in range(pdf_reader.getNumPages()):
        print("Página %s de %s..." %(page_number, pdf_reader.numPages))

        page = pdf_reader.getPage(page_number)
        
        # Extraia o text da página
        text = page.extractText()
        
        # Divida o text em words usando espaços e outras pontuações como delimitadores
        words = text.split()
        
        # Adicione as words à lista
        all_words.extend(words)

new_words = []

for word in all_words:
    if(d.check(word)):
        print(f"Word found {word}")
        new_words.append(word)
    
print(len(new_words))
print(len(all_words))

# Agora, todas as words estão na lista "all_words"
print(new_words)

print("--- %s seconds ---" % (time.time() - start_time))