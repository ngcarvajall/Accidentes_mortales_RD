# --------- Creación ---------

query_creacion_defunciones_predict = """ 
    CREATE TABLE IF NOT EXISTS defunciones_predict (
    fecha DATE,
    predicciones int
    );

"""

query_creacion_parque_vehicular_predict = """ 
    CREATE TABLE IF NOT EXISTS parque_veh_predict (
    fecha DATE,
    predicciones int);

"""

query_creacion_poblacion_predict = """ 
    CREATE TABLE IF NOT EXISTS poblacion_predict (
    fecha DATE,
    predicciones int);

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

# --------- Llamada ---------

query_EDA_1 = """
            SELECT fecha, count(*) AS casos_defunciones
FROM defunciones d
GROUP BY fecha
ORDER BY fecha ;
"""