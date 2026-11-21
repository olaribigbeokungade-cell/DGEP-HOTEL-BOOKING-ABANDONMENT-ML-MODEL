
def generate_recommendation(probability):

    if probability >= 0.70:
        risk = "HIGH"
        recommendations = [
            "Send an immediate booking reminder",
            "Offer a promotional discount",
            "Provide alternative room options",
            "Offer customer support assistance",
            "Simplify Checkout"
        ]

    elif probability >= 0.40:
        risk = "MEDIUM"
        recommendations = [
            "Send a booking reminder",
            "Provide additional booking information",
            "Highlight available room benefits"
        ]

    else:
        risk = "LOW"
        recommendations = [
            "Continue normal booking process",
            "Send a confirmation reminder if necessary"
        ]

    return risk, recommendations
