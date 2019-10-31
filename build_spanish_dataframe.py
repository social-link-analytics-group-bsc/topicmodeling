# coding: utf-8
"""
@author: Fabio Curi
fabio.curipaixao@bsc.es
"""

import numpy as np
import pandas as pd
from dateutil.parser import parse

def build_foundation_dataframe(filename, code, file_type, encoding, sep=None):
    if file_type == 'csv':
        if sep:
            dataframe = pd.read_csv(filename, sep=sep, encoding=encoding)
        else:
            dataframe = pd.read_csv(filename, encoding=encoding)

    if file_type == 'xls' or file_type == 'xlsx':
        if sep:
            dataframe = pd.read_excel(filename, sep=sep, encoding=encoding)
        else:
            dataframe = pd.read_excel(filename, encoding=encoding)

    dataframe['Origen'] = code
    return dataframe

def remove_bckts(dataframe, column):
    dataframe[column] = dataframe[column].str.replace('[', '')
    dataframe[column] = dataframe[column].str.replace(']', '')
    return dataframe[column]

def remove_spaces(dataframe, column):
    dataframe[column] = dataframe[column].str.replace(' ', '')
    return dataframe[column]

def remove_n(dataframe, column):
    dataframe[column] = dataframe[column].str.replace('\n', '')
    return dataframe[column]

def remove_blanks(dataframe, column):
    dataframe[column] = dataframe[column].astype(str)
    dataframe[column] = dataframe[column].str.replace(u'-- Selecciona --', str(np.nan))
    dataframe[column] = dataframe[column].str.replace(u'---------------------', str(np.nan))
    dataframe[column] = dataframe[column].str.replace(u'---', str(np.nan))
    return dataframe[column]

def day_month_year(dataframe, column):
    for i in range(len(dataframe)):
        try:
            dataframe.iloc[i][column] = parse(dataframe.iloc[i][column]).strftime("%d-%m-%Y")
        except:
            continue
    return dataframe[column]

