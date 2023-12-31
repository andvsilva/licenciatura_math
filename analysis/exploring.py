
# importing required modules
import PyPDF2
import time
import enchant
import nltk
from nltk.tokenize import word_tokenize
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, Dataset
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
import pandas as pd
nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('all')
from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer

# get dictionary US
d = enchant.Dict("en_US")

# create preprocess_text function
def preprocess_text(text):
    # Tokenize the text
    tokens = word_tokenize(text.lower())

    # Remove stop words
    filtered_tokens = [token for token in tokens if token not in stopwords.words('english')]

    # Lemmatize the tokens
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(token) for token in filtered_tokens]


    # Join the tokens back into a string
    processed_text = ' '.join(lemmatized_tokens)
    return processed_text

# Carregue e pré-processe seus dados de texto
# (você pode usar as etapas de pré-processamento mencionadas anteriormente)

# Vetorize seus dados usando TF-IDF
vectorizer = TfidfVectorizer()

nltk.download('all')

# get dictionary US
d = enchant.Dict("en_US")

start_time = time.time()

analyzer = SentimentIntensityAnalyzer()

# Crie uma classe personalizada do conjunto de dados PyTorch
class TextDataset(Dataset):
    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return torch.tensor(self.data[idx].toarray(), dtype=torch.float32)

# Abra o arquivo PDF
with open('dataset/books/humanaction_bodytest.pdf', 'rb') as pdf_file:
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
        #print(f"Word found {word}")
        new_words.append(word)

istart = 0
iend = 100
review = ""
index = []

for jlist in new_words:
    review += jlist + " "
    index.append(istart)

    if istart == iend:
        #scores = analyzer.polarity_scores(review)
        #print(f'>>> {scores}')
        istart = 0
        break
    istart += 1

tfidfv = TfidfVectorizer().fit(review)
tfidfv.transform(review).toarray()

print(tfidfv.transform(review).toarray())
print(tfidfv.vocabulary_)
X = vectorizer.fit_transform()

# Divida seus dados em treinamento e teste
X_train, X_test = train_test_split(X, test_size=0.2, random_state=42)

# Crie conjuntos de dados e carregadores de dados
train_dataset = TextDataset(X_train)
train_loader = DataLoader(train_dataset, batch_size=64, shuffle=True)

# Defina a arquitetura do autoencoder de linguagem
class Autoencoder(nn.Module):
    def __init__(self, input_size, hidden_size):
        super(Autoencoder, self).__init__()
        self.encoder = nn.Linear(input_size, hidden_size)
        self.decoder = nn.Linear(hidden_size, input_size)

    def forward(self, x):
        x = self.encoder(x)
        x = self.decoder(x)
        return x
    
# Crie o modelo e defina hiperparâmetros
input_size = X_train.shape[1]
hidden_size = 256
model = Autoencoder(input_size, hidden_size)
criterion = nn.MSELoss()
optimizer = torch.optim.Adam(model.parameters(), lr=0.001)

# Treine o autoencoder
num_epochs = 10
for epoch in range(num_epochs):
    for batch in train_loader:
        optimizer.zero_grad()
        outputs = model(batch)
        loss = criterion(outputs, batch)
        loss.backward()
        optimizer.step()
    print(f'Época [{epoch + 1}/{num_epochs}], Perda: {loss.item():.4f}')

# Use as saídas do encoder como representações latentes
representacoes_latentes = model.encoder(torch.tensor(X_test.toarray(), dtype=torch.float32))

#istart = 0
#iend = 100
#review = ""
#
for jlist in new_words:
    review += jlist + " "
    if istart == iend:
        scores = analyzer.polarity_scores(review)
        print(f'>>> {scores}')
        istart = 0
    istart += 1


#print(len(new_words))
#print(len(all_words))
#
## Agora, todas as words estão na lista "all_words"
#print(new_words)

print("--- %s seconds ---" % (time.time() - start_time))