#!/usr/bin/env python
# coding: utf-8

import pandas as pd

if '__main__' == __name__:

    # Import dataframe

    final_database = pd.read_excel('./data/spanish_dataframe.xlsx', encoding='utf-8')

    # Catalan to Spanish with Apertium !

    dataframe_in_catalan = final_database.loc[final_database['Origen'].isin(['cat1', 'cat2'])]

    to_be_translated = ['Actividades', 'Ambitogeo_actuacion', 'Areas_actividad', 'Clasificacion',
                        'Clasificacion_especifica', 'Fines', 'Historia',
                        u'Sectores atendidos: Culturales, investigación, medio ambiente o cooperación',
                        'Sectores atendidos: servicios sociales y salud', 'Tipo_actividades']
    dataframe_in_catalan = dataframe_in_catalan[to_be_translated]

    writer = pd.ExcelWriter('./data/catalan_dataframe.xlsx')
    dataframe_in_catalan.to_excel(writer)
    writer.save()

    ######## Manually translate in Apertium ! https://www.apertium.org

    dataframe = pd.read_excel('./data/catalan_dataframe_translated.xlsx', encoding='utf-8')

    columns = ['Actividades', 'Ambitogeo_actuacion', 'Areas_actividad', 'Clasificacion', 'Clasificacion_especifica',
               'Finas', 'Historia', 'Sectores atendidos: Culturales, investigación, medio ambiento o cooperación',
               'Sectores atendidos: servicios sociales y salud', 'Tipo_actividades']

    dataframe = dataframe[columns]

    for col in list(columns):
        for idx in dataframe.index.tolist():
            final_database[col][idx] = dataframe[col][idx]

    to_be_translated = [u'Actividades', u'Areas_actividad', u'Clasificacion', u'Clasificacion_especifica',
                        u'Codig_actividad', u'Fines', u'Historia',
                        u'Sectores atendidos: Culturales, investigación, medio ambiente o cooperación',
                        u'Sectores atendidos: servicios sociales y salud', u'Tipo_actividades']
    final_database = final_database[to_be_translated]

    writer = pd.ExcelWriter('./data/spanish_dataframe.xlsx')
    final_database.to_excel(writer, index=False)
    writer.save()
