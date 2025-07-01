from translate import Translator
import time
import json
import os
import argparse

def get_required_assets():
    with open("language_support.json", "r") as jfp:
        supported_langs = json.load(jfp)
        supported_langs_list = supported_langs.get('supported_langs')
        supported_langs_dict = supported_langs.get('supported_langs_dict')
    return supported_langs_list, supported_langs_dict

def check_args(file_path: os.PathLike, target_lang: str):
    absolute_path = os.path.abspath(file_path)
    _, ext = os.path.splitext(absolute_path)

    if not os.path.exists(absolute_path):
        raise FileNotFoundError(f"{absolute_path} cannot be find.")

    if not ext or ext != '.txt':
        raise ValueError("A non .txt file has been passed thus it cannot be treated.")

    supported_langs_list, supported_langs_dict = get_required_assets()
    if len(target_lang) != 2 or target_lang.lower() not in supported_langs_list:
        raise ValueError(f"Unsupported Lang {target_lang}")

    else:
        target_lang = target_lang.lower()
        return  absolute_path, target_lang, supported_langs_dict[target_lang]


def translate_file(file, target_language):
    file_path, target_lang, target_lang_full_name = check_args(file, target_language)

    with open(file_path, 'r') as text:
        lines = (line.rstrip() for line in text)

        # Extract the file name and extension
        base_name, ext = os.path.splitext(file_path)
        output_file = f"{base_name}_to_{target_lang}{ext}"

        with open(output_file, 'w') as translated_text:
            translator = Translator(to_lang=target_lang, from_lang='autodetect')
            translated_text.write(f"Translated text to {target_lang_full_name}:\n\n")
            t1 = time.perf_counter()
            for line in lines:
                translated_text.write(f"{translator.translate(line)}\n")
            t2 = time.perf_counter()

        print(f"Done within {t2 - t1:.4f}s")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="This is a basic Python program that helps its users in translating files from a language to another.")
    parser.add_argument('file', help="Get the file that the user wants to translate.")
    parser.add_argument('target_language', help='Specify the wanted language to translate to.')

    args = parser.parse_args()
    translate_file(args.file, args.target_language)