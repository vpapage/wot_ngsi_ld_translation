from argparse import ArgumentParser
from translation_controller import TranslationController


# Parse the input file_path
parser = ArgumentParser()
parser.add_argument('-f', '--file_path', action='store', type=str, default="")  
args = parser.parse_args()
FILE_PATH = args.file_path

if FILE_PATH=="":
    FILE_PATH = "data/wot-coffee-machine.td.json"
    
  

from_wot = TranslationController("WoT", FILE_PATH)
from_wot.generate_ngsild_entity(
    folder_path="data/results/", 
    context_file_destination="PLACEHOLDER_CONTEXT_FILE_DESTINATION"   # in this example we have already saved a context file
)
