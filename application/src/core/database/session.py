import sqlalchemy.orm


from src.core.database.engine import engine



# Construye un generador de sesiones SQLAlchemy con configuraciones específicas.
#   - autocommit      Desactiva la confirmación automática de transacciones.
#   - autoflush       Desactiva la actualización automática de objetos en la sesión.
#   - bind            Asocia el motor creado anteriormente con las sesiones.
session = sqlalchemy.orm.sessionmaker(autocommit=False, autoflush=False, bind=engine)