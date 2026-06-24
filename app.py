import numpy as np
import pandas as pd
import streamlit as st
import plotly.express as px

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Toronto Island Ferry Dashboard",
    layout="wide"
)

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Toronto Island Ferry Dashboard",
    page_icon="🚢",
    layout="wide"
)

# -----------------------------
# FERRY / WATER THEME
# -----------------------------
st.markdown("""
<style>

/* Main App Background */
[data-testid="stAppViewContainer"] {
    background: linear-gradient(
        180deg,
        #EAF6FB 0%,
        #F8FDFF 100%
    );
}

/* Main Content Area */
.main {
    background-color: transparent;
}

/* Headers */
h1 {
    color: #0B3C5D;
    font-weight: 700;
}

h2, h3 {
    color: #134E6F;
}

/* KPI Cards */
[data-testid="stMetric"] {
    background-color: white;
    border-left: 5px solid #0EA5E9;
    border-radius: 12px;
    padding: 18px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background: linear-gradient(
        180deg,
        #001F3F 0%,
        #003566 100%
    );
}

/* Sidebar Text */
section[data-testid="stSidebar"] * {
    color: white;
}

/* Selectboxes */
.stSelectbox div[data-baseweb="select"] {
    border-radius: 10px;
}

/* Buttons */
.stButton > button {
    background-color: #0EA5E9;
    color: white;
    border-radius: 8px;
    border: none;
}

.stButton > button:hover {
    background-color: #0284C7;
    color: white;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# DASHBOARD HEADER
# -----------------------------
st.markdown("""
# 🚢 Toronto Island Ferry Analytics Dashboard

### Real-Time Passenger Flow & Demand Monitoring (2015–2025)
""")

st.markdown("""
### Dashboard Overview

Monitor ferry ticket sales, redemptions, passenger movement,
seasonal demand patterns, and peak-hour activity across
Toronto Island Park ferry operations.
""")

# -----------------------------
# LOAD DATA
# -----------------------------
@st.cache_data
def load_data():

    df = pd.read_csv("Toronto Island Ferry Tickets.csv")

    df["Timestamp"] = pd.to_datetime(df["Timestamp"])

    df["Date"] = df["Timestamp"].dt.date
    df["Hour"] = df["Timestamp"].dt.hour
    df["Month"] = df["Timestamp"].dt.month

    # Season
    season_num = df["Timestamp"].dt.month % 12 // 3 + 1

    season_map = {
        1: "Winter",
        2: "Spring",
        3: "Summer",
        4: "Autumn"
    }

    df["Season"] = season_num.map(season_map)

    # Peak Status
    df["Peak_Status"] = np.where(
        df["Hour"].between(10, 17),
        "Peak",
        "Off-Peak"
    )

    return df

df = load_data()

role = st.selectbox(
    "Select User Role",
    [
        "Management Stakeholder",
        "Operations Team",
        "Policy Planner"
    ]
)

if role == "Management Stakeholder":
    st.success("Focus: KPI monitoring and strategic decisions.")

elif role == "Operations Team":
    st.success("Focus: Peak hours, staffing and ferry allocation.")

elif role == "Policy Planner":
    st.success("Focus: Seasonal demand and long-term planning.")

# -----------------------------
# SIDEBAR HEADER
# -----------------------------
st.sidebar.markdown("""
<div style='text-align:center; padding-top:10px;'>

<div style='font-size:55px;'>⛴️</div>

<h1 style='color:#1f77b4; margin-bottom:0px;'>
FerryFlow
</h1>

<p style='font-size:14px; letter-spacing:1px; margin-top:0px;'>
TORONTO ISLAND PARK • 2015–2025
</p>

<hr style='margin-top:15px; margin-bottom:15px;'>

</div>
""", unsafe_allow_html=True)

# -----------------------------
# SIDEBAR FILTERS
# -----------------------------
st.sidebar.header("Filters")

start_date = st.sidebar.date_input(
    "Start Date",
    value=df["Date"].min(),
    min_value=df["Date"].min(),
    max_value=df["Date"].max()
)

end_date = st.sidebar.date_input(
    "End Date",
    value=df["Date"].max(),
    min_value=df["Date"].min(),
    max_value=df["Date"].max()
)

selected_hours = st.sidebar.multiselect(
    "Select Hours",
    sorted(df["Hour"].unique()),
    default=sorted(df["Hour"].unique())
)

# ADD THIS HERE
season_options = ["Winter", "Spring", "Summer", "Autumn"]

selected_seasons = st.sidebar.multiselect(
    "Select Season",
    options=season_options,
    default=season_options
)

filtered_df = df[
    (df["Hour"].isin(selected_hours)) &
    (df["Season"].isin(selected_seasons)) &
    (df["Date"] >= start_date) &
    (df["Date"] <= end_date)
]

# -----------------------------
# KPI SECTION
# -----------------------------
sales_per_hour = filtered_df["Sales Count"].mean()

redeemed_per_hour = filtered_df["Redemption Count"].mean()

net_movement = (
    filtered_df["Sales Count"].sum()
    - filtered_df["Redemption Count"].sum()
)

peak_hour = (
    filtered_df
    .groupby("Hour")["Sales Count"]
    .sum()
    .idxmax()
)

# Off-Season Utilization Index
off_season = filtered_df[
    filtered_df["Season"] == "Winter"
]

overall_avg_sales = filtered_df["Sales Count"].mean()

off_season_avg_sales = off_season["Sales Count"].mean()

if overall_avg_sales > 0:
    off_season_utilization_index = (
        off_season_avg_sales / overall_avg_sales
    ) * 100
else:
    off_season_utilization_index = 0

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric(
    "Tickets Sold / Hour",
    f"{sales_per_hour:.0f}"
)

col2.metric(
    "Tickets Redeemed / Hour",
    f"{redeemed_per_hour:.0f}"
)

col3.metric(
    "Net Passenger Movement",
    f"{int(net_movement):,}"
)

col4.metric(
    "Peak Demand Hour",
    f"{peak_hour}:00"
)

col5.metric(
    "Off-Season Utilization",
    f"{off_season_utilization_index:.2f}%"
)

# -----------------------------
# KEY TAKEAWAYS
# -----------------------------
st.divider()

highest_season = (
    filtered_df.groupby("Season")["Sales Count"]
    .sum()
    .idxmax()
)

st.subheader("🚢 Key Insights")

st.info(f"""
• Peak passenger demand occurs around {peak_hour}:00.

• Net passenger movement during the selected period is {int(net_movement):,}.

• {highest_season} records the highest ferry demand.

• Off-season utilization remains at {off_season_utilization_index:.2f}% of average demand.

• Additional ferry capacity and staffing should be prioritized during peak operating hours.
""")


tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
    "📈 Sales Trends",
    "⚙️ Operations",
    "🚶 Passenger Flow",
    "📅 Monthly Trends",
    "🌦️ Seasonal Analysis",
    "📄 Data Explorer"
])

with tab1:

    st.subheader("📈 Sales & Redemption Trend")

    daily = (
        filtered_df
        .groupby("Date")[["Sales Count", "Redemption Count"]]
        .sum()
        .reset_index()
    )

    fig = px.line(
        daily,
        x="Date",
        y=["Sales Count", "Redemption Count"],
        color_discrete_map={
            "Sales Count": "#1f77b4",
            "Redemption Count": "#ff7f0e"
        }
    )

    fig.update_layout(
        legend_title_text=""
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

    st.info("""
    Insight:
    Sales and redemptions generally move together over time,
    indicating consistent passenger travel demand.
    """)

with tab2:

    # -----------------------------
    # PEAK VS OFF-PEAK
    # -----------------------------
    st.subheader("🚢 Peak vs Off-Peak Comparison")

    peak_df = (
        filtered_df
        .groupby("Peak_Status")
        [["Sales Count", "Redemption Count"]]
        .sum()
        .reset_index()
    )

    fig2 = px.bar(
        peak_df,
        x="Peak_Status",
        y=["Sales Count", "Redemption Count"],
        barmode="group",
        color_discrete_map={
            "Sales Count": "#1f77b4",
            "Redemption Count": "#ff7f0e"
        }
    )

    fig2.update_layout(
        legend_title_text=""
    )

    st.plotly_chart(
        fig2,
        use_container_width=True
    )

    st.info("""
    Insight:
    Passenger activity is concentrated during peak operating hours,
    highlighting the importance of staffing and ferry allocation.
    """)

    # -----------------------------
    # PEAK DEMAND WINDOWS
    # -----------------------------
    st.subheader("⏰ Peak Demand Windows")

    hourly_sales = (
        filtered_df
        .groupby("Hour")["Sales Count"]
        .sum()
        .reset_index()
    )

    fig3 = px.bar(
        hourly_sales,
        x="Hour",
        y="Sales Count",
        color_discrete_sequence=["#1f77b4"]
    )

    fig3.update_layout(
        showlegend=False
    )

    st.plotly_chart(
        fig3,
        use_container_width=True
    )

    st.info(f"""
    Insight:
    The busiest demand window occurs around {peak_hour}:00,
    which should receive priority for operational planning.
    """)


with tab3:

    # -----------------------------
    # NET PASSENGER MOVEMENT
    # -----------------------------
    st.subheader("🚶 Net Passenger Movement by Hour")

    net_df = filtered_df.copy()

    net_df["Net Passenger Movement"] = (
        net_df["Sales Count"]
        - net_df["Redemption Count"]
    )

    hourly_net = (
        net_df
        .groupby("Hour")["Net Passenger Movement"]
        .sum()
        .reset_index()
    )

    fig_net = px.bar(
        hourly_net,
        x="Hour",
        y="Net Passenger Movement",
        color="Net Passenger Movement",
        color_continuous_scale="RdYlGn"
    )

    fig_net.update_layout(
        coloraxis_showscale=False
    )

    st.plotly_chart(
        fig_net,
        use_container_width=True
    )

    st.info("""
    Insight:

    Positive values indicate more tickets sold than redeemed,
    while negative values indicate higher redemption activity.

    This helps identify passenger flow imbalances across the day.
    """)

with tab4:

    # -----------------------------
    # MONTHLY SALES TREND
    # -----------------------------
    st.subheader("📅 Monthly Sales Trend")

    monthly_sales = (
        filtered_df
        .groupby("Month")["Sales Count"]
        .sum()
        .reset_index()
    )

    month_names = {
        1: "January",
        2: "February",
        3: "March",
        4: "April",
        5: "May",
        6: "June",
        7: "July",
        8: "August",
        9: "September",
        10: "October",
        11: "November",
        12: "December"
    }

    monthly_sales["Month_Name"] = (
        monthly_sales["Month"]
        .map(month_names)
    )

    fig4 = px.line(
        monthly_sales,
        x="Month_Name",
        y="Sales Count",
        markers=True
    )

    fig4.update_xaxes(
        categoryorder="array",
        categoryarray=[
            "January", "February", "March", "April",
            "May", "June", "July", "August",
            "September", "October", "November", "December"
        ]
    )

    fig4.update_traces(
        line_color="#1f77b4"
    )

    st.plotly_chart(
        fig4,
        use_container_width=True
    )

with tab5:

    # -----------------------------
    # SEASONAL DEMAND COMPARISON
    # -----------------------------
    st.subheader("🌦️ Seasonal Demand Comparison")

    seasonal_sales = (
        filtered_df
        .groupby("Season")["Sales Count"]
        .sum()
        .reset_index()
    )

    season_order = ["Winter", "Spring", "Summer", "Autumn"]

    seasonal_sales["Season"] = pd.Categorical(
        seasonal_sales["Season"],
        categories=season_order,
        ordered=True
    )

    seasonal_sales = seasonal_sales.sort_values("Season")

    fig5 = px.bar(
        seasonal_sales,
        x="Season",
        y="Sales Count",
        color="Season"
    )

    st.plotly_chart(
        fig5,
        use_container_width=True
    )

    st.info("""
    Insight:
    Seasonal demand differences help evaluate ferry utilization
    throughout the year and support long-term planning.
    """)

csv = filtered_df.to_csv(index=False)

with tab6:

    st.download_button(
        label="📥 Download Filtered Dataset",
        data=csv,
        file_name="Toronto_Ferry_Filtered_Data.csv",
        mime="text/csv"
    )

    st.subheader("📄 Filtered Dataset")

    st.dataframe(
        filtered_df,
        use_container_width=True
    )


st.divider()

st.subheader("📌 Business Recommendations")

st.success("""
1. Increase ferry frequency during peak demand hours.

2. Deploy additional staff between 10 AM and 5 PM.

3. Monitor off-season demand to optimize operating costs.

4. Use hourly demand patterns to improve scheduling efficiency.

5. Prepare additional ferry capacity during seasonal demand spikes.
""")