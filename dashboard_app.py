import streamlit as st
import pandas as pd

# Data for banks
banks = {
    "Chime": {
        "HQ": "United States",
        "Regulatory Status": "FDIC insured via partner banks",
        "Active Users (2025)": "8.6M",
        "2024 Revenue": "$1.7B",
        "Q1 2025 Revenue": "$518M",
        "Business Model": "76% interchange-driven (2024)",
        "Notes": "IPO June 2025; SpotMe and MyPay features; 67% use as primary account (2025)"
    },
    "SoFi": {
        "HQ": "United States",
        "Regulatory Status": "Full bank charter",
        "Members (2025)": "10.9M",
        "Q1 2025 Revenue": "$772M",
        "Q1 2025 Net Income": "$71M",
        "Business Model": "Diversified (lending, tech, services)",
        "Notes": "High APY; cross-product ecosystem; 15.9M total products (2025)"
    },
    "Ally Bank": {
        "HQ": "United States",
        "Regulatory Status": "Full bank charter",
        "Customers (2024)": "~11M",
        "2024 Deposits": "$143B",
        "2024 Consumer Loans": "$100.8B",
        "Business Model": "75% net interest income (2023)",
        "Notes": "High-yield savings; digital-only; 24/7 support"
    },
    "Monzo": {
        "HQ": "United Kingdom",
        "Regulatory Status": "FSCS insured",
        "Customers (2025)": "12M+",
        "2025 Revenue": "£1.2B (+48%)",
        "2025 Profit": "£113.9M (8x increase)",
        "Weekly Active Users (2025)": "6.9M",
        "Notes": "Subscription and savings growth; 1M+ paid subscribers (2025)"
    },
    "Revolut": {
        "HQ": "United Kingdom",
        "Regulatory Status": "UK banking license mobilization phase",
        "Customers (2025)": "52M+",
        "2025 Revenue": "£3.1B (+72%)",
        "2025 Profit Before Tax": ">£1B",
        "Notes": "Multi-currency, crypto, premium tiers; FSCS coverage pending"
    },
    "Nubank": {
        "HQ": "Brazil",
        "Regulatory Status": "Licensed bank",
        "Q1 2025 Revenue": "$3.2B (+40%)",
        "Q1 2025 Net Earnings": "$606.5M (+62%)",
        "Credit Portfolio (2025)": "$24.1B",
        "Notes": "Leading LatAm neobank"
    }
}

st.title("Digital Banking Sector Dashboard (2025)")

selected_bank = st.selectbox("Select a Digital Bank", list(banks.keys()))

if selected_bank:
    info = banks[selected_bank]
    st.subheader(selected_bank)
    for key, value in info.items():
        st.write(f"**{key}:** {value}")


st.markdown("## Bank Summary")
st.table(pd.DataFrame(banks).T)
