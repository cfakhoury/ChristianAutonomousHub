import streamlit as st
import pandas as pd
import pydeck as pdk

# Official 2025 data for major digital banks
banks = {
    "Chime": {
        "HQ": "United States",
        "Regulatory Status": "FDIC insured via partner banks",
        "Active Users (2025)": "8.6M",
        "2024 Revenue": "$1.7B",
        "Q1 2025 Revenue": "$518M",
        "Business Model": "76% interchange-driven (2024)",
        "Notes": "IPO June 2025; SpotMe and MyPay features; 67% use as primary account (2025)",
        "Latitude": 37.7749,
        "Longitude": -122.4194,
    },
    "SoFi": {
        "HQ": "United States",
        "Regulatory Status": "Full bank charter",
        "Members (2025)": "10.9M",
        "Q1 2025 Revenue": "$772M",
        "Q1 2025 Net Income": "$71M",
        "Business Model": "Diversified (lending, tech, services)",
        "Notes": "High APY; cross-product ecosystem; 15.9M total products (2025)",
        "Latitude": 37.7749,
        "Longitude": -122.4194,
    },
    "Ally Bank": {
        "HQ": "United States",
        "Regulatory Status": "Full bank charter",
        "Customers (2024)": "~11M",
        "2024 Deposits": "$143B",
        "2024 Consumer Loans": "$100.8B",
        "Business Model": "75% net interest income (2023)",
        "Notes": "High-yield savings; digital-only; 24/7 support",
        "Latitude": 42.3314,
        "Longitude": -83.0458,
    },
    "Monzo": {
        "HQ": "United Kingdom",
        "Regulatory Status": "FSCS insured",
        "Customers (2025)": "12M+",
        "2025 Revenue": "£1.2B (+48%)",
        "2025 Profit": "£113.9M (8x increase)",
        "Weekly Active Users (2025)": "6.9M",
        "Notes": "Subscription and savings growth; 1M+ paid subscribers (2025)",
        "Latitude": 51.5074,
        "Longitude": -0.1278,
    },
    "Revolut": {
        "HQ": "United Kingdom",
        "Regulatory Status": "UK banking license mobilization phase",
        "Customers (2025)": "52M+",
        "2025 Revenue": "£3.1B (+72%)",
        "2025 Profit Before Tax": ">£1B",
        "Notes": "Multi-currency, crypto, premium tiers; FSCS coverage pending",
        "Latitude": 51.5074,
        "Longitude": -0.1278,
    },
    "Nubank": {
        "HQ": "Brazil",
        "Regulatory Status": "Licensed bank",
        "Q1 2025 Revenue": "$3.2B (+40%)",
        "Q1 2025 Net Earnings": "$606.5M (+62%)",
        "Credit Portfolio (2025)": "$24.1B",
        "Notes": "Leading LatAm neobank",
        "Latitude": -23.5505,
        "Longitude": -46.6333,
    },
}

st.title("Digital Banking Sector Dashboard (2025)")

# Interactive globe map using PyDeck
map_data = pd.DataFrame(
    [
        {
            "Bank": name,
            "lat": info["Latitude"],
            "lon": info["Longitude"],
        }
        for name, info in banks.items()
    ]
)

layer = pdk.Layer(
    "ScatterplotLayer",
    data=map_data,
    get_position="[lon, lat]",
    get_color="[200, 30, 0, 160]",
    get_radius=200000,
    pickable=True,
)

view_state = pdk.ViewState(latitude=20, longitude=0, zoom=0.5, pitch=0)

deck = pdk.Deck(layers=[layer], initial_view_state=view_state, map_style="mapbox://styles/mapbox/light-v9")

st.pydeck_chart(deck)

# Select bank for details
def display_bank_details(bank_name):
    st.subheader(bank_name)
    info = banks[bank_name]
    for key, value in info.items():
        if key in ["Latitude", "Longitude"]:
            continue
        st.write(f"**{key}:** {value}")

selected_bank = st.selectbox("Select a Digital Bank for details", list(banks.keys()))
if selected_bank:
    display_bank_details(selected_bank)

# Comparative table
st.markdown("## Bank Summary")
summary_cols = [k for k in list(banks[next(iter(banks))].keys()) if k not in ["Latitude", "Longitude"]]
summary_df = pd.DataFrame([{ "Bank": name, **{k: info.get(k, "Not disclosed") for k in summary_cols} } for name, info in banks.items()])
summary_df = summary_df.set_index("Bank")
st.table(summary_df)

# Consumer decision considerations
st.markdown("## Consumer Decision Considerations")
st.markdown("- Will my money be safe?\n- How much are their fees?\n- When can I get my money?\n- What are the interest rates?\n- What other benefits/features do they have?")

# Market and Industry Insights
st.markdown("## Market and Industry Insights (2025)")
st.write(
    "Open banking, embedded finance, and AI-driven personalization continue to shape the sector. "
    "Regulatory developments such as Revolut's UK banking license mobilization and Chime's IPO in 2025 highlight the evolving landscape. "
    "Consumers increasingly expect instant access, low fees, and high APY offerings. "
    "Monzo reported an eightfold profit increase, Chime completed its IPO, and Nubank's earnings grew 62% year over year."
)
