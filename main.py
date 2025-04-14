import streamlit as st
import json
from PIL import Image
import os

PAGE_TITLE = "HAIDAR SKAIF"
st.set_page_config(page_title=PAGE_TITLE, layout="wide")

def load_font_css():
    font_css = """
    <style>
    @font-face {
        font-family: 'Playfair';
        src: url('assets/fonts/PlayfairDisplay-Regular.ttf') format('truetype');
    }
    @font-face {
        font-family: 'SourceSans';
        src: url('assets/fonts/SourceSansPro-Regular.ttf') format('truetype');
    }

    html, body, [class*="css"]  {
        font-family: 'SourceSans', sans-serif;
        color: #333333;
        background-color: #fff8f0;
    }

    h1, h2, h3, h4 {
        font-family: 'Playfair', serif;
        color: goldenrod;
    }

    .card {
        border: 1px solid #f3e5ab;
        border-radius: 10px;
        background-color: #fffef9;
        padding: 1rem;
        margin-bottom: 1rem;
    }
    </style>
    """
    st.markdown(font_css, unsafe_allow_html=True)

def load_json(path):
    with open(path, 'r', encoding='utf-8') as f:
        return json.load(f)

def render_section(title, items):
    st.markdown(f"## {title}")
    for item in items:
        with st.container():
            st.markdown(f"**{item['title']}** — *{item.get('company', '')}*  \n*{item.get('date', '')} – {item.get('location', '')}*")
            for d in item.get("details", []):
                st.markdown(f"- {d}")

def render_languages(lang_dict):
    st.markdown("## Languages")
    for lang, lvl in lang_dict.items():
        st.progress(lvl / 5, text=lang)

def render_slider(title, data,arg_use_column_width='auto'):
    st.markdown(f"## {title}")
    cols = st.columns(len(data))
    for i, item in enumerate(data):
        with cols[i]:
            st.image(item['image'], use_column_width=arg_use_column_width)
            st.markdown(f"**{item['title']}**")
            st.markdown(item.get('issuer') or f"*{item.get('company', '')} - {item.get('year', '')}*")
            for desc in item.get('description', []):
                st.markdown(f"- {desc}")

def main():
    load_font_css()

    cv_data = load_json("assets/config_files/cv.json")
    projects = load_json("assets/config_files/projects.json")
    certs = load_json("assets/config_files/certificates.json")

    # Sidebar
    with st.sidebar:
        st.image("assets/imgs/mine.png", width=200)
        st.markdown(f"### {cv_data['name']}")
        st.markdown(f"*{cv_data['title']}*")
        st.markdown(f"📧 {cv_data['contact']['email']}")
        st.markdown(f"📞 {cv_data['contact']['phone']}")
        st.markdown(f"📍 {cv_data['contact']['location']}")
        st.markdown(f"[LinkedIn]({cv_data['contact']['linkedin']})")

    # Main sections
    st.title("Curriculum Vitae")

    render_section("Experience", cv_data['experience'])

    st.markdown("## Skills")
    st.markdown(" • " + " | ".join(cv_data["skills"]))

    render_languages(cv_data["languages"])

    st.markdown("## Education")
    for edu in cv_data["education"]:
        st.markdown(f"**{edu['degree']}**, {edu['institution']} — *{edu['location']}*")

    st.markdown("## Philosophy")
    st.info(cv_data["philosophy"])

    render_slider("Projects", projects)
    render_slider("Certificates", certs)

if __name__ == "__main__":
    main()
