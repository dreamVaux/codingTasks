# This program will calculate a user’s total holiday cost,
# which includes the plane cost, hotel cost, and car-rental cost.

# Ask the user which city they will be flying to.
city_flight = input("Which city will you be flying to?(Tokyo/New York/London)")
while city_flight not in ["Tokyo", "New York", "London"]:
    print("Enter your answer again.")
    city_flight = input(
        "Which city will you be flying to?(Tokyo/New York/London)"
        )


# Ask the user the number of nights they will be staying at a hotel.
while True:
    try:
        num_nights = int(input(
            "How many nights will you be staying at a hotel?(enter a number)"
            ))
        if num_nights < 0:
            print("Enter a positive integer.")
            continue
        break
    except ValueError:
        print("That's not a valid number. Please enter a valid integer number.")


# Ask the user the number of days for which they will be hiring a car.
while True:
    try:
        rental_days = int(input(
            "How many days will you be hiring a car?(enter a number)"
            ))
        if rental_days < 0:
            print("Enter a positive integer.")
            continue
        break
    except ValueError:
        print("That's not a valid number. Please enter a valid integer number.")


# Define function to calculate the flight cost.
def plane_cost():
    """
    This function will take city_flight as an argument and return a cost for
    the flight.
    """
    if city_flight == "Tokyo":
        planeCost = 590
    elif city_flight == "New York":
        planeCost = 710
    elif city_flight == "London":
        planeCost = 650
    return planeCost


# Define function to calculate the hotel cost.
def hotel_cost():
    """
    This function will take num_nights as an argument, and return a total cost
    for the hotel stay.
    """
    global hotelCostPerNight
    if city_flight == "Tokyo":
        hotelCostPerNight = 600
    elif city_flight == "New York":
        hotelCostPerNight = 520
    elif city_flight == "London":
        hotelCostPerNight = 680
    hotelCost = num_nights * hotelCostPerNight
    return hotelCost


# Define function to calculate the car rental.
def car_rental():
    """
    This function will take rental_days as an argument and return the
    total cost of the car rental.
    """
    global rentalPerDay
    if city_flight == "Tokyo":
        rentalPerDay = 200
    elif city_flight == "New York":
        rentalPerDay = 300
    elif city_flight == "London":
        rentalPerDay = 320
    carRental = rental_days * rentalPerDay
    return carRental


# Define function to calculate the total holiday cost.
def holiday_cost():
    """
    This function takes three arguments: num_nights, city_flight, 
    and rental_days. Using these three arguments, 
    call the hotel_cost(), plane_cost(), and car_rental() functions with their
    respective arguments, and finally return the total cost for the holiday.
    """
    holidayCost = hotel_cost() + plane_cost() + car_rental()
    return holidayCost


# Call these functions in advence to make hotelCostPerNight
# and rentalPerDay global.
hotel_cost()
car_rental()


# Show the user the flight cost.
print(
    f"Your destination is {city_flight}. Your flight cost is ${plane_cost()}."
    )

# Show the user the hotel cost.
print(
    f"Your hotel cost is {num_nights} * ${hotelCostPerNight} = ${hotel_cost()}."
    )

# Show the user the car rental.
print(f"Your car rental is {rental_days} * ${rentalPerDay} = ${car_rental()}.")

# Show the user the total holiday cost.
print(f"Overall, your holiday cost is = ${holiday_cost()}")
