🏦 EDA Banco Portugal

📘 Descripción del proyecto

He realizado un Análisis Exploratorio de Datos (EDA) sobre las campañas de marketing directo de una institución bancaria portuguesa.
El objetivo principal ha sido comprender el comportamiento de los clientes y los factores que influyen en la contratación de depósitos a plazo, a partir de datos reales obtenidos por el banco.

🎯 Objetivos del análisis

Mi propósito en este proyecto es analizar y optimizar los datos de una campaña de marketing directo para identificar:
- Los factores de éxito que impulsan la conversión.
- Las áreas de mejora para futuras campañas.
- Los segmentos de clientes más propensos a responder positivamente.

💡 Valor para el negocio:

Los resultados permiten maximizar el retorno de inversión (ROI), ajustar estrategias de marketing y mejorar la segmentación de clientes potenciales.

📊 Descripción del conjunto de datos

El dataset contiene información sobre campañas de marketing realizadas mediante llamadas telefónicas a clientes de un banco portugués.
Está compuesto por 29 columnas distribuidas en dos archivos principales.

🧩 Primer dataset: Datos de campaña
Incluye información sobre las interacciones y características de los clientes:

  - age:	Edad del cliente
  - job:	Ocupación o profesión
  - marital:	Estado civil
  - education:	Nivel educativo
  - default:	Historial de impagos (1 = Sí, 0 = No)
  - housing:	Préstamo hipotecario (1 = Sí, 0 = No)
  - loan:	Otro tipo de préstamo (1 = Sí, 0 = No)
  - contact:	Método de contacto (teléfono, celular, etc.)
  - duration:	Duración de la llamada (segundos)
  - campaign:	Nº de contactos realizados durante la campaña
  - pdays:	Días desde el último contacto previo
  - previous:	Nº de contactos previos
  - poutcome:	Resultado de la campaña anterior
  - emp.var.rate:	Tasa de variación del empleo
  - cons.price.idx:	Índice de precios al consumidor
  - cons.conf.idx:	Índice de confianza del consumidor
  - euribor3m:	Tasa de interés a tres meses
  - nr.employed:	Nº de empleados
  - y: Variable objetivo: suscripción al producto (yes/no)
  - date:	Fecha del contacto
  - contact_month:	Mes del contacto
  - contact_year:	Año del contacto
  - id_	Identificador: único del registro

👥 Segundo dataset: Datos del cliente

  - Income:	Ingreso anual del cliente
  - Kidhome:	Nº de niños en el hogar
  - Teenhome:	Nº de adolescentes en el hogar
  - Dt_Customer:	Fecha en que el cliente se unió al banco
  - NumWebVisitsMonth:	Nº de visitas mensuales al sitio web
  - ID:	Identificador único del cliente

⚙️ Instalación y configuración

