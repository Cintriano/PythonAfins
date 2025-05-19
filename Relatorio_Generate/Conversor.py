import os
from datetime import datetime
import locale

locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

"""data_execucao/hora_execucao/tipo_processo/data_captura/dia_captura/mes_captura/ano_captura/nome_novo/nome_antigo/dispositivo
   09.04.2025/20:10:34/r/06.04.2025/06/Abril/2025/06.04.2025_46192.CR2/_MG_3671.CR2/Canon EOS REBEL T5i"""

# Função para converter a linha
def transformar_linha(linha):
    partes = [p.strip() for p in linha.split('/')]

    data_execucao = partes[0]
    hora_execucao = partes[1]
    tipo_processo = partes[2]
    nome_novo = partes[3]
    nome_antigo = partes[4]
    dispositivo = partes[5]

    # Extrair data da captura do nome_novo (antes do underline)
    data_captura_raw = nome_novo.split('_')[0]

    # Converter data para objetos e partes
    try:
        data_obj = datetime.strptime(data_captura_raw, "%d.%m.%Y")
    except ValueError:
        return f"# ERRO: data inválida em nome_novo: {nome_novo}"

    dia_captura = data_obj.strftime("%d")
    mes_captura = data_obj.strftime("%B").capitalize().replace("Marã§o", "Marco")  # mês por extenso
    ano_captura = data_obj.strftime("%Y")

    # Montar linha final
    nova_linha = f"{data_execucao}/{hora_execucao}/{tipo_processo}/{data_captura_raw}/{dia_captura}/{mes_captura}/{ano_captura}/{nome_novo}/{nome_antigo}/{dispositivo}"
    return nova_linha


# Leitura e escrita
def transformar_arquivo(pasta):
    if not os.path.exists(pasta):
        return "Pasta não Existente"

    caminho_arquivo = os.path.join(pasta)

    nome_saida = caminho_arquivo[53:]

    with open(caminho_arquivo, 'r', encoding='utf-8') as f:
        linhas = f.readlines()

    with open(nome_saida, 'w', encoding='utf-8') as f_out:
        # Escreve o cabeçalho novo
        f_out.write("data_execucao/hora_execucao/tipo_processo/data_captura/dia_captura/mes_captura/ano_captura/nome_novo/nome_antigo/dispositivo\n")

        for linha in linhas:
            if linha.strip() and not linha.startswith("data"):
                nova = transformar_linha(linha)
                f_out.write(nova + '\n')
    return True


if __name__=="__main__":
    nome_arq = "LOG_02.02.2025_97220.txt"
    transformar_arquivo(fr"C:\Users\danil\OneDrive\Publicação\Upload\Log\{nome_arq}")
