%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% Este é um modelo Latex para monografias de  Mestrado e Teses de doutorado de Demografia do Instituto de Filosofia e Ciências Humanas da Universidade 
% Estadual de Campinas (UNICAMP).
%
% Este Modelo foi adaptado do Modelo criado pelo autor André Leon Sampaio Gradvohl (gradvohl@ft.unicamp.br), Dr. para a FT da UNICAMP

% Autor: Jose H C Monteiro da Silva
% Email: j117439@dac.unicamp.br
%  
% Última versão: 06/Março/2019
%
% Primeira versão (06/Março/2019): adaptação do modelo inicial desenvolvido pelo André para a FT de modo a adequá-lo às normas do IFCH.


\NeedsTeXFormat{LaTeX2e}
\ProvidesClass{tese-IFCH}[]
\typeout{tese-IFCH}

\def\thesislanguage#1{\gdef\@thesislanguage{#1}}
\DeclareOption{Ingles}{
  \thesislanguage{0}
  \typeout{tese-IFCH: ingles.}
}
\DeclareOption{Espanhol}{
  \thesislanguage{1}
  \typeout{tese-IFCH: espanhol.}
}
\DeclareOption{Portugues}{
  \thesislanguage{2}
  \typeout{tese-IFCH: portugues.}
}
\newif\iffinalversion
\DeclareOption{Final}{
  \finalversiontrue
  \typeout{tese-IFCH: versao final.}
}

\ProcessOptions\relax

% Classe base: Relatório
\LoadClass[12pt,a4paper]{report}
%
%Pacotes padrão para as línguas usadas no texto.
\RequirePackage[english,spanish,brazil,portuguese]{babel}
%Pacotes para determinar o tipo de fonte usada para imprimir o texto
\RequirePackage{lmodern}
\RequirePackage[T1]{fontenc}
%Pacotes para determinar o tipo de fonte usada para escrever o texto
\RequirePackage[utf8]{inputenc}
%Pacotes para facilitar a inclusão das figuras
\RequirePackage{graphicx}
\graphicspath{{./logotipos/}{./figuras/}}
\PassOptionsToPackage{table}{xcolor}
%Pacotes para incluir os hiperlinks no texto
\RequirePackage{hyperref}
%Mantenha o pacote a seguir para incluir a lista de símbolos.
\usepackage{nomencl} \makenomenclature
\RequirePackage{pdfpages}
\RequirePackage{xspace}
\RequirePackage{setspace}
\RequirePackage{geometry}
\geometry{a4paper,top=30mm,bottom=20mm,left=30mm,right=20mm}
\RequirePackage{csquotes}
% numeracao da pagina no canto superior esquerdo
\RequirePackage{fancyhdr}
% identar primeiro paragrafo de cada secao 
%\RequirePackage{indentfirst}

% legenda das figuras e tabelas em tamanho 10
\RequirePackage[font=footnotesize,labelfont=bf]{caption}
%\RequirePackage[hyphenbreaks]{breakurl}

%Pacotes para adicionar a bibliografia
%\RequirePackage[style=abnt-numeric,
%                language=english,
%                usedashes,
%                giveninits,
%                backend=biber,
%                uniquename=false]{biblatex}

