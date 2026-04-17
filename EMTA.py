import streamlit as st
import pandas as pd
import duckdb
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("emta_data.csv")

st.write("# Ettevõtluse statistika maakondade lõikes")
"""
"""
col1, col2 = st.columns(2)
with col1:
    aasta = st.selectbox("Aasta", options=sorted(data["aasta"].unique(), reverse=True))
with col2:
    kvartal = st.selectbox(
        "Kvartal", 
        options=duckdb.sql(f""" SELECT DISTINCT kvartal FROM data WHERE aasta = {aasta} ORDER BY kvartal DESC""")
        )

count_by_county = duckdb.sql(f""" 
    SELECT
        maakond, 
        count (distinct registrikood) AS ettevotete_arv
    FROM data
    WHERE Aasta = {aasta} AND Kvartal = {kvartal}
    GROUP BY maakond
    HAVING maakond IS NOT NULL
    ORDER BY ettevotete_arv DESC
""").df()
"""
"""
"""
"""
st.write("### Ettevõtete arv maakondade lõikes / interaktiivne")
"""
"""
st.bar_chart(count_by_county, y="ettevotete_arv", x="maakond", sort=False, horizontal=True)
"""
"""
"""
"""
st.write("### Ettevõtete arv maakondade lõikes")
"""
"""
fig = plt.figure(figsize=(14,5))
sns.barplot(count_by_county, y="ettevotete_arv", x="maakond")
st.pyplot(fig)
"""
"""
"""
"""
st.write("### Ettevõtete arv maakonna & kov lõikes")
"""
"""
Maakond: str = st.selectbox("maakond", options=data["maakond"].unique())
"""
"""
"""
"""
st.write(duckdb.sql(f"""
    SELECT
        kov,
        count(DISTINCT registrikood) AS ettevotete_arv,
        round(avg(kaive) / 3)::int AS keskmine_kuine_kaive,
        round(avg(kaive))::int AS keskmine_kvartaalne_kaive
    FROM data
    WHERE aasta = 2026 AND kvartal = 1
    GROUP BY kov
    ORDER BY kov ASC
""").df())