# DEF4TGB

This project contains an algorithmic trading system template with modular design, secure secrets management, and a basic structure for development.

## 📥 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-user/DEF4TGB.git
   cd DEF4TGB
   ```

2. **Install Poetry**  
   Follow the [official guide](https://python-poetry.org/docs/#installing-with-the-official-installer).

   Example (Linux/Mac):  
   ```bash
   curl -sSL https://install.python-poetry.org | python3 -
   ```

3. **Install dependencies from `poetry.lock`**  
   ```bash
   poetry install
   ```

   This will:  
   - Create/activate a virtual environment.  
   - Install all exact versions defined in `poetry.lock`.


## ▶️ Running the Project

You can run Python scripts inside the Poetry environment without entering the shell:

```bash
poetry run python -m src.main
```