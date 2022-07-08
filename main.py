import streamlit as st
import pandas as pd
import numpy as np
from data_university import *
from weather import *

st.title(' 💬 Hello there... Nice you made it to the page ')

def space(num_lines=1):
    """Adds empty lines to the Streamlit app."""
    for _ in range(num_lines):
        st.write("")
space(2)

name = st.text_input("Enter your name")

if not name:
    st.warning("This field needs to be filled")

space(1)
x = st.slider('How are you?', min_value=0, max_value=10, value=5)

space(1)
def mood_categorizer(x):
    if x in range(3, 6):
        st.write('Okay ',x,' good enough :sunglasses:')
    elif x == 10:
        st.write('Can not be better. Great. :)')
    elif x >= 6:
        st.write(x,
                 '!!! Wow cool glad to read this. However I hope your good mood will not distract you from going through this page :P',
                )
    else:
        st.write('Awh ', name, 'okay lets try to find out the reasons why that is.\n Now ask yourself is it possible to change?\n YES? Then You can do it :)')


mood_categorizer(x)
space(2)
st.title('🎓 University Choices')
space(2)


df = create_df()
source = df['City'].unique().tolist()
selected_options = st.multiselect("Filter on city", source, source[:3])
filtered_df = df[df["City"].isin(selected_options)]

st.write(filtered_df.to_html(escape=False, index=False), unsafe_allow_html=True)


st.write('* WS = Winter Semester = September')
st.write('* Sos = Sommer Semester = ?')


space(2)


st.header('My Opinion')
space(1)
st.write('To be honest, I would not choose a Math Study for you. Though it is not included. '
         'Not that I think you can not do it, just that it is very dry study, in the sense that it is extremely theoretical. '
         'Also it does not help so much in the future job.')
st.write('I would choose some applied studies such as Econometrics or Computational Social Science. However I could not yet find them in '
         'Germany but I will continue looking through some more universities and websites.')
st.write('Why I think it is the best? --> As it is the most related to real world scenarios.')
st.write('Also I saw that a lot of universities have a Zulassungsbeschrankung, I have no clue how you were doing at '
         'high school neither what kind of specialisation. BUT the hu-berlin for Informatik does not have any so that is great :smiley:'
         'This would be a goood option?')

space(2)
url = "https://careers.adyen.com/career-types/nextgen"

st.write('Next I would apply during my studies to work as a working student. I did not have enough time to look for'
         ' a lot of companies which give this possibilities. Adyen does and  the students also get paid. I think this is the best way to enter '
         'in a company. Also there is an office in Berlin. Everything is in english, I also checked the Berlin office channel they are all'
         ' talking in English in the chats. [Check Adyen NextGen Program](%s)' % url)
st.write('Also I would talk with different people it is not completely necessary to study something technical to enter. Talk to Efi, '
         'I think her program was  not technical, also those people are needed and then you can always change while working in the company. '
         'The only thing is that the pool of people is bigger so it is more difficult :grimacing:. And not all companies give you the opportunity to switch departments.-')

space(3)
st.write('I hope I could help you a bit... But what you do out of it is on you. Also to find out what you would like to do.')


st.header('Anyway ')
city = st.text_input("In which City are you? ")

if st.button("search"):
    if city != '':
        city = city + " weather"
        st.write(weather(city))
    else:
        pass


