# --------- Creación ---------

query_creacion_parque_vehicular = """ 
    CREATE TABLE IF NOT EXISTS parque_vehicular (
    anio int,
    automoviles int,
    autobuses int,
    jeep int,
    carga int,
    motocicletas int,
    volteo int,
    maquinas_pesadas int,
    otros int,
    total int
);

"""


# --------- Inserción ---------

query_inser_parque_vehicular = '''
    INSERT INTO parque_vehicular (anio, automoviles, autobuses, 
    jeep, carga, motocicletas, 
    volteo, maquinas_pesadas, 
    otros, total) 
    values (%s, %s,%s, %s, %s, %s, %s, %s, %s, %s);
'''

# --------- Llamada ---------

query_autos_historico = """
SELECT anio, total
FROM parque_vehicular;
"""