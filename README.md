# Hash Generator

Este proyecto contiene un script en Python que genera los hashes MD5 y SHA-1 de las palabras contenidas en un archivo de texto. Los resultados se almacenan en archivos separados para cada tipo de hash.

## Descripción

El script lee un archivo de texto de entrada, donde cada línea contiene una palabra o frase. Luego, calcula el hash MD5 y SHA-1 de cada palabra y guarda estos valores en archivos de salida separados.

## Archivos generados

El script produce dos archivos de salida:
- `palabras_md5.txt`: Contiene las palabras y sus respectivos hashes MD5.
- `palabras_sha1.txt`: Contiene las palabras y sus respectivos hashes SHA-1.

## Uso

### Requisitos previos

Asegúrate de tener instalado Python 3 en tu sistema.

### Ejecución

1. Coloca el archivo de entrada `palabras.txt` en el mismo directorio que el script.
2. Ejecuta el script utilizando Python:

   ```bash
   python3 hash_generator.py
Nota: Asegúrate de que el archivo de entrada exista y esté correctamente ubicado.

Una vez ejecutado el script, se generarán dos archivos de salida en el mismo directorio:
palabras_md5.txt
palabras_sha1.txt
Personalización
Si deseas cambiar el nombre del archivo de entrada o los nombres de los archivos de salida, puedes editar las siguientes líneas en el script:


input_file = "palabras.txt"  # Cambia esto por la ruta correcta si es necesario
output_md5_file = "palabras_md5.txt"
output_sha1_file = "palabras_sha1.txt"
Ejemplo
Si el archivo palabras.txt contiene lo siguiente:

hello
world
El script generará dos archivos de salida con el siguiente contenido:

palabras_md5.txt


hello -> 5d41402abc4b2a76b9719d911017c592
world -> 7d793037a0760186574b0282f2f435e7
palabras_sha1.txt


hello -> aaf4c61ddcc5e8a2dabede0f3b482cd9aea9434d
world -> 7c211433f02071597741e6ff5a8ea34789abbf43

Contribuciones
Las contribuciones son bienvenidas. Siéntete libre de abrir un issue o hacer un pull request.

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
# Hash Generator

This project contains a Python script that generates MD5 and SHA-1 hashes for words contained in a text file. The results are stored in separate files for each type of hash.

## Description

The script reads an input text file, where each line contains a word or phrase. It then calculates the MD5 and SHA-1 hash for each word and saves these values in separate output files.

## Generated Files

The script produces two output files:
- `palabras_md5.txt`: Contains the words and their corresponding MD5 hashes.
- `palabras_sha1.txt`: Contains the words and their corresponding SHA-1 hashes.

## Usage

### Prerequisites

Make sure you have Python 3 installed on your system.

### Execution

1. Place the input file `palabras.txt` in the same directory as the script.
2. Run the script using Python:

   ```bash
   python3 hash_generator.py
