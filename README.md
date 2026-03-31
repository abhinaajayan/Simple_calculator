# Scientific Calculator

A modern, responsive Flask web application that provides both basic and scientific mathematical operations. Features a sleek dark/light theme interface with support for trigonometric functions, logarithms, and more.

## 🌟 Features

- **Basic Operations**: Addition, Subtraction, Multiplication, Division
- **Scientific Operations**: 
  - Trigonometric functions (sin, cos, tan) with automatic degree-to-radian conversion
  - Logarithmic function (log base 10)
  - Square root
  - Power/Exponentiation
- **Error Handling**: Graceful error messages for invalid inputs and division by zero
- **Responsive Design**: Works seamlessly on desktop and mobile devices
- **Theme Support**: Toggle between dark and light modes
- **Modern UI**: Styled with smooth animations and gradient effects

## 📁 Project Structure

```
Project_Flask/
├── main.py                 # Flask application and routes
├── static/                 # Static files (CSS, images, etc.)
├── templates/
│   ├── index.html         # Calculator interface
│   └── about.html         # About page
└── README.md              # This file
```

## 🚀 Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Steps

1. **Clone or download the project**
   ```bash
   cd Project_Flask
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   ```

3. **Activate the virtual environment**
   - **Windows**:
     ```bash
     venv\Scripts\activate
     ```
   - **macOS/Linux**:
     ```bash
     source venv/bin/activate
     ```

4. **Install Flask**
   ```bash
   pip install flask
   ```

5. **Run the application**
   ```bash
   python main.py
   ```

6. **Open in browser**
   Navigate to `http://localhost:5000` in your web browser

## 💻 Usage

### Calculator Page (/)
1. Enter a number in the first input field
2. (Optional) Enter a second number if needed for operations like divide, subtract, power, etc.
3. Select an operation from the dropdown menu
4. Click the "Calculate" button
5. View the result displayed below

### Available Operations
- `add` - Addition (num1 + num2)
- `subtract` - Subtraction (num1 - num2)
- `multiply` - Multiplication (num1 × num2)
- `divide` - Division (num1 ÷ num2)
- `sin` - Sine function (angle in degrees)
- `cos` - Cosine function (angle in degrees)
- `tan` - Tangent function (angle in degrees)
- `log` - Logarithm base 10
- `sqrt` - Square root
- `power` - Exponentiation (num1 ^ num2)

### About Page (/about)
Visit the about page to learn more about the application.

## 🎨 Theme Customization

The application includes both dark and light themes. The UI uses CSS variables that can be easily customized by modifying the theme colors in `templates/index.html`.

## 📝 Code Highlights

- **Flask Routes**:
  - `GET/POST /` - Main calculator page
  - `GET /about` - About page

- **Python Libraries Used**:
  - `flask` - Web framework
  - `math` - For scientific calculations

## 🐛 Error Handling

- Division by zero: Returns "Cannot divide by zero"
- Invalid inputs: Returns "Invalid Input"
- Invalid operations: Falls through gracefully

## 📦 Dependencies

- Flask
- Python standard library (math)

## 🔧 Development

To modify the calculator:
1. Edit `main.py` to add new operations or modify routes
2. Update `templates/index.html` to change the UI or add new features
3. Modify styles in the `<style>` tag within the HTML files

## 📄 License

This project is open source and available for personal and educational use.

## 👨‍💻 Author

Created as a learning project for Flask web development.

---

**Happy Calculating!** 🧮
