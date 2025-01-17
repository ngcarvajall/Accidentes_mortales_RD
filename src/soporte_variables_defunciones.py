# --------- Creación ---------

query_creacion_provincia = """ 
    CREATE TABLE IF NOT EXISTS provincia (
    id_provincia int PRIMARY KEY,
    provincia varchar(100));

"""

query_creacion_dia_sem = """ 
    CREATE TABLE IF NOT EXISTS dia_semana (
    id_dia_semana int PRIMARY KEY,
    dia_semana varchar(100));

"""

query_creacion_region = """ 
    CREATE TABLE IF NOT EXISTS region (
    id_region int PRIMARY KEY,
    region varchar(100));

"""

query_creacion_mes = """ 
    CREATE TABLE IF NOT EXISTS mes (
    id_mes int PRIMARY KEY,
    mes varchar(100));

"""

query_creacion_rhora = """ 
    CREATE TABLE IF NOT EXISTS rango_hora (
    id_rango_hora int PRIMARY KEY,
    rango_hora varchar(100));

"""

query_creacion_tvia = """ 
    CREATE TABLE IF NOT EXISTS tipo_via (
    id_tipo_via int PRIMARY KEY,
    tipo_via varchar(100));

"""

query_creacion_sexo = """ 
    CREATE TABLE IF NOT EXISTS sexo (
    id_sexo int PRIMARY KEY,
    sexo varchar(100));

"""

query_creacion_gedad = """ 
    CREATE TABLE IF NOT EXISTS grupo_edad (
    id_grupo_edad int PRIMARY KEY,
    grupo_edad varchar(100));

"""

query_creacion_condivictima = """ 
    CREATE TABLE IF NOT EXISTS condicion_victima (
    id_condicion_victima int PRIMARY KEY,
    condicion_victima varchar(100));

"""

query_creacion_tipo_accidente = """ 
    CREATE TABLE IF NOT EXISTS tipo_accidente (
    id_tipo_accidente int PRIMARY KEY,
    tipo_accidente varchar(100));

"""

query_creacion_mediot = """ 
    CREATE TABLE IF NOT EXISTS mediotrans (
    id_medio_trans int PRIMARY KEY,
    medio_trans varchar(100));

"""

query_creacion_defunciones = """ 
    CREATE TABLE IF NOT EXISTS defunciones (
    fecha DATE,
    id_region int,
    id_provincia int,
    id_dia_semana INT,
    id_mes INT,
    anio INT,
    id_rango_hora INT,
    id_tipo_via INT, 
    id_sexo INT, 
    id_grupo_edad INT,
    id_condicion_victima INT, 
    id_tipo_accidente INT,
    id_medio_trans INT,
            CONSTRAINT fk_region FOREIGN KEY (id_region)
        REFERENCES region(id_region),
            CONSTRAINT fk_provincia FOREIGN KEY (id_provincia)
        REFERENCES provincia(id_provincia),
            CONSTRAINT fk_dia_semana FOREIGN KEY (id_dia_semana)
        REFERENCES dia_semana(id_dia_semana),
            CONSTRAINT fk_mes FOREIGN KEY (id_mes)
        REFERENCES mes(id_mes),
            CONSTRAINT fk_rango_hora FOREIGN KEY (id_rango_hora)
        REFERENCES rango_hora(id_rango_hora),
            CONSTRAINT fk_tipo_via FOREIGN KEY (id_tipo_via)
        REFERENCES tipo_via(id_tipo_via),
            CONSTRAINT fk_sexo FOREIGN KEY (id_sexo)
        REFERENCES sexo(id_sexo),
            CONSTRAINT fk_grupo_edad FOREIGN KEY (id_grupo_edad)
        REFERENCES grupo_edad(id_grupo_edad),
            CONSTRAINT fk_condicion_victima FOREIGN KEY (id_condicion_victima)
        REFERENCES condicion_victima(id_condicion_victima),
            CONSTRAINT fk_tipo_accidente FOREIGN KEY (id_tipo_accidente)
        REFERENCES tipo_accidente(id_tipo_accidente),
            CONSTRAINT fk_mediotrans FOREIGN KEY (id_medio_trans)
        REFERENCES mediotrans(id_medio_trans)

    );

"""

# # # # #
query_creacion_caracteristicas = ''' #esta es que se alimenta de otras
    CREATE TABLE IF NOT EXISTS caracteristicas (
        id_contenido VARCHAR,
        guion VARCHAR,
        anio INT,
        mes VARCHAR,
        duracion VARCHAR,
        calificacion FLOAT,
        argumento VARCHAR,
        FOREIGN KEY (id_contenido) REFERENCES contenido(id_contenido)
            ON UPDATE CASCADE
            ON DELETE CASCADE
    );
'''



# --------- Inserción ---------

query_inser_region = '''
    INSERT INTO region (id_region, region) 
    values (%s, %s);
'''

query_inser_provincia = '''
    INSERT INTO provincia (id_provincia, provincia) 
    values (%s, %s);
'''

query_inser_dia_semana = '''
    INSERT INTO dia_semana (id_dia_semana, dia_semana) 
    values (%s, %s);
'''

query_inser_mes = '''
    INSERT INTO mes (id_mes, mes)
    values (%s, %s);
'''

query_inser_rango_hora = '''
    INSERT INTO rango_hora (id_rango_hora, rango_hora)
    values (%s, %s);
'''

query_inser_tipo_via = '''
    INSERT INTO tipo_via (id_tipo_via, tipo_via)
    values (%s, %s);
'''

query_inser_sexo = '''
    INSERT INTO sexo (id_sexo, sexo)
    values (%s, %s);
'''

query_inser_grupo_edad = '''
    INSERT INTO grupo_edad (id_grupo_edad, grupo_edad)
    values (%s, %s);
'''

query_inser_condicion_victima = '''
    INSERT INTO condicion_victima (id_condicion_victima, condicion_victima)
    values (%s, %s);
'''

query_inser_tipo_accidente = '''
    INSERT INTO tipo_accidente (id_tipo_accidente, tipo_accidente)
    values (%s, %s);
'''

query_inser_mediot = '''
    INSERT INTO mediotrans (id_medio_trans, medio_trans)
    values (%s, %s);
'''

query_inser_defunciones = '''
    INSERT INTO defunciones (fecha, id_region, id_provincia, id_dia_semana, id_mes, anio, 
    id_rango_hora, id_tipo_via, id_sexo, id_grupo_edad, id_condicion_victima, id_tipo_accidente,
    id_medio_trans)
    values (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
'''