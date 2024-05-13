# Holiday Cost Calculator

This repository contains a Python script named `holiday.py` that calculates the total cost of a holiday based on the user's chosen destination, number of nights in a hotel, and car rental duration.

## Description

The `holiday.py` script provides an interactive way for users to calculate the total cost of their holiday by entering specific details about their trip:
- **Destination City**: Determines the flight cost.
- **Number of Nights**: Determines the hotel cost.
- **Car Rental Duration**: Determines the car rental cost.

The script uses four functions to calculate these costs:
- `hotel_cost(num_nights)`: Returns the hotel cost based on the number of nights.
- `plane_cost(city_flight)`: Returns the flight cost depending on the destination city.
- `car_rental(rental_days)`: Returns the total cost for renting a car for a specified number of days.
- `holiday_cost(num_nights, city_flight, rental_days)`: Calculates the total holiday cost by summing the outputs of the other three functions.

## Getting Started

### Prerequisites

Ensure you have Python 3.x installed on your machine. Python can be downloaded from the official site at [python.org](https://www.python.org/downloads/).

### Installation

1. Clone this repository to your local machine using Git:
   ```bash
   git clone https://github.com/dreamVaux/my_bootcamp_tasks.git
2. Navigate to the cloned directory

### Usage
To run the script, execute the following command in your terminal:
```bash
python holiday.py
```
or
```bash
python3 holiday.py
```
Follow the on-screen prompts to enter your travel details. The script will calculate and display the total cost of your holiday based on your inputs.

### Contributing

We welcome contributions to this project. If you have ideas for improving the script or adding new features, please fork the repository and submit a pull request with your proposed changes.

### License

This project is licensed under the MIT License - see the LICENSE file for details.