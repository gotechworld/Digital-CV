from pathlib import Path

import streamlit as st
from PIL import Image



# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV_Petru_Lucian_Giurca.pdf"
profile_pic = current_dir / "assets" / "pg_04.png"
#st.image(profile_pic, width=300)
#page_icon = current_dir / "assets" / "pg_03.png"


# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Petru Lucian Giurca"
PAGE_ICON = ":technologist:"
NAME = "Petru Lucian Giurca"
DESCRIPTION = """
Mobile App: | Web App: | Software | Developer | You Tuber | Programmer | Generative AI Software Engineer at HCLTech.
"""

EMAIL = "petru.giurca@pm.me"


SOCIAL_MEDIA = {
    "YouTube": "https://www.youtube.com/@petrugiurca",
    "LinkedIn": "https://www.linkedin.com/in/petru-giurca-71a032203/",
    "GitHub": "https://github.com/gotechworld",
    "Twitter": "https://x.com/aiengineer2020",
}

st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON)


# --- LOAD CSS, PDF & PROFIL PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)


with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)


# --- HERO SECTION ---
col1, col2 = st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(NAME)
    #st.write(DESCRIPTION)
    st.markdown(f"<font color='lightblue'>{DESCRIPTION}<br><br></font>", unsafe_allow_html=True)
    st.download_button(
        label=" 📄 Download Resume",
        data=PDFbyte,
        file_name=resume_file.name,
        mime="application/octet-stream",
    )
    st.write("📫", EMAIL)



# --- SOCIAL LINKS ---
st.write('\n')
cols = st.columns(len(SOCIAL_MEDIA))
for index, (platform, link) in enumerate(SOCIAL_MEDIA.items()):
    cols[index].write(f"[ <font color='orange' size='+4'>{platform}</font> ]({link})", unsafe_allow_html=True)


# --- EXPERIENCE & QUALIFICATIONS ---
st.write('\n')
st.subheader("⏩Experience & Qulifications⏪")
st.write("---")
st.write(
    """
-    ✔️ 10+ Years experience extracting Full-Stack Software Development.
-    ✔️ Experience with securing AI/ML models, including access control, model
explainability, and auditing.
-    ✔️ Experience securing AI and machine learning systems, particularly those
involving large-scale LLMs or NLP models.
-    ✔️ Knowledge of ethical AI practices, data privacy, and the potential risks of AI
models.
-    ✔️ Hands-on experience with cloud platforms (AWS, GCP, Azure) and cloud security best practices.
-    ✔️ Strong scripting and automation skills (e.g., Python, Bash, or similar) for security operations tasks.
-    ✔️ Certifications in Cybersecurity and Artificial Intelligence.
-    ✔️ Experience with DevSecOps practices and integrating security into the software
development lifecycle (SDLC).
-    ✔️ Experience with security tools and practices such as SIEM, IDS/IPS, firewalls, encryption, vulnerability management, and incident response.
-    ✔️ Experience with containerization and orchestration tools (e.g., Docker, Kubernetes) and securing containerized applications.
-    ✔️ Familiarity with compliance frameworks and standards (e.g., GDPR, SOC 2, ISO 27001).
-    ✔️ Strong hands on experience and knowledge in Python, NodeJS, MongoDB , Postgres.
"""
)


# --- SKILLS ---
st.write('\n')
st.subheader("⏩Hard Skills⏪")
st.write("---")
st.write(
    """
-    👩‍💻  <font color='lightgreen'>Programming:</font> Python , JavaScript , Bash , MERN , SQL
-    📊  <font color='lightgreen'>RAG:</font> Vertex AI Search and Conversation
-    📚  <font color='lightgreen'>Agentic AI Framework:</font> LangGraph , CrewAI , AutoGen
-    🗄️  <font color='lightgreen'>Databases:</font> Postgres , MongoDB 
"""
, unsafe_allow_html=True)


# --- WORK HISTORY ---
st.write('\n')
st.subheader("⏩Work History⏪")
st.write("---")

# --- JOB 1
st.write("👨‍💻", "**Generative AI Software Engineer | [<font color='yellow'>HCLTech</font>](https://www.hcltech.com/)**", unsafe_allow_html=True)
st.write("-  🔵 August - 2023 ➖ Present")
st.write(
    """
- 🔶 Developing and implementing LLMs using LangChain, Streamlit, Google
Vertex AI, and Hugging Face Hub to select appropriate models, fine-tune
them for specific tasks, and optimize performance.
- 🔶 Writing clean, efficient, and well-documented code in Python and NodeJS
ensures the maintainability and scalability of the developed solutions.
- 🔶 Using LangChain within Vertex AI to interface with models hosted on
Hugging Face Hub.
- 🔶 Collaborative team player, effectively communicating with cross-functional teams to deliver high-quality software products.
- 🔶 Continuous learner, staying updated with emerging technologies and best practices to drive innovation in software development.
"""
)

