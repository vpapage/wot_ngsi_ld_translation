from argparse import ArgumentParser
from translation_controller import TranslationController


# Parse the input file-path
parser = ArgumentParser()
parser.add_argument('-f', '--file_path', action='store', type=str, default=None)  
args = parser.parse_args()
FILE_PATH = args.file_path

if FILE_PATH is None:
    FILE_PATH = "data/ngsild-building.jsonld"
    
  
ngsild = TranslationController("NGSI-LD", FILE_PATH)
ngsild.generate_wot_td(
    folder_path="data/results/", 
    ip="PLACEHOLDER_IP"
)
