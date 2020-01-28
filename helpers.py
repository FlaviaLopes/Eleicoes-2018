import pandas as pd
import numpy as np

pd.set_option('max_colwidth', 200)

def about(data_name=None):
    methods = {
    'bem_candidato': 'bem_candidato_leiame.txt', 
    'consulta_cand': 'consulta_cand_leiame.txt', 
    'consulta_coligacao': 'consulta_coligacao_leiame.txt',
    'consulta_vagas': 'consulta_vagas_leiame.txt',
    'motivo_cassacao': 'motivo_cassacao_leiame.txt'
    }
    if data_name not in methods.keys():
        msg = 'data_name deve assumir um dos valores: {}. Em vez disso você inseriu {}'.format(
            ', '.join(list(methods.keys())), data_name)
        raise ValueError(msg)

    with open(methods[data_name], 'r') as f:
        about = f.read()
        about = about.split('\n\n')
        about = [it.split(':\n') for it in about]
        del about[0:4]
        del about[-1]
        data = {}
        [data.update( {it[0]: [it[1]]}) for it in about]
        return pd.DataFrame(data=data)

def missing(dataframe):
    missing_data = dataframe.isnull()
    missing_data.replace(False, '0', inplace=True)
    missing_data.replace(True, '1', inplace=True)
    missing_data = missing_data.astype('int64')
    return missing_data.sum()[missing_data.sum() > 1]
