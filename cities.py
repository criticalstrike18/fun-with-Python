import json

# Paths to the JSON files in the cloned repository
COUNTRIES_FILE = "countries.json"
STATES_FILE = "states.json"
CITIES_FILE = "cities.json"

# India country code
INDIA_CODE = "IN"


def load_json(file_path):
    """Loads JSON data from a given file."""
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def get_indian_states(states_data):
    """Filter and return states that belong to India."""
    return [state for state in states_data if state['country_code'] == INDIA_CODE]


def get_cities_by_state(cities_data, state_id):
    """Return cities that belong to a given state ID."""
    return [city['name'] for city in cities_data if city['state_id'] == state_id]


def organize_indian_cities():
    """Organize cities by states in India."""
    # Load the countries, states, and cities data
    countries = load_json(COUNTRIES_FILE)
    states = load_json(STATES_FILE)
    cities = load_json(CITIES_FILE)

    # Filter states for India
    indian_states = get_indian_states(states)

    # Dictionary to hold cities by state
    india_cities_by_state = {}

    # For each state in India, get the corresponding cities
    for state in indian_states:
        state_name = state['name']
        state_id = state['id']

        # Get all cities for the current state
        state_cities = get_cities_by_state(cities, state_id)
        india_cities_by_state[state_name] = state_cities

    return india_cities_by_state


def save_to_json(data, filename):
    """Saves the organized data to a JSON file."""
    with open(filename, 'w', encoding='utf-8') as json_file:
        json.dump(data, json_file, indent=4)
    print(f"Data saved to {filename}")


if __name__ == "__main__":
    # Organize cities by state
    indian_cities = organize_indian_cities()

    # Save the result to a JSON file
    save_to_json(indian_cities, "indian_cities_by_state.json")
