import streamlit as st
import pandas as pd
import duckdb
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("emta_data.csv") 

st.write("# Palgad tööstusharude lõikes")
"""
"""
TAX_PERCENTAGE = 0.338 
salary_stats = duckdb.sql(f""" 
    SELECT 
        tegevusala,
        ROUND(avg(toojoumaksud / {TAX_PERCENTAGE} / tootajate_arv / 3), 2) AS keskmine_palk
    FROM data
    WHERE aasta = 2026 AND kvartal = 1 AND tegevusala IS NOT NULL
    GROUP BY tegevusala
    ORDER BY keskmine_palk DESC
    """).df()
"""
"""
"""
"""
st.write("### Tegevusala keskmine palk töötaja kohta")

"""
"""
st.write(salary_stats)
"""
"""
"""
"""
st.write("### Tegevusala keskmine palk töötaja kohta / interaktiivne")

"""
"""
st.bar_chart(salary_stats, x="tegevusala", y="keskmine_palk", sort=False, horizontal=True)