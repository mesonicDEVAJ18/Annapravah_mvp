# Annapravah
https://www.canva.com/design/DAGs5syhpG0/NjWI-KTBUVYCCiT2vvguTQ/edit?utm_content=DAGs5syhpG0&utm_campaign=designshare&utm_medium=link2&utm_source=sharebutton

## Bridging the Gap Between Food Waste and Hunger

### Team Members:
- Devaj Rathore
- Saanvi Singh
- Shubhi Jain
- Manaswi Singh

## Overview
Annapravah is a web-based platform built using Django that aims to reduce food waste by efficiently redistributing surplus food from donors (restaurants, grocery stores, wedding caterers) to NGOs and food banks in need. 


## Features
- **Real-time database in SQLite**: Efficiently stores and manages donation and request data.
- **Real-time geolocation in two formats**: Supports both address-based and coordinate-based location tracking.
- **Best Match algorithm for donations and requests**: Optimizes food distribution by pairing donors with recipients.
- **Live maps to show surplus and deficit in Leaflet**: Provides a visual representation of food availability and demand.
- **Navigation aid to aid in transport with Leaflet**: Helps volunteers and donors navigate efficiently.
- **Certificates for helping plan navigation using ReportLab**: Generates official certificates for contributions.
- **OOPS to maintain donations and requests**: Uses Object-Oriented Programming principles to manage system entities.
- **Archives**: Stores past donations and requests for reference and reporting.
- **User authentication**: Ensures secure access and data protection for users.


## Tech Stack
- **Django**: Backend framework for building and managing web applications.
- **HTML, CSS, JavaScript, Bootstrap**: Frontend technologies for designing an interactive UI.
- **Geopy**: Library for geocoding and handling geolocation data.
- **ReportLab**: Used for generating PDF certificates.
- **SQLite**: Lightweight database for efficient data storage.
- **Leaflet**: Interactive maps for geolocation and navigation.



## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo/annapravah.git
   cd annapravah
   ```
2. Create and activate a virtual environment:
   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Apply migrations:
   ```bash
   python manage.py migrate
   ```
5. Start the server:
   ```bash
   python manage.py runserver
   ```

## Usage
- Open `http://127.0.0.1:8000/` in your browser.
- Register as a **Donor** or **NGO** to start listing or requesting food donations.
- Use the **Navigate** feature to view real-time routes and delivery details.


<!-- ### PROJECT STRUCTURE:
\annapravah/
│── annapravah/           # Project settings
│── foodapp/              # Your app (Create with `python manage.py startapp foodapp`)
│   │── templates/        # Store all HTML files here
│   │   │── base.html     # Common layout (navbar, footer, etc.)
│   │   │── home.html     # Homepage
│   │   │── donor_dashboard.html
│   │   │── claimer_dashboard.html
│   │   │── ai_matching.html
│   │   │── logistics.html
│   │   │── admin_panel.html
│   │   │── monitor_matches.html
│   │   │── request_food.html
│── manage.py
│── db.sqlite3 -->
