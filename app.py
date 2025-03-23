import streamlit as st
from pathlib import Path
from PIL import Image
import pandas as pd
import plotly.express as px
from datetime import datetime

# --- PATH SETTINGS ---
current_dir = Path(__file__).parent if "__file__" in locals() else Path.cwd()
css_file = current_dir / "styles" / "main.css"
resume_file = current_dir / "assets" / "CV_Petru_Lucian_Giurca.pdf"
profile_pic = current_dir / "assets" / "pg_04.png"

# --- GENERAL SETTINGS ---
PAGE_TITLE = "Digital CV | Petru Lucian Giurca"
PAGE_ICON = "👨‍💻"
NAME = "Petru Lucian Giurca"
DESCRIPTION = "Mobile App | Web App | Software Developer | YouTuber | Programmer | Generative AI Software Engineer at HCLTech"
ABOUT_ME = "I am a passionate Generative AI Software Engineer with over 10 years of experience in full-stack development. My expertise spans across AI/ML model security, cloud platforms, and DevSecOps practices. I thrive on solving complex problems and building innovative solutions that make a difference."

EMAIL = "petru.giurca@pm.me"
PHONE = "+40 754 21 56 12"  # Replace with actual phone if desired
LOCATION = "Bucharest, Romania"

SOCIAL_MEDIA = {
    "YouTube": "https://www.youtube.com/@petrugiurca",
    "LinkedIn": "https://www.linkedin.com/in/petru-giurca-71a032203/",
    "GitHub": "https://github.com/gotechworld",
    "Twitter": "https://x.com/aiengineer2020",
}

PROJECTS = [
    {
        "title": "AI-powered Personalized Travel Recommendation",
        "description": "Developed an intelligent system using LangChain, Streamlit, and Google Vertex AI to deliver a comprehensive travel planning experience.",
        "technologies": ["Python", "LangChain", "Google Vertex AI", "Streamlit"],
        "year": 2025
    },
    {
        "title": "Secure DevOps Pipeline Framework",
        "description": "Created a comprehensive framework for integrating security checks throughout the CI/CD pipeline, reducing vulnerability detection time by 60%.",
        "technologies": ["Jenkins", "Docker", "Kubernetes", "GitGuardian", "OWASP ZAP"],
        "year": 2024
    },
    {
        "title": "Microservices Architecture Migration",
        "description": "Led the migration of a monolithic application to a microservices architecture, improving scalability and reducing deployment time by 75%.",
        "technologies": ["Docker", "Kubernetes", "Azure DevOps", "Terraform"],
        "year": 2023
    },
]

CERTIFICATIONS = [
    {"name": "Deploying and Evaluating GenAI Apps with MongoDB", "issuer": "MongoDB", "date": "2025"},
    {"name": "Certified Python Developer", "issuer": "Global Tech Council", "date": "2025"},
    {"name": "Conda Fundamentals Certification", "issuer": "Anaconda", "date": "2025"},
    {"name": "Certified LLM Developer", "issuer": "Blockchain Council", "date": "2024"},
    {"name": "Using MongoDB with Python", "issuer": "MongoDB", "date": "2024"},
    {"name": "MongoDB for SQL Experts", "issuer": "MongoDB", "date": "2024"},
    {"name": "Certified CyberSecurity Expert", "issuer": "Blockchain Council", "date": "2024"},
    {"name": "Certified Artificial Intelligence (AI) Developer", "issuer": "Blockchain Council", "date": "2024"},
    {"name": "Certified Artificial Intelligence (AI) Expert", "issuer": "Blockchain Council", "date": "2024"},
    {"name": "Certified Generative AI Expert", "issuer": "Blockchain Council", "date": "2024"},
    {"name": "Certified Full Stack Developer", "issuer": "GSDC - Global Skill Development Council", "date": "2023"},
    {"name": "Certified DevSecOps Engineer", "issuer": "GSDC - Global Skill Development Council", "date": "2023"},
    {"name": "Certified Information Security Executive", "issuer": "GSDC - Global Skill Development Council", "date": "2023"},
    {"name": "Certified DevOps Developer", "issuer": "International DevOps Certification Academy", "date": "2022"},
    {"name": "Certified Pentesting Expert", "issuer": "Global Tech Council", "date": "2021"},
    {"name": "Certified White Hat Hacker", "issuer": "Global Tech Council", "date": "2021"},
    {"name": "ISO 9001 Quality Management Systems Quality Manager", "issuer": "SkillFront", "date": "2021"},
    {"name": "ISO/IEC 27001 Information Security Manager", "issuer": "SkillFront", "date": "2021"},
    {"name": "DevOps Information Security Engineer", "issuer": "International DevOps Certification Academy", "date": "2020"},
    {"name": "Scrum Master", "issuer": "International DevOps Certification Academy", "date": "2020"},
    {"name": "DevOps Operations Engineer", "issuer": "International DevOps Certification Academy", "date": "2020"},
]

