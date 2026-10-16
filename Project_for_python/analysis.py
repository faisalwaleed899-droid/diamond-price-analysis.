import pandas as pd
import plotly.express as px
import streamlit as st

# Set the dashboard title
st.title("💎 Diamond Price Analysis")

# Load the dataset
df = pd.read_csv("data/diamonds.csv")

# Create a carat range slider
min_carat, max_carat = st.slider(
    "Select carat range",
    min_value=0.0,
    max_value=5.0,
    value=(0.5, 1.5),
    step=0.1
)

# Filter the diamonds
filtered_df = df[
    (df["carat"] >= min_carat) &
    (df["carat"] <= max_carat)
]
# Convert filtered data to CSV
csv_data = filtered_df.to_csv(index=False)

# Add a download button
st.download_button(
    label="Download Filtered Data",
    data=csv_data,
    file_name="filtered_diamonds.csv",
    mime="text/csv"
)

# Show the number of matching diamonds
col1, col2, col3 = st.columns(3)

col1.metric("Diamonds Found", len(filtered_df))

if not filtered_df.empty:
    col2.metric(
        "Average Price",
        f"${filtered_df['price'].mean():,.2f}"
    )

    col3.metric(
        "Highest Price",
        f"${filtered_df['price'].max():,.2f}"
    )
else:
    col2.metric("Average Price", "N/A")
    col3.metric("Highest Price", "N/A")

st.subheader("Filtered Diamond Data")

st.dataframe(
    filtered_df.head(20),
    use_container_width=True
)

# Create a box plot
fig = px.box(
    filtered_df,
    x="cut",
    y="price",
    title="Diamond Prices by Cut Quality",
    labels={
        "cut": "Cut Quality",
        "price": "Diamond Price ($)"
    }
)
# Average price by carat
price_by_carat = (
    filtered_df.groupby("carat", as_index=False)["price"]
    .mean()
)

fig2 = px.line(
    price_by_carat,
    x="carat",
    y="price",
    markers=True,
    title="Average Diamond Price by Carat"
)
fig3 = px.histogram(
    filtered_df,
    x="price",
    nbins=30,
    title="Distribution of Diamond Prices"
)

fig3.update_layout(
    xaxis_title="Diamond Price ($)",
    yaxis_title="Number of Diamonds"
)

st.plotly_chart(fig3, use_container_width=True)
st.subheader("Diamond Price Summary")

if not filtered_df.empty:
    price_summary = pd.DataFrame({
        "Statistic": ["Average Price", "Minimum Price", "Maximum Price"],
        "Price ($)": [
            filtered_df["price"].mean(),
            filtered_df["price"].min(),
            filtered_df["price"].max()
        ]
    })

    st.dataframe(price_summary, use_container_width=True)
else:
    st.warning("No diamonds match your selected filters.")


fig2.update_layout(
    xaxis_title="Carat Weight",
    yaxis_title="Average Price ($)"
)
fig2.add_annotation(
    x=1.0,
    y=5000,
    text="1 carat Example",
    showarrow=True,
    arrowhead=2
)
fig2.update_layout(
    title="Average Diamond Price by Carat",
    xaxis_title="Carat Weight",
    yaxis_title="Average Price ($)"
)

st.plotly_chart(fig2, use_container_width=True)

# Display the chart inside the dashboard
st.plotly_chart(fig, use_container_width=True)
# Let the user select a diamond color
colors = ["All"] + sorted(df["color"].dropna().unique().tolist())

selected_color = st.selectbox(
    "Select diamond color",
    colors
)
# Select diamond cut quality
cuts = ["All"] + sorted(df["cut"].dropna().unique().tolist())

selected_cut = st.selectbox(
    "Select cut quality",
    cuts
)

# Apply cut filter
if selected_cut != "All":
    filtered_df = filtered_df[
        filtered_df["cut"] == selected_cut
    ]

# Select a price range
min_price, max_price = st.slider(
    "Select price range ($)",
    min_value=int(df["price"].min()),
    max_value=int(df["price"].max()),
    value=(500, 5000),
    step=100
)

# Apply the price filter
filtered_df = filtered_df[
    (filtered_df["price"] >= min_price) &
    (filtered_df["price"] <= max_price)
]

# Apply the color filter
if selected_color != "All":
    filtered_df = filtered_df[
        filtered_df["color"] == selected_color
    ]