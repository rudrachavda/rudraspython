def flea_vs_hare():
    hare_leap_distance = 1000  # Hare's leap distance in meters
    flea_leap_distance = 0.01
    
    total_distance_hare = 0
    total_distance_flea = 0

    while True:
        total_distance_hare += hare_leap_distance
        total_distance_flea *= flea_leap_distance * 2  # Flea's distance doubles with each hare jump

        print(f"Hare's total distance: {total_distance_hare} meters")
        print(f"Flea's total distance: {total_distance_flea} centimeters\n")

        # Check if the flea has caught up with or surpassed the hare
        if total_distance_flea >= total_distance_hare:
            print("The flea has caught up with or surpassed the hare!")
            break

if __name__ == "__main__":
    flea_vs_hare()
