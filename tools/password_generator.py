import random
import string

def gerar_senha(tamanho):
    caracteres = (
        string.ascii_letters +
        string.digits +
        string.punctuation
    )

    senha = ""

    for _ in range(tamanho):
        senha += random.choice(caracteres)

    return senha


def salvar_senha(senha):
    with open("tools/passwords.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(senha + "\n")


def main():
    print("=" * 40)
    print("PASSWORD GENERATOR")
    print("=" * 40)

    while True:

        tamanho = int(input("Tamanho da senha: "))

        senha = gerar_senha(tamanho)

        print(f"\nSenha gerada:\n{senha}\n")

        resposta = input("Usar esta senha? (S/N): ").strip().upper()

        if resposta == "S":
            salvar_senha(senha)
            print("\nSenha salva com sucesso!")
            break

        print("\nGerando outra senha...\n")


if __name__ == "__main__":
    main()