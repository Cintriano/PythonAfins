import serial
import time
import tkinter as tk

def comando_arduino(sinal):
    arduino = serial.Serial('COM9', 9600)
    time.sleep(2)
    arduino.write(sinal.encode())  # Envia o comando para o Arduino
    resposta = arduino.readline().decode().strip()  # Lê a resposta do Arduino
    print(f"Arduino: {resposta}")
    arduino.close()


# Criar a janela principal
janela = tk.Tk()
janela.title("Comando do Portão")
janela.geometry("300x100")

# Criar um botão
botao = tk.Button(janela, text="Executar", command=lambda: comando_arduino(True))
botao.pack(pady=20)

janela.mainloop()
