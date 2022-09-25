import streamlit as st
import pandas as pd
import seaborn as sns

# Title of  the dashborad
st.title('Breast Cancer Diagnostic')

@st.cache
def load_data():
    """Utility function for loading the Breastcencer dataset as a dataframe."""
    df = pd.read_table(r'C:\Users\user\Documents\JupyterWork\CMSE830_FDS\clean_data.csv',sep=',')

    return df

# load dataset
data = load_data()
numeric_columns = data.select_dtypes(['float64', 'float32', 'int64', 'int32']).columns
category_columns = data.select_dtypes(['object']).columns
print(category_columns)

#checkbox widget
checkbox = st.sidebar.checkbox("Reveal data")

if checkbox:
    # st.write(data)
    st.dataframe(data=data)


# create histograms
st.sidebar.subheader("Histogram setup")
select_box3 = st.sidebar.selectbox(label="Feature",options=numeric_columns)
histogram_slider = st.sidebar.slider(label="Number of Bins", min_value=5, max_value=100, value=30)
fig_2 = sns.displot(data[select_box3], bins=histogram_slider)
st.pyplot(fig_2)

# create scatterplots
st.sidebar.subheader("Scatter plot setup")
# add select widget
select_box7 = st.sidebar.selectbox(label='Scatter plot hue', options=category_columns)
select_box1 = st.sidebar.selectbox(label = "X axis", options = numeric_columns)
select_box2 = st.sidebar.selectbox(label = "Y axis", options = numeric_columns)
fig_1 = sns.relplot(x=select_box1, y=select_box2, hue = select_box7, data=data, kind="line")
st.pyplot(fig_1)

# create catlpot
st.sidebar.subheader("Cat plot setup")
select_box8 = st.sidebar.selectbox(label="Cat plot hue", options=category_columns)
select_box9 = st.sidebar.selectbox(label="Catogory", options=category_columns)
select_box10 = st.sidebar.selectbox(label="x-axis", options = numeric_columns)
fig_4 = sns.catplot(x=select_box9, y=select_box10, hue=select_box8, data=data, kind="box")
st.pyplot(fig_4)

st.text('For IndexError, please select the different x and y options') 
st.text('under the Joint plot setup on your left sidebar!')

# create jointplots
st.sidebar.subheader("Joint plot setup")
select_box6 = st.sidebar.selectbox(label="Joint plot hue", options=category_columns)
select_box4 = st.sidebar.selectbox(label="x (Please select the option different from y's)", options=numeric_columns)
select_box5 = st.sidebar.selectbox(label="y (Please select the option different from x's)", options=numeric_columns)
fig_3 = sns.jointplot(x=select_box4, y=select_box5, hue = select_box6 ,data=data, kind="kde")


st.pyplot(fig_3)