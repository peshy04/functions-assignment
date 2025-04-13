def calculate_discount(price, discount_percent):
    """
    Calculate the final price after applying a discount.
    If the discount percentage is 20% or higher, apply the discount.
    Otherwise, return the original price.

    :param price: Original price of the item
    :param discount_percent: Discount percentage to be applied
    :return: Final price after applying the discount or original price
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        return price - discount_amount
    else:
        return price


# Prompt the user for input
try:
    original_price = float(input("Enter the original price of the item: "))
    discount_percentage = float(input("Enter the discount percentage: "))

    # Calculate the final price
    final_price = calculate_discount(original_price, discount_percentage)

    # Print the result
    if final_price == original_price:
        print(f"No discount applied. The original price is: ${original_price:.2f}")
    else:
        print(f"The final price after applying the discount is: ${final_price:.2f}")
except ValueError:
    print("Invalid input. Please enter numeric values for price and discount percentage.")