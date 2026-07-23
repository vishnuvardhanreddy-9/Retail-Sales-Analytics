from generators.categories import generate_categories
from generators.suppliers import generate_suppliers
from generators.stores import generate_stores
from generators.employees import generate_employees
from generators.customers import generate_customers
from generators.products import generate_products
from generators.orders import generate_orders
from generators.order_items import generate_order_items
from generators.inventory import generate_inventory
from generators.payments import generate_payments
from generators.returns import generate_returns


def main():

    print("=" * 60)
    print("Retail Sales Analytics Dataset Generator")
    print("=" * 60)

    generate_categories()
    generate_suppliers()
    generate_stores()

    generate_employees()
    generate_customers()
    generate_products()

    generate_orders()
    generate_order_items()

    generate_inventory()
    generate_payments()
    generate_returns()

    print("\n🎉 All datasets generated successfully!")


if __name__ == "__main__":
    main()