# Toronto Island Ferry Ticket Sales, Redemption & Demand Trend Analysis

# Overview
An interactive data analytics project built using Python, Pandas, Plotly, and Streamlit to analyze Toronto Island Ferry ticket sales and redemption patterns across hourly, daily, and seasonal time periods.

The project transforms raw ferry transaction data into actionable operational insights that support:
- passenger demand forecasting,
- peak travel period identification,
- seasonal trend analysis,
- ferry capacity planning,
- service optimization, and
- data-driven operational decision-making.

# Live Dashboard


# Problem → Solution → Impact

# ⚠️ Problem

Ferry operators lacked clear visibility into passenger demand patterns, peak travel periods, and seasonal fluctuations. Raw ticket sales and redemption data alone made it difficult to identify operational trends and optimize ferry services.

# ⚙️ Solution

Developed an analytics dashboard and exploratory data analysis framework to examine:

- ticket sales and redemption trends
- hourly, daily, and seasonal demand patterns
- passenger movement behavior
- peak demand periods
- operational KPIs and utilization metrics

# 📈 Impact

- Identifies peak travel hours for effective capacity planning
- Reveals seasonal demand fluctuations and passenger behavior patterns
- Supports data-driven scheduling and resource allocation decisions
- Improves operational efficiency through demand trend monitoring
- Provides actionable insights for ferry service optimization

# Core Analytical Areas

# 📊 Ticket Sales & Redemption Analysis

- Sales and redemption trend analysis
- Ticket utilization tracking
- Sales vs redemption comparison
- Passenger movement assessment

# ⏰ Demand Pattern Analysis

- Hourly demand trend analysis
- Peak demand hour identification
- Daily passenger traffic monitoring
- Travel behavior pattern discovery

# 🌤️ Seasonal & Temporal Analysis

- Seasonal demand comparison
- Monthly and yearly trend analysis
- Weekend vs weekday performance evaluation
- Off-season utilization assessment

# 📈 Time-Series Trend Analysis

- Rolling average demand analysis
- Long-term trend identification
- Demand fluctuation monitoring
- Seasonal pattern detection
- 
# 📋 Operational KPI Analysis

- Net passenger movement tracking
- Peak demand period analysis
- Utilization index measurement
- Capacity planning insights

# 🎯 Business Insights & Optimization

- High-demand period identification
- Resource allocation insights
- Service scheduling optimization
- Data-driven operational decision support

## 📌 Key KPIs

| KPI | Description |
|------|-------------|
| Tickets Sold / Hour | Average number of ferry tickets sold per hour |
| Tickets Redeemed / Hour | Average number of ferry tickets redeemed per hour |
| Net Passenger Movement | Total Sales Count − Total Redemption Count |
| Peak Demand Hour | Hour with the highest ticket sales volume |
| Off-Season Utilization Index | Winter demand as a percentage of overall average demand |
| Highest Demand Season | Season generating the highest passenger demand |
| Peak vs Off-Peak Demand | Passenger activity comparison across operating periods |

---

# 🛠️ Tech Stack

| Category | Technologies |
|----------|-------------|
| Programming Language | Python |
| Dashboard Framework | Streamlit |
| Data Processing | Pandas, NumPy |
| Data Visualization | Plotly Express |
| Data Caching | Streamlit Cache (`@st.cache_data`) |
| User Interface | Streamlit Components & Custom HTML |
| Analytics | Time-Series, Seasonal & Demand Analysis |
| Deployment | Streamlit Community Cloud |


# ✨ Dashboard Features

| Feature | Description |
|----------|-------------|
| Role-Based Views | Management, Operations, and Policy Planner perspectives |
| Interactive Filters | Date, Hour, and Season filtering |
| KPI Dashboard | Real-time operational metrics |
| Sales Trends | Daily sales and redemption analysis |
| Operations Analytics | Peak vs Off-Peak demand monitoring |
| Passenger Flow Analysis | Net passenger movement tracking |
| Monthly Trends | Month-wise demand patterns |
| Seasonal Analysis | Demand comparison across seasons |
| Data Explorer | Downloadable filtered dataset |
| Business Recommendations | Automated operational insights |

# 💡 Business Insights Generated

The dashboard helps uncover:

- Peak passenger demand hours and seasonal travel patterns.
- Differences between ticket sales and redemptions across time periods.
- Net passenger movement trends to support operational planning.
- Weekend versus weekday demand behavior.
- Off-season utilization levels and service efficiency.
- Long-term demand trends using rolling average analysis.
- High-traffic periods requiring additional ferry capacity and resource allocation.

# 🚢 Demand & Operational Analysis

The project incorporates:

- Hourly, daily, monthly, and seasonal demand analysis.
- Passenger movement tracking using ticket sales and redemption data.
- Peak demand window identification for operational optimization.
- Off-season utilization measurement to evaluate service effectiveness.
- Rolling average trend analysis for long-term demand forecasting.

This enables data-driven decisions for ferry scheduling, capacity planning, resource allocation, and passenger flow management.

# Project Structure

## Project Structure

```text
Toronto-Island-Ferry-Ticket-Analytics/
│
├── app.py                          # Streamlit dashboard application
├── requirements.txt                # Project dependencies
├── README.md                       # Project documentation
│
├── data/
│   └── ferry_ticket_data.csv       # Raw dataset
│
└── notebooks/
    └── Toronto_Island_Ferry_Tickets.ipynb
```

# 🎓 Key Learnings

Through this project, I gained hands-on experience in:

- Exploratory Data Analysis (EDA) and data storytelling.
- Time-series analysis using ticket sales and redemption data.
- Building interactive dashboards with Streamlit and Plotly.
- Designing user-centric analytics solutions for different stakeholder groups.
- Creating KPI-driven dashboards for operational decision-making.
- Transforming raw transportation data into actionable business insights.

The project also strengthened my understanding of:

- Passenger demand forecasting and trend analysis.
- Seasonal and temporal pattern identification.
- Operational performance monitoring through KPIs.
- Data visualization best practices.
- Dashboard design and deployment using Streamlit Community Cloud.

# 🚀 Future Improvements

Potential future enhancements include:

- Demand forecasting using machine learning.
- Real-time ticket sales integration.
- Weather-based demand analysis.
- Automated report generation.
- Route and capacity optimization recommendations.

These enhancements would further improve decision-making, operational efficiency, and long-term planning for ferry services.

# 🤝 Feedback & Connect

Feedback, suggestions, and improvement ideas are always welcome.

If you'd like to discuss data analytics, business intelligence, dashboard development, operational analytics, or data visualization, feel free to connect with me on LinkedIn.

LinkedIn: https://www.linkedin.com/in/md-arjan-afridi-7288b7233
Email: arjanafridi123@gmail.com

⭐ If you found this project interesting, consider exploring the dashboard, reviewing the analysis, and sharing your feedback.

Thank you for visiting this project!
