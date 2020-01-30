import pandas as pd


class TestBase:
    def __init__(self, dataframe):
        self.data = dataframe
        self.cols_obj = []
        self.cols_int = []
        self.cols_flo = []
        self.test_title = ''''''
        self.msg = ''''''

    @property
    def missing_values_is_npnan(self):
        hasNULO = True in [(self.data[it] == '#NULO#').any() for it in self.cols_obj]
        hasNE = True in [(self.data[it] == '#NE').any() for it in self.cols_obj]
        hasminus3 = True in [(self.data[it] == -3).any() for it in (self.cols_int + self.cols_flo)]
        hasminus1 = True in [(self.data[it] == -1).any() for it in (self.cols_int + self.cols_flo)]

        if hasNULO:
            self.msg += 'Melhor substituir "#NULO#" nas colunas de tipo object para np.nan\n'
        if hasNE:
            self.msg += 'Melhor substituir "#NE" nas colunas de tipo object para np.nan\n'
        if hasminus3:
            self.msg += 'Melhor substituir "-3" nas colunas de tipo int ou float para np.nan\n'
        if hasminus1:
            self.msg += 'Melhor substituir "-1" nas colunas de tipo int ou float para np.nan\n'

        return (not hasNULO) and (not hasNE) and (not hasminus3) and (not hasminus1)

    @property
    def dtypes_is_correct(self):
        cols_obj = set(self.cols_obj).issubset(set(self.data.dtypes[self.data.dtypes == 'object'].index.tolist()))
        cols_int = set(self.cols_int).issubset(set(self.data.dtypes[self.data.dtypes == 'int64'].index.tolist()))
        cols_flo = set(self.cols_flo).issubset(set(self.data.dtypes[self.data.dtypes == 'float64'].index.tolist()))

        if not cols_obj: self.msg += 'Estas colunas deveriam ser "object": {}\n'.format(
            set(self.cols_obj).difference(set(self.data.dtypes[self.data.dtypes == 'object'].index.tolist())))
        if not cols_int: self.msg += 'Estas colunas deveriam ser "int64": {}\n'.format(
            set(self.cols_int).difference(set(self.data.dtypes[self.data.dtypes == 'int64'].index.tolist())))
        if not cols_flo: self.msg += 'Estas colunas deveriam ser "float": {}\n'.format(
            set(self.cols_flo).difference(set(self.data.dtypes[self.data.dtypes == 'float64'].index.tolist())))

        return cols_obj and cols_int and cols_flo

    @property
    def execute(self):
        output = ''
        output += 'Dtype columns test: passed\n' if self.dtypes_is_correct else 'Dtype columns test: fault\n'
        output += 'np.nan test: passed\n' if self.missing_values_is_npnan else 'np.nan test: fault\n'

        print('{}\nExecutando: {}\nResultado:\n{}\n{}{}'.format('*' * 10, self.test_title, output, self.msg, '*' * 10))


class TestBemCandidato(TestBase):
    def __init__(self, dataframe):
        super().__init__(dataframe)

        self.cols_obj = ['DT_GERACAO', 'HH_GERACAO', 'NM_TIPO_ELEICAO', 'DS_ELEICAO', 'DT_ELEICAO', 'SG_UF', 'SG_UE',
                         'NM_UE', 'DS_TIPO_BEM_CANDIDATO', 'DS_BEM_CANDIDATO', 'DT_ULTIMA_ATUALIZACAO',
                         'HH_ULTIMA_ATUALIZACAO']
        self.cols_int = ['ANO_ELEICAO', 'CD_TIPO_ELEICAO', 'CD_ELEICAO', 'SQ_CANDIDATO', 'NR_ORDEM_CANDIDATO',
                         'CD_TIPO_BEM_CANDIDATO']
        self.cols_flo = ['VR_BEM_CANDIDATO']
        self.test_title = 'Teste Bem Candidato'

        self.execute


