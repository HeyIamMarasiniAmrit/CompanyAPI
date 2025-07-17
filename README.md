CompanyAPI 🚀
A simple REST API built with Python, Django, and Django REST Framework for managing company data. This project serves as a backend foundation for handling CRUD operations on companies.

🔥 Features
List all companies

Retrieve single company details

Create new companies

Update existing companies

Delete companies

Built with Django REST Framework for easy API development

🛠️ Tech Stack
Python 

Django 

Django REST Framework 

SQLite (default)

🚀 Getting Started
1️⃣ Clone the Repository
git clone https://github.com/yourusername/companyapi.git
cd companyapi

2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows

3️⃣ Install Dependencies
pip install -r requirements.txt
Example requirements.txt:
Django>=4.0
djangorestframework

4️⃣ Apply Migrations
bash
Copy
Edit
python manage.py migrate

5️⃣ Run the Development Server
python manage.py runserver
📡 API Endpoints
Method	Endpoint	Description
GET	/api/companies/	List all companies
POST	/api/companies/	Create a company
GET	/api/companies/{id}/	Retrieve a company
PUT	/api/companies/{id}/	Update a company
DELETE	/api/companies/{id}/	Delete a company

📄 License
This project is open source and available under the MIT License.

🤝 Contributing
Pull requests are welcome! Feel free to fork and submit a PR.

