"""
Laboratorio - Manipulación de Datos usando Pandas
-----------------------------------------------------------------------------------------

Este archivo contiene las preguntas que se van a realizar en el laboratorio.

Utilice los archivos `tbl0.tsv`, `tbl1.tsv` y `tbl2.tsv`, para resolver las preguntas.

"""

import pandas as pd

tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
tbl1 = pd.read_csv("tbl1.tsv", sep="\t")
tbl2 = pd.read_csv("tbl2.tsv", sep="\t")


def pregunta_01():
    """
    ¿Cuál es la cantidad de filas en la tabla `tbl0.tsv`?

    Rta/
    40

    """
    tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
    rta= len(tbl0)
    return rta


def pregunta_02():
    """
    ¿Cuál es la cantidad de columnas en la tabla `tbl0.tsv`?

    Rta/
    4

    """
    tbl0 = pd.read_csv("tbl0.tsv", sep="\t")
    cols= len(tbl0.axes[1])
    print(cols)
    return cols
    


def pregunta_03():
    """
    ¿Cuál es la cantidad de registros por cada letra de la columna _c1 del archivo
    `tbl0.tsv`?

    Rta/
    A     8
    B     7
    C     5
    D     6
    E    14
    Name: _c1, dtype: int64

    """
    import numpy as np
    data3 = pd.read_csv('tbl0.tsv', sep = '\t')
    data3 = data3.groupby(['_c1'])['_c1'].count()
    print(data3)
    return data3


def pregunta_04():
    """
    Calcule el promedio de _c2 por cada letra de la _c1 del archivo `tbl0.tsv`.

    Rta/
    A    4.625000
    B    5.142857
    C    5.400000
    D    3.833333
    E    4.785714
    Name: _c2, dtype: float64
    """
    data4 = pd.read_csv('tbl0.tsv', sep = '\t')
    data4 = data4.groupby(['_c1'])['_c2'].mean()
    print(data4)
    return data4



def pregunta_05():
    """
    Calcule el valor máximo de _c2 por cada letra en la columna _c1 del archivo
    `tbl0.tsv`.

    Rta/
    _c1
    A    9
    B    9
    C    9
    D    7
    E    9
    Name: _c2, dtype: int64
    """
    data5 = pd.read_csv('tbl0.tsv', sep = '\t')
    data5 = data5.groupby(['_c1'])['_c2'].max()
    print(data5)
    return data5


def pregunta_06():
    """
    Retorne una lista con los valores unicos de la columna _c4 de del archivo `tbl1.csv`
    en mayusculas y ordenados alfabéticamente.

    Rta/
    ['A', 'B', 'C', 'D', 'E', 'F', 'G']

    """
    import numpy as np

    data6 = pd.read_csv('tbl1.tsv', sep = '\t')
    data6 = data6['_c4'].unique()
    data6 = np.sort(data6)
    j = []
    for i in data6:
        j.append(i.upper())
    print(j)
    return j


def pregunta_07():
    """
    Calcule la suma de la _c2 por cada letra de la _c1 del archivo `tbl0.tsv`.

    Rta/
    _c1
    A    37
    B    36
    C    27
    D    23
    E    67
    Name: _c2, dtype: int64
    """
    data7 = pd.read_csv('tbl0.tsv', sep = '\t')
    data7 = data7.groupby(['_c1'])['_c2'].sum()
    print(data7)
    return data7



def pregunta_08():
    """
    Agregue una columna llamada `suma` con la suma de _c0 y _c2 al archivo `tbl0.tsv`.

    Rta/
        _c0 _c1  _c2         _c3  suma
    0     0   E    1  1999-02-28     1
    1     1   A    2  1999-10-28     3
    2     2   B    5  1998-05-02     7
    ...
    37   37   C    9  1997-07-22    46
    38   38   E    1  1999-09-28    39
    39   39   E    5  1998-01-26    44

    """
    data8 = pd.read_csv('tbl0.tsv', sep = '\t')
    data8.dtypes
    data8['suma'] = data8['_c0']+ data8['_c2']
    print(data8)  
    return data8


def pregunta_09():
    """
    Agregue el año como una columna al archivo `tbl0.tsv`.

    Rta/
        _c0 _c1  _c2         _c3  year
    0     0   E    1  1999-02-28  1999
    1     1   A    2  1999-10-28  1999
    2     2   B    5  1998-05-02  1998
    ...
    37   37   C    9  1997-07-22  1997
    38   38   E    1  1999-09-28  1999
    39   39   E    5  1998-01-26  1998

    """
    df= pd.read_csv('tbl0.tsv', sep='\t')
    df['year'], df['mes'],df['dia'] = df['_c3'].str.split('-', 2).str
    df = df.drop(['mes','dia'], axis=1)
    print(df)
    return df
    

