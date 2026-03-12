import pandas as pd
from pathlib import Path

class DataHandler:
  def __init__(self, input_file_path):
    """
    Inicializa o handler com o path para o arquivo Excel.
    """
    self.input_file_path = input_file_path


  def load_fidedignas(self):
    """
    Carrega a planilha fidedignas em um DataFrame.
    """
    if not Path(self.input_file_path).exists():
      raise FileNotFoundError(f"Could not find the file: {self.input_file_path}")
        
    return pd.read_excel(self.input_file_path)

  def create_mapping_dict(self, df, col_codigo_lotacao, col_key, skip):
    """
    Limpa o dataframe, explode as linhas delimitadas e retorna um dicionario
    """
    # Gera um subset
    subset = df.iloc[skip:].copy()
    subset = subset[[col_codigo_lotacao, col_key]].dropna(subset=[col_key])
    
    # Separa as chaves que estão delimitadas por '/'
    subset[col_key] = subset[col_key].astype(str).str.split('/')

    # Explode o dataframe
    df_exploded = subset.explode(col_key)

    # Limpa o dataframe
    # Remove registros vazios e cria uma cópia final
    df_clean = df_exploded.dropna(how='any').copy()
    
    # Remove espaços em branco sobressalentes
    df_clean[col_key] = df_clean[col_key].str.strip()
    df_clean[col_codigo_lotacao] = df_clean[col_codigo_lotacao].str.strip()

    # Retorna o dicionário
    return dict(zip(df_clean[col_key], df_clean[col_codigo_lotacao]))
