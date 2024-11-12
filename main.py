import streamlit as st
from streamlit_option_menu import option_menu
import json
import time
import re
from mail import *

def load_user_info():
    try:
        with open('user_info.json', encoding='utf-8') as json_file:
            return json.load(json_file)
    except FileNotFoundError:
        st.error("The user_info.json file was not found.")
    except json.JSONDecodeError:
        st.error("Error decoding the JSON file.")
    return {}

# Load the JSON content every time the app runs
user_info = load_user_info()

# Set page configuration
page_title = user_info.get("personal_info", {}).get("name", "").title()+"'s Portfolio"
page_icon = user_info.get("icon", "🌟")
st.set_page_config(page_title=page_title, page_icon=page_icon)

# Function to apply custom styling
def add_styling():
    st.markdown("""
        <style>
        .header-style {
            font-size: 28px;
            font-weight: bold;
            color: #2c3e50;
            padding-top: 20px;
            border-bottom: 2px solid #d3d3d3;
            margin-bottom: 10px;
        }
        .subheader-style {
            font-size: 20px;
            font-weight: bold;
            color: #34495e;
            margin-top: 10px;
        }
        .text-style {
            font-size: 16px;
            color: #555;
            margin-bottom: 10px;
        }
        .line {
            border-bottom: 1px solid #ddd;
            margin: 20px 0;
        }
        .image-style {
            display: block;
            margin-left: auto;
            margin-right: auto;
            width: 150px;
            border-radius: 50%;
        }
        .hr {
            border: 3px solid black;
            margin: 10px 0;
        }
        </style>
    """, unsafe_allow_html=True)

def add_info_box(key,value):
    st.markdown(f"**{key.title()} :**",unsafe_allow_html=True)
    st.info(f"{value}", icon="ℹ")

# Function to add a footer to the app
def add_footer():
    footer_info = user_info.get("footer_info", {})
    name = footer_info.get("name", "User")
    linkedin_url = footer_info.get("linkedin_url", "#")
    year = footer_info.get("year", "2024")
    st.markdown(f"""
        <style>
        .footer {{
            position: fixed;
            left: 0;
            bottom: 0;
            width: 100%;
            background-color: #f1f1f1;
            color: #2c3e50;
            text-align: center;
            padding: 10px;
            font-size: 14px;
            font-weight: bold;
            border-top: 1px solid #ddd;
        }}
        .footer a {{
            color: #2c3e50;
            text-decoration: none;
            font-weight: normal;
        }}
        </style>
        <div class="footer">
            Created by <a href="{linkedin_url}" target="_blank">{name}</a> |
            © {year} All rights reserved
        </div>
    """, unsafe_allow_html=True)

def make_hyperlink(key, value):
    return st.markdown(f"<div class='text-style'><strong>{key.replace('hyperlink_', '').capitalize()}:</strong> <a href='{value}' target='_blank'>{value}</a></div>", unsafe_allow_html=True)

def make_download_btn(key, value):
    with open(value, "rb") as file:
        btn_label = f"Download {key.replace('download_btn_', '').capitalize()}"
        btn_name = f"{key.replace('download_btn_', 'Download ').capitalize()}"
        st.download_button(label=btn_name, data=file, file_name=f"{btn_label}.pdf")
        
def is_valid_email(email):
    email_regex = r'^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$'
    return re.match(email_regex,email) is not None

@st.dialog(" ")
def contact_me():
    with st.form("my_form"):
        st.write('<h1>Contact me via mail :</h1><hr style="border-top: 1px solid white;">',unsafe_allow_html=True)
        name = st.text_input("Name : ")
        email = st.text_input("Email : ")
        message = st.text_area("Your Message : ")
        submitted = st.form_submit_button("submit")
        if submitted:
            if not name:
                st.error("Please give name.",icon="😒")
                st.stop()
            
            if not email:
                st.error("Please give email address.",icon="🤔")
                st.stop()
                
            if not is_valid_email(email):
                st.error("Please give valid email address.",icon="😫")
                st.stop()
                
            if not message:
                st.error("Please give message!",icon="😣")
                st.stop()
                
            if send_email(name,email,message) == "Message Sent!":
                st.success("Your Email Successfully Sent!",icon="🤩")
                time.sleep(4)
                st.rerun()
            else:
                st.error("There is an issue. Come back later!",icon="😣")

def display_contact_dialog_box(key, booltype, btn_name):
    if key == "Contact_me":
        if bool(booltype):
            with st.container():
                st.write("")
                if st.button(f"{btn_name}"):
                    contact_me()    
        else:
            return None
 
