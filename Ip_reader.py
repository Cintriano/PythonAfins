import socket
import re

"""
    Ex: 192.168.0.1
    Classe A 1:126
    Classe B 128:191
    Classe C 192:223
"""

def ip_reader(ip):

    list_octetos = ip.split(".")
    try:
        if  0 < int(list_octetos[0]) < 127:
            classe = "A"
            new_ip = list_octetos[0] + "." + "255.255.255"
            useful_range_start = list_octetos[0] + "." + "0.0.1"
            useful_range_end = list_octetos[0] + "." + "255.255.254"
        elif 127 < int(list_octetos[0]) < 192:
            classe = "B"
            new_ip = list_octetos[0] + "." + list_octetos[1] + "." + "255.255"
            useful_range_start = list_octetos[0] + "." + list_octetos[1] + "." + "0.1"
            useful_range_end = list_octetos[0] + "." + list_octetos[1] + "." + "255.254"
        elif 190 < int(list_octetos[0]) < 224:
            classe = "C"
            new_ip = list_octetos[0] + "." + list_octetos[1] + "." + list_octetos[2] + ".255"
            useful_range_start = list_octetos[0] + "." + list_octetos[1] + "." + list_octetos[2] + ".1"
            useful_range_end = list_octetos[0] + "." + list_octetos[1] + "." + list_octetos[2] + ".254"
        elif int(list_octetos[0]) == 127:
            print(f"""
            ip: {ip}
            Classe: Loopback
            """)
            return
        else:
            print("Ip invalido")
            return

        print(f"""
        ip: {ip}
        Classe {classe}
        BroadCast: {new_ip}
        Useful range: Start ({useful_range_start}) -> End ({useful_range_end})
        """)
    except Exception as e:
        print("Erro: ", e)


def validar_ip(ip):
    padrao_ip = r"^([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})\.([0-9]{1,3})$"

    if re.match(padrao_ip, ip):
        octetos = ip.split('.')
        for octeto in octetos:
            if not 0 <= int(octeto) <= 255:
                return False
        return True
    else:
        return False

"""
    ID: 192.168.0.0
    Classe: A
    Mascara: 255.255.255.128
    CIDR: 25
    BroadCast: 192.168.0.127
    Conexoes: 128
    UsefullRage: 192.168.0.1  192.168.0.126
"""

def cidr_masc_end(busca, aux):
    dic = {24:0, 25:128, 26:192, 27:224, 28:240, 29:248, 30:252, 31:254, 32:255}
    if aux == "cidr":
        for key, value in dic.items():
            if value == busca:
                return key
    elif aux == "masc_end":
        for key,value in dic.items():
            if key == busca:
                return value
    else:
        return "valores invalidos"


# redes = [[2, 64], [1, 128]]
# div_redes = [["A", 0, 63],["B", 64, 127], ["C", 128, 255]]
def divisao(id_rede, redes, cidr):
    alph = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
    div_redes = []
    nome_idx = 0
    aux = 0
    if cidr == 24:
        for i in range(len(redes)):
            for j in range(redes[i][0]):
                inter_inicial = aux
                inter_final = aux + redes[i][1] - 1
                aux = inter_final + 1
                div_redes.append([alph[nome_idx], inter_inicial, inter_final])
                nome_idx += 1
        pos(id_rede, div_redes)
        return "\n==================== Finalizado ===================="
    else:
        return "Valores invalidos"


# div_redes = [["A", 0, 63],["B", 64, 127], ["C", 128, 255]]
def pos(id_rede, redes):
    octetos = id_rede.split(".")[0:3]
    octetos = ".".join(octetos) + "."
    for rede in redes:
        broadcast = octetos + str(rede[2])
        id_rede = octetos + str(rede[1])
        usefull_rage = octetos + str(rede[1]+1) +" -> "+ octetos + str(rede[2]-1)
        qt_conexoes = (rede[2] - rede[1]) + 1
        masc = "255.255.255." + str(256 - qt_conexoes)
        cidr = cidr_masc_end((256 - qt_conexoes), "cidr")
        print(
            f"""
        Rede: {rede[0]}
        Quantidade de Conexões: {qt_conexoes}
        ID-rede: {id_rede}
        Broadcast: {broadcast}
        Usefull range: {usefull_rage}
        Mascara: {masc}
        CIDR: {cidr}""")




if __name__ == "__main__":

    print(divisao("201.109.100.0",[[4, 16], [2, 32], [1, 128]], 24))

    '''ip_input = ""

    print("""
    0 - Ip da Maquina
    1 - Ip Personalizado
    """)

    op = input("Opção: ")

    if op == "0":
        hostname = socket.gethostname()
        ip_input = socket.gethostbyname(hostname)
        ip_reader(ip_input)
    elif op == "1":
        ip_input = input("Digite o IP: ")
        if validar_ip(ip_input):
            ip_reader(ip_input)
        else:
            print("IP invalido")
    else:
        print("Opção invalida")'''
