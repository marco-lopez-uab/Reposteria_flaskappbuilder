from app import app, db
from app.models import Categoria, Ingrediente

with app.app_context():
    metadata = Categoria.metadata
    engine=db.engine
    print ("Se crearon las tablas")
    for tabla in metadata.sorted_tables:
        print ("--", tabla.name)
    metadata.create_all(bind=engine)
   
    print("creado correctamente")