# 📦 Flask-Based Student Registration Web Application Deployed Using Jenkins

---

## 🎯 Objective  
To develop and deploy a web-based student registration system using Flask that allows users to submit their details through a form. The data is stored securely in a MySQL database and can be retrieved and displayed in tabular format. The deployment process is automated using Jenkins CI/CD pipeline.

---

## 🧾 Project Overview  
This project replicates a real-world student registration system used by training institutes. Traditionally, student data is maintained manually using spreadsheets, which is inefficient and prone to errors.  

This application provides a digital solution where users can register through a web interface, and their data is stored securely in a MySQL database. The project also integrates DevOps practices by automating build and deployment using Jenkins.

---

## 🛠️ Technology Stack  

| Layer | Technology Used |
|------|----------------|
| Frontend | HTML, CSS |
| Backend | Python (Flask) |
| Database | MySQL |
| Version Control | Git & GitHub |
| CI/CD Tool | Jenkins |
| Deployment | AWS EC2 (Optional) |

---

## ⚙️ Functional Requirements  

### 1. Registration Form  
- Name  
- Email  
- Phone Number  
- Course  
- Address  
- Client-side validation using HTML  
- Server-side validation using Flask  

---

### 2. Data Handling  
- Flask handles form submission  
- Data stored in MySQL database  
- Success / failure messages displayed on UI  

---

### 3. Data Retrieval  
- Route created to display all students  
- Data shown in HTML table format  

---

## 🏗️ System Architecture  

```
User (Browser)
        ↓
Frontend (HTML Form)
        ↓
Flask Backend (Python)
        ↓
MySQL Database
        ↓
Display Data (HTML Table)
```

---

## 🚀 Jenkins CI/CD Pipeline Flow  

```
GitHub Push
        ↓
Jenkins Trigger
        ↓
Install Dependencies
        ↓
Run Flask Application
        ↓
Application Deployment
```

---

## 🧩 Database Schema  

```sql
CREATE DATABASE student_db;

USE student_db;

CREATE TABLE students (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    phone VARCHAR(15),
    course VARCHAR(50),
    address TEXT
);
```

---

## ⚙️ Setup Instructions  

1. Create project folder manually  
2. Add project files (`app.py`, `templates`, `requirements.txt`)  
3. Install dependencies  
   ```bash
   pip install -r requirements.txt
   ```
4. Setup MySQL database  
   - Create database `student_db`  
   - Create table `students`  
5. Configure database in `app.py`  
6. Run application  
   ```bash
   python app.py
   ```
7. Open in browser  
   ```
   http://localhost:5000
   ```

---

## 📸 Screenshots  

- Registration Form Page  
- Successful Submission Message  
- Student List Table  
- Edit Student Info  
- Jenkins Build Success Console  

---

## 🧠 Conclusion  
This project demonstrates the development of a full-stack web application using Flask and MySQL. It also showcases DevOps practices by integrating Jenkins for CI/CD automation. The system improves efficiency by replacing manual data entry with a secure and scalable web-based solution.

---

## 👩‍💻 Author  

**Pooja Dange**  
Cloud & DevOps Learner  

📧 Email: poojadange1501@gmail.com  
🔗 LinkedIn: https://www.linkedin.com/in/pooja-dange-0270072b3  
💻 GitHub: https://github.com/pooja-dange1501/student-registration-flask.git  

---
