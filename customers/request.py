CUSTOMERS = [
    {
      "id": 1,
      "name": "Hannah Hall",
      "address": "7002 Chestnut Ct"
    },
    {
      "id": 2,
      "name": "Zach Maas",
      "address": "8458 South Avenue"
    },
    {
      "email": "samanthajmaas@gmail.com",
      "password": "Bikes689",
      "name": "Samantha Maas",
      "id": 3
    }
]


def get_all_customers():
    return CUSTOMERS

    
def get_single_customer(id):
    
    requested_customer = None

    
    for customer in CUSTOMERS:
        
        if customer["id"] == id:
            requested_customer = customer

    return requested_customer