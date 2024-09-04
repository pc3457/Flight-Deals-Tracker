# Flight-Deals-Tracker
This project is a comprehensive flight deal management system designed to automate the process of searching for and organizing flight data, helping users find the best available deals. It integrates various components to fetch, structure, and store flight information, making it easier for users to access and manage flight deals.

## Table of Contents

- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Modules](#modules)
- [Contributing](#contributing)
- [License](#license)

## Features

- **Automated Flight Searching:** Connects to the Amadeus API to find flights based on predefined criteria.
- **Structured Flight Data:** Organizes flight information into a consistent format for easy access and management.
- **Data Management:** Integrates with Google Sheets via the Sheety API to store and retrieve flight prices and user data.

## Installation

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/flight-deal-management.git
   cd flight-deal-management

Modules

1. **data_manager.py**
This module handles data management by interacting with external services like Google Sheets through the Sheety API. It is responsible for storing and retrieving user data and flight prices.

2. **flight_data.py**
Defines the FlightData class, which structures and organizes flight information. This ensures data such as prices, origin and destination airports, and travel dates are consistently formatted.

3. **flight_search.py**
This module connects to the Amadeus API to search for flights. It retrieves and filters flight information based on criteria such as destination, date, and budget.

Contributing

Contributions are welcome! Please submit a pull request or open an issue for any enhancements or bugs.

