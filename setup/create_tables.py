import sys
import os

# Add the project root to Python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.append(project_root)

print("Added to sys.path:", project_root)

from app.core.database import engine, Base
from app.models.plant import Plant
from app.models.sensor import Sensor

# Import models so SQLAlchemy knows about them
print("Creating database tables...")

# Create all tables
Base.metadata.create_all(bind=engine)

print("✅ Tables created successfully!")