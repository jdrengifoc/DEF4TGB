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

## 🛠️ Development Plan

### Interfaz
1. **API o clase de Python** que sirva como interfaz para operaciones comunes y que los códigos de trading se conecten vía dicha interfaz.
   - Conexión/Desconexión
   - Definir modo (demo/real)
   - Controles
   - Quotas: definir los límites tanto del broker como nuestros
   - Apagar TP y SL en rollovers
   - Obtener datos
   - Abrir y cerrar operación con TP y SL
   - Actualizar TP y SL
   - Información activo: rollover, swap, margin, margin_level, comisión, contract_value, pip, horario, spread

2. **Ciclo de vida de los datos**
   - Descargar los datos iniciales (ancho_de_ventana y temporalidad)
   - Actualizar los datos (frecuencia y temporalidad)
   - Limpieza

3. **Modelo**
   - Inputs: datos, info_activo
   - Hiperparámetros: ancho_de_ventana y temporalidad
   - Output: forecast, decision_rule → pending order (sell/buy + price + volumen/pip, TP/SL)

4. **Retroalimentación**
   - Logs
   - Métricas de error
   - Informes (conexión, financiero, pipeline, errores)

### 📚 ¿Cómo aprendemos?
- Políticas
- Lectura