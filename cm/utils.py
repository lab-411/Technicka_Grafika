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
from IPython.display import HTML, display

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

def cm_compile(file_name, cm_data='', dpi=300, log=False):
    '''
    Konverzia textu s makrami na obrazok.
    Vyuziva pycirkuit.
    '''
    fp = open( file_name + '.ckt', 'w'); 
    fp.write(cm_start + cm_data + cm_end);
    fp.close()

    os.environ["QT_LOGGING_RULES"] = "qt5ct.debug=false"
    os.environ["QT_QPA_PLATFORM"] = "xcb"
    
    if log==True:
        os.system(r'pycirkuit --links --overwrite --dpi ' + str(dpi) +' -p ' + file_name + '.ckt ')
    else:
        os.system(r'pycirkuit --links --overwrite --dpi ' + str(dpi) +' -p ' + file_name + '.ckt > /dev/null')

    return file_name + '.ckt'
    
#-----------------------------------------------------------------------

CIRCUIT_MACROS_PATH = './img/cm'

def cm2ps(fname):
    '''
    Konverzia cm na eps
    '''

    fname_base = os.path.splitext(fname )[0]
    texfile      = fname_base + '_pst'
    templatefile = fname_base + '.tex'
    epsfile      = fname_base + '.eps'

    #print('>> m4 pstricks')
    os.system( 'm4 -I %s pstricks.m4 %s | dpic -p > %s'%(CIRCUIT_MACROS_PATH, fname, texfile+'.tex') )

    latextemplate = '''\\documentclass{article}
    \\usepackage{times,pstricks,pst-eps,pst-grad,xfrac}
    \\usepackage{graphicx}
    \\begin{document}
    \\begin{TeXtoEPS}
    \\input %s
    \\end{TeXtoEPS}\\end{document}
    '''%texfile

    f = open( templatefile, 'w' )
    f.write( latextemplate )
    f.flush()
    f.close()

    #print('>> latex')    
    os.system( 'latex -output-directory=./img/  %s'%templatefile )       

    #print('>> dvips')
    os.system( 'dvips  -E %s -o %s '%(fname_base, epsfile) ) 
    
    # na poradi argumentov ZALEZI !!!
    #print('>> convert eps to png')
    os.system('convert -density 600 -quality 100 -flatten %s -colorspace RGB %s'%(epsfile, fname_base+'.png'))

    #os.system( 'dvips -Ppdf -G0 -E %s -o %s'%(fname_base, epsfile) )
    #os.system( 'rm '+fname_base + '.dvi' ) 
    #os.system( 'rm '+fname_base + '.aux' ) 
    #os.system( 'rm '+fname_base + '.log' ) 
        