# --- JOB 2
st.write('\n')
st.write("👨‍💻", "**DevSecOps Expert | [<font color='yellow'>HCLTech</font>](https://www.hcltech.com/)**", unsafe_allow_html=True)
st.write("-  🔵 October - 2022 ➖ July - 2023")
st.write(
    """
- 🔶 Collect, preprocess, and analyze large datasets to extract valuable insights and patterns.
- 🔶 Identifying, analyzing, and resolving infrastructure vulnerabilities and
application deployment issues.  
- 🔶 Creating CA policies in Entra ID to allow or deny access to network
resources
- 🔶 Scanning for CVE vulnerabilities inside the
components libraries dependencies files in the repositories.
- 🔶 Performing the scanning of GIT secrets (tokens, certs, ssh keys) using
GitGuardian, OXSecurity, MegaLinter in VCS using CICD pipelines (Azure
DevOps and GitHub Actions), config files (environment variables), config
management and secret management system.
- 🔶 Performing Dynamic Analysis for web server using OWASP ZAP to scan
for dangerous files programs, weak configurations, etc.


"""
)

# --- JOB 3
st.write('\n')
st.write("👨‍💻", "**DevSecOps Engineer | [<font color='yellow'>Axsys Business Technology</font>](https://www.axsys.ro/)**", unsafe_allow_html=True)
st.write("-  🔵 March - 2022 ➖ September - 2022")
st.write(
    """
- 🔶 Providing leadership in the DevSecOps areas of Vulnerability Scanning,
Certificate Management, Password Policy Management, Data Analysis of
security monitoring outputs, coordination of Remediation Patching, and other
daily Security and Compliance efforts.
- 🔶 Reviewing and analyzing vulnerability data to identify security risks to the
organization's network, infrastructure, and applications and determine any
reported vulnerabilities that are false positives.
- 🔶 Experience creating pods and clusters in Kubernetes and deploying those
using the Red Hat OpenShift Platform.
- 🔶 Comfortable with securing a production container ecosystem (Docker, EKS,
Fargate/ECS, Kubernetes, service discovery, and service registry) in a
continuous delivery environment using Jenkins, Ansible, and Terraform.
- 🔶 Passionate about staying informed on the latest trends and advancements in mobile technology, delivering innovative solutions to meet user needs.
"""
)

# --- JOB 4
st.write('\n')
st.write("👨‍💻", "**Sr DevOps Engineer | [<font color='yellow'>Arnia Software</font>](https://www.arnia.com/)**", unsafe_allow_html=True)
st.write("-  🔵 September - 2021 ➖ February - 2022")
st.write(
    """
- 🔶 Write clean, high-performance, well tested infrastructure code with a focus
on reusability and automation (i.e. Ansible, Terraform).
- 🔶 Strong analytical and problem-solving skills, capable of optimizing code for performance and scalability to meet business requirements.
- 🔶 Effective communicator and team player, collaborating with diverse teams to deliver high-quality software solutions within specified timelines.
- 🔶 Adaptable and quick learner, staying abreast of emerging technologies and industry trends to drive innovation in software development practices.
- 🔶 Commitment to continuous improvement, actively seeking feedback and refining processes to enhance productivity and deliver value to stakeholders.
"""
)

# --- JOB 5
st.write('\n')
st.write("👨‍💻", "**DevSecOps Specialist | [<font color='yellow'>General Electric</font>](https://www.ge.com/)**", unsafe_allow_html=True)
st.write("-  🔵 July - 2019 ➖ September - 2021")
st.write(
    """
- 🔶 Developing and implementing build processes and procedures for
maintaining build plans, version control, and defect tracking.
- 🔶 Ability to design and implement responsive and visually appealing user interfaces, ensuring seamless user experiences across devices and platforms.
- 🔶 Strong problem-solving skills, capable of architecting scalable and maintainable software solutions to meet project requirements.
- 🔶 Collaborative mindset, working closely with designers and other stakeholders to ensure alignment between design and development goals.
- 🔶 Passionate about exploring new technologies and methodologies, continuously seeking opportunities to innovate and optimize development processes.
"""
)


# --- JOB 6
st.write('\n')
st.write("👨‍💻", "**IT System Engineer | [<font color='yellow'>BullGuard Software</font>](https://www.bullguard.com)**", unsafe_allow_html=True)
st.write("-  🔵 April - 2018 ➖ June - 2019")
st.write(
    """
- 🔶 Working closely with solution architects and cloud engineers and provide
support to senior staff, ensuring designs align with technical and business
direction across the company.
- 🔶 Experience in automation exposure using Azure DevOps, Terraform,
PowerShell, Python, Docker, and Kubernetes (AKS) as part of a POC project.
- 🔶 Exposure to Microservices architecture (CI/CD pipeline using Azure
Pipelines).
- 🔶 Writing clean, high-performance, well-tested infrastructure code with a focus
on reusability and automation (i.e., Shell, Python, Terraform).
- 🔶 Experience with monitoring tools like Prometheus and Grafana.
"""
)
