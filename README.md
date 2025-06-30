# IoT Semantic Translator
The IoTSemanticTranslator is a Python-based tool designed for semantic translation between the Web of Things (WoT) and NGSI-LD data models.

## Description
This repository contains a translation utility that bridges semantic differences between WoT and NGSI-LD IoT models. It enables the conversion of configuration files, supporting interoperability across IoT platforms.

The project follows a **Model-View-Controller (MVC)** architecture for clean separation of concerns and improved extensibility.

### Repository Structure

- `semantic_translation/`: Contains the core translation classes `TranslateNGSILDtoWoT` and `TranslateWoTtoNGSILD`
- `run_translation_wot_to_ngsild.py`: Performs translation from WoT to NGSI-LD
- `run_translation_ngsild_to_wot.py`: Performs translation from NGSI-LD to WoT
- `TranslationController`: Handles input/output and calls the relevant translation logic

## Using the Translator
The tool provides two translation directions:
- **WoT → NGSI-LD**
- **NGSI-LD → WoT**

To use it, pass the model type (`"WoT"` or `"NGSI-LD"`) and the path to the source configuration file to the controller. The output is a translated file in either JSON-LD or WoT Thing Description format.

### Quick Guide

You can use the provided scripts or import the logic into your own code.

#### Example with provided scripts:
```bash
python run_translation_wot_to_ngsild.py -f path/to/wot-config.json
python run_translation_ngsild_to_wot.py -f path/to/ngsild-config.json
```

#### Example in Python:
```python
from semantic_translation.translation_controller import TranslationController

controller = TranslationController("WoT", "examples/input/wot-example.json")
controller.generate_ngsild_entity("examples/results/")
```

### Output
- NGSI-LD Entity: `ngsild-entity.jsonld`
- NGSI-LD Data Model: `ngsild-data-model.yaml`
- WoT TD: `wot-thing-description.json`

## Restrictions and Assumptions
The design of the IoT Model Translator is based on specific considerations to manage complexity and ensure efficient translation between WoT and NGSI-LD configurations. Here are the key restrictions and assumptions:

### Supported Data Types
The translation process supports the following data types for configuration items:
- Number
- String/Text
- Boolean
- Arrays

This approach is adopted to avoid adding excessive complexity to the solution, focusing on the essential elements that represent most IoT device configurations and leaving aside the object structure that could display an unsightly diversity in configuration files.

### Focus Areas
The tool specifically targets the mapping of properties and actions between the two models. It manages configuration files containing such information, intending to extend support to more elaborate devices in the future.

### Measurement Units
The translator recognizes and manages the following list of measurement units, which are commonly used across various physical and electrical quantities in IoT configurations:

```plaintext
Physical Quantities:
- Temperature: celsius, fahrenheit, kelvin
- Distance: meters, kilometers
- Weight-Mass: grams, kilograms, pounds
- Volume: liters, milliliters, cubic meters
- Speed: meters per second, kilometers per hour, miles per hour
- Pressure: pascals, bar, atmospheres
- Energy: joules, calories

Electrical Quantities:
- Power: watts, kilowatts

Time:
- Time: seconds, minutes, hours, days
```

This managed list of measurement units ensures that the translator can handle a broad range of IoT device configurations without compromising on the accuracy of the physical representations in both models.

## Notes

Please ensure that your configuration files adhere to the supported formats and limitations mentioned above to guarantee successful translation.
Some fields may include PLACEHOLDER values which must be customized manually after translation.
