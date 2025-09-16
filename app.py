import streamlit as st
import random
import string

st.set_page_config(page_title="🔐 Password Generator", page_icon="🔑")

st.title("🔐 Secure Password Generator")
st.write("Generate strong and secure passwords based on your preferences!")

# User settings
length = st.slider("Password length", min_value=6, max_value=32, value=12)
include_digits = st.checkbox("Include digits (0-9)", value=True)
include_symbols = st.checkbox("Include symbols (!, @, #, ...)", value=True)
include_uppercase = st.checkbox("Include uppercase letters (A-Z)", value=True)
include_lowercase = st.checkbox("Include lowercase letters (a-z)", value=True)

if st.button("Generate Password"):
    characters = ""
    if include_digits:
        characters += string.digits
    if include_symbols:
        characters += string.punctuation
    if include_uppercase:
        characters += string.ascii_uppercase
    if include_lowercase:
        characters += string.ascii_lowercase

    if characters:
        password = "".join(random.choice(characters) for _ in range(length))
        st.success("Your generated password:")
        st.code(password, language="text")
    else:
        st.error("You must select at least one character type!")
