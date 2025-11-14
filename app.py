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

# --------- DATA ---------
RESUME_PATH = Path("assets/resume.pdf")
NAME = "Sai Vara Prasad Bhaskarla"
TAGLINE = "Data Analyst • SQL • Python • BI • Cloud"
LOCATION = "California, USA"
PHONE = "+1 (628) 230-2884"
EMAIL = "bsaivaraprasad01@gmail.com"
LINKEDIN = "https://linkedin.com/in/bhaskarla-sai-vara-prasad"
GITHUB = "https://github.com/Svprasad01"

SUMMARY_TEXT = """
Data Analyst with 3 years of experience in healthcare and finance domains, skilled in data extraction, cleansing, transformation, 
and visualization. Proficient in SQL, Python, cloud platforms, and BI tools to build automated dashboards, streamline reporting processes, 
and support data-driven decision-making across cross-functional teams and enterprise environments.
"""

SKILLS = {
    "Programming Languages": ["Python", "R", "SQL"],
    "Packages": ["NumPy", "Pandas", "Matplotlib", "SciPy", "Scikit-learn", "TensorFlow", "Seaborn", "dplyr", "ggplot2", "Keras"],
    "Data Visualization & BI": ["Tableau", "Power BI", "Looker", "Qlik Sense", "Excel (Power Query, Power Pivot, Pivots)"],
    "Databases & Warehousing": ["Snowflake", "Redshift", "BigQuery", "Oracle", "MongoDB", "PostgreSQL"],
    "Big Data & Cloud": ["AWS (S3, EMR, Lambda, Glue, Redshift)", "Azure", "Apache Spark", "Hadoop"],
    "Analytics": ["EDA", "Regression", "ANOVA", "Hypothesis Testing", "A/B Testing", "Predictive Modeling"],
    "Workflow & Tools": ["Git", "GitHub", "Jira", "Confluence", "Agile/Scrum"],
    "Other Skills": ["Data Cleaning", "Data Validation", "Profiling", "Data Governance", "HIPAA/GDPR Compliance", "API Integration"]
}

EXPERIENCE = [
    {
        "role": "Data Analyst",
        "org": "UnitedHealth Group",
        "period": "Aug 2024 – Present",
        "bullets": [
            "Consolidated 40M+ claims and clinical records from Epic EHR, SQL Server, and AWS Redshift into a unified member-level dataset, improving data accuracy by 25%.",
            "Engineered 150+ clinical and utilization features using PySpark on AWS EMR, reducing manual feature creation time by 30%.",
            "Validated predictive model inputs using Python (pandas, NumPy), improving recall for high-cost member identification by 12%.",
            "Designed Tableau dashboards for AUC, calibration, and risk distributions, cutting reporting turnaround by 40%.",
            "Built Python & SQL QA scripts to detect anomalies and enforce HIPAA compliance, reducing data quality issues by 30%.",
            "Generated risk cohorts for care management teams, increasing enrollment by 10% and avoiding $2.5M in projected costs."
        ]
    },
    {
        "role": "Data Analyst",
        "org": "Deloitte",
        "period": "Jun 2021 – Jul 2023",
        "bullets": [
            "Collaborated with FP&A teams to define reporting requirements for revenue, expense, and profitability KPIs—reducing ad-hoc reporting by 20%.",
            "Automated SAP ERP (GL, AR, AP) & Salesforce CRM data consolidation using Python and VBA, saving 25 hours monthly.",
            "Performed data cleansing and validation using SQL (joins, CTEs, stored procedures) and Pandas, reaching 98% accuracy.",
            "Designed a centralized SQL Server model standardizing financial & sales data for consistent enterprise reporting.",
            "Developed Power BI dashboards for revenue trends, profitability, and variance analysis used by leadership.",
            "Built automated ETL workflows via Python & SQL Server Jobs to refresh dashboards daily, eliminating manual steps.",
            "Led UAT with finance teams, achieving zero critical errors during production rollout.",
            "Implemented automation for forecasting & expense allocation, reducing quarterly close cycles by 15%."
        ]
    }
]

EDUCATION = [
    {
        "degree": "Master of Science in Computer Science",
        "school": "California State University, San Bernardino",
        "location": "California, USA"
    },
    {
        "degree": "Bachelor of Technology in Computer Science and Engineering",
        "school": "JNTUH University College of Engineering Manthani",
        "location": "India"
    }
]

PROJECTS = [...]  # keep your existing projects unless you'd like me to rewrite them

# --------- HELPERS ---------
def download_button_from_file(path: Path, label: str):
    if not path.exists():
        st.info("Add your resume at **assets/resume.pdf** and the download button will appear.")
        return
    with open(path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
    href = f'<a href="data:application/octet-stream;base64,{b64}" download="{path.name}">{label}</a>'
    st.markdown(href, unsafe_allow_html=True)


def section_header(title: str, subtitle: str | None = None, icon: str = "🧭"):
    st.markdown(f"### {icon} {title}")
    if subtitle:
        st.caption(subtitle)


# --------- SECTIONS ---------
def show_about():
    section_header("About Me", None, "👋")
    st.write(f"### {NAME}")
    st.write(f"{TAGLINE}")
    st.write(f"📍 {LOCATION} | 📞 {PHONE}")
    st.markdown(f"✉️ [{EMAIL}](mailto:{EMAIL}) • 🔗 [LinkedIn]({LINKEDIN}) • 🐙 [GitHub]({GITHUB})")
    st.write("—")
    st.write(SUMMARY_TEXT)

    st.write("### Skills")
    cols = st.columns(2)
    items = list(SKILLS.items())
    for i, (group, skills) in enumerate(items):
        with cols[i % 2]:
            st.markdown(f"**{group}**")
            st.markdown(" ".join([f'<span class="chip">{s}</span>' for s in skills]), unsafe_allow_html=True)

    st.write("—")
    st.write("**Resume**")
    download_button_from_file(RESUME_PATH, "⬇️ Download my resume")


def show_experience():
    section_header("Experience", "Roles and key accomplishments", "💼")
    for item in EXPERIENCE:
        with st.container(border=True):
            st.markdown(f"**{item['role']}**, {item['org']}")
            st.caption(item["period"])
            for b in item["bullets"]:
                st.markdown(f"- {b}")


def show_education():
    section_header("Education", None, "🎓")
    for ed in EDUCATION:
        with st.container(border=True):
            st.markdown(f"**{ed['degree']}**")
            st.caption(f"{ed['school']} — {ed['location']}")


def show_contact():
    section_header("Contact", "Reach out for roles, collaborations, or networking ☕", "📬")
    st.markdown(f"- 📞 **Phone:** {PHONE}")
    st.markdown(f"- ✉️ **Email:** [{EMAIL}](mailto:{EMAIL})")
    st.markdown(f"- 🔗 **LinkedIn:** [{LINKEDIN}]({LINKEDIN})")
    st.markdown(f"- 🐙 **GitHub:** [{GITHUB}]({GITHUB})")


# --------- NAVIGATION ---------
st.sidebar.title("Navigate")
page = st.sidebar.radio("Go to", ["About", "Experience", "Education", "Projects", "Contact"])

if page == "About":
    show_about()
elif page == "Experience":
    show_experience()
elif page == "Education":
    show_education()
elif page == "Projects":
    show_projects()
else:
    show_contact()

st.sidebar.markdown("---")
st.sidebar.caption("Made with Streamlit")
