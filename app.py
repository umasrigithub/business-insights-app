import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.set_page_config(page_title="Unified Analytics View | Umasri Bhavanasi", layout="wide")

# ---------- Data ----------
months = pd.date_range("2025-01-01", periods=12, freq="MS")
revenue = pd.DataFrame({
    "Month": months,
    "Revenue": [420, 450, 470, 495, 530, 565, 590, 610, 640, 675, 710, 745],
    "Orders": [1200, 1260, 1290, 1350, 1415, 1490, 1540, 1605, 1660, 1735, 1810, 1885],
    "AOV": [350, 357, 364, 367, 375, 379, 383, 380, 386, 389, 392, 395],
})

channels = pd.DataFrame({
    "Channel": ["Paid Search", "Organic", "Email", "Retail Partner", "Social"],
    "Spend_k": [180, 40, 35, 90, 120],
    "Revenue_k": [520, 260, 240, 410, 210],
    "CAC": [84, 22, 18, 39, 67],
    "LTV": [190, 210, 225, 170, 120],
})
channels["ROAS"] = (channels["Revenue_k"] / channels["Spend_k"]).round(2)

cohort = pd.DataFrame({
    "Month": ["Month 1", "Month 2", "Month 3", "Month 4", "Month 5", "Month 6"],
    "Retention": [100, 74, 58, 52, 49, 47]
})

products = pd.DataFrame({
    "Product": ["Core Subscription", "Starter Kit", "Premium Bundle", "Retail Exclusive"],
    "Revenue Share %": [46, 18, 27, 9],
    "Growth %": [18, 7, 24, -6]
})

# ---------- Sidebar ----------
st.sidebar.title("Why this experience")
st.sidebar.write(
    "A compact analytics story that shows how I translate fragmented business data into clear decisions."
)
st.sidebar.markdown("**Built to demonstrate:**")
st.sidebar.markdown("- KPI framing\n- Cross-functional analytics thinking\n- Business insight communication\n- Dashboard clarity for leadership")

# ---------- Header ----------
st.title("From Raw Data to Decisions")
st.subheader("A unified analytics view designed to show how I think as an Analytics Lead")

st.markdown(
    "**Umasri Bhavanasi**  \\n"
    "I turn fragmented data into actionable insight by combining data structure, business context, and clear storytelling."
)

st.divider()

# ---------- Problem / Approach ----------
col1, col2 = st.columns([1.2, 1])
with col1:
    st.markdown("### The business problem")
    st.write(
        "Leadership often receives disconnected updates from sales, marketing, customer, and product teams. "
        "That makes it hard to answer simple questions quickly: Which channels are efficient? Where is retention weakening? "
        "Which products drive growth?"
    )
with col2:
    st.markdown("### My approach")
    st.write(
        "I structured this experience around three layers: a unified KPI view, targeted diagnostic analysis, and concise decision-ready insights. "
        "The goal is not just to show charts, but to show how analytics supports action."
    )

# ---------- KPI cards ----------
st.markdown("### Executive KPI snapshot")
k1, k2, k3, k4 = st.columns(4)
k1.metric("Annual Revenue", "$6.9M", "+15.4%")
k2.metric("Orders", "18.9K", "+13.2%")
k3.metric("Avg. Order Value", "$395", "+12.9%")
k4.metric("6-Month Retention", "47%", "-3 pts vs target")

# ---------- Charts ----------
st.markdown("### Unified performance dashboard")
left, right = st.columns(2)

with left:
    line = alt.Chart(revenue).mark_line(point=True).encode(
        x=alt.X("Month:T", title="Month"),
        y=alt.Y("Revenue:Q", title="Revenue ($K)")
    ).properties(height=320)
    st.altair_chart(line, use_container_width=True)

with right:
    bars = alt.Chart(channels).mark_bar().encode(
        x=alt.X("Channel:N", sort="-y"),
        y=alt.Y("ROAS:Q", title="ROAS"),
        tooltip=["Channel", "Spend_k", "Revenue_k", "ROAS"]
    ).properties(height=320)
    st.altair_chart(bars, use_container_width=True)

left2, right2 = st.columns(2)
with left2:
    retention = alt.Chart(cohort).mark_line(point=True).encode(
        x=alt.X("Month:N", title="Cohort Month"),
        y=alt.Y("Retention:Q", title="Retention %")
    ).properties(height=300)
    st.altair_chart(retention, use_container_width=True)
with right2:
    prod = alt.Chart(products).mark_bar().encode(
        x=alt.X("Product:N", sort="-y"),
        y=alt.Y("Revenue Share %:Q"),
        tooltip=["Product", "Revenue Share %", "Growth %"]
    ).properties(height=300)
    st.altair_chart(prod, use_container_width=True)

# ---------- Insights ----------
st.markdown("### What I would tell leadership")
ins1, ins2, ins3 = st.columns(3)
with ins1:
    st.info(
        "**Retention risk**  \nRetention drops sharply after Month 2, which suggests an onboarding or early-value gap. "
        "I would investigate first-use behavior, support touchpoints, and activation milestones."
    )
with ins2:
    st.info(
        "**Channel efficiency**  \nOrganic and Email are the most efficient channels, while Social shows weak LTV/CAC economics. "
        "This points to a budget reallocation opportunity rather than simply increasing spend."
    )
with ins3:
    st.info(
        "**Revenue concentration**  \nCore Subscription drives the largest share of revenue, but Premium Bundle is growing faster. "
        "That suggests expansion through upsell/cross-sell, not just acquisition."
    )

# ---------- How I think ----------
st.markdown("### How I think about analytics")
with st.expander("Open my working style"):
    st.markdown(
        "**1. Define the decision first**  \\n"
        "Before building anything, I anchor on the business question and the KPI that best supports it.  \\n\\n"
        "**2. Create a reliable data structure**  \\n"
        "I bring together fragmented sources into a consistent model so teams are working from one version of the truth.  \\n\\n"
        "**3. Diagnose, then prioritize**  \\n"
        "I go beyond reporting by identifying what changed, why it matters, and where action will have the highest return.  \\n\\n"
        "**4. Communicate clearly**  \\n"
        "I translate analysis into concise recommendations that leadership can act on quickly."
    )

# ---------- Closing ----------
st.divider()
st.markdown("### Why this reflects my fit")
st.write(
    "This experience is intentionally simple, but it reflects how I work: structure messy data, focus on the right metrics, "
    "surface the story behind the numbers, and turn insight into action. That combination of analytics, communication, "
    "and business judgment is what I would bring to this role."
)

st.caption("Built in Streamlit as a compact, decision-oriented analytics experience.")
