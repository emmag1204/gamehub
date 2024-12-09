# GameHub

**GameHub** is a web application we built using Flask
by **Emma Alfaro** and **Vincent Nguyen**
This app allows users to view, add, and organize games by category.

## Features

- View games by different categories, watch every category on the main page.
- Add new games with details (name, description, platform, image)

## Technologies Used

- Flask (for the web framework)
- HTML, CSS (for styling)
- SQLAlchemy (for database management)

## Setup

### Prerequisites

- Python 3.9 or higher

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/emmag1204/gamehub.git
   cd gamehub
 2. Create a Virtual Environment:
A virtual environment helps manage dependencies without conflicting with other projects.
- On macOS/Linux:
  ```bash
  python3 -m venv venv
  source venv/bin/activate
- On Windows:
  ```bash
  venv\Scripts\activate
3. Install Required Dependencies:
   ```bash
   pip install -r requirements.txt
4. Initialize the Database Migration:
   ```bash
   flask db init
   flask db migrate
   flask db upgrade
   flask seed
5. Run the application:
   ```bash
   flask run
- App will start by default on http://127.0.0.1:5000/

