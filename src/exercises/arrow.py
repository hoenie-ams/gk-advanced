"""
Refactor the code below. Try go get the functions' bodies
as close to the left side as possible (only one indentation deep).
"""
movies = {
    "tomorrow_never_dies": {"name": "Tomorrow Never Dies", "genre": "Action"},
    "robin_hood": {"name": "Robin Hood", "genre": "Adventure"},
    "pulp_fiction": {"name": "Pulp Fiction", "genre": "Crime"},
}


def invoice(movie, tickets):
    if movie not in movies:
        raise LookupError("Movie not available")
    if tickets == 0:
        raise ValueError("Cannot calculate price for 0 tickets")

    price = price_for(movie)
    discount = discount_for(tickets)

    total_amount = (tickets * price) - discount
    return total_amount


def price_for(title):
    if movies[title]["genre"] == "Action":
        price = 12
    else:
        price = 10
    return price


def discount_for(tickets):
    if tickets >= 5:
        discount = 10
    else:
        discount = 0
    return discount


print(invoice("pulp_fiction", 6))
