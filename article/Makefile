# Makefile para compilar um documento LaTeX

# Nome do arquivo LaTeX (sem a extensão .tex)
FILENAME = main

# Comando LaTeX (pode variar de acordo com o sistema)
LATEX = pdflatex

# Comando para limpar os arquivos auxiliares gerados pelo LaTeX
CLEAN = rm -f *.aux *.log *.out *.toc main.pdf

all: $(FILENAME).pdf

$(FILENAME).pdf: $(FILENAME).tex
	$(LATEX) $(FILENAME).tex
	$(LATEX) $(FILENAME).tex
	$(LATEX) $(FILENAME).tex

clean:
	$(CLEAN)

.PHONY: all clean