# --- PAGE CONFIGURATION ---
st.set_page_config(page_title=PAGE_TITLE, page_icon=PAGE_ICON, layout="wide")

# --- LOAD CSS, PDF & PROFILE PIC ---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)

with open(resume_file, "rb") as pdf_file:
    PDFbyte = pdf_file.read()
profile_pic = Image.open(profile_pic)

# --- CUSTOM CSS ---
st.markdown("""
<style>
    .main {
        padding: 2rem 3rem;
        background-color: #0e1117;
    }
    .stTabs [data-baseweb="tab-list"] {
        gap: 24px;
    }
    .stTabs [data-baseweb="tab"] {
        height: 50px;
        white-space: pre-wrap;
        background-color: #1e2530;
        border-radius: 4px;
        padding: 10px 16px;
        font-weight: 600;
    }
    .stTabs [aria-selected="true"] {
        background-color: #4c8bf5 !important;
        color: white !important;
    }
    .skill-box {
        background-color: #1e2530;
        border-radius: 8px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
    }
    .project-card {
        background-color: #1e2530;
        border-radius: 8px;
        padding: 20px;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        transition: transform 0.3s ease;
    }
    .project-card:hover {
        transform: translateY(-5px);
    }
    .tech-tag {
        background-color: #4c8bf5;
        color: white;
        padding: 5px 10px;
        border-radius: 15px;
        font-size: 0.8em;
        margin-right: 5px;
        display: inline-block;
        margin-top: 5px;
    }
    .cert-card {
        background-color: #1e2530;
        border-radius: 8px;
        padding: 15px;
        margin-bottom: 15px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    .progress-container {
        width: 100%;
        background-color: #2d3748;
        border-radius: 10px;
        margin-top: 5px;
    }
    .progress-bar {
        height: 10px;
        border-radius: 10px;
        background-color: #4c8bf5;
    }
    .timeline-item {
        border-left: 2px solid #4c8bf5;
        padding-left: 20px;
        padding-bottom: 30px;
        position: relative;
    }
    .timeline-item:before {
        content: '';
        position: absolute;
        left: -10px;
        top: 0;
        width: 18px;
        height: 18px;
        border-radius: 50%;
        background-color: #4c8bf5;
    }
</style>
""", unsafe_allow_html=True)

# --- NAVIGATION ---
tabs = st.tabs(["🏠 Home", "💼 Experience", "🛠️ Skills", "🚀 Projects", "🎓 Education", "📞 Contact"])

# --- HOME TAB ---
with tabs[0]:
    col1, col2 = st.columns([1, 2], gap="large")
    
    with col1:
        st.image(profile_pic, width=280)
        
        # Contact Info Section
        st.markdown("### 📬 Contact Information")
        st.markdown(f"📧 **Email:** {EMAIL}")
        st.markdown(f"📱 **Phone:** {PHONE}")
        st.markdown(f"📍 **Location:** {LOCATION}")
        
        # Social Media Links
        st.markdown("### 🔗 Connect With Me")
        for platform, link in SOCIAL_MEDIA.items():
            st.markdown(f"[<img src='https://img.shields.io/badge/{platform}-0077B5?style=for-the-badge&logo={platform.lower()}&logoColor=white' height='30'>]({link})", unsafe_allow_html=True)
        
        # Download Resume Button
        st.markdown("### 📄 Resume")
        st.download_button(
            label="Download CV",
            data=PDFbyte,
            file_name=resume_file.name,
            mime="application/octet-stream",
            use_container_width=True,
        )
    
    with col2:
        st.markdown(f"# {NAME}")
        st.markdown(f"<p style='font-size: 1.5em; color: #4c8bf5;'>{DESCRIPTION}</p>", unsafe_allow_html=True)
        
        # About Me Section
        st.markdown("## 👨‍💻 About Me")
        st.markdown(ABOUT_ME)
        
        # Key Skills Overview
        st.markdown("## 🔑 Key Skills")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.markdown("#### AI & ML")
            st.markdown("- LangChain")
            st.markdown("- Vertex AI")
            st.markdown("- RAG Systems")
            st.markdown("- LLM Fine-tuning")
        
        with col2:
            st.markdown("#### DevSecOps")
            st.markdown("- CI/CD Pipelines")
            st.markdown("- Kubernetes")
            st.markdown("- Docker")
            st.markdown("- Terraform")
        
        with col3:
            st.markdown("#### Development")
            st.markdown("- Python")
            st.markdown("- JavaScript")
            st.markdown("- MERN Stack")
            st.markdown("- SQL/NoSQL")
        
        # Professional Summary
        st.markdown("## 🎯 Professional Summary")
        st.markdown("""
        Experienced Generative AI Software Engineer with a strong background in DevSecOps and full-stack development. 
        Specialized in building secure, scalable AI solutions using cutting-edge technologies. 
        Proven track record of implementing robust security measures for AI/ML models and cloud infrastructure.
        """)

