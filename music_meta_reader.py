import os
import mutagen
from mutagen.id3 import ID3

#TPE2 Artista do album
#TPE1 Artistas participantes
#<unknown>

def troca_artist(pasta):
    for arquivo in os.listdir(pasta):
        if arquivo.endswith(".mp3"):
            caminho_arquivo = os.path.join(pasta, arquivo)
            music = mutagen.File(caminho_arquivo)
            if valida_artist(caminho_arquivo):
                for tag_id, value in music.items():
                    if tag_id == "TPE1":
                        artista_part = str(value)
                        music.tags.add(mutagen.id3.TPE2(encoding=3, text=artista_part))
                        music.tags.add(mutagen.id3.TPE1(encoding=3, text=""))
                        music.save()

def define_artist(pasta, artist):
    for arquivo in os.listdir(pasta):
        if arquivo.endswith(".mp3"):
            caminho_arquivo = os.path.join(pasta, arquivo)
            music = mutagen.File(caminho_arquivo)
            music.tags.add(mutagen.id3.TPE2(encoding=3, text=artist))
            music.save()

def preenche_titulo(pasta):
    for arquivo in os.listdir(pasta):
        if arquivo.endswith(".mp3"):
            caminho_arquivo = os.path.join(pasta, arquivo)
            music = mutagen.File(caminho_arquivo)
            nome = arquivo.replace(".mp3", "")
            music.tags.add(mutagen.id3.TIT2(encoding=3, text=nome))
            music.save()

def remove_unknown(pasta):
    for arquivo in os.listdir(pasta):
        if arquivo.endswith(".mp3"):
            caminho_arquivo = os.path.join(pasta, arquivo)
            music = mutagen.File(caminho_arquivo)
            tags_a_remover = []
            for tag_id, value in music.items():
                if value == "<unknown>" or value == "Artista Desconhecido":
                    tags_a_remover.append(tag_id)
            for tag_id in tags_a_remover:
                del music.tags[tag_id]
            music.save()

def valida_artist(caminho_arquivo):
    try:
        artist = False
        music = mutagen.File(caminho_arquivo)
        for tag_id, value in music.items():
            if tag_id == "TPE1":
                artist = True
        if artist:
            return True
        return False
    except Exception as e:
        print("Erro Função(valida_artist): ", e)


caminho = r"C:\Users\danil\OneDrive\Audios\Music\X-Geladeira\Rock"
troca_artist(caminho)
remove_unknown(caminho)
preenche_titulo(caminho)
#define_artist(caminho, "Dario Marianelli")
