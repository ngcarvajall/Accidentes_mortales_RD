# --------- Creación ---------

query_creacion_defunciones_predict = """ 
    CREATE TABLE IF NOT EXISTS defunciones_predict (
    fecha DATE,
    predicciones int
    );

"""

query_creacion_parque_vehicular_predict = """ 
    CREATE TABLE IF NOT EXISTS parque_veh_predict (
    anio int,
    predicciones int);

"""

query_creacion_poblacion_predict = """ 
    CREATE TABLE IF NOT EXISTS poblacion_predict (
    anio int,
    predicciones int);

"""

# --------- Inserción ---------

query_inser_defunciones_predict = '''
    INSERT INTO defunciones_predict (fecha, predicciones) 
    values (%s, %s);
'''

query_inser_parque_vehicular_predict = '''
    INSERT INTO parque_veh_predict (anio, predicciones) 
    values (%s, %s);
'''

query_inser_poblacion_predict = '''
    INSERT INTO poblacion_predict (anio, predicciones) 
    values (%s, %s);
'''

# --------- Llamada ---------

query_EDA_1 = """
            SELECT fecha, count(*) AS casos_defunciones
FROM defunciones d
GROUP BY fecha
ORDER BY fecha ;
"""