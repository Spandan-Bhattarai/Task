# Backend Internship Assignment – Intuji

## Author
**Spandan Bhattarai**  
Date: July 25, 2025

---

## 📌 Overview

This repository contains the solution for the Backend Internship Assignment provided by **Intuji**. It includes:

- A Flask-based RESTful API for blog management
- A Python function to find a pair of numbers in an array that sum to a target value
- Postman collection to test the APIs
- A detailed report documenting the approach and implementation (available in both DOCX and PDF)

---

## 📁 Folder Structure

- app.py # Flask application for blog APIs
-  pair_sum.py # Function to find a pair with a given sum
-  postman_collection.json # Postman collection for API testing
- Backend_Internship_Assignment_Report_Spandan.docx
- Backend_Internship_Assignment_Report_Spandan.pdf

## Blog API (Flask)

### Features
- Add a blog (`POST /blogs`)
- View all blogs (`GET /blogs`)
- View blog by ID (`GET /blogs/<id>`)
- Update blog (`PUT /blogs/<id>`)

### Requirements
- Python 3.8+
- Flask
- SQLite

### Setup Instructions

```bash
# Clone the repo
git clone https://github.com/Spandan-Bhattarai/backend-internship-assignment.git
cd backend-internship-assignment

# Create virtual environment (optional but recommended)
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate

# Install dependencies
pip install flask flask_sqlalchemy

# Run the server
python app.py
```

## Pair with Given Sum

**File**: `pair_sum.py`

This script takes an integer array and a target value, and prints a pair (if found) that adds up to the target sum using an optimized hash-based approach with O(n) time complexity.

---

## Postman Collection

The file `postman_collection.json` contains sample requests for:

- Creating a blog
- Fetching blogs
- Updating a blog

You can import this collection into Postman to test the API endpoints quickly and efficiently.

---

## Report

Refer to the attached documentation files:

- `Backend_Internship_Assignment_Report_Spandan.docx`
- `Backend_Internship_Assignment_Report_Spandan.pdf`

These documents include:

- Problem breakdown
- Implementation logic
- Code snippets
- Sample inputs and expected outputs

---

## Contact

Feel free to reach out for any queries:

**Spandan Bhattarai**  
Email: spandanbhattarai@gmail.com  
GitHub: [https://github.com/Spandan-Bhattarai](https://github.com/Spandan-Bhattarai)
