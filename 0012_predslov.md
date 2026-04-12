---
jupytext:
  formats: md:myst
  text_representation:
    extension: .md
    format_name: myst
    format_version: 0.13
    jupytext_version: 1.11.5
kernelspec:
  display_name: Python 3
  language: python
  name: python3
---


# <font color='navy'> Predslov  </font> 

Publikácia "Programová tvorba technickej grafiky" je venovaná tvorbe technickej grafiky pre publikovanie v profesionálnej kvalite. Je určená študentom technických odborov, technikom, špecialistom, vedeckým pracovníkom ako aj všetkým záujemcom o prezentovanie výsledkov svojej práce pomocou kvalitného grafického výstupu. Publikácia popisuje základy tvorby schém a zapojení pomocou open-source programovacieho jazyka *dpic* a knižnice makier pre kreslenie elektronických prvkov *CircuitMacros* ako aj tvorbu špecifických grafických komponentov pomocou uživateľom vytvorených vlastných makier. Publikácia obsahuje príklady typických konštruktov v často používaných zapojeniach, nepokrýva ale všetky možnosti, ktoré sú súčasťou knižnice *CicuitMacros*, v prípade záujmu odporúčame čitateľa ku štúdiu dokumentácie. 

Kolektív autorov.

Apríl 2026


# <font color='navy'> Preface  </font> 

Circuit diagrams are a class of technical drawings that has evolved
according to convention and published standards, so that complex
electrical and electronic structures can be described clearly.  These are
primarily line diagrams, without extensive use of color or other effects
allowed by modern publication methods. Consequently, many software tools
are capable of producing circuit diagrams.

This book describes one set of tools for drawing circuit diagrams
for publications produced by LaTeX but also with application elsewhere,
such as in web documents.  Starting with the basics, it describes the
installation and use of the freely available Circuit_macros distribution.
Drawing requires the creation of an ordinary text document that is processed
into a diagram that can be produced in several possible formats.

Briefly, a diagram is produced by being processed through dpic, an
implementation of the pic "little language" originally developed for the
comfort of non-programmers using the Unix operating system.  Dpic code
is easily readable and can be learned in an hour or so to produce line
diagrams very simply but it has the power to perform complex geometrical
computations when necessary.  The language is extended and specialized by
the use of macros written for the simple and powerful m4 macro processor,
which can access extensive libraries of predefined circuit elements.

The book gives a clear description of how to install m4, dpic, and
pycircuit, a graphical interface designed for Circuit_macros.  It then
describes basic usage, hints, and tricks with liberal use of examples.

Development of the Circuit_macros distribution began in the late 1980s
when there was very little choice of drawing tools integrated with LaTeX.
The distribution has been freely available since the mid-1990s and
has grown and evolved according to comments and requests from users.
The manual contains a "Developer's notes" section that describes
the motivation, evolution, and compromises made for the distribution.
The macros were developed initially as an extension of the dpic language
and were given easily recognizable names rather than less readable names
that would avoid all name clashes. Compatibility with older distributions
was preserved as the macros evolved but, as new options and additions
were added, some macros became more difficult to read and customize.
Since all possible circuit elements and styles cannot be anticipated and
included, the user is encouraged to customize existing element macros
or to create compatible new elements. A selection of new and customized
elements is included with this book.

Creating a circuit diagram for a technical document is like writing: authors
should all understand the basic tools, but producing the best examples
is an art. This book assists with both the basics and more refined diagrams.

Dwight Aplevich

December, 2025