# --- EXPERIENCE TAB ---
with tabs[1]:
    st.markdown("## 💼 Professional Experience")
    
    # Timeline-style work history
    with st.container():
        st.markdown('<div class="timeline-item">', unsafe_allow_html=True)
        st.markdown("### Generative AI Software Engineer | HCLTech")
        st.markdown("#### August 2023 - Present")
        st.markdown("""
        - Developing and implementing LLMs using LangChain, Streamlit, Google Vertex AI, and Hugging Face Hub
        - Writing clean, efficient, and well-documented code in Python and NodeJS
        - Using LangChain within Vertex AI to interface with models hosted on Hugging Face Hub
        - Collaborating with cross-functional teams to deliver high-quality AI solutions
        - Staying updated with emerging AI technologies and best practices
        """)
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="timeline-item">', unsafe_allow_html=True)
        st.markdown("### DevSecOps Expert | HCLTech")
        st.markdown("#### October 2022 - July 2023")
        st.markdown("""
        - Collected, preprocessed, and analyzed large datasets to extract valuable insights
        - Identified, analyzed, and resolved infrastructure vulnerabilities and application deployment issues
        - Created CA policies in Entra ID to manage network resource access
        - Scanned for CVE vulnerabilities in component libraries using GitGuardian, OXSecurity, MegaLinter
        - Performed Dynamic Analysis for web servers using OWASP ZAP
        """)
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="timeline-item">', unsafe_allow_html=True)
        st.markdown("### DevSecOps Engineer | Axsys Business Technology")
        st.markdown("#### March 2022 - September 2022")
        st.markdown("""
        - Led DevSecOps initiatives in Vulnerability Scanning, Certificate Management, and Security Compliance
        - Analyzed vulnerability data to identify security risks and determine false positives
        - Created pods and clusters in Kubernetes and deployed using Red Hat OpenShift Platform
        - Secured production container ecosystems in continuous delivery environments
        - Stayed informed on the latest trends in security and mobile technology
        """)
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="timeline-item">', unsafe_allow_html=True)
        st.markdown("### Sr DevOps Engineer | Arnia Software")
        st.markdown("#### September 2021 - February 2022")
        st.markdown("""
        - Wrote clean, high-performance infrastructure code with a focus on reusability and automation
        - Optimized code for performance and scalability to meet business requirements
        - Collaborated with diverse teams to deliver high-quality software solutions
        - Stayed abreast of emerging technologies and industry trends
        - Actively sought feedback and refined processes to enhance productivity
        """)
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="timeline-item">', unsafe_allow_html=True)
        st.markdown("### DevSecOps Specialist | General Electric")
        st.markdown("#### July 2019 - September 2021")
        st.markdown("""
        - Developed and implemented build processes for maintaining build plans and version control
        - Designed and implemented responsive user interfaces for seamless user experiences
        - Architected scalable and maintainable software solutions
        - Collaborated with designers and stakeholders to align design and development goals
        - Explored new technologies and methodologies to optimize development processes
        """)
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="timeline-item">', unsafe_allow_html=True)
        st.markdown("### IT System Engineer | BullGuard Software")
        st.markdown("#### April 2018 - June 2019")
        st.markdown("""
        - Worked with solution architects and cloud engineers to align designs with business direction
        - Gained experience in automation using Azure DevOps, Terraform, PowerShell, Python, Docker, and Kubernetes
        - Contributed to Microservices architecture and CI/CD pipeline using Azure Pipelines
        - Wrote infrastructure code with a focus on reusability and automation
        - Worked with monitoring tools like Prometheus and Grafana
        """)
        st.markdown('</div>', unsafe_allow_html=True)

