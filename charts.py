import pandas as pd
import plotly.express as px


# -------------------------------------------------
# Common Chart Styling
# -------------------------------------------------

def style_chart(fig):
    """
    Apply a consistent professional style to all charts.
    """

    fig.update_layout(
        template="plotly_white",
        font=dict(
            family="Arial",
            size=13
        ),
        title=dict(
            x=0.5,
            xanchor="center",
            font=dict(size=20)
        ),
        margin=dict(
            l=20,
            r=20,
            t=60,
            b=20
        ),
        paper_bgcolor="white",
        plot_bgcolor="white",
        hovermode="x unified",
        coloraxis_showscale=False
    )

    return fig


# -------------------------------------------------
# Revenue by Category
# -------------------------------------------------

def revenue_by_category_chart(sales_df):

    revenue = (
        sales_df
        .groupby("category_name")["total_price"]
        .sum()
        .reset_index()
        .sort_values("total_price", ascending=False)
    )

    fig = px.bar(
        revenue,
        x="category_name",
        y="total_price",
        title="Revenue by Category",
        text_auto=".2s",
        color="total_price",
        color_continuous_scale="Blues"
    )

    fig.update_traces(
        hovertemplate="<b>%{x}</b><br>Revenue: ₹%{y:,.0f}<extra></extra>"
    )

    fig.update_layout(
        xaxis_title="Category",
        yaxis_title="Revenue (₹)"
    )

    fig.update_yaxes(
        tickprefix="₹",
        separatethousands=True
    )

    return style_chart(fig)


# -------------------------------------------------
# Monthly Revenue Trend
# -------------------------------------------------

def revenue_trend_chart(sales_df):

    df = sales_df.copy()

    df["order_date"] = pd.to_datetime(df["order_date"])

    monthly = (
        df.groupby(df["order_date"].dt.to_period("M"))["total_price"]
        .sum()
        .reset_index()
    )

    monthly["order_date"] = monthly["order_date"].astype(str)

    fig = px.line(
        monthly,
        x="order_date",
        y="total_price",
        title="Monthly Revenue Trend",
        markers=True
    )

    fig.update_traces(
        line=dict(width=4),
        marker=dict(size=8),
        hovertemplate="<b>%{x}</b><br>Revenue: ₹%{y:,.0f}<extra></extra>"
    )

    fig.update_layout(
        xaxis_title="Month",
        yaxis_title="Revenue (₹)"
    )

    fig.update_yaxes(
        tickprefix="₹",
        separatethousands=True
    )

    return style_chart(fig)
# -------------------------------------------------
# Revenue by Store
# -------------------------------------------------

def revenue_by_store_chart(sales_df):

    revenue = (
        sales_df
        .groupby("store_name")["total_price"]
        .sum()
        .reset_index()
        .sort_values("total_price", ascending=False)
        .head(10)
    )

    fig = px.bar(
        revenue,
        x="store_name",
        y="total_price",
        title="Top 10 Stores by Revenue",
        text_auto=".2s",
        color="total_price",
        color_continuous_scale="Greens"
    )

    fig.update_traces(
        hovertemplate="<b>%{x}</b><br>Revenue: ₹%{y:,.0f}<extra></extra>"
    )

    fig.update_layout(
        xaxis_title="Store",
        yaxis_title="Revenue (₹)",
        xaxis_tickangle=-35
    )

    fig.update_yaxes(
        tickprefix="₹",
        separatethousands=True
    )

    return style_chart(fig)


# -------------------------------------------------
# Top Products
# -------------------------------------------------

def top_products_chart(sales_df):

    top_products = (
        sales_df
        .groupby("product_name")["total_price"]
        .sum()
        .reset_index()
        .sort_values("total_price", ascending=False)
        .head(10)
    )

    fig = px.bar(
        top_products,
        x="product_name",
        y="total_price",
        title="Top 10 Products by Revenue",
        text_auto=".2s",
        color="total_price",
        color_continuous_scale="Purples"
    )

    fig.update_traces(
        hovertemplate="<b>%{x}</b><br>Revenue: ₹%{y:,.0f}<extra></extra>"
    )

    fig.update_layout(
        xaxis_title="Product",
        yaxis_title="Revenue (₹)",
        xaxis_tickangle=-35
    )

    fig.update_yaxes(
        tickprefix="₹",
        separatethousands=True
    )

    return style_chart(fig)
# -------------------------------------------------
# Payment Method
# -------------------------------------------------

def payment_method_chart(sales_df):

    payments = (
        sales_df
        .groupby("payment_method")["amount"]
        .sum()
        .reset_index()
        .sort_values("amount", ascending=False)
    )

    fig = px.pie(
        payments,
        names="payment_method",
        values="amount",
        title="Payment Method Distribution",
        hole=0.55,
        color_discrete_sequence=px.colors.qualitative.Set2
    )

    fig.update_traces(
        textposition="inside",
        textinfo="percent+label",
        hovertemplate="<b>%{label}</b><br>Amount: ₹%{value:,.0f}<br>%{percent}<extra></extra>",
        pull=[0.03] * len(payments)
    )

    fig.update_layout(
        legend_title="Payment Method",
        legend_orientation="h",
        legend_y=-0.15,
        legend_x=0.5,
        legend_xanchor="center"
    )

    return style_chart(fig)


# -------------------------------------------------
# Order Status
# -------------------------------------------------

def order_status_chart(sales_df):

    status = (
        sales_df
        .groupby("order_status")
        .size()
        .reset_index(name="Orders")
        .sort_values("Orders", ascending=False)
    )

    fig = px.pie(
        status,
        names="order_status",
        values="Orders",
        title="Order Status Distribution",
        hole=0.55,
        color_discrete_sequence=px.colors.qualitative.Pastel
    )

    fig.update_traces(
        textposition="inside",
        textinfo="percent+label",
        hovertemplate="<b>%{label}</b><br>Orders: %{value:,}<br>%{percent}<extra></extra>",
        pull=[0.03] * len(status)
    )

    fig.update_layout(
        legend_title="Order Status",
        legend_orientation="h",
        legend_y=-0.15,
        legend_x=0.5,
        legend_xanchor="center"
    )

    return style_chart(fig)