def display_section(section_key, header_title, section_data, display_type):
    st.markdown(f"<div class='header-style'>{header_title}</div>", unsafe_allow_html=True)
    
    # Function to display personal information in a container with image and details in separate columns
    def display_personal_info(section_data):
        if display_type == "list":
            st.image(section_data["profile_image"], width=150, caption=section_data.get("", ""))
            for key, value in section_data.items():
                if key != "profile_image" and key.startswith("hyperlink_") == False and not key.startswith("download_btn_"):
                    st.markdown(f"<div class='text-style'><strong>{key.replace('_', ' ').capitalize()}:</strong> {value}</div>", unsafe_allow_html=True)
                if key.startswith("hyperlink_") and key != "Profile_image":
                    make_hyperlink(key,value)
                if key.startswith("download_btn_") and not key == "profile_image" and not key.startswith("hyperlink_"):
                    make_download_btn(key,value)
        else:
            with st.container(border=True):
                col1, col2 = st.columns([2, 3])
                with col1:
                    st.image(section_data["profile_image"], use_column_width=True, caption=section_data.get("", ""))
                with col2:
                    for key, value in section_data.items():
                        if key == "profile_image":
                            continue
                        if key.startswith("hyperlink_"):
                            st.markdown(f"<div class='text-style'><strong>{key.replace('hyperlink_', '').replace('_', ' ').capitalize()}:</strong> <a href='{value}' target='_blank'>{value}</a></div>", unsafe_allow_html=True)
                        elif key.startswith("download_btn_") and value:
                            make_download_btn(key,value)
                        elif not key.startswith("download_btn_"):
                            st.markdown(f"<div class='text-style'><strong>{key.replace('_', ' ').capitalize()}:</strong> {value}</div>", unsafe_allow_html=True)

    # Function to display individual items
    def display_item(item):
        if isinstance(item, dict):
            for key, value in item.items():
                if key == "add_dialog_box":
                    continue
                if key.startswith("hyperlink_"):
                    make_hyperlink(key, value)
                
                if key.startswith("info_box_"):
                    add_info_box(key.replace("info_box_", "").title(), value)
                
                if key.startswith("download_btn_"):
                    make_download_btn(key,value)
                
                if key == "image":
                    st.image(value, caption=item.get("title", ""), use_column_width=True)
                    
                elif not key.startswith("hyperlink_") and not key.startswith("download_btn_") and not key.startswith("info_box_"):
                    st.markdown(f"<div class='subheader-style'>{key.replace('_', ' ').capitalize()}:</div>", unsafe_allow_html=True)
                    st.markdown(f"<div class='text-style'>{value}</div>", unsafe_allow_html=True)
            st.markdown("<hr class='hr'></hr>", unsafe_allow_html=True)
        else:
            st.write(item)

    if section_key == "personal_info":
        display_personal_info(section_data)
    else:
        if display_type == "grid":
            cols = st.columns(2)
            for idx, item in enumerate(section_data):
                col = cols[idx % 2]
                with col:
                    display_item(item)
        else:
            for item in section_data:
                display_item(item)

# Apply custom styling
add_styling()

# Define a list of section options based on the JSON headers
options = [header["name"] for header in user_info.get("headers", [])]
option_to_key = {header["name"]: header["section"] for header in user_info.get("headers", [])}

# Ensure icons are valid Font Awesome icons
icons = [header.get("icon", "question-circle") for header in user_info.get("headers", [])]

# Check if options list is empty
if not options:
    st.error("No sections available to display.")
else:
    # Create the option menu on the left side
    with st.sidebar:
        selected_section = option_menu(
            menu_title="My Portfolio",  # Required
            options=options,  # List of section names to show
            icons=icons,  # Updated icons for each section
            menu_icon="cast",  # Menu icon
            default_index=0,  # The first option is selected by default
        )

    # Display the corresponding section based on the user's selection
    if selected_section:
        section_key = option_to_key[selected_section]  # Get the corresponding section key
        if section_key in user_info:
            # Get the display type for the selected section
            display_type = next(header["display_type"] for header in user_info["headers"] if header["name"] == selected_section)
            display_section(section_key, selected_section, user_info[section_key], display_type)

        # Show the contact me button only on the contact page
        if selected_section == "Contact":
            contact_info = user_info.get("contact", [{}])[0]
            display_contact_dialog_box("Contact_me", contact_info.get("add_dialog_box", False), "Contact Me")

# Call the function to add the footer
add_footer()
