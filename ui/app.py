import streamlit as st
import os
import subprocess

st.title("🤖 Codebase Genius")
st.write("Automatically generate documentation for any GitHub repository.")

repo_url = st.text_input("Enter GitHub Repository URL", "https://github.com/pallets/flask")

if st.button("Generate Documentation"):
    st.info("Running Codebase Genius, please wait...")
    try:
        result = subprocess.run(
            ["jac", "run", "main.jac", f'repo_url="{repo_url}"'],
            capture_output=True, text=True
        )
        st.code(result.stdout)
        st.success("Documentation generated! Check 'outputs/' folder.")
        st.write("### Preview of docs.md:")
        files = os.listdir("outputs")
        latest = max(files, key=lambda f: os.path.getctime(os.path.join("outputs", f)))
        st.text(open(os.path.join("outputs", latest), encoding="utf-8").read()[:1500])
    except Exception as e:
        st.error(f"Error: {e}")
