import streamlit as st
import pandas as pd
import plotly.express as px
import os
import pandas as pd


# Nome do arquivo CSV diretamente especificado
csv_filename = 'df_new_4.csv'

def load_csv_file(filename):
    """
    Carrega um arquivo CSV com base no nome fornecido, no mesmo diretório do script.
    """
    try:
        # Diretório do script atual
        script_dir = os.path.dirname(os.path.abspath(__file__))
        file_path = os.path.join(script_dir, filename)

        # Verificar se o arquivo existe
        if not os.path.exists(file_path):
            raise FileNotFoundError(f"Erro: O arquivo '{filename}' não foi encontrado no caminho '{file_path}'.")

        # Carregar o arquivo CSV
        return pd.read_csv(file_path)

    except FileNotFoundError as e:
        print(e)
        return None
    except Exception as e:
        print(f"Erro inesperado ao carregar o arquivo '{filename}': {e}")
        return None


# Carregar o dataset
data = load_csv_file(csv_filename)

if data is not None:
    # Criar DataFrame
    df = pd.DataFrame(data)

    # Ajustar o formato de data, se a coluna 'Year' existir
    if 'Year' in df.columns:
        try:
            df['Year'] = pd.to_datetime(df['Year'], format='%Y')
        except Exception as e:
            print(f"Erro ao formatar a coluna 'Year': {e}")
    else:
        print("Aviso: A coluna 'Year' não foi encontrada no dataset.")

    # Exibir as primeiras linhas do DataFrame
    print("Primeiras linhas do DataFrame:")
    print(df.head())
else:
    print("Erro: Não foi possível carregar o dataset.")





########################
# Função para carregar o arquivo de forma robusta
#def load_csv_file(filename):
  #  """
   # Tenta carregar o arquivo CSV fornecido no mesmo diretório do script.
   # """
  #  try:
    #    # Obter o diretório atual do script
    #    script_dir = os.path.dirname(os.path.abspath(__file__))
     #   file_path = os.path.join(script_dir, filename)

     #   # Verificar se o arquivo existe
     #   if not os.path.exists(file_path):
       #     raise FileNotFoundError(f"Error: The file '{filename}' could not be found at '{file_path}'.")

      #  # Carregar o arquivo CSV
       # data = pd.read_csv(file_path)
       # return data

 #   except FileNotFoundError as e:
     #   print(e)
     #   return None
   # except Exception as e:
     #   print(f"An unexpected error occurred: {e}")
     #   return None


# Nome do arquivo CSV
#csv_filename = 'df_new_4.csv'

# Carregar o dataset
#data = load_csv_file(csv_filename)

#if data is not None:
    # Criar DataFrame
  #  df = pd.DataFrame.from_dict(data)

    # Fazer uma cópia e ajustar o formato de data
  #  df2 = df.copy()
  #  df2['Year'] = pd.to_datetime(df2['Year'], format='%Y')
#
    # Exibir as primeiras linhas do DataFrame
  #  print(df.head())
#else:
   # print("Dataset could not be loaded.")




#try:
    # Assuming df_new_4.csv is in the same directory as dataset.py
   # file_path = os.path.join(os.getcwd(), 'df_new_4.csv')
   # file = open(file_path)
   # data = pd.read_csv(file)

    # Rest of your code using the data
#except FileNotFoundError:
  #  print("Error: The file 'df_new_4.csv' could not be found. Please check the file path.")
# Carregar o dataset
# file = open('df_new_4.csv')
# data = pd.read_csv(file)


# print(data.head())
#df = pd.DataFrame.from_dict(data)
#df2 = df.copy()
#df2['Year'] = pd.to_datetime(df2['Year'], format='%Y')

#print(df.head())

#file.close()
