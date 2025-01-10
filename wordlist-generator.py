from tqdm import tqdm
import itertools
import argparse
import string
import sys

lettersMinus = string.ascii_lowercase
lettersMayus = string.ascii_uppercase
numbers = string.digits
symbols = string.punctuation

def main():
    parser = argparse.ArgumentParser(description="Wordlists generator")
    parser.add_argument("-o", "--output", type=str, help="Output de archivo")

    custom_options = parser.add_argument_group("Opciones de personalización")
    custom_options.add_argument("-start", "--startwith", help="Inicio de cada cadena")
    custom_options.add_argument("-lr", "--length-range", type=int, dest="longitud", help="Longitud de cadena")
    custom_options.add_argument("-end", "--endwith", help="Final de cada cadena")

    custom_options.add_argument("--numbers", "-n", choices=["even", "odd", "all"], nargs='?', const="all", 
                                help="Cadena de números: 'even' para pares, 'odd' para impares, 'all' para todos (por defecto)")
    custom_options.add_argument("--letters", "-l", choices=["upper", "lower", "all"], nargs='?', const="all",
                                help="Cadena de letras: 'upper' para mayúsculas, 'lower' para minúsculas, 'all' para todas (por defecto)")
    
    custom_options.add_argument("--all", action="store_true", help="Letras (mayus y minus), números y simbolos")
    custom_options.add_argument("--symbols", "-s", action="store_true", help="Solo simbolos")

    if len(sys.argv) <= 1:
        parser.print_help()
        exit(0)

    args = parser.parse_args()

    if args.longitud is None or args.longitud <= 0:
        print("Debe especificar una longitud válida mayor que 0.")
        exit(1)

    caracteres = ""

    if args.all:
        caracteres = lettersMayus + lettersMinus + numbers + symbols
    else:
        if args.letters:
            if args.letters == "upper":
                caracteres += lettersMayus
            elif args.letters == "lower":
                caracteres += lettersMinus
            else:
                caracteres += lettersMayus + lettersMinus
        if args.numbers:
            caracteres += numbers
        if args.symbols:
            caracteres += symbols

    if not caracteres:
        caracteres = lettersMayus + lettersMinus + numbers + symbols

    combinations = itertools.product(caracteres, repeat=args.longitud)

    total_combinations = len(caracteres) ** args.longitud
    cadena_length = (len(args.startwith or '') + len(args.endwith or '') + args.longitud)
    total_size = total_combinations * cadena_length

    def tiene_simbolo(cadena):
        return any(char in symbols for char in cadena)

    if args.output:
        with open(args.output, 'w') as f:
            with tqdm(total=total_size, unit_scale=True, unit_divisor=1024, unit="B", desc="Proceso de guardado") as pbar:
                for combo in combinations:
                    cadena = f"{args.startwith or ''}{''.join(combo)}{args.endwith or ''}"

                    numeros_en_combo = ''.join([c for c in combo if c.isdigit()])
                    if numeros_en_combo:
                        es_par = int(numeros_en_combo) % 2 == 0
                    else:
                        es_par = False
                    
                    if args.numbers == "even":
                        if es_par and tiene_simbolo(cadena):
                            f.write(cadena + "\n")
                        elif es_par:
                            f.write(cadena + "\n")
                    elif args.numbers == "odd":
                        if not es_par:
                            f.write(cadena + "\n")
                    else:
                        f.write(cadena + "\n")
                    pbar.update(cadena_length)
    else:
        for combo in combinations:
            cadena = f"{args.startwith or ''}{''.join(combo)}{args.endwith or ''}"
            print(cadena)

if __name__ == "__main__":
    main()
