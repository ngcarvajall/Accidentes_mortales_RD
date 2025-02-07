# **Análisis del Parque Vehicular, Mortalidad Vial y Crecimiento Poblacional en República Dominicana**

## **Resumen del Proyecto**
Este proyecto analiza la evolución del parque vehicular, la mortalidad vial y el crecimiento poblacional en la República Dominicana, utilizando datos históricos y modelos predictivos para evaluar tendencias y posibles soluciones. Con más de **6 millones de vehículos registrados en 2024** y una tasa de **65 muertes por cada 100,000 habitantes**, la República Dominicana se encuentra entre los países con la mayor siniestralidad vial del mundo. 

Los hallazgos destacan el rápido crecimiento del parque vehicular en comparación con la población, el predominio de motocicletas en accidentes fatales y la falta de una infraestructura adecuada para garantizar la seguridad vial.

---

## **Principales Hallazgos**
### **1. Defunciones por Accidentes de Tránsito**
- **Total de registros analizados:** 31,351.
- **Año con más muertes:** 2010 (2,132 defunciones).
- **Mes más peligroso:** **Diciembre**.
- **Día de mayor riesgo:** **Domingos**.
- **Horarios críticos:** 16:00 - 22:00.
- **Regiones con más víctimas:** Ozama, Cibao Norte y Cibao Sur.
- **Grupo de edad más afectado:** **20-29 años**.
- **Medio de transporte más peligroso:** **Motocicletas (63.73%)**.

> 🔍 **Insight:** Más del **87% de las víctimas son hombres**, lo que sugiere un problema de educación vial en este segmento de la población.

---

### **2. Crecimiento del Parque Vehicular**
- **Total de vehículos en 2024:** **6,160,988**.
- **Crecimiento exponencial:**
  - **1998:** 1 millón de vehículos.
  - **2012:** 3 millones.
  - **2024:** 6 millones.
- **Distribución geográfica:**
  - **Región Ozama (Distrito Nacional y Santo Domingo):** 45% del parque vehicular.
  - **Santiago y La Vega:** Aportan otro 15% al total.
- **Categoría predominante:** **Motocicletas (56%)**.

> 🔍 **Insight:** La tasa de crecimiento de vehículos es **4-7 veces mayor que la tasa de crecimiento poblacional**, lo que sugiere un incremento descontrolado del parque vehicular sin una infraestructura adecuada.

---

### **3. Crecimiento Poblacional**
- **Población en 1960:** 3 millones.
- **Población en 2024:** 11.4 millones.
- **Tasa de crecimiento decreciente:** Aunque la población sigue aumentando, la tasa de crecimiento está en declive.

> 🔍 **Insight:** El crecimiento poblacional y el parque vehicular están **directamente correlacionados**, pero los vehículos aumentan a un ritmo mayor.

---

### **4. Modelos Predictivos**
#### **Defunciones (Modelo ARIMA)**
- **Mejor modelo:** ARIMA (3,0,4).
- **MAPE:** 10.84% (mejor que el baseline del 15.14%).
- **Predicción para 2025:** **1,816 defunciones**.

#### **Parque Vehicular (Modelo Prophet)**
- **MAPE:** **1.35%** (mejor que el baseline de 5.8%).
- **Predicción para 2025:** **6,385,468 vehículos**.

#### **Población (Modelo Prophet)**
- **MAPE:** **0.03%**.
- **Predicción para 2025:** **11,599,481 habitantes**.

> 🔍 **Insight:** Aunque la mortalidad por vehículos ha disminuido, el número absoluto de muertes sigue siendo alarmante. Se prevé que el parque vehicular continúe en expansión.

---

## **Impacto de la Ley 63-17 en Infracciones**
- **Antes de 2018:** Existían solo 10 infracciones principales.
- **Después de 2018:** Se han registrado más de **100 tipos de multas nuevas**.
- **Aumento en la aplicación de multas:**
  - **Antes de 2018:** Menos de **1 millón** de infracciones anuales.
  - **Después de 2018:** Se han registrado más de **2 millones de infracciones anuales**.

> 🔍 **Insight:** La implementación de nuevas multas ha aumentado la fiscalización, pero **no ha reducido significativamente la siniestralidad**.

---

## **Recomendaciones y Soluciones**
1. **Implementación del sistema de puntos en la licencia:**  
   - Penalizar reincidencias y promover una conducción más responsable.

2. **Campañas de concienciación sobre seguridad vial:**  
   - Enfocadas en jóvenes y motociclistas, quienes representan el grupo más afectado.

3. **Mejoras en el transporte público:**  
   - Desincentivar el uso excesivo de vehículos privados mediante **buses modernos, ciclovías y medios de transporte compartidos**.

4. **Controles más estrictos de alcoholemia y velocidad:**  
   - Reducción de muertes por accidentes en horarios críticos.

5. **Renovación del parque vehicular:**  
   - Más del **45% de los vehículos tienen más de 20 años**.
   - Retiro de chatarra y regulación de importaciones de vehículos usados.

6. **Diversificación del transporte:**  
   - Incentivar **alternativas sostenibles** como bicicletas y corredores exclusivos para buses.

7. **A/B Testing para medir impacto:**  
   - Evaluar el efecto de nuevas medidas en la reducción de accidentes.

---

## **Conclusión**
El crecimiento descontrolado del parque vehicular, combinado con una infraestructura vial deficiente y una fiscalización insuficiente, ha llevado a que la República Dominicana tenga la tasa de mortalidad vial más alta del mundo. 

Aunque se han implementado regulaciones como la **Ley 63-17**, la falta de estrategias integrales ha impedido una reducción significativa en las muertes por accidentes de tránsito.

Los modelos predictivos muestran que la cantidad de defunciones disminuirá ligeramente, pero sin reformas estructurales, la crisis de seguridad vial persistirá.

---

## **Próximos Pasos**
- **Monitorear el impacto de políticas públicas y nuevas regulaciones.**
- **Desarrollar dashboards interactivos en Power BI para visualizar tendencias en tiempo real.**
- **Colaborar con entidades gubernamentales para optimizar estrategias de seguridad vial.**

> 🚀 **Este análisis no solo busca entender el problema, sino también proponer soluciones concretas para salvar vidas.**
