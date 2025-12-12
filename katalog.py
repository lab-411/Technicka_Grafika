'''
Generator katalogu v *.md subore

Ver. 0.1
'''

from src.utils import *
import re

file = '0210_ex_makra.md'


def katalog(prg, file, chapter, text):

    for n,i in enumerate(prg):
        code = i[0] + i[1]
        print(re.sub(r"[\n\t]*", "", code))
        cm_compile(chapter+"_"+str(n), re.sub(r"[\n\t]*", "", code),  dpi=600)  

    fp = open('../'+file,'a')
    fp.write(text)

    for i in range(len(prg)):
        
        cmd = prg[i][1]
        img = chapter+"_"+str(i)+".png"
        width = prg[i][2]
        
        s='''
::::{grid} 2
:gutter: 0
:margin: 0

:::{grid-item}
:columns: 5

```{figure} ./src/''' + img + '''
:width: ''' + str(width) + '''px
```
:::

:::{grid-item}
:columns: 7

    ''' + cmd + '''
:::
::::
'''
        #print(s)
        fp.write(s)
    fp.close()

#-----------------------------------------------------------------------

def title(txt):
    fp = open(file,'w')
    fp.write(txt)
    fp.close()
    
def text(txt):
    fp = open(file,'a')
    fp.write(txt)
    fp.close()

#=======================================================================


title("# <font color='navy'> Katalóg </font> \n Katalóg obsahuje najčastejšie používané prvky zapojení. \n\n")

prg_comp = [
    ('', 'resistor(,E);llabel(,R_1,);rlabel(,10k,)', 120),
    ('', 'resistor(,E);llabel(,R_1,);\n\tb_current(i);\n\trarrow(u);', 120),
    ('', 'resistor(,E);variable(,A,,elen_*0.65);', 120),
    ('', 'capacitor(,,,0.55,0.15); \n\tllabel(,C_1,);rlabel(,100 nF,);', 120 ),
    ('', 'capacitor(,K+,,0.55, 0.18); \n\tllabel(,C_1,);rlabel(,10 \\mu F,)', 120 ),
    ('', 'inductor(,L,6); \n\tllabel(,L_1,);rlabel(,100 \\mu H,);', 120 ),
    ('', 'L1:[Q: inductor(,L,6); linethick_(2); \n\tline dimen_*0.7 at Q.c + (0,0.25);];\
          \n\t"$L_1$" at L1.n above;', 140 ),
    ('', 'TR:[Q:transformer(down_ 1.5,L,6,W,4); \n\t line from Q.S1 to (Q.S1,Q.P1);\
         \n\t line from Q.S2 to (Q.S2,Q.P2)]; \n\t "$L_1$" at TR.w rjust; "$L_2$" at TR.e ljust;', 120 ),
    ('include(lib_user.ckt);', 'line 1.5; l_current(i_1,above,0.5); dot; \
      \n\t{ line right_ 1 up_ 1; l_current(i_2,above rjust)\n\t};\
      \n\tline right_ 1 down_ 1;l_current(i_3,above ljust);', 120),
   
]

s = "## <font color='teal'> Pasívne prvky </font> \n"
katalog(prg_comp, file, 'comp', s)

#-----------------------------------------------------------------------

prg_graph = [
    ('include(lib_color.ckt); color_red;','sinusoid(1.0, pi_*4/10,-pi_/2, 0, 10);', 380),
    ('','hatchbox(wid 3 ht 1.5,,dashed,angle=125 );', 150 ),
    ('','shadebox(box wid 3 ht 1.5 "text", 2);', 150 ),
    ('B: box wid 10 ht 2; move to B.w;', 'for x = 0 to 10  by 0.05 do \n\t   { line to (x, rand()*0.25); } ;', 380 ),
]

s = "## <font color='teal'> Grafické prvky </font> \n"
katalog(prg_graph, file, 'graph', s)

#-----------------------------------------------------------------------

prg_work = [
    ('include(lib_base.ckt);', 'Grid(5,2);', 300 ),
]

s = "## <font color='teal'> Pracovná plocha </font> \n"
katalog(prg_work, file, 'space', s)


