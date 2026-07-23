def calculate_metrics(sales_df):
    """
    Calculate all dashboard KPI metrics.
    """

    if sales_df.empty:

        return {
            "Total Revenue": 0,
            "Total Orders": 0,
            "Total Customers": 0,
            "Total Products": 0,
            "Total Stores": 0,
            "Average Order Value": 0,
        }

    total_revenue = sales_df["total_price"].sum()

    total_orders = sales_df["order_id"].nunique()

    total_customers = sales_df["customer_id"].nunique()

    total_products = sales_df["product_id"].nunique()

    total_stores = sales_df["store_id"].nunique()

    average_order_value = (
        sales_df
        .groupby("order_id")["total_price"]
        .sum()
        .mean()
    )

    metrics = {
        "Total Revenue": total_revenue,
        "Total Orders": total_orders,
        "Total Customers": total_customers,
        "Total Products": total_products,
        "Total Stores": total_stores,
        "Average Order Value": average_order_value,
    }

    return metrics