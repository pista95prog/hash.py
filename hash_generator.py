import os
import hashlib

def hash_words(input_file, output_md5_file, output_sha1_file):

    if not os.path.isfile(input_file):
        print(f"Error: El archivo '{input_file}' no existe.")
        return
    

    with open(input_file, 'r') as infile, \
         open(output_md5_file, 'w') as md5file, \
         open(output_sha1_file, 'w') as sha1file:
        

        for line in infile:
            word = line.strip()  
            
            # hash MD5
            hash_md5 = hashlib.md5(word.encode('utf-8')).hexdigest()
            # hash SHA-1
            hash_sha1 = hashlib.sha1(word.encode('utf-8')).hexdigest()
            
            
            md5file.write(f"{word} -> {hash_md5}\n")
            sha1file.write(f"{word} -> {hash_sha1}\n")
    
    print(f"Hashing completado. Archivos generados:\n- {output_md5_file}\n- {output_sha1_file}")

def main():
    
    input_file = "palabras.txt"  # Cambia esto por la ruta correcta si es necesario
    output_md5_file = "palabras_md5.txt"
    output_sha1_file = "palabras_sha1.txt"
    

    hash_words(input_file, output_md5_file, output_sha1_file)

if __name__ == "__main__": 
    main()
