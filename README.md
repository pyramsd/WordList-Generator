# WordList-Generator

## Usage
```
usage: wordlist-generator.py [-h] [-o OUTPUT] [-start STARTWITH] [-lr LONGITUD] [-end ENDWITH] [--numbers [{even,odd,all}]] [--letters [{upper,lower,all}]] [--all] [--symbols]

Wordlists generator

options:
  -h, --help            show this help message and exit
  -o OUTPUT, --output OUTPUT
                        Output de archivo

Opciones de personalización:
  -start STARTWITH, --startwith STARTWITH
                        Inicio de cada cadena
  -lr LONGITUD, --length-range LONGITUD
                        Longitud de cadena
  -end ENDWITH, --endwith ENDWITH
                        Final de cada cadena
  --numbers [{even,odd,all}], -n [{even,odd,all}]
                        Cadena de números: 'even' para pares, 'odd' para impares, 'all' para todos (por defecto)
  --letters [{upper,lower,all}], -l [{upper,lower,all}]
                        Cadena de letras: 'upper' para mayúsculas, 'lower' para minúsculas, 'all' para todas (por defecto)
  --all                 Letras (mayus y minus), números y simbolos
  --symbols, -s         Solo simbolos
```