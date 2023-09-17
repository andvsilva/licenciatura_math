# Nome do arquivo principal (sem extensão)
FILENAME = report

# Comando para compilar o documento LaTeX
LATEX = pdflatex

all: $(FILENAME).pdf

$(FILENAME).pdf: $(FILENAME).tex
		$(LATEX) $(FILENAME).tex
	$(LATEX) $(FILENAME).tex

clean:
		rm -f $(FILENAME).pdf
	rm -f *.log *.aux *.out

.PHONY: all clean