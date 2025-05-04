def calcular_tempos_velocidades():
    """
    Calcula o tempo necessário para assistir um vídeo em múltiplas velocidades pré-definidas,
    mostrando tempo necessário, diferença absoluta e porcentagem de economia.
    """
    print("Calculadora de Tempo de Visualização em Diferentes Velocidades")
    print("-----------------------------------------------------------")

    try:
        # Obter a duração original do vídeo
        duracao_str = input("Digite a duração do vídeo (formato HH:MM:SS ou MM:SS): ")

        # Converter a string de duração para segundos
        partes = duracao_str.split(':')
        if len(partes) == 3:  # Formato HH:MM:SS
            horas = int(partes[0])
            minutos = int(partes[1])
            segundos = int(partes[2])
        elif len(partes) == 2:  # Formato MM:SS
            horas = 0
            minutos = int(partes[0])
            segundos = int(partes[1])
        else:
            raise ValueError("Formato de tempo inválido.")

        duracao_total_segundos = horas * 3600 + minutos * 60 + segundos

        # Velocidades pré-definidas
        velocidades = [1.25, 1.5, 1.75, 2.0]

        # Exibir cabeçalho
        print(f"\nTempo original do vídeo: {horas:02d}:{minutos:02d}:{segundos:02d}\n")
        print("Velocidade | Tempo Necessário | Diferença    | Economia")
        print("---------- | ---------------- | ------------ | --------")

        for velocidade in velocidades:
            # Calcular o tempo necessário
            tempo_necessario_segundos = duracao_total_segundos / velocidade

            # Converter para HH:MM:SS
            horas_final = int(tempo_necessario_segundos // 3600)
            minutos_final = int((tempo_necessario_segundos % 3600) // 60)
            segundos_final = int((tempo_necessario_segundos % 3600) % 60)

            # Calcular diferença absoluta
            diferenca_segundos = duracao_total_segundos - tempo_necessario_segundos
            horas_diff = int(diferenca_segundos // 3600)
            minutos_diff = int((diferenca_segundos % 3600) // 60)
            segundos_diff = int((diferenca_segundos % 3600) % 60)

            # Calcular porcentagem de economia
            if velocidade > 1.0:
                economia_percent = (1 - (1 / velocidade)) * 100
            else:
                economia_percent = 0.0

            # Exibir resultados formatados
            print(f"{velocidade:4.2f}x    | {horas_final:02d}:{minutos_final:02d}:{segundos_final:02d} | "
                  f"{horas_diff:02d}:{minutos_diff:02d}:{segundos_diff:02d} | "
                  f"{economia_percent:5.1f}%")

    except ValueError as e:
        print(f"Erro: {e}. Por favor, insira valores válidos.")


if __name__ == "__main__":
    calcular_tempos_velocidades()