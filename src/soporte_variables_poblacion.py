# --------- Creación ---------

query_creacion_poblacion = """ 
    CREATE TABLE IF NOT EXISTS poblacion (
    anio int, 
    poblacion int
);

"""


# --------- Inserción ---------

query_inser_poblacion_dominicana = '''
    INSERT INTO poblacion (anio, poblacion) 
    values (%s, %s);
'''

# --------- Llamada ---------

query_poblacion = """
SELECT *
FROM poblacion;
"""