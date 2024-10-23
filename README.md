# Python Environment Setup

A user-friendly GUI application for creating and configuring Python virtual environments with pre-configured package sets for different development scenarios.

<p align="center">
  <picture>
    <source media="(prefers-color-scheme: dark)" srcset="./Assets/View.png">
    <img src="./Assets\View.png">
  </picture>
</p>

## Features

- Create virtual environments with custom or auto-generated names
- Pre-configured package sets for:
  - Data Science (numpy, pandas, scipy, scikit-learn, matplotlib, seaborn)
  - Flask Web Development (flask, flask-sqlalchemy, flask-migrate, flask-wtf)
  - Django Web Development (django, djangorestframework, psycopg2)
  - General Scripting (requests, beautifulsoup4, openpyxl, pdfplumber)
- Support for custom requirements.txt files
- Progress tracking with visual feedback
- Modern and intuitive user interface using CustomTkinter
- Cross-platform compatibility (Windows, macOS, Linux)

## Prerequisites

- Python 3.x
- pip (Python package installer)

## Installation

1. Clone the repository or download the source code:
```bash
git clone hhttps://github.com/dote7ant/Environments_Automation.git
cd Environments_Automation
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

or 

```bash
pip install customtkinter
```

## Usage

1. Run the application:
```bash
python auto.py
```

2. Follow these steps in the GUI:
   - Select an environment category (Data Science, Flask, Django, or Scripting)
   - Optionally enable and specify a custom environment name
   - Choose whether to use a requirements.txt file
   - Select the directory where the virtual environment will be created
   - Click "Create Environment" and wait for the process to complete

## Project Structure

```
Environments_Automation/
├── auto.py                 # Main application file
├── themes/                 # Custom themes directory
│   └── violet.json        # Violet theme configuration
├── README.md              # Project documentation
└── requirements.txt       # Project dependencies
└──  LICENSE     # Project license

```

## Customization

### Adding New Package Sets

To add new package sets, modify the package lists at the beginning of `auto.py`:

```python
new_category_packages = ['package1', 'package2', 'package3']
```

Alternatively you can also use a requirements.txt file to use your own packages without hardcoding them into the program.

### Changing Theme

The application uses a custom violet theme by default. To modify the appearance:

1. Edit the theme file in `themes/violet.json`
2. Or create a new theme file and update the theme setting in `main.py`:
```python
ctk.set_default_color_theme("themes/your_theme.json")
```

## Contributing

1. Fork the repository
2. Create a new branch for your feature
3. Commit your changes
4. Push to the branch
5. Create a new Pull Request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [CustomTkinter](https://github.com/TomSchimansky/CustomTkinter) for the modern UI components
- Python venv module for virtual environment management

## Support

For support, please open an issue in the GitHub repository or contact [tonymwaura7@gmail.com].