El proyecto se ha desarrollado en Python utilizando Pandas, NumPy, Matplotlib, Seaborn y Jupyter Notebook, dentro de Visual Studio Code.

  🔧 Pasos para la instalación
  
      1. Clonar el repositorio
      git clone https://github.com/tu_usuario/EDA_Banco_Portugal.git
      cd EDA_Banco_Portugal
      2. Crear un entorno virtual
      python3 -m venv venv
      source venv/bin/activate   # En Mac/Linux
      venv\Scripts\activate      # En Windows
      3. Instalar dependencias
      pip install -r requirements.txt
      4. Abrir el proyecto en Visual Studio Code y ejecutar los notebooks dentro de la carpeta Jupyters.

  🧹 Proceso de limpieza y transformación
  Durante la etapa de preparación de los datos realicé las siguientes tareas:
  - Estandaricé nombres de columnas (minúsculas, sin espacios ni puntos).
  - Eliminé columnas innecesarias (Unnamed: 0).
  - Corregí formatos numéricos y de fechas.
  - Creé nuevas variables derivadas de la fecha (year, month, day, quarter).
  - Identifiqué y traté valores nulos y outliers.
  - Documenté todas las funciones de limpieza en el archivo sp_limpieza.py dentro de la carpeta SRC.
    
  📁 Archivos generados:
  data_transformacion_limpieza.csv
  data_limpios.csv
  datos_metricas.csv
  
  📈 Análisis exploratorio (EDA)
  Dividí el análisis en dos grandes bloques:
  
  1️⃣ Columnas categóricas
  
  - Detecté que no existía una categoría predominante en ninguna variable.
  - Los valores nulos fueron reemplazados con "Unknown" al no superar el 30%.
  - Creé visualizaciones de distribución mediante Seaborn y Matplotlib.
  - Guardé las funciones en sp_eda.py y sp_visualizacion.py.
  
  2️⃣ Columnas numéricas
  
  - Identifiqué outliers en variables como duration, campaign, previous, loan, pdays y default.
  - Convertí a nulos los valores extremos que representaban menos del 1%.
  - Imputé valores faltantes:
    - 🔹 <10% de nulos → media o mediana.
    - 🔹 >10% de nulos → Iterative Imputer.
  - Documenté el proceso en sp_nulos_num.py.
  
  📊 Métricas de marketing calculadas


  Calculé métricas clave para evaluar el rendimiento de las campañas:

  - Tasa de conversión:	% de clientes contactados que aceptaron la oferta
  - Tasa de rechazo:	% de clientes que no aceptaron
  - Éxito por campaña:	Promedio de contactos necesarios para lograr una conversión
  - Duración media de llamada:	Tiempo promedio de las llamadas
  - Contactos promedio por cliente:	Número medio de intentos de contacto
  - Tiempo promedio desde último contacto:	Promedio de días entre contactos
  - Tasa de conversión por segmento:	Por profesión, estado civil, nivel educativo, tipo de contacto, préstamo/hipoteca, mes, año
  - Ratio de eficiencia por duración:	Relación entre duración de llamada y tasa de éxito
  - Correlaciones:	Variables numéricas más asociadas con la variable objetivo y
    
📊 Visualizaciones destacadas
  📈 Distribución de la variable objetivo (y)
  📊 Histogramas y boxplots para detectar outliers
  🎯 Tasa de conversión por segmento (edad, profesión, educación, etc.)
  📆 Evolución temporal de la tasa de conversión por mes y año
  
🧭 Conclusiones

Tras analizar los datos, llegué a las siguientes conclusiones:
- El perfil de cliente más propenso a contratar el depósito a plazo bancario es:
  - 👩‍🎓 Estudiante, con nivel educativo bajo o sin estudios,
  - 📱 Prefiere ser contactado por teléfono móvil,
  - 🗓️ Y responde favorablemente durante todo el año.
Estos hallazgos permiten al banco mejorar la eficiencia de sus campañas, optimizar los recursos y dirigir las estrategias hacia los segmentos de mayor conversión.

💻 Tecnologías utilizadas
  - Python 
  - Pandas
  - NumPy
  - Matplotlib
  - Seaborn
  - Jupyter Notebook
  - Visual Studio Code
  
🧩 Estructura del repositorio
```bash
EDA_Banco_Portugal/
│
├── Data/
│   ├── bank-additional.csv
│   ├── customer-details.xlsx
│   ├── data_transformacion_limpieza.csv
│   └── data_limpios.csv
│
├── Jupyters/
│   ├── eda_preliminar.ipynb
│   ├── limpieza.ipynb
│   ├── columnas_categoricas.ipynb
│   └── columnas_numericas.ipynb
│   └── marketing.ipynb
│
├── SRC/
│   ├── sp_limpieza.py
│   ├── sp_eda.py
│   ├── sp_visualizacion.py
│   └── sp_nulos_num.py
│
├── requirements.txt
└── README.md
```
✍️ Autor
 Aïna [GitHub Profile](https://github.com/Ainamg)





