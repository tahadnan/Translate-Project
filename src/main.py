#Exercise: Translator
from translate import Translator
from sys import argv
import time
from resources import *
import os
src = argv[1]
lang = argv[2].lower()

try:
    if len(lang) != 2 or lang not in supported_langs:
        print("Invalid option")
        exit()
    else:
       with open(src,'r') as text:
        lines = (line.rstrip() for line in text)

        # Extract the file name and extension
        base_name, ext = os.path.splitext(src)
        output_file = f"{base_name}_to_{lang}{ext}"

        with open(output_file,'a') as ttext:
            translang = Translator(to_lang=lang)
            ttext.write(f"\nTranslated text to {supported_langs_dict[lang]}:\n\n")
            t1 = time.perf_counter()
            for line in lines:
                ttext.write(f"{translang.translate(line)}\n")
            t2 = time.perf_counter()

        print(f"Done within {t2-t1:.4f}s")
except FileNotFoundError:
    print("File not found, check its presence in the current dir or give the full path")
