import streamlit as st

from data_loader import load_data
from queries import create_sales_dataframe
from metrics import calculate_metrics

from charts import (
    revenue_by_category_chart,
    revenue_trend_chart,
    revenue_by_store_chart,
    top_products_chart,
    payment_method_chart,
    order_status_chart
)

from filters import apply_filters
from utils import format_currency, format_number


# ---------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------

st.set_page_config(
    page_title="Retail Sales Analytics Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)


# ---------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------

st.markdown("""
<style>

.block-container{
    padding-top:1.5rem;
    padding-bottom:1rem;
}

[data-testid="stMetricValue"]{
    font-size:30px;
}

</style>
""", unsafe_allow_html=True)


# ---------------------------------------------------
# TITLE
# ---------------------------------------------------

st.title("📊 Retail Sales Analytics Dashboard")

st.markdown("""
Analyze business performance using **Python, Pandas, Plotly and Streamlit**.

This dashboard provides insights into revenue, customer activity, store performance and operational metrics.
""")

st.divider()


# ---------------------------------------------------
# LOAD DATA
# ---------------------------------------------------

with st.spinner("Loading data..."):

    data = load_data()

    sales_df = create_sales_dataframe(data)


# ---------------------------------------------------
# SIDEBAR FILTERS
# ---------------------------------------------------

sales_df = apply_filters(sales_df)


# ---------------------------------------------------
# METRICS
# ---------------------------------------------------

metrics = calculate_metrics(sales_df)


# ---------------------------------------------------
# KPI SECTION
# ---------------------------------------------------

st.subheader("📌 Business Overview")

col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        "💰 Total Revenue",
        format_currency(metrics["Total Revenue"])
    )

with col2:
    st.metric(
        "🛒 Total Orders",
        format_number(metrics["Total Orders"])
    )

with col3:
    st.metric(
        "👥 Total Customers",
        format_number(metrics["Total Customers"])
    )

col4, col5, col6 = st.columns(3)

with col4:
    st.metric(
        "📦 Products",
        format_number(metrics["Total Products"])
    )

with col5:
    st.metric(
        "🏪 Stores",
        format_number(metrics["Total Stores"])
    )

with col6:
    st.metric(
        "💳 Average Order Value",
        format_currency(metrics["Average Order Value"])
    )

st.divider()


# ---------------------------------------------------
# SALES ANALYSIS
# ---------------------------------------------------

st.header("📈 Sales Analysis")

left, right = st.columns(2)

with left:
    st.plotly_chart(
        revenue_trend_chart(sales_df),
        use_container_width=True
    )

with right:
    st.plotly_chart(
        revenue_by_category_chart(sales_df),
        use_container_width=True
    )

st.divider()


# ---------------------------------------------------
# STORE PERFORMANCE
# ---------------------------------------------------

st.header("🏪 Store Performance")

left, right = st.columns(2)

with left:
    st.plotly_chart(
        revenue_by_store_chart(sales_df),
        use_container_width=True
    )

with right:
    st.plotly_chart(
        top_products_chart(sales_df),
        use_container_width=True
    )

st.divider()


# ---------------------------------------------------
# OPERATIONS
# ---------------------------------------------------

st.header("⚙️ Operations")

left, right = st.columns(2)

with left:
    st.plotly_chart(
        payment_method_chart(sales_df),
        use_container_width=True
    )

with right:
    st.plotly_chart(
        order_status_chart(sales_df),
        use_container_width=True
    )

st.divider()


# ---------------------------------------------------
# DOWNLOAD FILTERED DATA
# ---------------------------------------------------

st.header("📥 Download Filtered Data")

st.write("Download the currently filtered sales data as a CSV file.")

csv = sales_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="📄 Download Filtered Sales Data",
    data=csv,
    file_name="filtered_sales_data.csv",
    mime="text/csv",
)

st.divider()


# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------

st.caption(
    "Retail Sales Analytics Dashboard • Built using Python • Pandas • Plotly • Streamlit"
)