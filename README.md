CompanyAPI 🚀
A simple REST API built with Python, Django, and Django REST Framework for managing company data. This project serves as a backend foundation for handling CRUD operations on companies.
crud operations 
<img width="1047" height="861" alt="Image" src="https://github.com/user-attachments/assets/e94ec3dc-abd2-4a49-9a8a-7aae8ae32ddd" />

testing in postman 
<img width="1841" height="837" alt="Image" src="https://github.com/user-attachments/assets/1c8f7f78-a792-42ba-8379-bbbb153ce030" />

create Employee class And test in crud operations
<img width="1017" height="947" alt="Image" src="https://github.com/user-attachments/assets/a034711f-7694-4d43-9bf9-25389517533f" />

creating comapny emplouees exits or not
<img width="962" height="891" alt="Image" src="https://github.com/user-attachments/assets/3fe8f405-29d2-4466-8e84-c4aec08edca0" />

tasting on postman
<img width="1443" height="903" alt="Image" src="https://github.com/user-attachments/assets/62e14527-eafb-4388-b0cc-d42bb000d475" />

companies exist or not
<img width="1013" height="685" alt="Image" src="https://github.com/user-attachments/assets/966cdb14-3c99-4de8-93ee-8a7e10f1f85a" />
🔥 Features
List all companies

Retrieve single company details

Create new companies.

Update existing companies.

Delete companies.

Built with Django REST Framework for easy API development.

🛠️ Tech Stack
Python 

Django 

Django REST Framework 

SQLite (default)

🚀 Getting Started
1️⃣ Clone the Repository
git clone https://github.com/companyapi.git
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


🤝 Contributing
Pull requests are welcome! Feel free to fork and submit a PR.

