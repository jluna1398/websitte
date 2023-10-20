import requests
import streamlit as st
from streamlit_lottie import st_lottie

st.title("Jose Luna")
st.text("UC Davis 2023 - B.S in Statistics")
st.download_button("Resume", data='images/c.png')

# st.button("Resume", use_container_width=False)




def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()


lotio_url = "https://lottie.host/64fc4140-e1dd-4d2f-b206-bbe3f5d084ed/4OnXmcbJdw.json"
lottie_download = load_lottieurl(lotio_url)




st.write(
    "Welcome to my personal website. This websites is intenede to serve as my portfolio, where i will be showing the "
    "statistical and data analysis skills I had learn through my school and personal development. I have apassion for fnance, consulting, dta anslysis and fincae. I woile lik wto work in a PWC comanies"
    ""
    "- I want to be a new person"
)
col1, col2 = st.columns(2)
with col1:

    st.write("""
    -   I Easyted U c adbasdasd
    -   Sdasdasd
    -   safsdfgsdgfsdgf
    -   sdfsdfgsdagfsdgsdg
    sfoaish fpoiahsoboi sabh fdoui hasoibaousd foious0fer tqewr tert werytwer hz dbaerhadhaerthtjrstjwrtjrtjssrtjsrtjsrtjpihsdhn qwf8gq powihschqo 0iwfqpwsfowiqpoifb jwfd    
    """)
    st.write("kjashf oisahrh af ih ihf isd hfhdsihd fh i fhqwh fpihfosb dfoihi fhpidsfhphdsf sdf wetewgasery  rturtuwtr uwtryiy¬f hjylryfl dksrjamrjsxdkjhgstm sd hsrhj sfdhjsrjrsjf gjsrtjs rfjsrtjsrtjfsg")
with col2:
    st_lottie(lottie_download, key="hello")

st.write("sdf hisdoufhgohdew rtertewrtertertwerterwtertertertf us8dgfhsr urwuqareyuadfhaeryaeryaeyuhszdncxvhjsr thjxcdfnsrtjhzdfhhjsrtusfgjhsrtjhsrhdgoipshdgoshdouihsoidh s difgapsd hgfioahsw0gfhwqaeoghoisdhvoihsadgokbsd ogihasdhgfpisfvgs")