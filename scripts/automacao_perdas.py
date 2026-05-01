import pandas as pd
import os

def processar_dados_varejo():
    # Caminho do arquivo conforme sua estrutura
    arquivo_entrada = "../data/App Analise de Perdas.xlsx"
    arquivo_saida = "../data/Base_Analise_Limpa.xlsx"

    print(f"Iniciando o processamento do arquivo: {arquivo_entrada}")

    try:
        # 1. Extração: Carrega os dados recebidos originalmente em Excel
        df = pd.read_excel(arquivo_entrada)

        # 2. Transformação: Exclusão da coluna 'ID' e filtragem seletiva
        # Mantendo apenas: Loja, Ano, Mês, Perdas(Brt)
        colunas_selecionadas = ['Loja', 'Ano', 'Mês', 'Perdas(Brt)']
        
        # O script filtra apenas as colunas necessárias para a análise no Power BI
        df_final = df[colunas_selecionadas].copy()

        # 3. Limpeza: Removendo possíveis linhas vazias (comum em arquivos XLSX manuais)
        df_final.dropna(subset=['Perdas(Brt)'], inplace=True)

        # 4. Carga: Gera o arquivo higienizado para o Power BI
        df_final.to_excel(arquivo_saida, index=False)
        
        print(f"Sucesso! Coluna ID removida. Dados salvos em: {arquivo_saida}")

    except Exception as e:
        print(f"Erro ao processar o arquivo: {e}")

if __name__ == "__main__":
    processar_dados_varejo()