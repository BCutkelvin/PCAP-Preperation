# - - - - - - - SECTION 1: MODULES AND PACKAGES - - - - - - -
# - - - - - - - PCAP-31-03 1.5 Create and uer-defined modules and packages
'billing.py'


def calculate_tax(price, tax):
    return price * tax


def print_billing_doc():
    tax_rate = 1.0
    products = [{'name': 'Book', 'price': 30},
                {'name': 'Pen', 'price': 5}]

    print(f'\nName\tPrice\ttax')

    for i in products:
        tax = calculate_tax(i['price'], tax_rate)
        print(f"{i['name']}\t{i['price']}\t{tax}")


print(__name__)

if __name__ == '__main__':
    print_billing_doc()
