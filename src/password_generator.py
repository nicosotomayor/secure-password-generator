import random
import string
import argparse

def generar_contraseña(longitud=16, mayus=True, numeros=True, simbolos=True):
    caracteres = string.ascii_lowercase
    if mayus:
        caracteres += string.ascii_uppercase
    if numeros:
        caracteres += string.digits
    if simbolos:
        caracteres += string.punctuation

    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="🔐 Generador de Contraseñas Seguras")
    parser.add_argument("-l", "--longitud", type=int, default=16, help="Longitud de la contraseña (default: 16)")
    parser.add_argument("-nm", "--no-mayus", action="store_true", help="Excluir mayúsculas")
    parser.add_argument("-nn", "--no-numeros", action="store_true", help="Excluir números")
    parser.add_argument("-ns", "--no-simbolos", action="store_true", help="Excluir símbolos")

    args = parser.parse_args()

    password = generar_contraseña(
        longitud=args.longitud,
        mayus=not args.no_mayus,
        numeros=not args.no_numeros,
        simbolos=not args.no_simbolos
    )

    print(f"✅ Tu contraseña segura es: {password}")
