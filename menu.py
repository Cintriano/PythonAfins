from music_meta_manager import remove_unknown, troca_artist, define_artist, preenche_titulo

opeacao = ""

while opeacao != "sair":
    print("1 - remover(unknow)\n2 - Trocar artistas\n3 - Adicionar artista\n4 - Preencher artista")

    opeacao = input(str("Operação: "))
    if opeacao == "sair":
        break

    pasta = input(str("Caminho da pasta"))
    if pasta == "sair":
        break

    if opeacao == "1":
        remove_unknown(pasta)
    elif opeacao == "2":
        troca_artist(pasta)
    elif opeacao == "3":
        artist = input(str("Artista: "))
        define_artist(pasta, artist)
    elif opeacao == "4":
        preenche_titulo(pasta)
    else:
        print("Operação invalida")
