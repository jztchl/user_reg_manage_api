
<br />
<div align="center">
  <a href="https://github.com/kmvishnu625/blog">
    <img src="favicon.ico" alt="Logo" width="80" height="80">
  </a>

<h1 align="center">User Registration and Management API</h1>

  <p align="center">
  An Django Rest API to create ,update and delete users on the go
  </p>
</div>


```markdown
# User Registration and Management API



An API to create, update, and delete users on the go using Django Rest Framework.

## About

This project is a simple REST API built with Django Rest Framework to manage user registrations and their management. It provides endpoints to create, update, retrieve, and delete user information.

## Features

- **User Registration**: Create new users with the necessary details.
- **User Management**: Update and delete existing users.
- **User Retrieval**: Retrieve user information by ID.
- **RESTful Endpoints**: Fully RESTful API endpoints for seamless integration.

## Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/jztchl/user_reg_manage_api.git
   cd user_reg_manage_api
   ```

2. **Create and Activate a Virtual Environment**
   ```bash
   python3 -m venv env
   source env/bin/activate  # On Windows use `env\Scripts\activate`
   ```

3. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Apply Migrations**
   ```bash
   python manage.py migrate
   ```

5. **Run the Server**
   ```bash
   python manage.py runserver
   ```

## API Endpoints

The following endpoints are available:

- **POST /api/users/**: Create a new user.
- **GET /api/users/**: Retrieve a list of users.
- **GET /api/users/{id}/**: Retrieve a user by ID.
- **PUT /api/users/{id}/**: Update a user by ID.
- **DELETE /api/users/{id}/**: Delete a user by ID.

## Project Structure

- **appapi/**: Directory containing the main application logic.
- **projectapi/**: Directory containing the project settings and configurations.
- **db.sqlite3**: SQLite database file.
- **manage.py**: Django management script.
- **requirements.txt**: File listing required Python packages.
- **Readme.md**: Project documentation.

## Contributing

Contributions are welcome! Please create an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License.

```

Feel free to customize this README further to better suit your project’s specifics and additional details.
