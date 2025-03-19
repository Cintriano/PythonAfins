import os
from pathlib import Path
from bs4 import BeautifulSoup


def find_image_paths(root_directory, exclude_paths=None):
    """
    Percorre diretórios e coleta caminhos de imagens.

    Args:
        root_directory: Diretório raiz para buscar imagens
        exclude_paths: Lista de caminhos a serem excluídos

    Returns:
        Lista de tuplas (caminho_imagem, nome_alt)
    """
    if exclude_paths is None:
        exclude_paths = [r"C:\Users\danil\OneDrive\Cofre Pessoal\MC\Fotos\07.08.2021_17114.jpg",
                         r"C:\Users\danil\OneDrive\Cofre Pessoal\MC\Fotos\06.12.2021_2800.jpg",
                         r"C:\Users\danil\OneDrive\Cofre Pessoal\MC\Fotos\04.11.2021_1549.jpg",
                         r"C:\Users\danil\OneDrive\Cofre Pessoal\MC\Fotos\08.07.2022_0041.jpg",
                         r"C:\Users\danil\OneDrive\Cofre Pessoal\MC\Fotos\10.01.2022_0001.jpg",
                         r"C:\Users\danil\OneDrive\Cofre Pessoal\MC\Fotos\13.07.2022_86802.jpg",
                         r"C:\Users\danil\OneDrive\Cofre Pessoal\MC\Fotos\13.07.2022_92308.jpg",
                         r"C:\Users\danil\OneDrive\Cofre Pessoal\MC\Fotos\20.09.2021_0006.jpg",
                         r"C:\Users\danil\OneDrive\Cofre Pessoal\MC\Fotos\20.09.2021_0007.jpg",
                         r"C:\Users\danil\OneDrive\Cofre Pessoal\MC\Fotos\20.09.2021_0008.jpg",
                         r"C:\Users\danil\OneDrive\Cofre Pessoal\MC\Fotos\21.05.2022_2052.jpg",
                         r"C:\Users\danil\OneDrive\Cofre Pessoal\MC\Fotos\22.11.2021_0020.jpg",
                         r"C:\Users\danil\OneDrive\Cofre Pessoal\MC\Fotos\24.04.2022_0002.jpg",
                         r"C:\Users\danil\OneDrive\Cofre Pessoal\MC\Fotos\25.09.2021_0011.jpg",
                         r"C:\Users\danil\OneDrive\Cofre Pessoal\MC\Fotos\27.11.2021_4835.jpg",
                         r"C:\Users\danil\OneDrive\Cofre Pessoal\MC\Fotos\29.10.2021_0019.jpg",
                         r"C:\Users\danil\OneDrive\Cofre Pessoal\MC\Fotos\29.07.2021_22163.jpg",]

    # Extensões de imagens comuns
    extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp', '.webp', '.svg']

    # Coleta os caminhos de imagens
    image_paths = []

    # Converte caminhos para objetos Path
    root_path = Path(root_directory)
    exclude_paths = [Path(path) for path in exclude_paths]

    # Percorre os diretórios e arquivos
    for current_path, _, files in os.walk(root_path):
        current_path_obj = Path(current_path)

        # Pula caminhos excluídos
        skip = False
        for exclude_path in exclude_paths:
            try:
                if current_path_obj == exclude_path or current_path_obj.is_relative_to(exclude_path):
                    skip = True
                    break
            except AttributeError:  # Para Python < 3.9
                if str(current_path_obj).startswith(str(exclude_path)):
                    skip = True
                    break

        if skip:
            continue

        # Processa os arquivos
        for file in files:
            file_path = current_path_obj / file
            if file_path.suffix.lower() in extensions:
                image_paths.append((str(file_path), file_path.stem))

    return image_paths


def update_html_gallery(template_html_file, output_html_file, image_paths):
    """
    Atualiza o HTML com os links de imagem.

    Args:
        template_html_file: Caminho do arquivo HTML de template
        output_html_file: Caminho para salvar o novo arquivo HTML
        image_paths: Lista de tuplas (caminho_imagem, nome_alt)
    """
    # Lê e modifica o HTML
    with open(template_html_file, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')

    # Encontra a seção de galeria
    galeria_section = soup.select_one('#galeria')

    # Cria o novo container
    gallery_container = soup.new_tag('div')
    gallery_container['class'] = 'imagem-gallery'
    galeria_section.append(gallery_container)

    # Adiciona as imagens
    for img_src, img_alt in image_paths:
        img_tag = soup.new_tag('img')
        img_tag['src'] = img_src
        img_tag['alt'] = img_alt
        gallery_container.append(img_tag)

    # Salva o resultado
    with open(output_html_file, 'w', encoding='utf-8') as f:
        f.write(str(soup))


# Função principal que utiliza as duas funções separadas
def generate_image_gallery(root_directory, template_html_file, output_html_file, exclude_paths=None):
    """
    Gera uma galeria HTML com imagens encontradas em um diretório e suas subpastas.
    Todas as imagens são adicionadas em um container com classe 'imagem-gallery'.
    """
    # Encontra os caminhos de imagens
    image_paths = find_image_paths(root_directory, exclude_paths)

    # Atualiza o HTML
    update_html_gallery(template_html_file, output_html_file, image_paths)


if __name__ == "__main__":
    # Configurações
    root_dir = r"C:\Users\danil\OneDrive\Cofre Pessoal\MC\Fotos"
    template_html = r"C:\Users\danil\OneDrive\Cofre Pessoal\Visum\public\template.html"
    output_html = r"C:\Users\danil\OneDrive\Cofre Pessoal\Visum\public\template.html"
    exclude_paths = []

    # Executa a função
    generate_image_gallery(root_dir, template_html, output_html, exclude_paths)