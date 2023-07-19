import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(layout = "wide")

df = pd.read_csv(StudentsPerformance.csv)
df['Average_marks'] = df.mean(axis=1)

st.title(':green[Student Dataset] Analysis :girl: :boy: :bar_chart:') 
st.markdown("This dashboard helps us to explore the **relationship** between ***marks*** of students and their ***attributes.*** ")
st.sidebar.header("Dashboard `Project 1`")

### METRICS
st.markdown('### Metrics')
col1, col2, col3 = st.columns(3)
col1.metric("Writing Score",df['writing score'].mean())
col2.metric("Reading Score", df['reading score'].mean())
col3.metric("Math Score", df['math score'].mean())

##--------
##CONTAINER

container = st.container()
chart1, chart2 = container.columns(2)

### GRAPH 2
with chart1:
    st.sidebar.subheader("SCATTER: Gender")
    ed = st.sidebar.selectbox('Color by',(df["gender"].unique()))
    filtered_df = df[df["gender"] == ed]
    st.markdown("### Reading, Writing and Math Score")
    fig3 =  px.scatter(filtered_df,x='reading score',y='writing score',size='math score',color='lunch',width=350,height=400)
    st.plotly_chart(fig3)

### GRAPH 3
with chart2:
    st.markdown("### Average Marks according to attributes")
    fig4 = px.sunburst(df, path=['gender', 'lunch', 'test preparation course'],values='Average_marks', color='gender',width=350,height=400)
    st.plotly_chart(fig4)

### GRAPH 1
#Creating sidebar and slider
st.sidebar.subheader("BAR: Test Preparation Course")
gender_color = st.sidebar.selectbox('Color by',(df['test preparation course'].unique()))
plot_height = st.sidebar.slider('Specify plot height', 300, 500, 400)

#Linking graph and slidebar
filtered_df = df[df["test preparation course"] == gender_color]

#Row A
st.markdown("### Average Marks and Parental level of Education")
fig2= px.bar(filtered_df, x="gender", y="Average_marks",color='race/ethnicity',barmode='stack')

#Linking graph and slider
fig2.update_layout(height=plot_height)

#Displaying graph
st.plotly_chart(fig2)

st.sidebar.markdown('''
---
Created by Sneha Gupta!
''')

