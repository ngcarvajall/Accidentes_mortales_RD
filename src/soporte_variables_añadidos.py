# --------- Creación ---------

query_creacion_parque_vehicular_es = """ 
    CREATE TABLE IF NOT EXISTS parque_vehicular_es (
    anio int PRIMARY KEY,
    camiones_furgonetas int,
    autobuses int,
    turismos int,
    motocicletas int,
    tractores int,
    remolques int,
    otros int, 
    ciclomotores int,
    total int
    );

"""

query_creacion_defunciones_es = """ 
    CREATE TABLE IF NOT EXISTS defunciones_es (
    anio int PRIMARY KEY,
    fallecidos int);

"""

query_creacion_antiguedad_pveh = """ 
    CREATE TABLE IF NOT EXISTS antiguedad_pveh_rd (
    anio int PRIMARY KEY,
    motocicletas int, 
    automoviles int,
    jeeps int,
    carga int, 
    autobuses int,
    maquinas_pesadas int, 
    volteo int,
    otros int, 
    total int);

"""

query_creacion_genero_provincia = """ 
    CREATE TABLE IF NOT EXISTS vehiculos_genero_provincia (
    provincia VARCHAR (100) PRIMARY KEY,
    femenino int,
    masculino int,
    total int);

"""


query_creacion_propietario = """ 
    CREATE TABLE IF NOT EXISTS propietario (
    propietario VARCHAR(100) PRIMARY KEY,
    motocicletas int,
    automoviles int,
    jeep int,
    carga int,
    autobuses int,
    maquinas_pesadas int,
    volteo int,
    otros int,
    total int
    );

"""



# --------- Inserción ---------

query_inser_parque_vehicular_es = '''
    INSERT INTO parque_vehicular_es (anio, camiones_furgonetas,
    autobuses, turismos, motocicletas,
    tractores, remolques, otros, ciclomotores, total) 
    values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
'''

query_inser_defunciones_es = '''
    INSERT INTO defunciones_es (anio, fallecidos) 
    values (%s, %s);
'''

query_inser_antiguedad_pveh = '''
    INSERT INTO antiguedad_pveh_rd (anio, motocicletas, automoviles, 
    jeeps, carga, autobuses, maquinas_pesadas, volteo,
    otros, total) 
    values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
'''

query_inser_genero_provincia = '''
    INSERT INTO vehiculos_genero_provincia (provincia, femenino, masculino, total)
    values (%s, %s, %s, %s);
'''

query_inser_propietario = '''
    INSERT INTO propietario (propietario, motocicletas, automoviles, 
    jeep, carga, autobuses, maquinas_pesadas, volteo,
    otros, total)
    values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
'''

# --------- Llamada ---------

query_EDA_1 = """
            SELECT fecha, count(*) AS casos_defunciones
FROM defunciones d
GROUP BY fecha
ORDER BY fecha ;
"""