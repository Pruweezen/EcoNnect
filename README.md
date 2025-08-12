# EcoNnect 

EcoNnect connects LGUs, companies, and jobseekers around green jobs.
This README explains how to set up the project locally, run each module (LGU / Company / Jobseeker) independently or together, 
run DB migrations, and follow the git workflow for collaboration.

---

## Prerequisites

Before you begin, make sure you have installed:

- **Python 3.10+** → [Download Python](https://www.python.org/downloads/)
- **pip** (comes with Python)
- **Git** → [Download Git](https://git-scm.com/downloads)
- A **GitHub account**
- (Optional) **Visual Studio Code** or any preferred IDE

---

## Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/Pruweezen/EcoNnect.git
cd EcoNnect
 ```

### 2. Create a Virtual Environment
```bash
python -m venv venv
 ```

### 3. Activate the Virtual Environment
```bash
venv\Scripts\activate
 ```

### 4. Install Dependencies
```bash
pip install -r requirements.txt
 ```
### 5. Create Your .env File
```bash
FLASK_ENV=development
SECRET_KEY=replace-with-a-real-secret
DB_HOST=localhost
DB_PORT=3306
DB_NAME=econnnect_db
DB_USER=econnnect_user
DB_PASSWORD= (your pass here)

 ```

### 6. Initialize the Database (First Time Only)
```bash
flask db init
flask db migrate -m "Initial migration"
flask db upgrade
 ```

### 6. Run the App (Jobseeker-side)
```bash
py run_jobseeker.py
 ```

## Branch Workflow (For Collaborators)

### 1. Check out the main branch and pull the latest changes
```bash
git checkout main
git pull origin main
 ```

### 2. Create your branch
```bash
git checkout -b feature/<your-feature-name>
 ```

## Notes
* Always activate your virtual environment before working.
* Never push changes directly to main.
* Pull the latest code from main before creating your feature branch.
