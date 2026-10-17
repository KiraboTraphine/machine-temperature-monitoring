def classify_temperature(temperature):
    if temperature < 40:
        return "Normal"
    elif temperature < 70:
        return "Warning"
    else:
        return "Critical"


def process_readings():
    readings = []

    try:
        count = int(input("Number of temperature readings: "))
    except ValueError:
        print("Number of readings must be numeric")
        return

    if count <= 0:
        print("Number of readings must be greater than zero")
        return

    for i in range(count):

        print("\nReading", i + 1)

        reading_number = input("Reading number: ")

        try:
            temperature = float(input("Temperature (°C): "))
        except ValueError:
            print("Temperature must be numeric")
            continue

        if temperature < -273.15:
            print("Invalid temperature: below absolute zero")
            continue

        status = classify_temperature(temperature)

        readings.append({
            "reading_number": reading_number,
            "temperature": temperature,
            "status": status
        })

    print("\nTEMPERATURE REPORT")

    for reading in readings:
        print(
            reading["reading_number"],
            "| Temperature:", reading["temperature"], "°C",
            "| Status:", reading["status"]
        )


process_readings()