# --- SKILLS TAB ---
with tabs[2]:
    st.markdown("## 🛠️ Technical Skills")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Programming Languages
        st.markdown('<div class="skill-box">', unsafe_allow_html=True)
        st.markdown("### 💻 Programming Languages")
        
        languages = {
            "Python": 95,
            "JavaScript": 90,
            "TypeScript": 85,
            "Bash/Shell": 80,
            "SQL": 85,
            "HTML/CSS": 90
        }
        
        for lang, proficiency in languages.items():
            st.markdown(f"#### {lang}")
            st.markdown(
                f'<div class="progress-container"><div class="progress-bar" style="width:{proficiency}%"></div></div>',
                unsafe_allow_html=True
            )
        st.markdown('</div>', unsafe_allow_html=True)
        
        # AI & ML Technologies
        st.markdown('<div class="skill-box">', unsafe_allow_html=True)
        st.markdown("### 🧠 AI & ML Technologies")
        
        ai_ml_tech = {
            "LangChain": 90,
            "Google Vertex AI": 85,
            "Hugging Face": 80,
            "RAG Systems": 85,
            "LangGraph": 75,
            "CrewAI": 70,
            "AutoGen": 75
        }
        
        for tech, proficiency in ai_ml_tech.items():
            st.markdown(f"#### {tech}")
            st.markdown(
                f'<div class="progress-container"><div class="progress-bar" style="width:{proficiency}%"></div></div>',
                unsafe_allow_html=True
            )
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        # DevOps & Cloud
        st.markdown('<div class="skill-box">', unsafe_allow_html=True)
        st.markdown("### ☁️ DevOps & Cloud")
        
        devops_cloud = {
            "Docker": 90,
            "Kubernetes": 85,
            "Terraform": 80,
            "AWS": 85,
            "Azure": 90,
            "GCP": 80,
            "CI/CD Pipelines": 95
        }
        
        for tech, proficiency in devops_cloud.items():
            st.markdown(f"#### {tech}")
            st.markdown(
                f'<div class="progress-container"><div class="progress-bar" style="width:{proficiency}%"></div></div>',
                unsafe_allow_html=True
            )
        st.markdown('</div>', unsafe_allow_html=True)
        
        # Security
        st.markdown('<div class="skill-box">', unsafe_allow_html=True)
        st.markdown("### 🔒 Security")
        
        security = {
            "OWASP ZAP": 85,
            "GitGuardian": 80,
            "OXSecurity": 75,
            "MegaLinter": 70,
            "Vulnerability Management": 90,
            "Compliance Frameworks": 85,
            "AI/ML Security": 90
        }
        
        for tech, proficiency in security.items():
            st.markdown(f"#### {tech}")
            st.markdown(
                f'<div class="progress-container"><div class="progress-bar" style="width:{proficiency}%"></div></div>',
                unsafe_allow_html=True
            )
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Databases
    st.markdown('<div class="skill-box">', unsafe_allow_html=True)
    st.markdown("### 🗄️ Databases")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown("#### PostgreSQL")
        st.progress(0.9)
    
    with col2:
        st.markdown("#### MongoDB")
        st.progress(0.85)
    
    with col3:
        st.markdown("#### Redis")
        st.progress(0.8)
    
    with col4:
        st.markdown("#### MySQL")
        st.progress(0.75)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Soft Skills
    st.markdown("### 🤝 Soft Skills")
    
    soft_skills = [
        "Problem Solving", "Team Collaboration", "Communication", 
        "Project Management", "Leadership", "Adaptability",
        "Time Management", "Critical Thinking"
    ]
    
    cols = st.columns(4)
    for i, skill in enumerate(soft_skills):
        with cols[i % 4]:
            st.markdown(f"- {skill}")

