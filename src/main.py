#Exercise: Translator
from translate import Translator
import time
from resources import *
import os
import argparse

parser = argparse.ArgumentParser(description="This is a basic Python program that helps its users in translating files from a language to another.")
parser.add_argument('file',help="Get the file that the user wants to translate.")
parser.add_argument('target_language',help='Specify the wanted language to translate to.')

args = parser.parse_args()
try:
    if len(args.target_language) != 2 or args.target_language.lower() not in supported_langs:
        print("Invalid option")
        exit()
    else:
       with open(args.file,'r') as text:
        lines = (line.rstrip() for line in text)

        # Extract the file name and extension
        base_name, ext = os.path.splitext(args.file)
        output_file = f"{base_name}_to_{args.target_language}{ext}"

        with open(output_file,'a') as translated_text:
            translang = Translator(to_lang=args.target_language)
            translated_text.write(f"Translated text to {supported_langs_dict[args.target_language.lower()]}:\n\n")
            t1 = time.perf_counter()
            for line in lines:
                translated_text.write(f"{translang.translate(line)}\n")
            t2 = time.perf_counter()

        print(f"Done within {t2-t1:.4f}s")
except FileNotFoundError:
    print("File not found, check its presence in the current dir or give the full path")
