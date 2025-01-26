# Bike Shop 

This is a Django-based web application for managing a bike shop. The application allows users to view available bikes, place orders, and manage inventory.

Web applications help various businesses promote their products, manage orders effectively, and communicate well with customers. In this project, I will implement a web application for a bike shop. The application will allow customers to order a custom bike of their choice, provided that the relevant bike parts are in store. The shop employees will be able to manage the orders and update the status of the available parts. Ready for a ride? Let's go!

## Table of Contents
- [Installation](#installation)
- [Usage](#usage)
- [Features](#features)
- [Contributing](#contributing)
- [License](#license)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/AstronauticalCodes/bikeShop.git
   ```

2. Navigate to the project directory:
   ```bash
   cd bikeShop
   ```

3. Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

4. Install the dependencies:
   ```bash
   pip install -r requirements.txt
   ```

5. Apply the migrations:
   ```bash
   python manage.py migrate
   ```

6. Run the development server:
   ```bash
   python manage.py runserver
   ```

## Usage

Navigate to `http://127.0.0.1:8000/` in your web browser to access the application. The homepage provides a link to visit the bike shop.

## Features

- **View available bikes**: Users can view a list of available bikes and their details.
- **Place orders**: Users can place orders for bikes, and the inventory is updated accordingly.
- **Admin management**: Admins can manage the inventory and view orders.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch`
3. Make your changes and commit them: `git commit -m 'Add new feature'`
4. Push to the branch: `git push origin feature-branch`
5. Open a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---