% Definição de novos comandos
\newcommand{\@IFCH}{\small \textnormal{Licenciatura em Matem\'atica}}
\newcommand{\@UNICAMP}{GRUPO EDUCACIONAL IBRA}

% Criação de variáveis para o texto.
\let\@titulo\relax
\def\titulo#1{\gdef\@titulo{#1}}

\let\@autor\relax
\def\autor#1{\gdef\@autor{#1}}
\author{\@autor}

\let\@autora\relax
\def\autora#1{\gdef\@autora{#1}}

\def\grau#1{\gdef\@grau{#1}}

\newif\ifmaster

%\let\@tipotexto\relax
%\def\tipotexto#1{\def\@tipotexto{#1}}
%%%%

\gdef\qualificacaoMestrado{
%added 
  \gdef\@textoaviso{\clearpage}
  \if\@autora\relax
  \gdef\@degnamept{Mestre em Demografia}
  \gdef\@degnamees{Maestro en Demografía}
  \gdef\@artigo{o}
  \else
  \gdef\@degnamept{Mestra em Demografia}
  \gdef\@degnamees{Maestra en Demografía}
  \gdef\@artigo{a}
  \fi
  \gdef\@degnameen{Master of Science}
  \gdef\@monopt{Monografia de qualificação}
  \gdef\@monoes{Monografía de calificación}
  \gdef\@monoen{Qualification monograph}
}
%%%%
\gdef\qualificacaoDoutorado{
%added 
  \gdef\@textoaviso{\clearpage}
  \if\@autora\relax
  \gdef\@degnamept{Doutor em Ciências}
  \gdef\@degnamees{Doctor en Demografía}
  \gdef\@artigo{o}
  \else
  \gdef\@degnamept{Doutora em Ciências}
  \gdef\@degnamees{Doctora en Demografía}
  \gdef\@artigo{a}
  \fi
  \gdef\@degnameen{Doctor in Science}
  \gdef\@monopt{Monografia }
  \gdef\@monoes{Monografía de calificación}
  \gdef\@monoen{Qualification monograph}
}
\gdef\mestrado{
%added 
  \gdef\@textoaviso{\clearpage \cathpage}
  \if\@autora\relax
  \gdef\@degnamept{Mestre em Ciências}
  \gdef\@degnamees{Maestro en Demografía}
  \gdef\@artigo{o}
  \else
  \gdef\@degnamept{Mestra em Ciências}
  \gdef\@degnamees{Maestra en Demografía}
  \gdef\@artigo{a}
  \fi
  \gdef\@degnameen{Master of Science}
  \gdef\@monopt{Dissertação de Mestrado}
  \gdef\@monoes{Dissertacíon}
  \gdef\@monoen{Master Thesis}
}
%%%%
\gdef\doutorado{
%added 
  \gdef\@textoaviso{\clearpage \cathpage}
  \if\@autora\relax
  \gdef\@degnamept{Doutor em Ciências}
  \gdef\@degnamees{Doctor en Demografía}
  \gdef\@artigo{o}
  \else
  \gdef\@degnamept{Doutora em Ciências}
  \gdef\@degnamees{Doctora en Demografía}
  \gdef\@artigo{a}
  \fi
  \gdef\@degnameen{Doctor of Science}
  \gdef\@monopt{Tese}
  \gdef\@monoes{Tesis}
  \gdef\@monoen{Thesis}
}

\let\@orientador\relax
\def\orientador#1{\gdef\@orientador{#1}}

\let\@orientadora\relax
\def\orientadora#1{\gdef\@orientadora{#1}}

\gdef\@advisors{1}
\let\@coorientador\relax
\def\coorientador#1{\gdef\@coorientador{#1}\gdef\@advisors{2}}

\let\@coorientadora\relax
\def\coorientadora#1{\gdef\@coorientadora{#1}\gdef\@advisors{2}}

\def\datadadefesa#1#2#3{
  \gdef\@dia{#1}
  \gdef\@mes{#2}
  \gdef\@ano{#3}
}

\let\@fichacatalografica\relax
\def\fichacatalografica#1{\gdef\@fichacatalografica{#1}}

\let\@avalA\relax
\let\@avalB\relax
\let\@avalC\relax
\let\@avalD\relax
\let\@avalE\relax
\let\@avalF\relax
\let\@avalG\relax
\let\@avalH\relax
\let\@instavalA\relax
\let\@instavalB\relax
\let\@instavalC\relax
\let\@instavalD\relax
\let\@instavalE\relax
\let\@instavalF\relax
\let\@instavalG\relax
\let\@instavalH\relax

\def\avaliadorA#1#2{\gdef\@avalA{#1}\gdef\@instavalA{#2}}
\def\avaliadorB#1#2{\gdef\@avalB{#1}\gdef\@instavalB{#2}}
\def\avaliadorC#1#2{\gdef\@avalC{#1}\gdef\@instavalC{#2}}
\def\avaliadorD#1#2{\gdef\@avalD{#1}\gdef\@instavalD{#2}}
\def\avaliadorE#1#2{\gdef\@avalE{#1}\gdef\@instavalE{#2}}
\def\avaliadorF#1#2{\gdef\@avalF{#1}\gdef\@instavalF{#2}}
\def\avaliadorG#1#2{\gdef\@avalG{#1}\gdef\@instavalG{#2}}
\def\avaliadorH#1#2{\gdef\@avalH{#1}\gdef\@instavalH{#2}}

\let\@cotutela\relax
\def\cotutela#1{\gdef\@cotutela{#1}}

\let\@areaConcentracao\relax
\def\areaConcentracao#1{\gdef\@areaConcentracao{#1}}

\def\paginasiniciais{
  \newlength{\oldparindent}
  \setlength{\oldparindent}{\parindent}
  \setlength\parindent{0pt}
  \thispagestyle{empty}
  \pagestyle{empty}  
  \makeatletter
  \let\ps@mystyle\ps@plain
  \let\ps@plain\ps@empty
  \makeatother
  \openningpage
  \clearpage
  \titlepage

  \@textoaviso

  \clearpage
  \approvalpage
  \clearpage
  \setlength{\parindent}{\oldparindent}
  \resetlang
}


\def\logos{
    \noindent
    \raisebox{-.5\height}{\includegraphics[width=2.2cm]{logoibra.png}}

    \vspace*{2cm}
    
    \noindent
    \begin{center} \large
        \bf{\MakeUppercase{\@UNICAMP}}\\
        \bf{\MakeUppercase{\@IFCH}}
    \end{center}
}

\def\openningpage{
  \logos
  \vskip 35mm
  \begin{center}
    \Large
    {\sc \Large \@title}
    \vskip 25mm
    {\MakeUppercase{\bf \if\@autora\relax\@autor\else\@autora\fi}}
    \vskip 25mm
    {\sc \Large \@titulo}
    \vfill
    \large
    Campinas\\\@ano
  \end{center}
}


\def\titlepage{
  \large\bf
  \vfill
  \begin{center}
    \sc \@titulo\\
    \vspace*{0.5cm}
    \sc  \@title\\
    \vspace*{1.3cm}
    \sc \if\@autora\relax\@autor\else\@autora\fi\\
  \end{center}
  \vfill
  \normalfont
  \normalsize
  \hfill\begin{minipage}[t]{0.54\textwidth}
    \supresshyphen
    Trabalho de Conclusão de Curso apresentado ao Grupo Educacional IBRA como requisito para a aprovação na disciplina de TCC
    Trabalho orientado de forma digital pelo corpo docente do Grupo Educacional IBRA
  \end{minipage}
  \vskip 8mm
  \hfill\begin{minipage}[t]{0.54\textwidth}
    \supresshyphen
    %...
    \end{minipage}
    
  \vfill
  \ifcase\@thesislanguage
    {\bf Supervisor/Orientador}\hspace{-0.9ex}
  \or
    \if\@orientadora\relax {\bf Director/}\else {\bf Directora/}\fi\hspace{-0.9ex}
  \fi
  \if\@orientadora\relax {\bf: \@orientador}
  \else {\bf Orientadora: \@orientadora}
  \fi
  \ifnum\@advisors=2
    \\
    \ifcase\@thesislanguage
      {\bf Co-supervisor}\hspace{-0.7ex}
    \or
      \if\@coorientadora\relax {\bf Co-director/}\else {\bf Co-directora/}\fi\hspace{-0.7ex}
    \fi
    \if\@coorientadora\relax {\bf Coorientador: \@coorientador}
    \else {\bf Coorientadora: \@coorientadora}
    \fi
  \fi
  \vfill
  \iffinalversion
    \begin{minipage}[t]{0.5\textwidth}
      \supresshyphen
      \sc Este exemplar corresponde à versão final da \@monopt\xspace defendida por
      \if\@autora\relax\@autor\else\@autora\fi\xspace e orientada
      \if\@orientadora\relax pelo \@orientador\else pela \@orientadora\fi.
    \end{minipage}
  \else
    \begin{minipage}[t]{0.5\textwidth}
      \supresshyphen
      %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
      % uncomment this for the final version, PLEASE!
      \sc Este trabalho corresponde à versão final 
      da \@monopt defendida pelo aluno \@autor.
      %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
    \end{minipage}
  \fi
  \vfill
  \begin{center}
    \large
    Campinas\\ \@ano
  \end{center}
}

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
% comment this
\def\cathpage{
  \ifx\@fichacatalografica\relax
  %Na versão final, esta página será substituída pela
  %ficha catalográfica na dissertação de mestrado e ou na
  %tese de doutorado.
  %
  %No caso de TCC, deixe essa página em branco.\\
  %Adicione o arquivo PDF com a ficha catalográfica no comando \textbackslash\texttt{fichacatalografica\{\,\}} no arquivo principal.
  %
  %De acordo com o padrão da CCPG: ``Quando se tratar de Teses e
  %Dissertações financiadas por agências de fomento, os beneficiados
  %deverão fazer referência ao apoio recebido e inserir esta
  %informação na ficha catalográfica, além do nome da agência, o
  %número do processo pelo qual recebeu o auxílio.''\\e\\``caso a
  %tese de doutorado seja feita em Cotutela, será necessário informar na
  %ficha catalográfica o fato, a Universidade convenente, o país e o
  %nome do orientador.''
  \else
  \includepdf[pagecommand={}]{\@fichacatalografica}
  \fi
}

\def\approvalpage{
  \iffinalversion
    \logos
%    \noindent\centerline{\large\MakeUppercase{\textbf{Folha de Aprovação}}}
    \vskip 20mm
    
    A Comissão Julgadora dos trabalhos de Defesa de \@monopt\xspace, composta pelos Professores Doutores a seguir descritos, em sessão pública realizada em \@dia\xspace de \ifcase \@mes \or janeiro\or fevereiro\or março\or abril\or maio\or junho\or julho\or agosto\or setembro\or outubro\or novembro\or      dezembro\fi\xspace de \@ano\xspace, considerou \@artigo\xspace candidat\@artigo\xspace \if\@autora\relax\@autor\else\@autora\fi\xspace aprovad\@artigo\xspace.

    \vfill

    \ifx\@avalA\relax
    \else
       \noindent \textbf{\@avalA}\newline 
       \noindent Presidente da Comissão Julgadora \vspace*{3em}%\@instavalA 
       
       \ifx\@avalB\relax\else \noindent \textbf{\@avalB}\newline\@instavalB\vspace*{3em}\fi
       
       \ifx\@avalC\relax\else \noindent \textbf{\@avalC}\newline\@instavalC\vspace*{3em}\fi
       
       \ifx\@avalD\relax\else \noindent \textbf{\@avalD}\newline\@instavalD\vspace*{3em}\fi
       
       \ifx\@avalE\relax\else \noindent \textbf{\@avalE}\newline\@instavalE\vspace*{3em}\fi
       
       \ifx\@avalF\relax\else \noindent \textbf{\@avalF}\newline\@instavalF\fi
    \fi
    \vfill
    %\hfill\begin{minipage}[t]{\textwidth}
      %\begin{center}
      
      \supresshyphen
      \noindent
      A Ata de Defesa com as respectivas assinaturas dos membros encontra-se no SIGA/Sistema de Fluxo de Dissertações/Teses e na Secretaria do Programa de Pós-Graduação em Demografia do Instituto de Filosofia e Ciências Humanas.

      %\end{center}
    %\end{minipage}
    % \vfill
    % \hfill\begin{minipage}[t]{\textwidth}
    %   \begin{center}
    %   Limeira, \@dia\xspace de
    %   \ifcase \@mes \or janeiro\or fevereiro\or março\or abril\or maio\or
    %   junho\or julho\or agosto\or setembro\or outubro\or novembro\or
    %   dezembro\fi\xspace
    %   de \@ano
    %   \end{center}
    % \end{minipage}
    \vfill
  \else
    %Na versão final, esta página será substituída por outra
    %informando a composição da banca e que a ata de defesa está arquivada
    %pela Unicamp.
  \fi
}


\def\prefacesection#1{
  \chapter*{#1}
  %\addcontentsline{toc}{chapter}{#1}
  \pagestyle{empty}
  \thispagestyle{empty}
}


\gdef\resetlang{
  \ifcase\@thesislanguage\relax
  \selectlanguage{english}
  \or\selectlanguage{spanish}
  \or\selectlanguage{brazil}
  \fi
}

\gdef\supresshyphen{
  \tolerance=1
  \emergencystretch=\maxdimen
  \hyphenpenalty=10000
  \hbadness=10000
}

% Definição dos Elementos Pré-textuais
\newenvironment{resumo}{\prefacesection{Resumo}\selectlanguage{brazil}}{\resetlang \newpage} 
\renewenvironment{abstract}{\prefacesection{Abstract}\selectlanguage{english}}{\resetlang \newpage}
\newenvironment{resumen}{\prefacesection{Resumen}\selectlanguage{spanish}}{\resetlang \newpage}

\newenvironment{epigrafe}{\newpage\mbox{}\vfill\hfill\begin{minipage}[t]{0.5\textwidth}}
{\end{minipage}\newpage}

\newcommand{\fimdaspaginasiniciais}{
\newpage 
\makeatletter
\let\ps@plain\ps@mystyle
\renewcommand\chapter{\if@openright\cleardoublepage\else\clearpage\fi
                    \pagestyle{fancy}
                    \fancyhf{}
                \renewcommand{\headrulewidth}{0.5pt} 
                \fancyhead[L]{\rightmark}
                    \fancyhead[R]{\thepage}% 
                    \global\@topnum\z@
                    \@afterindentfalse
                    \secdef\@chapter\@schapter}
\makeatother


\setstretch{1.5} %Definido espaçamento entre linhas de 1,5
\setlength{\parindent}{0.635cm}% 

}

%controle de linhas órfãs e viúvas.
\widowpenalty10000
\clubpenalty10000

%comandos específicos para Figuras, Tabelas, Seções etc.
\newcommand{\Capitulo}[1] {Capítulo~\ref{#1}}
\newcommand{\Equacao}[1] {Equação~\ref{#1}}
\newcommand{\Figura}[1]{Figura~\ref{#1}}
\newcommand{\Secao}[1] {Seção~\ref{#1}}
\newcommand{\Tabela}[1] {Tabela~\ref{#1}}