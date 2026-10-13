verLetterbox = input("O Otávio está mexendo no Letterbox? (Sim / Não): ")
i = int(input("Escolha um número até 1000: "))
j = 0
Professor = input("Qual professor vai participar da conversa? (Nelci / Jonhson / Sonsino): ")

while j < i:
    if verLetterbox.lower() == "sim":
        print("\n",
              "-", Professor, ":"
              "\n"
              "Porra Hortelã, Vai Trabalhar")
    
    if verLetterbox.lower() == "não":
        print("\n",
              "-", Professor, ":"
              "\n"
              "Parabéns Hortelã, Estou Orgulhoso")
    j += 1

if verLetterbox.lower() == "não":
    print("\n"
          "O Otávio foi elogiado", i, "vezes!!!")

if verLetterbox.lower() == "sim":
    print("\n"
          "O Otávio foi xingado", i, "vezes!!!")
    
