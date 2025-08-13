
import streamlit as st
from pathlib import Path
import base64

# --------- CONFIG ---------
st.set_page_config(
    page_title="Sai Vara Prasad Bhaskarla — Portfolio",
    page_icon="🧰",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown(
    '''
    <style>
    .chip {display:inline-block; padding: .2rem .6rem; margin:.2rem; border-radius: 999px; font-size: .85rem; border: 1px solid rgba(127,127,127,0.3);}
    .muted {opacity:.8}
    </style>
    ''',
    unsafe_allow_html=True
)

# --------- DATA / SETTINGS ---------
RESUME_PATH = Path("assets/resume.pdf")
NAME = "Sai Vara Prasad Bhaskarla"
TAGLINE = "Data Analyst • SQL • Python • R • BI"
LOCATION = "California, USA"
EMAIL = "bhaskarlasvprasad@gmail.com"
LINKEDIN = "https://linkedin.com/in/bhaskarla-sai-vara-prasad"
GITHUB = "https://github.com/Svprasad01"

PROJECTS = [
    {
        "title": "Medicaid PMPM Cost Forecasting",
        "description": "Python time-series + regression models to forecast monthly PMPM and catch overruns.",
        "highlights": ["Pandas", "NumPy", "Time Series", "Power BI"],
        "links": {"Code": "https://github.com/Svprasad01"}
    },
    {
        "title": "Refund Anomaly Detection for Payments",
        "description": "ETL + rolling-window analytics to flag abnormal refunds, recovering ~$75K.",
        "highlights": ["Talend", "AWS S3", "Python", "PostgreSQL", "Tableau"],
        "links": {"Code": "https://github.com/Svprasad01"}
    },
    {
        "title": "Claims Trend Dashboards",
        "description": "Tableau/Power BI dashboards for utilization & avoidable ER insights.",
        "highlights": ["SQL", "Tableau", "Power BI", "Excel/VBA"],
        "links": {"Code": "https://github.com/Svprasad01"}
    },
]

SKILLS = {
    "Languages": ["Python", "R", "SQL"],
    "Data/ML": ["NumPy", "Pandas", "scikit-learn", "TensorFlow", "Seaborn", "EDA", "Forecasting"],
    "BI": ["Tableau", "Power BI", "Excel (VLOOKUP, Pivots, Macros)"],
    "Databases": ["MySQL", "SQL Server", "PostgreSQL", "MongoDB"],
    "Cloud/ETL": ["AWS", "SSIS", "Talend"],
    "Methods": ["A/B Testing", "Hypothesis Testing", "ANOVA", "Regression", "Clustering", "Classification"]
}

EXPERIENCE = [
    {"role": "Data Analyst", "org": "Molina Healthcare", "period": "Aug 2024 — Present",
      "bullets": [
          "Unified 1.2M+ Medicaid claims for trend analysis; improved per-member cost tracking by 30%.",
          "Built Python forecasting for PMPM; supported rate planning and reduced misalignment by $800K.",
          "Identified avoidable ER cost spikes; drove interventions cutting ER costs by 9%.",
          "Automated variance reporting in Power BI/Excel; helped catch $1.7M in overruns."
      ]},
    {"role": "Data Analyst", "org": "Druva Software", "period": "Jun 2021 — Jul 2023",
      "bullets": [
          "Automated Talend ETL from S3/MySQL/CSV; daily refreshes with schema validation.",
          "Python validation prevented corrupted inputs; improved anomaly detection integrity.",
          "Recovered ~$75K via rolling-window trend analysis and refund anomaly detection.",
          "Built Tableau dashboards; informed prioritization of 3 system patch releases."
      ]},
]

# --------- HELPERS ---------
def download_button_from_file(path: Path, label: str):
    if not path.exists():
        st.info("Add your resume at **assets/resume.pdf** and the download button will appear here.")
        return
    with open(path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
    href = f'<a href="data:application/octet-stream;base64,{b64}" download="{path.name}">{label}</a>'
    st.markdown(href, unsafe_allow_html=True)

def section_header(title: str, subtitle: str | None = None, icon: str = "🧭"):
    left, right = st.columns([0.85, 0.15], vertical_alignment="center")
    with left:
        st.subheader(f"{icon} {title}")
        if subtitle:
            st.caption(subtitle)
    with right:
        st.write("")

def show_about():
    section_header("About", "Who I am & what I love building", "👋")
    st.write(f"### {NAME}")
    st.write(TAGLINE)
    st.write(f"📍 {LOCATION}")
    st.markdown(f"🔗 [LinkedIn]({LINKEDIN}) • [GitHub]({GITHUB}) • ✉️ [{EMAIL}](mailto:{EMAIL})")

    st.write("—")
    st.write("Results-driven Data Analyst experienced across healthcare and financial domains. I build reliable data pipelines, clear dashboards, and pragmatic models that support decisions.")

    cols = st.columns(2)
    groups = list(SKILLS.items())
    for i, (group, items) in enumerate(groups):
        with cols[i % 2]:
            st.markdown(f"**{group}**")
            st.markdown(" ".join([f'<span class="chip">{x}</span>' for x in items]), unsafe_allow_html=True)

    st.write("—")
    st.write("**Resume**")
    download_button_from_file(RESUME_PATH, "⬇️ Download my resume")

def show_projects():
    section_header("Projects", "Curated, impact-first selection", "🧰")
    for proj in PROJECTS:
        with st.container(border=True):
            st.markdown(f"### {proj['title']}")
            st.markdown(proj["description"])
            if proj.get("highlights"):
                st.markdown(" ".join([f'<span class="chip">{x}</span>' for x in proj["highlights"]]), unsafe_allow_html=True)
            if proj.get("links"):
                link_bits = []
                for name, url in proj["links"].items():
                    if url:
                        link_bits.append(f"[{name}]({url})")
                if link_bits:
                    st.markdown(" • ".join(link_bits))

def show_resume():
    section_header("Resume", "Inline view (optional)", "📄")
    if RESUME_PATH.exists():
        st.write("Inline preview:")
        try:
            base64_pdf = base64.b64encode(RESUME_PATH.read_bytes()).decode('utf-8')
            pdf_display = f'<iframe src="data:application/pdf;base64,{base64_pdf}" width="100%" height="900" type="application/pdf"></iframe>'
            st.markdown(pdf_display, unsafe_allow_html=True)
        except Exception as e:
            st.warning(f"Could not embed PDF: {e}")
    else:
        st.info("Add your resume at **assets/resume.pdf** to enable the inline preview.")
    st.write("—")
    download_button_from_file(RESUME_PATH, "⬇️ Download my resume")

def show_contact():
    section_header("Contact", "Reach out for roles, collabs, or coffee ☕", "📬")
    st.write("I'm open to roles in data analytics and data engineering.")
    st.markdown(f"- ✉️ Email: [{EMAIL}](mailto:{EMAIL})")
    st.markdown(f"- 💼 LinkedIn: [{LINKEDIN}]({LINKEDIN})")
    st.markdown(f"- 🐙 GitHub: [{GITHUB}]({GITHUB})")
    st.write("—")
    st.write("Prefer a quick note?")
    with st.form("contact_form", border=True):
        name = st.text_input("Your name")
        message = st.text_area("Message")
        send = st.form_submit_button("Copy to clipboard")
        if send:
            st.code(f"""Hi {NAME},

My name is {name}.
{message}

— Sent via your Streamlit portfolio
""", language="markdown")

def show_experience():
    section_header("Experience", "Roles, impact, and accomplishments", "💼")
    for item in EXPERIENCE:
        with st.container(border=True):
            st.markdown(f"**{item['role']}**, {item['org']}")
            st.caption(item["period"])
            for b in item["bullets"]:
                st.markdown(f"- {b}")

# --------- SIDEBAR NAV ---------
st.sidebar.title("Navigate")
page = st.sidebar.radio("Go to", ["About", "Projects", "Experience", "Resume", "Contact"], index=0)

if page == "About":
    show_about()
elif page == "Projects":
    show_projects()
elif page == "Experience":
    show_experience()
elif page == "Resume":
    show_resume()
else:
    show_contact()

st.sidebar.markdown("---")
st.sidebar.caption("Made with Streamlit")
