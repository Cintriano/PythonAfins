"""
        192.168.0.1
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

if __name__ == "__main__":
    ip_input = "128.168.1.1"

    ip_reader(ip_input)
