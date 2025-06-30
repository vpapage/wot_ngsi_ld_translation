assumption_about_the_available_measurement_units = {
    # Physical Quantities
    "Temperature": ['celsius', 'fahrenheit', 'kelvin'],
    "Distance": ['meters', 'kilometers'],
    "Weight-Mass": ['grams', 'kilograms', 'pounds'],
    "Volume": ['liters', 'milliliters', 'cubic meters'],
    "Speed": ['meters per second', 'kilometers per hour', 'miles per hour'],
    "Pressure": ['pascals', 'bar', 'atmospheres'],
    "Energy": ['joules','calories'],
    # Electrical Quantities
    "Power": ['watts', 'kilowatts'],
    # Time
    "Time": ['seconds', 'minutes', 'hours', 'days'],
}


def find_unit(unitCode):
    """ A Mapping from NGSI-LD to WoT unit measurements. """

    units = {
        # Temperature
        "CEL": "celsius",
        "FAH": "fahrenheit",
        "K": "kelvin",

        # Length/Distance
        "m": "meters",
        "km": "kilometers",

        # Mass/Weight
        "kg": "kilograms",
        "g": "grams",
        "lb": "pounds",

        # Volume
        "l": "liters",
        "L": "liters",
        "ml": "milliliters",
        "mL": "milliliters",
        "m3": "cubic meters",

        # Time
        "s": "seconds",
        "min": "minutes",
        "h": "hours",
        "d": "days",

        # Pressure
        "Pa": "pascals",
        "bar": "bar",
        "atm": "atmospheres",

        # Speed 
        "m/s": "meters per second",
        "km/h": "kilometers per hour",
        "mph": "miles per hour",

        # Energy
        "J": "joules",
        "cal": "calories",

        # Power
        "W": "Watts",
        "kW": "kilowatts",

    }

    return units.get(unitCode)


def find_unitCode(units):
    """ A Mapping from WoT to NGSI-LD unit measurements. """
    
    unitCode = {
        # Temperature
        "celsius": "CEL",
        "fahrenheit": "FAH",
        "kelvin": "K",

        # Length/Distance
        "meters": "m",
        "kilometers": "km",

        # Mass/Weight
        "kilograms": "kg",
        "grams": "g",
        "pounds": "lb",

        # Volume
        "liters": "l",
        "liters": "L",
        "milliliters": "ml",
        "milliliters": "mL",
        "cubic meters": "m3",

        # Time
        "seconds": "s",
        "minutes": "min",
        "hours": "h",
        "days": "d",

        # Pressure
        "pascals": "Pa",
        "bar": "bar",
        "atmospheres": "atm",

        # Speed 
        "meters per second": "m/s",
        "kilometers per hour": "km/h",
        "miles per hour": "mph",

        # Energy
        "joules": "J",
        "calories": "cal",

        # Power
        "Watts": "W",
        "kilowatts": "kW",

    }

    return unitCode.get(units)
