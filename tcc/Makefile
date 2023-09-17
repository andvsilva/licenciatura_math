############################################
# Makefile for thesis
############################################

all:
	mkdir -p figures_tikz
	mkdir -p figures_tikz/figures
	pdflatex -shell-escape thesis
	bibtex thesis
	pdflatex -shell-escape thesis
	pdflatex -shell-escape thesis
	date

clean:
	rm -rf *.gz *.bbl *.bcf *.aux *.log *.blg *.out thesis.pdf *~
	rm -rf figures_tikz

