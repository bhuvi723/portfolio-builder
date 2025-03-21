# 📄 Dynamic Formatted Portfolio Builder

## 📋 Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [JSON Format](#json-format)
- [Deployment](#deployment)
- [Contributing](#contributing)
- [License](#license)

## 🌟 Introduction
This project is a portfolio web application built using Streamlit. It allows users to display their personal information, certifications, education details, achievements, projects, hobbies, and contact information.

## ✨ Features
- Display personal information with profile image and links.
- List certifications and achievements.
- Show education details and projects with images and links.
- Contact form to send emails.
- Customizable footer.

## 🛠️ Installation
1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/yourrepository.git
    ```
2. Navigate to the project directory:
    ```bash
    cd yourrepository
    ```
3. Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

## 🔧 Configuration
1. Create a `.env` file in the root directory and add your email configuration:
    ```env
    SENDER_MAIL=your-email@example.com
    PASS_WORD=your-email-password
    ```
2. Update the `user_info.json` file with your personal information, certifications, education details, achievements, projects, hobbies, and contact information.

## 🚀 Usage
Run the Streamlit application:
```bash
streamlit run main.py
```

## 📄 JSON Format
The `user_info.json` file should follow this structure:
```json
{
    "headers": [
        {
            "section": "personal_info",
            "name": "Personal Information",
            "icon": "person",
            "display_type": "grid"
        },
        {
            "section": "certificates",
            "name": "Certifications",
            "icon": "file-earmark-post",
            "display_type": "list"
        },
        {
            "section": "education_details",
            "name": "Education",
            "icon": "book",
            "display_type": "grid"
        },
        {
            "section": "achievements",
            "name": "Achievements",
            "icon": "award",
            "display_type": "grid"
        },
        {
            "section": "projects",
            "name": "Projects",
            "icon": "file-code",
            "display_type": "grid"
        },
        {
            "section": "hobbies",
            "name": "Hobbies",
            "icon": "heart",
            "display_type": "grid"
        },
        {
            "section": "contact",
            "name": "Contact",
            "icon": "envelope",
            "display_type": "list"
        }
    ],
    "personal_info": {
        "name": "johnny",
        "bio": "Hello! I am johnny, a motivated Computer Science Engineering student with a passion for exploring various technologies.",
        "hyperlink_linkedin": "http://www.linkedin.com/in/kummari-geetha-a781a7229",
        "hyperlink_email": "kummarigeetha03@gmail.com",
        "profile_image": "images\\johnny.jpeg",
        "download_btn_resume" : "C:\\Users\\Lenovo\\Desktop\\portfolio templatizing\\utils\\Resume.pdf"
    },
    "certificates": [
        {
            "title": "HTML",
            "description": "Certified in static website development, responsive web design with Bootstrap and Flexbox.",
            "download_btn_project" : "C:\\Users\\Lenovo\\Desktop\\portfolio templatizing\\utils\\Resume.pdf"
        },
        {
            "title": "Python Programming, Machine Learning",
            "description": "Certified in Python programming, focusing on foundational and advanced programming concepts with machine learning algorithms.",
            "info_box_description" : "this is a my machine learning certification!"
        }
    ],
    "education_details": [
        {
            "degree": "B. Tech, HITAM - CSE",
            "board": "JNTUH",
            "year": "2025",
            "score": "8.5 CGPA",
            "hyperlink_email"  : "https://www.hitam.org/"
        },
        {
            "degree": "12th, Narayana Junior College",
            "board": "TSBIE",
            "year": "2021",
            "score": "96%"
        }
    ],
    "achievements": [
        {
            "title": "Sports",
            "description": "Honored for accomplishments in inter and intra-school badminton, kho-kho, and Bhagavad Gita chanting competitions."
        },
        {
            "title": "Singing",
            "description": "Secured 1st place in the inter-school singing competition."
        },
        {
            "title": "Dance",
            "description": "In dance i got 1st prize in inter school competition."
        }
    ],
    "projects": [
        {
            "title": "Password Strength Checker",
            "image": "images\\password.jpg",
            "description": "Developed a password strength checker to enhance security using Python.",
            "download_btn_project1" : "C:\\Users\\Lenovo\\Desktop\\portfolio templatizing\\utils\\Resume.pdf"
        },
        {
            "title": "Weather Forecasting System",
            "image": "images\\sonar.jpg",
            "hyperlink_email" : "https://www.weather.com/",
            "description": "Built a weather forecasting system using Python and APIs."
        },
        {
            "title": "Sonar-Based Mineral Detection",
            "image": "images\\sonar.jpg",
            "description": "Developed a sonar-based system for mineral detection using Machine Learning."
        }
    ],
    "hobbies": [
        "- Reading",
        "- Badminton",
        "- Cooking",
        "- Painting"
    ],
    "contact" : [
        {
        "hyperlink_email" : "kummarigeetha03@gmail.com",
        "hyperlink_linkedin" : "http://www.linkedin.com/in/kummari-geetha-a781a7229",
        "hyperlink_github": "https://github.com/bhuvi723",
        "add_dialog_box" : "True"
        }
    ],
    "footer_info": {
        "name": "johnny",
        "linkedin_url": "http://www.linkedin.com/in/kummari-geetha-a781a7229",
        "year": "2024"
    }
}
```

## 🌐 Deployment
To deploy the application on Render:
1. Create a new web service on Render.
2. Connect your GitHub repository.
3. Set the build command to:
    ```bash
    pip install -r requirements.txt
    ```
4. Set the start command to:
    ```bash
    streamlit run main.py
    ```
5. Add environment variables for email configuration in the Render dashboard.

## 🤝 Contributing
Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## 📜 License
This project is licensed under the MIT License.
