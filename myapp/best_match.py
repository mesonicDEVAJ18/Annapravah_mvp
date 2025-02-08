from geopy.distance import geodesic

# Placeholder geocoding function (replace with actual geolocation retrieval)
def geocode_location(location):
    # Replace this with actual geocoding logic to get lat, lon
    return (0.0, 0.0)  # Dummy value, replace with actual lat, lon

def find_best_match_for_request(request, donations):
    # Step 1: Find donations of the same food type
    matching_donations = [donation for donation in donations if donation.food_type == request.food_type]

    # If no matching donations, return None
    if not matching_donations:
        return None

    best_match = None
    best_distance = float('inf')

    # Step 2: Iterate over donations and try to match with the request
    for donation in matching_donations:
        # Geocode locations
        request_location = geocode_location(request.location)
        donation_location = geocode_location(donation.current_location)

        # Calculate the distance between the request and donation
        distance = geodesic(donation_location, request_location).km

        # Select the donation with the shortest distance
        if distance < best_distance:
            best_distance = distance
            best_match = (donation, request)

    return best_match

def find_best_match_for_donation(donation, requests):
    # Step 1: Find requests of the same food type
    matching_requests = [request for request in requests if request.food_type == donation.food_type]

    # If no matching requests, return None
    if not matching_requests:
        return None

    best_match = None
    best_distance = float('inf')

    # Step 2: Iterate over requests and try to match with the donation
    for request in matching_requests:
        # Geocode locations
        request_location = geocode_location(request.location)
        donation_location = geocode_location(donation.current_location)

        # Calculate the distance between the request and donation
        distance = geodesic(donation_location, request_location).km

        # Select the request with the shortest distance
        if distance < best_distance:
            best_distance = distance
            best_match = (donation, request)

    return best_match


