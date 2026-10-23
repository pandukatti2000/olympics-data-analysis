
import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Olympics Data Analysis",
    page_icon="🏅",
    layout="wide"
)

st.title("🏅 Olympics Data Analysis Dashboard")
st.markdown(
    "Explore Olympic participation, athletes, sports, "
    "and medal trends."
)

st.info(
    "This is a demonstration dashboard using illustrative data. "
    "It is not connected to the original PostgreSQL database."
)

# Summary metrics
c1, c2, c3, c4 = st.columns(4)
c1.metric("Olympic Games", "30+")
c2.metric("Sports", "Multiple")
c3.metric("Athletes", "Historical data")
c4.metric("Analysis", "5 themes")

st.divider()

st.header("Explore the project")

tab1, tab2, tab3, tab4, tab5 = st.tabs([
    "Overview",
    "Sports & Events",
    "Athletes",
    "Medals",
    "Regional Participation"
])

with tab1:
    st.subheader("Olympic data overview")
    st.write(
        "This project analyzes historical Olympic data using "
        "PostgreSQL, SQL, Python, Excel, and Power BI."
    )
    st.markdown("""
    - Database exploration and data quality checks
    - 18 SQL exploratory analysis questions
    - Five Power BI dashboard pages
    - Analysis of participation, demographics, and medals
    """)

with tab2:
    st.subheader("Sports and events")
    sports = pd.DataFrame({
        "Sport": ["Athletics", "Swimming", "Gymnastics",
                  "Cycling", "Fencing"],
        "Analysis focus": [
            "Events and participation",
            "Events and participation",
            "Events and participation",
            "Events and participation",
            "Events and participation"
        ]
    })
    st.dataframe(sports, use_container_width=True)
    st.caption("Illustrative examples, not calculated project results.")

with tab3:
    st.subheader("Athlete demographics")
    st.write(
        "The original analysis explores athlete participation "
        "and available age, height, and weight information."
    )
    st.warning(
        "Some source records contain missing or zero-valued "
        "height and weight placeholders."
    )

with tab4:
    st.subheader("Medal analysis")
    st.write(
        "The project investigates medal distributions and "
        "participation across Olympic Games."
    )
    st.caption(
        "No medal totals are displayed here because the original "
        "database is not connected to this public demonstration."
    )

with tab5:
    st.subheader("Regional participation")
    st.write(
        "The project explores participation by region and "
        "historical changes in country or region representation."
    )
    st.warning(
        "Historical regional mappings and multiple person-region "
        "records require careful interpretation."
    )

st.divider()
st.header("Project deliverables")
st.markdown(
    "[View the complete project and documentation on GitHub]"
    "(https://github.com/pandukatti2000/olympics-data-analysis)"
)
st.caption(
    "Created as an Olympic Games sports analytics project."
)
