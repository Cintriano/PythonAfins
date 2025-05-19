import os

def transformar_arquivo(caminho_arquivo):
    if not os.path.exists(caminho_arquivo):
        return "Arquivo não existente"

    nome_saida = f"convertido_{os.path.basename(caminho_arquivo)}"

    with open(caminho_arquivo, 'r', encoding='utf-8') as f:
        linhas = f.readlines()

    with open(nome_saida, 'w', encoding='utf-8') as f_out:
        for linha in linhas:
            if linha.strip():  # ignora linhas em branco
                nova_linha = linha.replace('/', ';')
                f_out.write(nova_linha)

    return f"Arquivo salvo como {nome_saida}"

if __name__ == "__main__":
    nome_arq = "LOG_15.05.2025_24940.txt"
    caminho_completo = fr"C:\Users\danil\OneDrive\Publicação\Upload\Log\{nome_arq}"
    print(transformar_arquivo(caminho_completo))
