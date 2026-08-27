import os # Biblioteca para habilitar cmd's terminal
import sqlite3 # Banco de dados 

#  Variável com o nome do BD a ser criado
CAMINHO_BANCO = "jogos.db"

def exibir_cabecalho(texto):
    os.system("cls") # Limpa a tela do terminal

    # Cria um efeito visual na palavra "GameVault"
    linha = "*" *len(texto)
    print(linha)
    print(texto)
    print(linha)
    print() # Pula uma linha

exibir_cabecalho("GameVault - Catálogo de Jogos")

# Função para inicializar o banco de dados
def inicializar_banco():
    # Abre a conexão com o banco de dados (O indicado em: "CAMINHO_BANCO" no caso: "jogos.db")
    conn = sqlite3.connect(CAMINHO_BANCO) # Cria o arquivo do banco de dados se não existir

    # Diz ao BD que de fato SQL está habilitado
    cursor = conn.cursor() 

    # Executa de fato o comendo SQL descrit abaixo
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS jogos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL,
            plataforma TEXT NOT NULL,
            zerado BOOLEAN NOT NULL DEFAULT 0
        )
        """
    )

    # Função como "Ctrl + S" do VSCode, que salva as alterações no banco de dados
    conn.commit()
    # Fecha a conexão com o banco de dados
    conn.close()

# Chamando a função para inicializar o banco de dados
inicializar_banco()

def listar_jogos():
    # Abre a conexão com o banco de dados (O indicado em: "CAMINHO_BANCO" no caso: "jogos.db")
    conn = sqlite3.connect(CAMINHO_BANCO) # Cria o arquivo do banco de dados se não existir
    
    # Diz ao BD que de fato SQL está habilitado
    cursor = conn.cursor() 
    cursor.execute("SELECT titulo, plataforma, zerado FROM jogos")

    # "fetchall" - Devolve TODAS as lihas do resultado como uma tupla
    jogos = cursor.fetchall()

    conn.close()

    # Se BD vazio mostra a mensagem a baixo
    if not jogos:
        print("Nenhum jogo cadastrado ainda!\n")
        return

    # Formam o cabeçalho visual antes de listar com 55 traços e alinhamento a esquerda "ljust"
    print(f"{'Título'.ljust(25)} | {'Plataforma'.ljust(12)} | Status")
    print("-" * 55)

    # Laço para exibir todos os jogos cadastrados
    for titulo, plataforma, zerado in jogos:
        status = "zerado" if zerado else "jogando"
        print(f"{titulo.ljust(25)} | {plataforma.ljust(12)} | {status}")

    print() 

# Chamando a função
listar_jogos()

def adicionar_jogo(titulo, plataforma):
    conn = sqlite3.connect(CAMINHO_BANCO)
    cursor = conn.cursor()

    # SQL - Para inserir novos jogos
    cursor.execute("INSERT INTO jogos (titulo, plataforma, zerado) VALUES (?, ?, ?)", (titulo, plataforma, False),
    )

    conn.commit()
    conn.close()

def marcar_como_zerado(titulo):
    conn = sqlite3.connect(CAMINHO_BANCO)
    cursor = conn.cursor()
    
    # SQL - Para att satus de jogando para zerado
    cursor.execute("UPDATE jogos SET zerado = ? WHERE titulo = ?", (True, titulo),
    )

    # Guarda qnts linhas foram afetadas na atualiazação
    encontrou = cursor.rowcount > 0

    conn.commit()
    conn.close()
    return encontrou

def exibir_menu():
    exibir_cabecalho("🎮 GameVault")
    print("1. Adicionar jogo")
    print("2. Listar jogo")
    print("3. Marcar jogo como zerado")
    print("4. Sair\n")

def pausar():
    input("Pressione Enter para voltar ao menu...")

def main():
    inicializar_banco()

    while True:
        exibir_menu()
        opcao = input("Ecolha uma opção: ")

        if opcao == "1":
            exibir_cabecalho("Adicionar jogo")
            titulo = input("Título do Jogo: ")
            plataforma = input("Plataforma: ")
            adicionar_jogo(titulo, plataforma)
            print(f"\n'{titulo}' adicionado com sucesso!")
            pausar()

        elif opcao == "2":
            exibir_cabecalho("Seus jogos")
            listar_jogos()
            pausar()

        elif opcao == "3":
            exibir_cabecalho("Marcar como zerado")
            titulo = input("Título do jogo que zerou: ")

            if marcar_como_zerado(titulo):
                print(f"\n'{titulo}' marcado como zerado!")

            else:
                print("Confira se digitou corretamente.")
                print()

        elif opcao == "4":
            print("Até a próxima! 💕")
            break 

        # Caso o usuário digite ua opção inválida. exemplo: 9 (não existe)
        else:
            print("Opção inválida! Escolha um número de 1 a 4.")
            pausar()

if __name__ == "__main__":
    main()