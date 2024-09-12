def calculate_total_sales(sales_totals):
    if not sales_totals:
        return 0.0
    total = 0
    for candy_name, candy_details in sales_totals.items():
         total += candy_details["quantity"] * candy_details["price"]
    return total


def calculate_average_sales(sales_totals):
    if not sales_totals:
        return 0.0
    total = calculate_total_sales(sales_totals)
    num_of_candies = len(sales_totals)
    average =  total / num_of_candies
    return average


def filter_to_better_than_average_sales(sales_totals):
    if not sales_totals:
        return {}
    
def ninety_nine_bottles(count, beverage):
    pass

