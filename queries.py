import pandas as pd


def create_sales_dataframe(data):
    """
    Create the master sales dataframe used throughout the dashboard.
    """

    customers = data["customers"]
    orders = data["orders"]
    order_items = data["order_items"]
    products = data["products"]
    categories = data["categories"]
    stores = data["stores"]
    employees = data["employees"]
    payments = data["payments"]

    # -------------------------------------------------
    # Orders + Order Items
    # -------------------------------------------------

    sales_df = orders.merge(
        order_items,
        on="order_id",
        how="inner"
    )

    # -------------------------------------------------
    # Product Information
    # -------------------------------------------------

    sales_df = sales_df.merge(
        products,
        on="product_id",
        how="left"
    )

    # -------------------------------------------------
    # Category Information
    # -------------------------------------------------

    sales_df = sales_df.merge(
        categories,
        on="category_id",
        how="left"
    )

    # -------------------------------------------------
    # Customer Information
    # -------------------------------------------------

    sales_df = sales_df.merge(
        customers,
        on="customer_id",
        how="left"
    )

    # -------------------------------------------------
    # Store Information
    # -------------------------------------------------

    sales_df = sales_df.merge(
        stores,
        on="store_id",
        how="left"
    )

    # -------------------------------------------------
    # Employee Information
    # -------------------------------------------------

    sales_df = sales_df.merge(
        employees,
        on="employee_id",
        how="left",
        suffixes=("", "_employee")
    )

    # -------------------------------------------------
    # Payment Information
    # -------------------------------------------------

    sales_df = sales_df.merge(
        payments,
        on="order_id",
        how="left"
    )

    # -------------------------------------------------
    # Data Cleaning
    # -------------------------------------------------

    sales_df["order_date"] = pd.to_datetime(
        sales_df["order_date"],
        errors="coerce"
    )

    sales_df = sales_df.drop_duplicates()

    return sales_df