# --- PROJECTS TAB ---
with tabs[3]:
    st.markdown("## 🚀 Featured Projects")
    
    for project in PROJECTS:
        st.markdown(f'<div class="project-card">', unsafe_allow_html=True)
        st.markdown(f"### {project['title']} ({project['year']})")
        st.markdown(project['description'])
        
        st.markdown("#### Technologies Used:")
        tech_html = ""
        for tech in project['technologies']:
            tech_html += f'<span class="tech-tag">{tech}</span>'
        st.markdown(tech_html, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Project Statistics
    st.markdown("### 📊 Project Statistics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Project categories pie chart
        categories = {
            "AI/ML": 45,
            "DevOps": 30,
            "Web Development": 15,
            "Security": 10
        }
        
        fig = px.pie(
            values=list(categories.values()),
            names=list(categories.keys()),
            title="Project Categories",
            color_discrete_sequence=px.colors.sequential.Blues_r
        )
        fig.update_traces(textposition='inside', textinfo='percent+label')
        fig.update_layout(
            margin=dict(t=50, b=20, l=20, r=20),
            height=350,
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(color="white")
        )
        st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Technologies used bar chart
        tech_usage = {
            "Python": 85,
            "JavaScript": 65,
            "Docker": 70,
            "Kubernetes": 60,
            "LangChain": 50,
            "Terraform": 45
        }
        
        fig = px.bar(
            x=list(tech_usage.keys()),
            y=list(tech_usage.values()),
            title="Technologies Used (Frequency %)",
            color=list(tech_usage.values()),
            color_continuous_scale=px.colors.sequential.Blues
        )
        fig.update_layout(
            xaxis_title="Technology",
            yaxis_title="Usage Frequency (%)",
            margin=dict(t=50, b=20, l=20, r=20),
            height=350,
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(color="white")
        )
        st.plotly_chart(fig, use_container_width=True)

# --- EDUCATION TAB ---
with tabs[4]:
    col1, col2 = st.columns([3, 2])
    
    with col1:
        st.markdown("## 🎓 Education")
        
        st.markdown('<div class="skill-box">', unsafe_allow_html=True)
        st.markdown("### Master's Degree in Computer Science")
        st.markdown("**University of Bucharest** | 2016 - 2018")
        st.markdown("Specialized in Artificial Intelligence and Machine Learning")
        st.markdown("**Thesis:** *Secure Implementation of AI Systems in Enterprise Environments*")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="skill-box">', unsafe_allow_html=True)
        st.markdown("### Bachelor's Degree in Computer Engineering")
        st.markdown("**Technical University of Cluj-Napoca** | 2012 - 2016")
        st.markdown("Focus on Software Development and System Architecture")
        st.markdown("**GPA:** 3.8/4.0")
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown("## 🏆 Certifications")
        
        for cert in CERTIFICATIONS:
            st.markdown(f'<div class="cert-card">', unsafe_allow_html=True)
            st.markdown(f"### {cert['name']}")
            st.markdown(f"**Issuer:** {cert['issuer']} | **Year:** {cert['date']}")
            st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown("## 📚 Continuous Learning")
        
        # Recent courses
        st.markdown("### Recent Courses")
        courses = [
            {"name": "Advanced LLM Engineering", "platform": "Coursera", "year": 2023},
            {"name": "Kubernetes Security Specialist", "platform": "Linux Foundation", "year": 2023},
            {"name": "Advanced RAG Techniques", "platform": "DeepLearning.AI", "year": 2022},
            {"name": "Cloud Security Architecture", "platform": "Pluralsight", "year": 2022}
        ]
        
        for course in courses:
            st.markdown(f"- **{course['name']}** ({course['platform']}, {course['year']})")
        
        # Skills timeline
        st.markdown("### Skills Timeline")
        
        # Create a dataframe for the timeline
        skills_data = {
            "Skill": ["Python", "DevOps", "Cloud", "AI/ML", "Security"],
            "Start": [2015, 2017, 2018, 2020, 2019],
            "End": [2025, 2025, 2025, 2025, 2025]
        }
        
        df = pd.DataFrame(skills_data)
        
        fig = px.timeline(
            df, 
            x_start="Start", 
            x_end="End", 
            y="Skill",
            color="Skill",
            color_discrete_sequence=px.colors.qualitative.Set1
        )
        
        fig.update_layout(
            title="Skills Development Timeline",
            xaxis_title="Year",
            yaxis_title="Skill Area",
            height=300,
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(color="white")
        )
        
        st.plotly_chart(fig, use_container_width=True)

# --- CONTACT TAB ---
with tabs[5]:
    st.markdown("## 📞 Get In Touch")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown("### 📬 Contact Information")
        st.markdown(f"📧 **Email:** {EMAIL}")
        st.markdown(f"📱 **Phone:** {PHONE}")
        st.markdown(f"📍 **Location:** {LOCATION}")
        
        st.markdown("### 🔗 Social Media")
        for platform, link in SOCIAL_MEDIA.items():
            st.markdown(f"[<img src='https://img.shields.io/badge/{platform}-0077B5?style=for-the-badge&logo={platform.lower()}&logoColor=white' height='30'>]({link})", unsafe_allow_html=True)
    
    with col2:
        st.markdown("### 📝 Send Me a Message")
        
        with st.form("contact_form", clear_on_submit=True):
            name = st.text_input("Name")
            email = st.text_input("Email")
            subject = st.text_input("Subject")
            message = st.text_area("Message")
            
            submitted = st.form_submit_button("Send Message")
            
            if submitted:
                st.success("Thanks for your message! I'll get back to you soon.")

# --- FOOTER ---
st.markdown("---")
st.markdown(
    f"<div style='text-align: center; color: #4c8bf5;'>© {datetime.now().year} {NAME} | Last Updated: {datetime.now().strftime('%B %Y')}</div>",
    unsafe_allow_html=True
)

