import streamlit as st
import pandas as pd


def apply_filters(sales_df):

    st.sidebar.header("🎛 Dashboard Filters")

    df = sales_df.copy()

    # ---------------------------------------
    # Year Filter
    # ---------------------------------------

    df["order_date"] = pd.to_datetime(df["order_date"])

    years = sorted(df["order_date"].dt.year.unique())

    year_options = ["All"] + [str(year) for year in years]

    selected_year = st.sidebar.selectbox(
        "Year",
        year_options
    )

    if selected_year != "All":
        df = df[df["order_date"].dt.year == int(selected_year)]

    # ---------------------------------------
    # Category Filter
    # ---------------------------------------

    categories = sorted(df["category_name"].dropna().unique())

    selected_category = st.sidebar.selectbox(
        "Category",
        ["All"] + categories
    )

    if selected_category != "All":
        df = df[df["category_name"] == selected_category]

    # ---------------------------------------
    # Store Filter
    # ---------------------------------------

    stores = sorted(df["store_name"].dropna().unique())

    selected_store = st.sidebar.selectbox(
        "Store",
        ["All"] + stores
    )

    if selected_store != "All":
        df = df[df["store_name"] == selected_store]

    # ---------------------------------------
    # Payment Method Filter
    # ---------------------------------------

    methods = sorted(df["payment_method"].dropna().unique())

    selected_method = st.sidebar.selectbox(
        "Payment Method",
        ["All"] + methods
    )

    if selected_method != "All":
        df = df[df["payment_method"] == selected_method]

    # ---------------------------------------
    # Order Status Filter
    # ---------------------------------------

    status = sorted(df["order_status"].dropna().unique())

    selected_status = st.sidebar.selectbox(
        "Order Status",
        ["All"] + status
    )

    if selected_status != "All":
        df = df[df["order_status"] == selected_status]

    # ---------------------------------------
    # Sidebar Information
    # ---------------------------------------

    st.sidebar.markdown("---")

    st.sidebar.metric(
        "Filtered Records",
        f"{len(df):,}"
    )

    return df