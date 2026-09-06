"""French bee — Butterfly Run · lanceur Streamlit (code d'accès + jeu embarqué)."""
from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(page_title="French bee — Butterfly Run", page_icon="🦋",
                   layout="wide", initial_sidebar_state="collapsed")

def access_code() -> str:
    try:
        return str(st.secrets["ACCESS_CODE"])
    except Exception:
        return "FRENCHBEE"  # repli local — à remplacer par un secret en production

if "unlocked" not in st.session_state:
    st.session_state.unlocked = False

if not st.session_state.unlocked:
    st.markdown("## 🦋 French bee — Butterfly Run")
    st.write("Entrez le code d'accès pour jouer.")
    code = st.text_input("Code d'accès", type="password",
                         label_visibility="collapsed", placeholder="Code d'accès")
    if st.button("Jouer", type="primary"):
        if code.strip() == access_code():
            st.session_state.unlocked = True
            st.rerun()
        else:
            st.error("Code incorrect. Réessayez.")
    st.caption("Accès réservé — surprise interne French bee.")
    st.stop()

# Strip Streamlit's chrome and let the embedded game fill the whole device
# viewport. The component <iframe> is pinned to the visual viewport (100dvh),
# so the game inside gets real width/height and can be responsive.
st.markdown(
    """
<style>
  header, footer, #MainMenu {visibility: hidden; height: 0;}
  [data-testid='stAppViewBlockContainer'], .block-container,
  [data-testid='stMainBlockContainer'], [data-testid='stVerticalBlock'] {
    padding: 0 !important; margin: 0 !important; max-width: 100% !important; gap: 0 !important;
  }
  [data-testid='stAppViewContainer'], [data-testid='stMain'], .stApp {
    overflow: hidden !important;
  }
  .stApp iframe, iframe[title='streamlit_component_v1'] {
    position: fixed !important;
    top: 0 !important; left: 0 !important;
    width: 100vw !important;
    height: 100vh !important;
    height: 100dvh !important;
    border: 0 !important;
    z-index: 2147483647 !important;
  }
</style>
""",
    unsafe_allow_html=True,
)
components.html((Path(__file__).parent / "game_bundle.html").read_text(encoding="utf-8"),
                height=800, scrolling=False)
