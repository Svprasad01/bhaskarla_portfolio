import streamlit as st
from pathlib import Path
import base64

# --------- CONFIG ---------
st.set_page_config(
    page_title="Sai Vara Prasad Bhaskarla — Portfolio",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown(
    """
    <style>
    .chip {
        display:inline-block;
        padding:.25rem .65rem;
        margin:.2rem;
        border-radius:999px;
        font-size:.85rem;
        border:1px solid rgba(127,127,127,0.3);
    }
    </style>
    """,
    unsafe_allow_html=True
)

# --------- BASIC INFO ---------
RESUME_PATH = Path("assets/resume.pdf")

NAME = "Sai Vara Prasad Bhaskarla"
TAGLINE = "Marketing Data Analyst • SQL • Python • Power BI • Cloud Analytics"
LOCATION = "California, USA"
PHONE = "+1 (628) 230-4775"
EMAIL = "saivaraprasad2001@gmail.com"
LINKEDIN = "https://linkedin.com/in/bhaskarla-sai-vara-prasad"
GITHUB = "https://github.com/Svprasad01"

# --------- SUMMARY ---------
SUMMARY_TEXT = """
Marketing Data Analyst with nearly four years of experience designing and managing end-to-end data pipelines using Azure Data Factory, BigQuery, and SQL, integrating data from CRM, ERP, POS, and web analytics platforms. Experienced in building interactive dashboards with Power BI and Tableau to deliver actionable insights for sales, marketing, and supply-chain teams. Proficient in Python (pandas, NumPy, scikit-learn) for data cleaning, statistical analysis, demand forecasting, predictive modeling, and personalization use cases. Strong background in customer segmentation, journey analysis, and A/B testing using Adobe Analytics and Adobe Target, with a proven ability to collaborate cross-functionally, define KPIs, automate reporting, and ensure data accuracy across analytics platforms.
"""

# --------- SKILLS ---------
SKILLS = {
    "Data Analysis & Programming": ["Python", "SQL", "R"],
    "Data Visualization & BI": [
        "Power BI", "Tableau", "Looker Studio", "Qlik Sense",
        "Excel (Power Query, Power Pivot, Pivot Tables)"
    ],
    "Databases & Warehousing": [
        "Google BigQuery", "Snowflake", "MySQL", "PostgreSQL", "Microsoft SQL Server"
    ],
    "Cloud & ETL": [
        "Azure Data Factory", "Azure SQL", "Google Cloud Platform"
    ],
    "Marketing & Web Analytics": [
        "Adobe Analytics", "Adobe Target", "Google Analytics 4",
        "Google Tag Manager", "SEMrush", "HubSpot"
    ],
    "Analytics Techniques": [
        "Customer Segmentation", "A/B Testing", "Attribution Modeling",
        "Forecasting", "Regression Analysis", "Hypothesis Testing"
    ],
    "Collaboration & Tools": [
        "Jira", "Confluence", "Git", "Agile/Scrum"
    ]
}

# --------- EXPERIENCE ---------
EXPERIENCE = [
    {
        "role": "Marketing Analyst – E-Commerce",
        "org": "Kroger",
        "period": "Aug 2024 – Present | California, USA",
        "bullets": [
            "Consolidated customer data from Adobe Analytics, CRM platforms, and in-store POS systems into Google BigQuery using Python and SQL, enabling unified customer and behavioral analysis.",
            "Segmented customers by loyalty tier, intent, recency, and browsing behavior using SQL, supporting targeted email and on-site personalization campaigns and driving a 15% lift in CTR.",
            "Analyzed customer journeys across web, mobile app, and BOPIS channels in Adobe Analytics, identifying checkout friction points that contributed to a 20% drop in cart abandonment.",
            "Built Python-based product recommendation logic using clickstream and purchase history data; partnered with engineering to integrate results into Adobe Target, increasing conversion by 12% and AOV by 8%.",
            "Executed A/B and multivariate tests in Adobe Target on filters, banners, and checkout flows, resulting in an 18% increase in customer engagement.",
            "Developed BigQuery-powered dashboards tracking conversion rate, revenue per visit, device performance, and segment engagement, improving visibility into e-commerce performance.",
            "Performed paid media, email, and display campaign ROI analysis using SQL-based attribution models, improving marketing efficiency by 10%.",
            "Identified cross-sell and upsell opportunities through product affinity analysis, supporting personalized promotions that increased upsell revenue by 7%."
        ]
    },
    {
        "role": "Data Analyst",
        "org": "Accenture (Client: ManKind Pharma)",
        "period": "Jun 2021 – Jul 2023 | India",
        "bullets": [
            "Built and maintained Azure Data Factory pipelines integrating sales, marketing, and supply-chain data into Azure Data Lake, reducing report delivery time from full-day to under four hours.",
            "Designed Power BI dashboards in Azure SQL Data Warehouse to track SKU-level sales, regional performance, and campaign effectiveness for products including Dolo 650, Nebulon, Livogen, and Digene.",
            "Used Python to analyze demand trends and seasonality, improving supply-chain forecasting accuracy and reducing inventory planning errors by 15%.",
            "Implemented SQL-based ETL processes to clean and combine SAP and CRM data, ensuring consistent and reliable reporting across business teams.",
            "Developed marketing performance dashboards tracking conversion, reach, and engagement, enabling leadership to improve ROI by 18%.",
            "Built real-time inventory and sales views by combining Azure SQL sales data with supply-chain updates, reducing stockouts and excess inventory by 25%.",
            "Automated data validation and Power BI refresh workflows using SQL stored procedures, saving over 10 hours of manual effort weekly.",
            "Partnered with sales, marketing, finance, and supply-chain stakeholders to define KPIs and identify growth opportunities, contributing to a 12% increase in sales for selected brands.",
            "Monitored and optimized Azure Data Factory pipelines and SQL queries, maintaining 99.9% uptime for business-critical dashboards."
        ]
    }
]

# --------- EDUCATION ---------
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

# --------- HELPERS ---------
def download_button_from_file(path: Path, label: str):
    if not path.exists():
        st.info("Add your resume at **assets/resume.pdf** to enable download.")
        return
    with open(path, "rb") as f:
        b64 = base64.b64encode(f.read()).decode()
    st.markdown(
        f'<a href="data:application/octet-stream;base64,{b64}" download="{path.name}">{label}</a>',
        unsafe_allow_html=True
    )

def section_header(title, subtitle=None, icon="📌"):
    st.markdown(f"### {icon} {title}")
    if subtitle:
        st.caption(subtitle)

# --------- SECTIONS ---------
def show_about():
    section_header("About Me", icon="👋")
    st.write(f"### {NAME}")
    st.write(TAGLINE)
    st.write(f"📍 {LOCATION} | 📞 {PHONE}")
    st.markdown(
        f"✉️ [{EMAIL}](mailto:{EMAIL}) • 🔗 [LinkedIn]({LINKEDIN}) • 🐙 [GitHub]({GITHUB})"
    )
    st.write("—")
    st.write(SUMMARY_TEXT)

    st.write("### Skills")
    cols = st.columns(2)
    items = list(SKILLS.items())
    for i, (group, skills) in enumerate(items):
        with cols[i % 2]:
            st.markdown(f"**{group}**")
            st.markdown(
                " ".join([f'<span class="chip">{s}</span>' for s in skills]),
                unsafe_allow_html=True
            )

    st.write("—")
    download_button_from_file(RESUME_PATH, "⬇️ Download Resume")

def show_experience():
    section_header("Experience", "Professional roles & impact", "💼")
    for item in EXPERIENCE:
        with st.container(border=True):
            st.markdown(f"**{item['role']} — {item['org']}**")
            st.caption(item["period"])
            for b in item["bullets"]:
                st.markdown(f"- {b}")

def show_education():
    section_header("Education", icon="🎓")
    for ed in EDUCATION:
        with st.container(border=True):
            st.markdown(f"**{ed['degree']}**")
            st.caption(f"{ed['school']} — {ed['location']}")

def show_contact():
    section_header("Contact", "Let’s connect", "📬")
    st.markdown(f"- 📞 **Phone:** {PHONE}")
    st.markdown(f"- ✉️ **Email:** [{EMAIL}](mailto:{EMAIL})")
    st.markdown(f"- 🔗 **LinkedIn:** [{LINKEDIN}]({LINKEDIN})")
    st.markdown(f"- 🐙 **GitHub:** [{GITHUB}]({GITHUB})")

# --------- NAVIGATION ---------
st.sidebar.title("Navigate")
page = st.sidebar.radio("Go to", ["About", "Experience", "Education", "Contact"])

if page == "About":
    show_about()
elif page == "Experience":
    show_experience()
elif page == "Education":
    show_education()
else:
    show_contact()

st.sidebar.markdown("---")
st.sidebar.caption("Built with Streamlit")
