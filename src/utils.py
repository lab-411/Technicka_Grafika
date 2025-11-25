'''
Utility pre pouzitie skriptov CircuitMacro v jupyter-book

Historia
220422  - doplnenie konverziu rad dpic prikladov
        - upravy utilit pre konverziu pomocou pycirkuit
240616  - uprava cesty pre zdielane kniznice v owncloud 
240830  - doplnenia a upravy

Otvorenie suboru v pycirkuit
          os.system('pycirkuit ' + file_name + ' &') 
'''

import os
import sys
#=======================================================================
# template - header
# template pre zahlavie suboru, predpoklada sa pouzitie z notebooku,
# ktory je v nadradenom adresari

cm_start = r'''
.PS
pi=3.14159265359
                        # parametre z PIC (resp. GNU PIC)
scale = 2.54            # cm - jednotka pre obrazok
maxpswid = 30           # rozmery obrazku
maxpsht = 30            # 30 x 30cm, default je 8.5x11 inch
cct_init                # inicializacia lokalnych premennych

arrowwid  = 0.127       # parametre sipok - sirka
arrowht = 0.254         # dlzka

'''


# template - footer
cm_end = r'''
.PE
'''

#======================================================================

def cm_compile(file_name, cm_data='', dpi=300):
    '''
    Konverzia textu s makrami na obrazok.
    Vyuziva pycirkuit.
    '''
    
    # kontrola home directory
    # vsetky bunky v jednom *.md subore pouzivaju jednu instanciu pythonu  
    wd =  os.getcwd()
    q = wd.split('/')
    if(q[-1] != 'src'):
        os.chdir('./src/')
        
    fp = open( file_name + '.ckt', 'w'); 
    fp.write(cm_start + cm_data + cm_end);
    fp.close()

    os.environ["QT_LOGGING_RULES"] = "qt5ct.debug=false"
    os.environ["QT_QPA_PLATFORM"] = "xcb"
        
    CIRCUIT_MACROS_PATH = './cm'
    
    # PSTRICKS
    #os.system( 'm4 -I %s pstricks.m4 %s | dpic -p > data.tex'%(CIRCUIT_MACROS_PATH, file_name+'.ckt') )
    # TIKZ 
    os.system( 'm4 -I %s pgf.m4  %s > data.dpc'%(CIRCUIT_MACROS_PATH, file_name+'.ckt') )
    # DPIC
    os.system( 'dpic -g data.dpc > data.tex') 
    
    temp = r'''
    \documentclass{article}
    \usepackage{amsmath}
    \usepackage{pstricks,pst-plot, pst-eps, tikz}
    \pagestyle{empty}
    \begin{document}
    \begin{TeXtoEPS}
    \input{data.tex}
    \end{TeXtoEPS}
    \end{document}
    '''
  
    f = open('template.tex', 'w' ) 
    f.write(temp)
    f.flush()
    f.close()
    
    # LATEX
    os.system( 'latex template.tex > latex.log')   
    
    # DVIPS
    os.system( 'dvips -q* -E template.dvi -G0 -o %s > dvips.log '%(file_name+'.eps') )
    #print('DVIPS')
    #os.system( 'dvips -E  template.dvi -G0 -o %s  '%(file_name+'.eps') )
    
    os.system('gs -dSAFER -dEPSCrop -r600 -sDEVICE=pngalpha -dALLOWPSTRANSPARENCY -o %s %s > gs.log'%(file_name+'.png', file_name+'.eps'))
    
    os.system( 'rm *.dvi' )
    os.system( 'rm *.aux' )
    #os.system( 'rm *.log' )
    os.system( 'rm *.tex' )
    os.system( 'rm *.eps' )
    os.system( 'rm *.dpc' )
    return file_name + '.ckt'
    
#-----------------------------------------------------------------------
        
data = r'''
include(lib_base.ckt)
include(lib_color.ckt)
Origin: Here 

Grid(5, 5);

P1: (1, 1);
P2: (4, 4);
P3: (3.5, 1.5)

circle rad 0.1 at P1;
circle rad 0.1 at P2;
circle rad 0.1 at P3;

color_red;
A1: arc cw from P1 to P2 
"A1" at A1.nw above rjust;
L1: line from P1 to P2 dashed; 
circle rad 0.1 at L1.c;
color_blue
A2: arc -> cw from P1 to P2 with .c at P3
line from P1 to P3 dashed;
line from P2 to P3 dashed;
"A2" at A2.nw above rjust;

'''

#_ = cm_compile('9999_cm_0110d', data, dpi=600)  


