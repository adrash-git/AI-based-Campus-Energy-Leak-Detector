import streamlit as st
from data_engine import generate_mock_data, calculate_leak_scores
from recommendations import get_ai_recommendations

st.set_page_config(page_title="AI Campus Energy Monitor", layout="wide")
st.title("⚡ AI-Based Campus Energy Leak Detector")

# Data Load
df = generate_mock_data()
df = calculate_leak_scores(df)

# Sidebar for Filtering
selected_room = st.sidebar.selectbox("Select Room", df['Room'].unique())
room_data = df[df['Room'] == selected_room]

# Dashboard Metrics
col1, col2, col3 = st.columns(3)
col1.metric("Current Avg Usage", f"{room_data['Usage_kW'].mean():.2f} kW")
col2.metric("Leak Alerts", len(room_data[room_data['Leak_Score'] > 0]))
col3.metric("Status", "Action Required" if room_data['Leak_Score'].max() > 10 else "Optimized")

# Table & Recommendations
st.subheader(f"Usage Logs for {selected_room}")
room_data['Actionable_Insight'] = room_data.apply(get_ai_recommendations, axis=1)
st.dataframe(room_data)

# Leak Visualization
st.line_chart(room_data.set_index('Hour')[['Usage_kW', 'Leak_Score']])