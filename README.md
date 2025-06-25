# recipify-backend
RECIPE SHARING PLATFORM
Full-Stack Web Application (React + Flask)

PROJECT OVERVIEW
A web application where users can:

Register, log in, and manage profiles.

Create, view, update, and delete recipes.

Add comments to recipes and search by keywords.

Securely authenticate using JWT.

TECH STACK

Frontend: React (CDN), Tailwind CSS, react-router-dom.

Backend: Flask, SQLite/PostgreSQL, Flask-JWT-Extended.

Authentication: JWT (JSON Web Tokens).

Deployment: Vercel (frontend), Render (backend).

SETUP INSTRUCTIONS

1. Backend Setup
Prerequisites: Python 3.8+, pip

Navigate to the backend folder:
cd backend

Create and activate a virtual environment:

Linux/macOS:
python3 -m venv venv
source venv/bin/activate

Windows:
python -m venv venv
.\venv\Scripts\activate

Install dependencies:
pip install -r requirements.txt

Set up environment variables:
Create a .env file in the backend folder with:

text
SECRET_KEY=your-secret-key  
DATABASE_URL=sqlite:///recipes.db  
JWT_SECRET_KEY=your-jwt-secret-key  
Initialize the database:

Run:
flask shell

In the Flask shell:

text
from app import create_app  
from models import db  
app = create_app()  
with app.app_context():  
    db.create_all()  
    exit()  
Start the backend server:
flask run
Server runs at: http://localhost:5555

2. Frontend Setup
Prerequisites: Node.js (if using npm)

Navigate to the frontend folder:
cd frontend

Install dependencies (if using npm):
npm install

Start the frontend:

npm start
Frontend runs at: http://localhost:3000

API ENDPOINTS

Authentication

POST /api/register: Register a new user.
Request: { "username": "test", "email": "test@example.com", "password": "1234" }

POST /api/login: Log in and get a JWT.
Request: { "username": "test", "password": "1234" }

Recipes

GET /api/recipes: List all recipes.

POST /api/recipes: Create a recipe (JWT required).
Request: { "title": "Pasta", "ingredients": "Flour, Water", "instructions": "Mix and cook" }

Comments

POST /api/comments: Add a comment (JWT required).
Request: { "text": "Delicious!", "recipe_id": 1 }

Search

GET /api/search?q=pasta: Search recipes by keyword.

TESTING

Backend tests:
Run pytest tests/ in the backend folder.

Frontend tests:
Run npm test (if using Jest/React Testing Library).

DEPLOYMENT

Backend:

Deploy to Render/Heroku with the DATABASE_URL set to a PostgreSQL instance.

Frontend:

Deploy to Vercel/Netlify by linking the Git repository.

TROUBLESHOOTING

Database Issues: Delete recipes.db and rerun db.create_all().

CORS Errors: Ensure the frontend URL is whitelisted in Flask-CORS.

Missing Dependencies: Re-run pip install -r requirements.txt.

CONTRIBUTORS

[Benson]

[Team Members (Alvin Kimani, Habert Otieno, Bramwel Mutngati)]