if '__main__' == __name__:

    file_RC = './data/RCdata.csv'
    file_CCF = './data/CCF.csv'
    file_CAT = './data/Generalitat.csv'
    file_euskadi = './data/Euskadi.xlsx'
    file_castillalamancha = './data/CLM.xls'
    file_aragon = './data/Aragon.csv'
    file_madrid = './data/Madrid.xls'
    file_castillayleon = './data/CYL.csv'

    df_RC = build_foundation_dataframe(file_RC, 'RC', 'csv', 'utf-8')
    df_CCF = build_foundation_dataframe(file_CCF, 'CAT1', 'csv', 'utf-8')
    df_CAT = build_foundation_dataframe(file_CAT, 'CAT2', 'csv', 'utf-8')
    df_euskadi = build_foundation_dataframe(file_euskadi, 'EUS', 'xlsx', 'utf-8')
    df_castillalamancha = build_foundation_dataframe(file_castillalamancha, 'CLM', 'xls', 'utf-8')
    df_aragon = build_foundation_dataframe(file_aragon, 'ARA', 'csv', 'utf-8', ';')
    df_madrid = build_foundation_dataframe(file_madrid, 'MAD', 'xls', 'utf-8')
    df_castillayleon = build_foundation_dataframe(file_castillayleon, 'CYL', 'csv', 'latin', sep=';')

    df_RC.columns = ['Nombre', 'NIF', 'N_registro', 'Fecha_extincion', 'Fecha_constitucion', 'Fecha_inscripcion',
                     'Domicilio', 'Localidad', 'Codigopostal', 'Provincia', 'Telefono', 'Fax', 'Correo_electronico', 'Web',
                     'Fines', 'Actividades', 'Fundadores', 'Patronos', 'Directivos', 'Organos', 'Origen']
    df_CCF.columns = ['Areas_actividad', 'Presupuesto_anual', 'Web', 'Protectorado', 'Ano_datos', 'Fecha_inscripcion',
                      'Ambitogeo_actuacion', 'Patronos', 'Actividades', 'Fax', 'Informacion_legal',
                      'Sectores atendidos: servicios sociales y salud', 'Codigopostal_ciudad', 'Domicilio', 'Historia',
                      'N_registro', 'Sectores atendidos: Culturales, Religión', 'Telefono',
                      'Participación en otros organismos', 'Fecha_constitucion', 'Persona_contacto', 'Directivos',
                      'Fundadores', 'Nombre', 'Fines', 'Tipo_actividades', 'Comarca', 'Correo_electronico',
                      'Sectores atendidos: Culturales, investigación, medio ambiente o cooperación', 'Origen']
    df_CAT.columns = ['Nombre', 'Tipo', 'N_registro', 'Fecha_inscripcion', 'Domicilio', 'Municipio', 'Codigopostal',
                      'Comarca', 'Clasificacion', 'Clasificacion_especifica', 'Telefono', 'Fax', 'Correo_electronico',
                      'Web', 'Origen']
    df_euskadi.columns = ['Nombre', 'Nombre2', 'N_registro', 'Nombre3', 'Fecha_constitucion', 'Fines', 'Codig_actividad',
                          'GPS', 'Lat', 'Lon', 'Nombre_lugar', 'Domicilio', 'Municipio', 'Codigo_municipio', 'Codigopostal',
                          'Provincia', 'Codigo_provincia', 'Pais', 'Codigo_pais', 'Telefono', 'Web', 'URL1', 'URL2', 'URL3',
                          'URL4', 'URL5', 'URL6', 'URL7', 'Origen']
    df_castillalamancha.columns = ['N_registro', 'Nombre', 'Fecha_inscripcion', 'Provincia', 'Localidad', 'Clasificacion',
                                   'Correo_electronico', 'Delete', 'Origen']
    df_aragon.columns = ['N_registro', 'Nombre', 'F_publiestatutos', 'Fecha_constitucion', 'Presidente', 'Domicilio',
                         'Estatutos', 'Telefono', 'Fax', 'Correo_electronico', 'NIF', 'Fines', 'Entidad_local',
                         'Codigo_entidad', 'RNUM', 'Delete', 'Origen']
    df_madrid.columns = ['Nombre', 'Nombreanterior', 'N_registro', 'HP', 'Tactual', 'Tprevio', 'TomoB', 'TomoA',
                         'Domicilio', 'Codigopostal', 'Municipio', 'Protectorado', 'Protectoradosigla', 'Fecha_inscripcion',
                         'CTAS', 'NIF', 'Anotificar', 'Observaciones', 'Origen']
    df_castillayleon.columns = ['Nombre', 'NIF', 'Domicilio', 'Telefono', 'Fax', 'Correo_electronico', 'Web', 'Provincia',
                                'Municipio', 'Fines', 'Origen']

    df_CCF['Codigopostal'], df_CCF['Ciudad'] = df_CCF['Codigopostal_ciudad'].str.split(' ', 1).str

    # Merge all dataframes

    final_database = pd.concat([df_RC, df_CCF, df_CAT, df_euskadi, df_castillalamancha, df_aragon, df_madrid,
                                df_castillayleon], axis=0, ignore_index=True)

    # Delete useless columns.

    to_be_deleted = ['Tactual', 'Protectoradosigla', 'Informacion_legal', 'F_publiestatutos', 'Codigopostal_ciudad', 'Tipo',
                     'Estatutos', 'Pais', 'Codigo_entidad', 'HP', 'Nombre2', 'Nombre3', 'Codigo_provincia', 'GPS', 'Delete',
                     'Observaciones', 'TomoA', 'Sectores atendidos: Culturales, Religión', 'TomoB', 'Anotificar',
                     'Nombre_lugar', 'Presidente', 'Nombreanterior', 'RNUM', 'Codigo_pais', 'Codigo_municipio', 'URL1',
                     'URL2', 'URL3', 'URL4', 'URL5', 'URL7', 'URL6', 'CTAS', 'Tprevio']
    final_database.drop(to_be_deleted, axis=1, inplace=True)

    final_database['Fecha_inscripcion'] = final_database['Fecha_inscripcion'].astype(str)

    list_w_bckts = ['Actividades', 'Ambitogeo_actuacion', 'Ano_datos', 'Areas_actividad', 'Ciudad', 'Codigopostal',
                    'Comarca', 'Correo_electronico', 'Directivos', 'Domicilio', 'Fax', 'Fecha_constitucion',
                    'Fecha_extincion', 'Fecha_inscripcion', 'Fines', 'Fundadores', 'Historia', 'N_registro', 'Nombre',
                    'Organos', 'Participación en otros organismos', 'Patronos', 'Persona_contacto', 'Presupuesto_anual',
                    'Protectorado', 'Sectores atendidos: Culturales, investigación, medio ambiente o cooperación',
                    'Sectores atendidos: servicios sociales y salud', 'Telefono', 'Tipo_actividades', 'Web']
    list_spaces = ['Codigopostal', 'Fax', 'Fecha_constitucion', 'Fecha_extincion', 'NIF', 'N_registro', 'Telefono']
    list_n = ['Actividades', 'Ambitogeo_actuacion', 'Ano_datos', 'Areas_actividad', 'Ciudad', 'Clasificacion',
              'Clasificacion_especifica', 'Codig_actividad', 'Codigopostal', 'Comarca', 'Correo_electronico', 'Directivos',
              'Domicilio', 'Entidad_local', 'Fax', 'Fecha_constitucion', 'Fecha_extincion', 'Fecha_inscripcion', 'Fines',
              'Fundadores', 'Historia', 'Localidad', 'Municipio', 'NIF', 'N_registro', 'Nombre', 'Organos', 'Origen',
              'Participación en otros organismos', 'Patronos', 'Persona_contacto', 'Presupuesto_anual',
              'Protectorado', 'Provincia', 'Sectores atendidos: Culturales, investigación, medio ambiente o cooperación',
              'Sectores atendidos: servicios sociales y salud', 'Telefono', 'Tipo_actividades', 'Web']

    for col in list_w_bckts:
        final_database[col] = remove_bckts(final_database, col)

    for col in list_spaces:
        final_database[col] = remove_spaces(final_database, col)

    for col in list_n:
        final_database[col] = remove_n(final_database, col)

    final_database['Codig_actividad'] = final_database['Codig_actividad'].str.replace('0', '')
    final_database['Correo_electronico'] = final_database['Correo_electronico'].str.replace(' ', '')
    final_database['Correo_electronico'] = final_database['Correo_electronico'].str.replace('&', ' & ')
    final_database['Correo_electronico'] = final_database['Correo_electronico'].str.replace('/', ' & ')
    final_database['Fecha_constitucion'] = final_database['Fecha_constitucion'].str.replace('/', '-')
    final_database['Fecha_extincion'] = final_database['Fecha_extincion'].str.replace('/', '-')
    final_database['Fecha_inscripcion'] = final_database['Fecha_inscripcion'].str.replace(' 00:00:00', '')
    final_database['Fecha_inscripcion'] = final_database['Fecha_inscripcion'].str.replace(' ', '')
    final_database['Fecha_inscripcion'] = final_database['Fecha_inscripcion'].str.replace('/', '-')
    final_database['Fecha_inscripcion'] = final_database['Fecha_inscripcion'].str.replace('.', ' ')
    final_database['Fecha_inscripcion'] = final_database['Fecha_inscripcion'].str.replace(' 0', '')
    final_database['Telefono'] = final_database['Telefono'].str.replace('.', '')
    final_database['Telefono'] = final_database['Telefono'].str.replace('-', '')
    final_database['Web'] = final_database['Web'].str.replace('http://www', 'www')
    final_database['Web'] = final_database['Web'].str.replace('www', 'http://www')
    final_database['Web'] = final_database['Web'].str.replace(' http', 'http')

    # Replace missing values

    final_database.replace('', str(np.nan), inplace=True)
    final_database.replace(u'', str(np.nan), inplace=True)
    final_database.replace(u'None', str(np.nan), inplace=True)
    final_database.replace(u'NaT', str(np.nan), inplace=True)
    final_database.fillna(str(np.nan), inplace=True)

    for col in list(final_database.columns):
        final_database[col] = remove_blanks(final_database, col)

    for col in ['Fecha_constitucion', 'Fecha_extincion', 'Fecha_inscripcion']:
        final_database[col] = day_month_year(final_database, col)

    final_database = final_database.apply(lambda x: x.astype(str).str.lower())

    writer = pd.ExcelWriter('./data/spanish_dataframe.xlsx')
    final_database.to_excel(writer, index=False)
    writer.save()
