# Project Title: Custom TOTP Generator

## Description
This project is a web application that generates a TOTP seed based on user input. Users can enter a description and issuer name, and the application will generate a unique seed and display the corresponding QR code for importing to supported applications.

This is ideal if you would like to create custom seeds for your own services, knowing that you are the only one creating the seed, without any potential for secret copying of the seed.

## Project Structure
```
web-project
├── src
│   ├── app.py
│   ├── static
│   │   └── styles.css
│   └── templates
│       └── index.html
├── requirements.txt
└── README.md
```

## Setup Instructions
1. Clone the repository to your local machine.
2. Navigate to the project directory.
3. Install the required dependencies by running:
   ```
   pip install -r requirements.txt
   ```
4. Start the internal web server by executing:
   ```
   python src/app.py
   ```
5. Open your web browser and go to `http://127.0.0.1:5000` to access the application.

## Usage Guidelines
- Enter the purpose name in the first input field.
- Enter the name of the issuer in the second input field.
- Click the "Generate QR Code" button to create the QR code.
- The generated QR code will be displayed below the input fields.

## Dependencies
- Flask
- qrcode
- hashlib
- base64
- random
