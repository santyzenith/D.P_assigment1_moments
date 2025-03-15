import os
from pathlib import Path

from dotenv import load_dotenv

dotenv_path = Path(__file__).resolve().parent / '.env'
if dotenv_path.exists():
    load_dotenv(dotenv_path)

from moments import create_app  # noqa

config_name = os.getenv('FLASK_CONFIG', 'development')
app = create_app(config_name)

# Activar el modo debug
app.config['DEBUG'] = True  # Asegúrate de que esta línea esté presente

if __name__ == "__main__":
    app.run(debug=True)  # Esto también asegura que Flask corra en modo debug