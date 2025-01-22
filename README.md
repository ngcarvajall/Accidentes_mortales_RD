# Proyecto_Final

En mis tablas de Accidentes y Defunciones existen numerosos duplicados, esto viene a ser explicado porque no existen fechas en concreto. La realidad es que los datos son generados para oscilar entre los 7 días de las semanas, durante un mes. Sin embaro, estos 7 días no se resaltan con un respectivo señalamiento específico de fecha. Por lo que aunque parezca que hay duplicados, simplemente ocurre porque no tenemos la certeza de que verdaderamente sean el mismo día o no.

Posibles soluciones:
- Licencia de conducir con sistema de puntos
- Tranporte público de calidad
- Vehículos privados que se puedan compartir
- Facilidades para el transporte en medios alternativos

Modelos para Defunciones:
    Modelo 1:
        Usando los parámetros 4,0,3 las métricas fueron:
        MAE para toda la serie: 16.033110000266465
        MAPE para toda la serie: 10.87%
        RMSE para toda la serie: 20.194327031630078

    Modelo 2:
        Usando los parámetros 3,0,4 las métricas fueron:
        MAE para toda la serie: 16.003515060683387
        MAPE para toda la serie: 10.84%
        RMSE para toda la serie: 20.224257761783214

    Modelo 3: 
        Con prophet fueron:
        MAE: 16.811434077383815
        MAPE: 11.77%
        RMSE: 21.806114837171673

    Considerando los resultados, el mejor modelo resulta ser el que usa los parámetros 3,0,4

Modelos para parque vehicular: evidentemente, Prophet es el mejor modelo
    Usando los mejores parámetros p=5, d=1, q=3
    MAE para toda la serie: 119967.95088712312
    MAPE para toda la serie: 3.65%
    RMSE para toda la serie: 180981.4978466559

    Usando los mejores parámetros p=3, d=1, q=2
    MAE para toda la serie: 63495.53548481269
    MAPE para toda la serie: 2.33%
    RMSE para toda la serie: 78715.83667445996

    Con prophet:
    MAE: 27953.415849852558
    MAPE: 1.20%
    RMSE: 35695.90172282073

Modelos para población: mejor modelo Prophet
    Usando los mejores parámetros p=1, d=2, q=1
    MAE para toda la serie: 31798.67148193125
    MAPE para toda la serie: 0.35%
    RMSE para toda la serie: RMSE: 54728.29433477469

        Usando los mejores parámetros p=2, d=1, q=6
    MAE para toda la serie: 7706.726807517435
    MAPE para toda la serie: 0.11%
    RMSE para toda la serie: 9764.193038815703

    Con Prophet:
        MAE para toda la serie: 2742.6311766910076
        MAPE para toda la serie: 0.03%
        RMSE para toda la serie: 5247.101222229977