def pregunta_10():
    """
    Construya una tabla que contenga _c1 y una lista separada por ':' de los valores de
    la columna _c2 para el archivo `tbl0.tsv`.

    Rta/
                                   _c1
      _c0
    0   A              1:1:2:3:6:7:8:9
    1   B                1:3:4:5:6:8:9
    2   C                    0:5:6:7:9
    3   D                  1:2:3:5:5:7
    4   E  1:1:2:3:3:4:5:5:5:6:7:8:8:9
    """
    data10= pd.read_csv('tbl0.tsv' , sep='\t')
    letters = sorted(pd.unique(data10._c1))
    serie = pd.Series(letters , name = '_c0')
    listas = []
    for letter in letters:
        temp = sorted(data10[data10['_c1'] == letter]._c2)
        empty = ""
        for num, let in enumerate(temp):
                if num == len(temp)-1:
                    empty = empty + str(let)
                else:
                    empty = empty + str(let)+":"                                      
        listas.append(empty)
    _c1 = pd.Series(listas, name = '_c1')
    rta10 = pd.concat([serie , _c1] , axis = 1)
    print(rta10)

    return rta10


def pregunta_11():
    """
    Construya una tabla que contenga _c0 y una lista separada por ',' de los valores de
    la columna _c4 del archivo `tbl1.tsv`.

    Rta/
        _c0      _c4
    0     0    b,f,g
    1     1    a,c,f
    2     2  a,c,e,f
    3     3      a,b
    ...
    37   37  a,c,e,f
    38   38      d,e
    39   39    a,d,f
    """
    
    data11 = pd.read_csv('tbl1.tsv' , sep='\t')
    x = sorted(pd.unique(data11._c0))
    serie = pd.Series(x , name = '_c0')
    listas = []
    for n in x:
        temp = sorted(data11[data11['_c0'] == n]._c4)
        empty = ""
        for num, let in enumerate(temp):
            if num == len(temp)-1:
                empty = empty + str(let)
            else:
                empty = empty + str(let)+","            
        listas.append(empty)
    _c4 = pd.Series(listas, name = '_c4')
    rta11 = pd.concat([serie , _c4] , axis = 1)
    print(rta11)
    return rta11


def pregunta_12():
    """
    Construya una tabla que contenga _c0 y una lista separada por ',' de los valores de
    la columna _c5a y _c5b (unidos por ':') de la tabla `tbl2.tsv`.

    Rta/
        _c0                                  _c5
    0     0        bbb:0,ddd:9,ggg:8,hhh:2,jjj:3
    1     1              aaa:3,ccc:2,ddd:0,hhh:9
    2     2              ccc:6,ddd:2,ggg:5,jjj:1
    ...
    37   37                    eee:0,fff:2,hhh:6
    38   38                    eee:0,fff:9,iii:2
    39   39                    ggg:3,hhh:8,jjj:5
    """
    import pandas as pd 
    data12 = pd.read_csv('tbl2.tsv' , sep='\t')
    y = sorted(pd.unique(data12._c0))
    serie = pd.Series(y, name= '_c0')
    data12['x2'] =  data12['_c5a'].astype(str) +':'+ data12['_c5b'].astype(str)
    listas = []
    for n in y:
        temp = sorted(data12[data12['_c0'] == n].x2)
        empty = ''
        for num, let in enumerate(temp):
            if num == len(temp)-1:
                empty = empty + str(let)
            else:
                empty = empty + str(let) + ','
        listas.append(empty)
    _c5 = pd.Series(listas, name='_c5')
    rta12 = pd.concat([serie , _c5], axis=1)
    print(rta12)
    return rta12


def pregunta_13():
    """
    Si la columna _c0 es la clave en los archivos `tbl0.tsv` y `tbl2.tsv`, compute la
    suma de tbl2._c5b por cada valor en tbl0._c1.

    Rta/
    _c1
    A    146
    B    134
    C     81
    D    112
    E    275
    Name: _c5b, dtype: int64
    """
    datos13 = pd.read_csv('tbl0.tsv', sep = '\t')
    datos132 = pd.read_csv('tbl2.tsv', sep = '\t')
    rta13 = pd.merge(datos13,datos132)
    rta13 = rta13.sort_values(by=['_c1'])
    rta13 = rta13.groupby('_c1')['_c5b'].sum()
    return rta13
    

