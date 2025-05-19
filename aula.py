from decimal import Decimal, getcontext

# Definindo a precisão (opcional)
getcontext().prec = 10

largura_fret = Decimal(input("Largura da frente: "))
largura_traz = Decimal(input("Largura de traz: "))
comprimento_esq = Decimal(input("Comprimento da esquerda: "))
comprimento_dir = Decimal(input("Comprimento da direita: "))

result = largura_traz * comprimento_esq

print(f"\n======================\n"
      f"Largura da frente: {largura_fret}\n"
      f"Largura do fundo do lote: {largura_traz}\n"
      f"Comprimento do lado Direito: {comprimento_dir}\n"
      f"Comprimento do lado Esquerdo: {comprimento_esq}\n"
      f"Area total do lote: {result}")