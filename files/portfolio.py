import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Nagapriya N — Portfolio",
    page_icon="💻",
    layout="wide"
)

# Navigation Sidebar
st.sidebar.title("Nagapriya N")
st.sidebar.markdown("Python Developer · Computer Science Student")
st.sidebar.markdown("---")
st.sidebar.markdown("[About](#about)")
st.sidebar.markdown("[Skills](#skills)")
st.sidebar.markdown("[Projects](#projects)")
st.sidebar.markdown("[Experience](#experience)")
st.sidebar.markdown("[Education](#education)")
st.sidebar.markdown("[Contact](#let-s-connect)")

# Header / Hero Section
st.title("Nagapriya N")
st.subheader("Python Developer · Computer Science Student")
st.write(
    "Final-year B.E. Computer Science student building data tools, dashboards and IoT systems with Python. "
    "I enjoy turning messy data into clear, reliable software."
)

col1, col2 = st.columns([1, 5])
with col1:
    st.link_button("View projects", "#projects")
with col2:
    st.link_button("Get in touch", "#let-s-connect")

st.divider()

# About Section
st.header("About")
st.caption("Background")
st.write(
    "I'm a final-year B.E. Computer Science and Engineering student at Sethu Institute of Technology "
    "with a CGPA of 8.22. My foundation is in data structures, algorithms and object-oriented programming, "
    "and I'm looking for a technical role in the IT sector where I can use Python to build scalable software."
)
st.write(
    "My recent work covers automated data cleaning pipelines, interactive data visualization "
    "and an IoT-based early warning system."
)

st.divider()

# Skills Section
st.header("Skills")
st.caption("Technical toolkit")

s_col1, s_col2, s_col3, s_col4 = st.columns(4)
with s_col1:
    st.subheader("Languages")
    st.write("• Python\n• Java")
with s_col2:
    st.subheader("Libraries")
    st.write("• NumPy\n• Pandas\n• Streamlit")
with s_col3:
    st.subheader("Core CS")
    st.write("• OOP\n• Data Structures\n• Algorithms\n• Exception Handling")
with s_col4:
    st.subheader("Database")
    st.write("• SQL\n• MySQL")

st.divider()

# Projects Section
st.header("Projects")
st.caption("Selected work")

with st.container(border=True):
    st.subheader("AI-Powered Business Intelligence Dashboard")
    st.caption("2026 · Completed · Python")
    st.write(
        "An automated data cleaning tool that detects data quality issues and applies smart fixes: "
        "duplicate removal, missing value handling, IQR-based outlier removal and column standardization. "
        "Works across CSV, Excel and JSON files, produces detailed cleaning reports with data quality scores, "
        "and processes data locally for security."
    )
    st.markdown("[Open live app →](#)")

with st.container(border=True):
    st.subheader("BI Dashboard")
    st.caption("2026 · Completed · Python, Streamlit")
    st.write(
        "An interactive Business Intelligence dashboard that centralizes data visualization, "
        "tracks key performance metrics and delivers actionable insights through a clean web interface."
    )
    st.markdown("[Open live app →](#)")

with st.container(border=True):
    st.subheader("Enviropulse — Smart IoT Early Warning System")
    st.caption("2025 – Present · MSME IDEA Hackathon 5.0 · Arduino, Sensors")
    st.write(
        "An IoT-based environmental monitoring and early warning system built with Arduino and sensors, "
        "submitted to the MSME IDEA Hackathon 5.0."
    )

st.divider()

# Experience & Education Columns
exp_col, edu_col = st.columns(2)

with exp_col:
    st.header("Experience")
    st.caption("Training & internships")
    
    st.subheader("Full Stack Java Web Development Internship")
    st.caption("Novi Tech · 30 days")
    st.write("Worked with Java, JDBC, Servlets, JSP and MySQL, with hands-on project implementation.")
    
    st.subheader("Full Stack Web Development Course (Java)")
    st.caption("Scope Tech Solutions · 1 week")
    st.write("Offline course with practical industry exposure.")

with edu_col:
    st.header("Education")
    st.caption("Academic background")
    
    st.subheader("B.E. Computer Science and Engineering")
    st.caption("2023 – 2027 · Sethu Institute of Technology · CGPA 8.22")
    
    st.subheader("HSC")
    st.caption("2022 – 2023 · Sundram Matriculation Higher Secondary School · 77%")

st.divider()

# Certifications & Achievements
cert_col, ach_col = st.columns(2)

with cert_col:
    st.header("Certifications")
    st.caption("Credentials")
    st.markdown("""
    - AWS — Getting Started with DevOps in AWS
    - Python Programming — Infosys Springboard
    - Google AI Essentials — Google
    - CRM Basics — Google Career Certificates
    - Data Science Certificate — TCSiON
    """)

with ach_col:
    st.header("Achievements")
    st.caption("Recognition")
    st.markdown("""
    - Submitted Enviropulse to MSME IDEA Hackathon 5.0
    - NPTEL Elite + Silver in Human-Computer Interaction (user-centered design, usability engineering, UX evaluation)
    """)

st.divider()

# Leadership Section
st.header("Leadership")
st.caption("Co-curricular activities")
st.markdown("""
- **NSS:** Editing Committee Member and Class Coordinator, leading community service projects and district-level programs.
- **Rotaract Club Member:** Hosted the Vigilance Program promoting community awareness and responsible civic engagement.
- Member of **ERUPTA** (CSE Department Committee) and volunteer for event and symposium planning.
- Attended workshops on *Technology in Talent Acquisition* and *Advanced Web Applications using Python Flask*.
- Volunteered in blood donation drives, an orphanage camp and event/discipline committees.
""")

st.divider()

# Contact / Footer
st.header("Let's connect")
st.write("Open to Python and technology roles.")
st.markdown("📧 **Email:** nagapriya.nstd@gmail.com | 🔗 [GitHub](#) | 🔗 [LinkedIn](#)")
st.caption("© 2026 Nagapriya N")
