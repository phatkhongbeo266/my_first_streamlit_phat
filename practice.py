import streamlit as st

st.title("HTML Basic Examples")

left,middle, right = st.columns([3,14,3])
if left.button("<Previous",type = "primary", use_container_width = True):
    left.markdown("Undeveloped")

if right.button("Next>",type = "primary", use_container_width = True):
    right.markdown("Undeveloped")
st.divider()
st.text("""In this chapter we will show some basic HTML examples.
Don't worry if we use tags you have not learned about yet.""")
st.divider()
st.header("HTML Documents")
st.markdown("""
All HTML documents must start with a document type declaration: :grey-background[:red[<!DOCTYPE html>]].

The HTML document itself begins with <html> and ends with :grey-background[:red[</html>]].

The visible part of the HTML document is between <body> and :grey-background[:red[</body>]].
            
""")

code = """
<!DOCTYPE html>
<html>
<body>

<h1>My First Heading</h1>
<p>My first paragraph.</p>

</body>
</html>
"""

container = st.container(border=True)
container.subheader("Example")
container.code(code,language = "HTML")
container.link_button("Try it yourself >>",
"https://www.w3schools.com/html/tryit.asp?filename=tryhtml_basic_document",
type="primary")

add_selectbox = st.sidebar.selectbox(
    "How would you like to be contacted?",
    ("Email", "Home phone", "Mobile phone")
)

# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )