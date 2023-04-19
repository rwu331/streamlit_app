import streamlit as st


st.title('Title of your application') # give warning, run python3 -m streamlist run app.py
st.markdown('this is **bold text**') # create markdown
st.markdown('this is *italic text*')

st.sidebar.title('title of sidebar') # anything do in streamlit can do in sidebar, but need to specify
st.sidebar.markdown('markdown **text** in the sidebar')

agree = st.checkbox('I agree') # create checkbox

if agree: # if click on checkbox, default is uncheck (don't need else)
    st.write('Great!')  # operation that happens after clicked
    st.markdown('this is markdown **text**')

agree_sidebar = st.sidebar.checkbox('side bar checkbox')

if agree_sidebar:
    #st.write('side bar checked') # wrote on same page
    st.sidebar.write('side bar checked') # wrote in sidebar
    