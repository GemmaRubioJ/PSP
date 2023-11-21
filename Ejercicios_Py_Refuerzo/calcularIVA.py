

def calculate_total_with_iva(total_purchase, payment_method, amount_paid):
    iva_rate = 0.16  # IVA is usually 12% but it may vary by country
    discount_rate = 0.05  # 5% discount for cash payment

    # Calculate discount if payment is by cash
    if payment_method.lower() == 'efectivo':
        total_purchase -= total_purchase * discount_rate

    # Calculate IVA
    total_with_iva = total_purchase * (1 + iva_rate)

    # Calculate change if payment is done
    change = amount_paid - total_with_iva if amount_paid > total_with_iva else 0

    # Calculate the denomination of the change
    denominations = [50, 20, 10, 5, 1, 0.50, 0.25, 0.10, 0.05, 0.01]
    change_denominations = {}

    for denom in denominations:
        count, change = divmod(change, denom)
        if count:
            change_denominations[denom] = int(count)

    return total_with_iva, change, change_denominations

def main():
    total_purchase_dummy = 100.00  # total amount of purchase
    payment_method_dummy = 'efectivo'  # payment method could be 'efectivo' or 'tc'
    amount_paid_dummy = 200.00  # amount paid by the user
    total_with_iva_dummy, change_dummy, change_denominations_dummy = calculate_total_with_iva(
    total_purchase_dummy,
    payment_method_dummy,
    amount_paid_dummy
    )
    print(f"total con iva : {total_with_iva_dummy}, cambio : {change_dummy}, cambios : {change_denominations_dummy}")

if __name__ == '__main__':
    main()