# Proyecto_Final

En mis tablas de Accidentes y Defunciones existen numerosos duplicados, esto viene a ser explicado porque no existen fechas en concreto. La realidad es que los datos son generados para oscilar entre los 7 días de las semanas, durante un mes. Sin embaro, estos 7 días no se resaltan con un respectivo señalamiento específico de fecha. Por lo que aunque parezca que hay duplicados, simplemente ocurre porque no tenemos la certeza de que verdaderamente sean el mismo día o no.

Posibles soluciones:
- Licencia de conducir con sistema de puntos
- Tranporte público de calidad
- Vehículos privados que se puedan compartir
- Facilidades para el transporte en medios alternativos

Modelos para Defunciones: ** el mejor es 4,1,3
    Usando los parámetros 3,0,4 las métricas fueron:
    MAE para toda la serie: 16.64075273195455
    MAPE para toda la serie: 11.28%
    RMSE para toda la serie: 22.167746562001817

    Usando los parámetros 4,1,3 las métricas fueron:
    MAE para toda la serie: 16.4907972167027
    MAPE para toda la serie: 11.26%
    RMSE para toda la serie: 22.432731437600925

    Con prophet fueron:
    MAE: 16.811434077383815
    MAPE: 11.77%
    RMSE: 21.806114837171673

    Considerando los resultados, el mejor modelo resulta ser el que usa los parámetros 4,1,3

Modelos para parque vehicular: 
    Usando los mejores parámetros p=5, q=3
    MAE para toda la serie: 150194.43418760004
MAPE para toda la serie: 7.22%
RMSE para toda la serie: 252972.20236123272

    Con prophet:
    MAE: 27953.415849852558
MAPE: 1.20%
RMSE: 35695.90172282073

