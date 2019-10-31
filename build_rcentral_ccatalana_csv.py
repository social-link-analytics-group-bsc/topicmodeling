# coding=utf-8
"""
@author: Fabio Curi
fabio.curipaixao@bsc.es
"""

import os
import sys
import codecs
import numpy as np
import pandas as pd
from collections import defaultdict

def delete_repetition(dataframe):
    columns = list(dataframe.columns)[0:14]
    for col in columns:
        dataframe[col] = dataframe[col].str.replace(col + u':', '')
    return dataframe

def sortFreqDict(freqdict):
    aux = [(freqdict[key], key) for key in freqdict]
    aux.sort()
    return aux

if '__main__' == __name__:
    cwd = os.getcwd()
    stdout = sys.stdout
    reload(sys)
    sys.setdefaultencoding('utf-8')
    sys.stdout = stdout

    # Script to gather all Spanish foundations from Registro Central into a single .csv file.

    path = cwd + '/RegistroCentral/'
    columns = ['Nombre fundación', 'NIF', 'Nº de registro', 'Fecha de extinción', 'Fecha de constitución',
               'Fecha de inscripción', 'Domicilio', 'Localidad', 'Código postal', 'Provincia', 'Teléfono',
               'Fax', 'Correo electrónico', 'Web', 'Fines', 'Actividades', 'Fundadores', 'Patronos', 'Directivos',
               'Organos']

    l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12, l13, l14, l15, l16, l17, l18, l19, l20 = [], [], [], [], [], [], [], \
                                                                                                [], [], [], [], [], [], [], \
                                                                                                [], [], [], [], [], []

    for filename in os.listdir(path):
        f = codecs.open(path + filename, 'r', encoding='utf-8')
        f = f.readlines()
        if f:
            l1.append(f[1])
            l2.append(f[2])
            l3.append(f[3])
            l4.append(f[4])
            l5.append(f[5])
            l6.append(f[6])
            l7.append(f[7])
            l8.append(f[8])
            l9.append(f[9])
            l10.append(f[10])
            l11.append(f[11])
            l12.append(f[12])
            l13.append(f[13])
            l14.append(f[14])
            idx_activities = f.index('Actividades:\n')
            idx_fundadores = f.index('Fundadores:\n')
            idx_patronos = f.index('Patronos:\n')
            idx_directivos = f.index('Directivos:\n')
            idx_organos = f.index('Órganos:\n')

            l15.append(f[16:idx_activities])
            l16.append(f[idx_activities + 1:idx_fundadores])
            l17.append(f[idx_fundadores + 1:idx_patronos])
            l18.append(f[idx_patronos + 1:idx_directivos])
            l19.append(f[idx_directivos + 1:idx_organos])
            l20.append(f[idx_organos + 1:])

    RCdata = pd.DataFrame(list(zip(l1, l2, l3, l4, l5, l6, l7, l8, l9, l10, l11, l12, l13, l14, l15, l16, l17, l18, l19, l20)))
    RCdata.columns = columns

    # Delete scrapping noise.

    RCdata = delete_repetition(RCdata)
    RCdata.to_csv(cwd + '/data/RCdata.csv', encoding='utf-8', index=False)

    # Script to gather all Catalan foundations from http://www.ccfundacions.cat/fundacions into a single .csv file.

    path = cwd + '/CoordCatalanaFund/'
    columns = [u'Director i/o gerent\n', u'Patronat\n', u'Nom\n', u'Codi postal i ciutat\n', u'Informaci\xf3 legal\n', 
               u'Adre\xe7a\n', u'Nombre de registre\n', u'Regi\xf3\n', u'Data de registre\n', 
               u"\xc0mbit geogr\xe0fic d'actuaci\xf3\n", u'Tel\xe8fon\n', u'Correu electr\xf2nic\n', u'Any de les dades\n', 
               u'Pressupost anual\n', u"\xc0rees d'activitats\n", u'Objectius\n', u'Persona de contacte\n', u'Fax\n', 
               u"Tipus d'activitats\n", u'Fundadors\n', u'Data, creaci\xf3 de la fundaci\xf3\n',
               u'Activitats representatives\n', u'Protectorat\n', u'Hist\xf2ria\n', 
               u'Sectors atesos: Culturals, recerca, medi ambient o cooperaci\xf3\n',
               u'Sectors atesos: Culturals, Religi\xf3\n', u'Sectors atesos: serveis socials i salut\n',
               u'Participaci\xf3 en altres organismes\n', u'Lloc web\n']

    dic = defaultdict(list)

    for filename in os.listdir(path):
        l = defaultdict(list)
        f = codecs.open(path + filename, 'r', encoding='utf-8')
        f = f.readlines()
        if f:
            for col in columns:
                try:
                    l[col] = f.index(col)
                except:
                    continue

            # l contains all elements from columns present in file f! Note that not all files contain all columns.

            sorted_dic = sortFreqDict(l)

            l_ex = []
            for existing in sorted_dic:
                l_ex.append(existing[1])

            remaining = [x for x in columns if x not in l_ex]

            # Append existing values
            c = 0
            list_dic = []

            for i, j in sorted_dic:
                list_dic.append(i)

            last = list_dic[-1]

            for i, j in sorted_dic:
                if i != last:
                    next_idx = sorted_dic[c + 1][0]
                    dic[j].append(f[i + 1:next_idx])
                    c += 1
                else:
                    dic[j].append(f[i + 1:])

            for el in remaining:
                dic[el].append(np.nan)

    CCFdata = pd.DataFrame.from_dict(dic, orient='index').transpose()
    CCFdata.to_csv(cwd + '/data/CCFdata.csv', encoding='utf-8', index=False)
