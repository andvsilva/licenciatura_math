# importing required modules
import PyPDF2
import time
import enchant
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, Dataset
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sympy.matrices import SparseMatrix

from nltk.corpus import stopwords
from nltk.stem import SnowballStemmer
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import torch
import torch.nn as nn
from torch.utils.data import DataLoader, Dataset
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer

import os.path
import sys
import gc
import pandas as pd
import numpy as np

# Crie uma classe personalizada do conjunto de dados PyTorch
class TextDataset(Dataset):
    def __init__(self, data):
        self.data = data

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return torch.tensor(self.data[idx], dtype=torch.float32)

# release memory RAM
def release_memory(df):   
    del df
    gc.collect() 
    df = pd.DataFrame() # point to NULL
    print('memory RAM released.')

# release memory for large arrays (dictionary)
def release_array(dd):
    del dd 
    gc.collect()
    dd = None


start_time = time.time()

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

cleaning_words = []

for word in all_words:
    if(d.check(word)):
        cleaning_words.append(word)

review = ""

istart = 0
iend = 100
ltexts = []

for jlist in cleaning_words:
    review += jlist + " "

    if istart == iend:
        ltexts.append(review)
        istart=0
    else:
        istart += 1

## Convert a collection of text documents to a matrix of token counts.
cv = CountVectorizer()

# feature
X = cv.fit_transform(ltexts).toarray() # array type

# Divida seus dados em treinamento e teste
X_train, X_test = train_test_split(X, test_size=0.2, random_state=42)

# release memory - array
release_array(X)

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

print("Training the model...")
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
representacoes_latentes = model.encoder(torch.tensor(X_test, dtype=torch.float32))

# Reconstrua o texto de exemplo
reconstrucao = model.decoder(representacoes_latentes)

# Calcule a diferença entre a entrada e a reconstrução
diferenca = np.mean(np.abs(X_train - reconstrucao.detach().numpy()))

# Defina um limite de anomalia
limite_anomalia = 0.1  # Ajuste este valor conforme necessário

# Verifique se é uma anomalia
if diferenca > limite_anomalia:
    print("Anomalia detectada!")
else:
    print("Não é uma anomalia.")

print("--- %s seconds ---" % (time.time() - start_time))