import deepl
import json
import re
import sys
from collections import OrderedDict
from os import listdir
from os.path import join
from tqdm import tqdm

def synchroniseAndTranslate(*, inputDir, authKey):
    # Get all the files in the input directory
    files = [f for f in listdir(inputDir) if f.endswith(".json")]
    defaultFile = [f for f in files if not '_' in f][0]
    
    allTerms = []
    fields = {}
    for file in files:
        with open(join(inputDir, file), 'r') as f:
            # Read JSON file into fields[file]
            fields[file] = json.load(f)
            for key in fields[file].keys():
                if not key in allTerms:
                    allTerms.append(key)
    allTerms = sorted(list(allTerms))

    # Set missing language keys to False
    for file in fields.keys():
        for term in allTerms:
            if term not in fields[file]:
                fields[file][term] = False

    # Write language files, automatically translating out missing fields
    translator = deepl.Translator(authKey)
    for file in fields:
        if file != defaultFile:
            print('Translating {}'.format(file))
            try:
                lang = re.findall(r'_(.*)\.json', file)[0].upper()
                if lang == 'EN':
                    lang = 'EN-GB'
            except:
                lang = False
            for term in tqdm(allTerms):
                if not fields[file][term]:
                    if lang:
                        try:
                            translation = translator.translate_text(fields[defaultFile][term], target_lang=lang, source_lang='EN')
                        except Exception as e:
                            print(e)
                            translation = False
                        fields[file][term] = str(translation)
            with open(join(inputDir, file), 'w', encoding='utf8') as f:
                json.dump(fields[file], f, indent=2, ensure_ascii=False, sort_keys=True)


if __name__ == "__main__":
    options = {}

    for i, arg in enumerate(sys.argv[1:]):
        if arg.startswith("--"):
            if not sys.argv[i + 2].startswith("--"):
                options[arg[2:]] = sys.argv[i + 2]
            else:
                print("Malformed arguments")
                sys.exit(1)

    if not 'deeplKey' in options:
        print("A Deepl API Auth Key needs to be provided via the --deeplKey option")
        sys.exit(1)

    if not 'inputDir' in options:
        print("An input directory needs to be provided via the --inputDir option")
        sys.exit(1)

    synchroniseAndTranslate(inputDir=options['inputDir'], authKey=options['deeplKey'])