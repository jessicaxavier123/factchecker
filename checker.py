from openai import OpenAI
import jsonlines
import streamlit as st
# Initialize OpenAI client
client = OpenAI(
    api_key="sk-70cdffb7a20b40adacc2998c436e6ed5",
    base_url="https://dashscope.aliyuncs.com/compatible-mode/v1"
)
def generate_and_print(client, q):
    st.write(f'{q}')
    # Prepare the input for the model
    input_text = f"""Here is a statement:
    {q}
    Is this statement correct? You can use tools to find information if needed.
    The final response is FALSE if the statement is FALSE. Otherwise, TRUE."""
    # Call the model
    completion = client.chat.completions.create(
        model="deepseek-r1",
        messages=[
            {'role': 'user', 'content': input_text}
        ]
    )
    answer = completion.choices[0].message.content
    #st.write(f"Generated Answer: {answer}")
    return answer
@st.cache_data
def read_questions():
    file = './knowledge_qa_test.jsonl'
    questions = []
    with jsonlines.open(file, 'r') as json_f:
        for data in json_f:
            questions.append(data)
    return questions
def main():
    st.set_page_config(layout= "wide")
    #st.image("https://e7.pngegg.com/pngimages/60/499/png-clipart-banner-logo-brand-flag-decal-god-bless-the-child-flag-bald-eagle.png", use_container_width=True,width=50)
    image_url = "https://images.rawpixel.com/image_png_800/cHJpdmF0ZS9sci9pbWFnZXMvd2Vic2l0ZS8yMDIzLTA4L3Jhd3BpeGVsX29mZmljZV8xMF9lYWdsZV9pc29sYXRlZF9vbl93aGl0ZV9iYWNrZ3JvdW5kXzQ1MzllOTY1LTc4ZDQtNGY3Yy1iNTFhLTU5YTc2ZjYwY2IxYi5wbmc.png"# Custom CSS to set the eagle image as background along with other styles
    st.markdown(
    """
    <style>
    /* Change overall background color to Dark Navy Blue */
    .stApp {
        background-color: #000080 !important; /* Dark Navy Blue */
        color: #FFFFFF !important; /* White text */
    }
    /* Primary button color (Gray) */
    .stButton>button {
        background-color: #808080 !important; /* Gray */
        color: white !important;
        font-weight: bold;
        border-radius: 8px;
        border: 2px solid #808080; /* Gray border */
    }
    /* Sidebar background (Light Gray for contrast) */
    .stSidebar {
        background-color: #F0F0F0 !important; /* Light Gray */
        border-radius: 8px;
    }
    /* Text input, select box, and text area */
    .stTextInput, .stSelectbox, .stMultiselect, .stTextArea {
        background-color: #F0F0F0 !important; /* Light Gray */
        border-radius: 8px;
    }
    /* Title (Red) */
    h1 {
        color: #FF0000 !important; /* Red */
    }
    /* Subtitles (White) */
    h2, h3 {
        color: #FFFFFF !important; /* White */
    }
    /* Links (Royal Blue) */
    a {
        color: #4169E1 !important; /* Royal Blue */
        font-weight: bold;
    }
    /* Customizing success messages (Green text, Light Green background) */
    .stAlert, .stSuccess {
        background-color: #CCFFCC !important; /* Very Light Green */
        color: #008000 !important; /* Dark Green Text */
        font-weight: bold;
        padding: 10px;
        border-radius: 5px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
    st.title("Political Fact Checker")
    col1, col2=st.columns((2,2))
    with col1:
        st.subheader("This platform is a tool designed to provide accurate information regarding news today. In light of changing events being brought on by new orders from the government, it's important to stay informed with the most up to date information. Use this tool to double check any questions and/or inquiries about the latest news.")
        #questions = read_questions()
        #for data in questions:
            #st.write("Prompt:", data.get("prompt", ""))
            #st.write("Response:", data.get("response", ""))
        fact_to_check = st.text_input("Fact Input","")
        if st.button("Submit"):
            st.success("Processing, please wait...")
            #answer = generate_and_print(client, fact_to_check)
            #st.session_state["fact_check_result"] = answer  # Store result in session state
    with col2:
        st.image(image_url, use_container_width=True)
        st.subheader("Fact-Check Result")
        answer = generate_and_print(client, fact_to_check)
        st.session_state["fact_check_result"] = answer
        # Display fact-checking result if available
        if "fact_check_result" in st.session_state:
            st.write(st.session_state["fact_check_result"])
if __name__ == "__main__":
    main()
