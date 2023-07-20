from PIL import Image
import streamlit as st
from streamlit_option_menu import option_menu
import subprocess


st.set_page_config(page_title="SuperTech Solutions", page_icon="lightning-charge", layout="wide")


#--------Sidebar---Main Menu--------
with st.sidebar:
    option = option_menu(
        menu_title= "Main Menu",
        options=["Home", "Fundamentals of Electrictal Engineering", "Analogue Electronics", "Electric Circuit Analysis", "Applied Electromagentics", "Digital Electronics", "Electrical Machines", "Measurements and Instrumentations", "Signals and Systems", "Electrical Machines Analysis and design", "Fundamentals of Power Systems", "Power Electronics"],
        icons=["house-gear-fill"],
        menu_icon="cpu",
        default_index=0,
)

#-----------Selecting From Main Menu-------------

#---------------Home-----------------------------
if option == "Home":
    # Use local css for styling (Contuct us)
    def local_css(file_name):
     with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

    local_css("style/style.css")

    #------Load Assets--------
    img_jedss = Image.open("images/jedss.png")
    img_jeds = Image.open("images/jeds.png")
    #img_super = Image.open("images/super.png")


    #-------HEADER---------
    st.title(":red[SuperT]:blue[ech] :green[Solutions]")      #NB The color-------------------------------------------
    st.subheader(":orange[The Art of Electrical Engineering]")
    st.write("---")
    st.header("ELECTRICAL ENGENEERING EDUCATIONAL CONTENT AND CAREER GUIDANCE")
    st.write("Welcome to our website, the best source for information about electrical engineering education and career guidance. Whether you're a professional hoping to develop your knowledge and advance your career or a student looking to start an exciting adventure in the field of electrical engineering, we have you covered. From basic circuit analysis to advanced topics such as power systems, control systems, and electronics, our engaging tutorials, articles, and videos will help you grasp complex concepts with ease. At our website, we are committed to empowering you with the knowledge and resources you need to succeed in the dynamic field of electrical engineering. Start your journey today and unlock endless possibilities for innovation, growth, and impact.")
    st.write("[Visit our YouTube Channel >](https://www.youtube.com/@joseftomassuper-t2158)")
    st.write("---")


    #------insert image-------
    col1, col2 = st.columns([1,1])
    col1.image(img_jedss, caption='University of Namibia(UNAM), School of Engineering And Built Environment')
    col2.image(img_jeds, caption='JEDS Campus')
    st.write("[Visit the University of Namibia's Websibe >](https://www.unam.edu.na/)")


    #-------CONTUCT US--------
    def left_column():
        left_column
    def right_column():
        right_column

    with st.container():
        st.write("---")
        st.header("Contact Us!")
        # https://formsubmit.co/ 
        contact_form = """ 
        <form action="https://formsubmit.co/joseftomassuper@gmail.com" method="POST">
            <input type="hidden" name="_captcha" value="false">
            <input type="text" name="name" placeholder="Your name" required>
            <input type="email" name="email" placeholder="Your email" required>
            <textarea name="message" placeholder="Your message here" required></textarea>
            <button type="submit">Send</button>
        </form>
        """
        left_column, right_column = st.columns(2)
        with left_column:
            st.markdown(contact_form, unsafe_allow_html=True)
        with right_column:
            st.empty()

#---------------FUNDAMENTALS OF ELECTRICAL ENGINEERING---------------------------------------
if option == "Fundamentals of Electrictal Engineering":
    st.title("Fundamentals of Electrictal Engineering")
#elif module == "" --------------------------------------------------------CONTINUE FROM HERE NEXT TIME


