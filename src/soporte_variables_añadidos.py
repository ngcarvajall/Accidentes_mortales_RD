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

query_creacion_parqueveh_2023 = """ 
    CREATE TABLE IF NOT EXISTS parque_veh_2023 (
    provincia VARCHAR(100) PRIMARY KEY,
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

query_creacion_infracciones = """ 
    CREATE TABLE IF NOT EXISTS infracciones (
    anio int,
    infraccion VARCHAR(150),
    total int
    );

"""

query_creacion_comparacion_es = """ 
    CREATE TABLE IF NOT EXISTS comparacion_modelo (
    anio int,
    valor int,
    tipo VARCHAR(100)
    );

"""

query_creacion_poblacion_es = """ 
    CREATE TABLE IF NOT EXISTS poblacion_es (
    anio int,
    poblacion int
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

query_inser_pveh_2023 = '''
    INSERT INTO parque_veh_2023 (provincia, automoviles, autobuses,
    jeep, carga, motocicletas, volteo, maquinas_pesadas,
    otros, total)
    values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
'''

query_inser_infracciones = '''
    INSERT INTO infracciones (anio, infraccion, total)
    values (%s, %s, %s);
'''

query_inser_comparacion_es = '''
    INSERT INTO comparacion_modelo (anio, valor, tipo) 
    values (%s, %s, %s);
'''

query_inser_poblacion_es = '''
    INSERT INTO poblacion_es (anio, poblacion) 
    values (%s, %s);
'''
# --------- Llamada ---------

query_EDA_1 = """
            SELECT fecha, count(*) AS casos_defunciones
FROM defunciones d
GROUP BY fecha
ORDER BY fecha ;
"""