class TestConsultaCand(TestBase):
    def __init__(self, dataframe):
        super().__init__(dataframe)
        self.cols_obj = ['DT_GERACAO', 'HH_GERACAO', 'NM_TIPO_ELEICAO', 'DS_ELEICAO',
                         'DT_ELEICAO', 'TP_ABRANGENCIA', 'SG_UF', 'SG_UE', 'NM_UE', 'DS_CARGO',
                         'NM_CANDIDATO', 'NM_URNA_CANDIDATO', 'NM_SOCIAL_CANDIDATO', 'NM_EMAIL',
                         'DS_SITUACAO_CANDIDATURA', 'DS_DETALHE_SITUACAO_CAND', 'TP_AGREMIACAO',
                         'SG_PARTIDO', 'NM_PARTIDO', 'NM_COLIGACAO', 'DS_COMPOSICAO_COLIGACAO',
                         'DS_NACIONALIDADE', 'SG_UF_NASCIMENTO', 'NM_MUNICIPIO_NASCIMENTO',
                         'DT_NASCIMENTO', 'DS_GENERO', 'DS_GRAU_INSTRUCAO', 'DS_ESTADO_CIVIL',
                         'DS_COR_RACA', 'DS_OCUPACAO', 'DS_SIT_TOT_TURNO', 'ST_REELEICAO',
                         'ST_DECLARAR_BENS', 'DS_SITUACAO_CANDIDATO_PLEITO',
                         'DS_SITUACAO_CANDIDATO_URNA', 'ST_CANDIDATO_INSERIDO_URNA']
        self.cols_int = ['ANO_ELEICAO', 'CD_TIPO_ELEICAO', 'NR_TURNO', 'CD_ELEICAO', 'CD_CARGO',
                         'SQ_CANDIDATO', 'NR_CANDIDATO', 'NR_CPF_CANDIDATO',
                         'CD_SITUACAO_CANDIDATURA', 'CD_DETALHE_SITUACAO_CAND', 'NR_PARTIDO',
                         'SQ_COLIGACAO', 'CD_NACIONALIDADE', 'CD_MUNICIPIO_NASCIMENTO',
                         'NR_IDADE_DATA_POSSE', 'NR_TITULO_ELEITORAL_CANDIDATO', 'CD_GENERO',
                         'CD_GRAU_INSTRUCAO', 'CD_ESTADO_CIVIL', 'CD_COR_RACA', 'CD_OCUPACAO',
                         'NR_DESPESA_MAX_CAMPANHA', 'CD_SIT_TOT_TURNO',
                         'NR_PROTOCOLO_CANDIDATURA', 'NR_PROCESSO',
                         'CD_SITUACAO_CANDIDATO_PLEITO', 'CD_SITUACAO_CANDIDATO_URNA']
        self.test_title = 'Teste Consulta Candidato'
        self.execute

    @property
    def missing_values_is_npnan(self):
        cols_about_age = ['CD_MUNICIPIO_NASCIMENTO', 'SG_UF_NASCIMENTO', 'NM_MUNICIPIO_NASCIMENTO', 'DT_NASCIMENTO',
                          'NR_IDADE_DATA_POSSE']
        hasNULO = True in [(self.data[it] == '#NULO#').any() for it in self.cols_obj]
        hasNE = True in [(self.data[it] == '#NE').any() for it in self.cols_obj]
        hasminus3 = True in [(self.data[it] == -3).any() for it in (self.cols_int + self.cols_flo)]
        hasminus1 = True in [(self.data[it] == -1).any() for it in (self.cols_int + self.cols_flo)]

        hasminus4 = True in [(self.data[it] == -4).any() for it in (self.cols_int + self.cols_flo)]
        hasEmptyAge = True in [(self.data[it] == '').any() for it in cols_about_age]

        if hasNULO: self.msg += 'Melhor substituir "#NULO#" nas colunas de tipo object para np.nan\n'
        if hasNE: self.msg += 'Melhor substituir "#NE" nas colunas de tipo object para np.nan\n'
        if hasminus3: self.msg += 'Melhor substituir "-3" nas colunas de tipo int ou float para np.nan\n'
        if hasminus1: self.msg += 'Melhor substituir "-1" nas colunas de tipo int ou float para np.nan\n'

        if hasminus4: self.msg += 'Melhor substituir "-4" nas colunas de tipo int ou float para np.nan\n'
        if hasEmptyAge: self.msg += 'Melhor substituir " " nas colunas relacionadas à idade do candidato para np.nan: {}\n'.format(
            cols_about_age)

        return (hasEmptyAge) and (hasminus4) and (not hasNULO) and (not hasNE) and (not hasminus3) and (not hasminus1)


class TestConsultaColigacao(TestBase):
    def __init__(self, dataframe):
        super().__init__(dataframe)
        self.cols_obj = ['DT_GERACAO', 'HH_GERACAO', 'NM_TIPO_ELEICAO', 'DS_ELEICAO',
                         'DT_ELEICAO', 'SG_UF', 'SG_UE', 'NM_UE', 'DS_CARGO', 'TP_AGREMIACAO',
                         'SG_PARTIDO', 'NM_PARTIDO', 'NM_COLIGACAO', 'DS_COMPOSICAO_COLIGACAO']
        self.cols_int = ['ANO_ELEICAO', 'CD_TIPO_ELEICAO', 'NR_TURNO', 'CD_ELEICAO', 'CD_CARGO',
                         'NR_PARTIDO', 'SQ_COLIGACAO']
        self.test_title = 'Teste Consulta Coligação'
        self.execute


class TestConsultaVagas(TestBase):
    def __init__(self, dataframe):
        super().__init__(dataframe)
        self.cols_obj = ['DT_GERACAO', 'HH_GERACAO', 'NM_TIPO_ELEICAO', 'DS_ELEICAO',
                         'DT_ELEICAO', 'DT_POSSE', 'SG_UF', 'SG_UE', 'NM_UE', 'DS_CARGO']
        self.cols_int = ['ANO_ELEICAO', 'CD_TIPO_ELEICAO', 'CD_ELEICAO', 'CD_CARGO', 'QT_VAGAS']
        self.test_title = 'Teste Consulta Vagas'
        self.execute


class TestMotivoCassacao(TestBase):
    def __init__(self, dataframe):
        super().__init__(dataframe)
        self.cols_obj = ['DT_GERACAO', 'HH_GERACAO', 'NM_TIPO_ELEICAO', 'DS_ELEICAO', 'SG_UF',
                         'SG_UE', 'NM_UE', 'DS_MOTIVO_CASSACAO']
        self.cols_int = ['ANO_ELEICAO', 'CD_TIPO_ELEICAO', 'CD_ELEICAO', 'SQ_CANDIDATO']
        self.test_title = 'Teste Motivo Cassação'
        self.execute
