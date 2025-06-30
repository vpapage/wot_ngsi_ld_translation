import json
import yaml
import logging
from semantic_translation.translate_ngsild_to_wot import TranslateNGSILDtoWoT
from semantic_translation.translate_wot_to_ngsild import TranslateWoTtoNGSILD


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class TranslationController():
    """
    This is a translation class which connects semantically the configuration files between the models WoT (Web of Things) and NGSI-LD.
    """
    
    def __init__(self, source_model, config_file_path):
        """ Initialize the IoT translation by loading source_model data from a JSON configuration file. 

        Parameters:
        - source_model (str): The source model type, either "WoT" or "NGSI-LD", indicating the format of the configuration file.
        - config_file_path (str): Path to the JSON configuration file that contains the source model data.
        """
        self.source_model = source_model
        self.source_data = self.read_json_file(config_file_path)
        if source_model!="WoT" and source_model!="NGSI-LD":
            raise Exception(f"The model {source_model} is not supported. Please try one of the following: WoT, NGSI-LD")
        logging.info(f"Process was started.")

    def generate_ngsild_entity(self, folder_path="", context_file_destination="PLACEHOLDER_CONTEXT_FILE_DESTINATION"):
        """ Translate the source_model data to the target_model format and save it to a specified folder. 

        Parameters:
        - folder_path (str): The folder path where the translated JSON data should be saved.
        """
        
        if self.source_model!="WoT": 
            raise Exception(f"Wrong Function. Only source_model=WoT here!")
        
        wot = TranslateWoTtoNGSILD(self.source_data)
        target_data_data_model = wot.translate_to_ngsild_data_model()
        self.write_yaml_file(target_data_data_model, f"{folder_path}ngsild-data-model.yaml")
        
        target_data = wot.translate_to_ngsild(context_file_destination)
        self.write_json_file(target_data, f"{folder_path}ngsild-entity.jsonld")
        
    def generate_wot_td(self, folder_path="", ip="PLACEHOLDER_IP"):
        """ Translate the source_model data to the target_model format and save it to a specified folder. 

        Parameters:
        - folder_path (str): The folder path where the translated JSON data should be saved.
        """  
        if self.source_model!="NGSI-LD": 
            raise Exception(f"Wrong Function. Only source_model=NGSI-LD here!")

        ngsild = TranslateNGSILDtoWoT(self.source_data)
        target_data = ngsild.translate_to_wot(ip)
        self.write_json_file(target_data, f"{folder_path}wot.td.json")

    #  ---------------------------- READ/WRITE FUNCTIONS ---------------------------- 

    def read_json_file(self, file_path):
        """ Reads a JSON file from a given file path and returns the data as a dictionary. """
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return json.load(file)
        except json.JSONDecodeError as e:
            raise Exception(f"Error decoding JSON: {e}")

    def write_json_file(self, data, file_path="configuration.jsonld"):
        """ Writes a dictionary to a JSON file at the specified file path. """
        try:
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(data, file, ensure_ascii=False, indent=4)
        except Exception as e:
            raise Exception(f"An error occurred while writing to the file: {e}")
        logging.info(f"Configuration created successfully: {file_path}")
        if file_path=="configuration.jsonld":
            logging.info("It is recommended to change the file name to something more model specific, eg. ngsi-entity.jsonld or wot-thing-description.td.jsonld")


    def read_yaml_file(self, file_path):
        """ Reads a YAML file from a given file path and returns the data as a dictionary. """
        try:
            with open(file_path, 'r') as file:
                return yaml.safe_load(file)   
        except json.JSONDecodeError as e:
            raise Exception(f"Error decoding JSON: {e}")

    def write_yaml_file(self, data, file_path="data-model.yaml"):
        """ Writes a given list of dictionaries to a YAML file at the specified file path. """
        target_yaml = yaml.dump(data, sort_keys=False)
        try:
            with open(file_path, 'w') as file:
                file.write(target_yaml)        
        except Exception as e:
            raise Exception(f"An error occurred while writing to the file: {e}")
        logging.info(f"Data Model created successfully: {file_path}")
        if file_path=="data-model.yaml":
            logging.info("It is recommended to change the file name to something more specific.")
