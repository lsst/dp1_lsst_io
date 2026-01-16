.. _portal-es-102-2:

#####################################
102.2. Consultando imágenes con SIAv2
#####################################

Para la Faceta Portal de la Plataforma Científica de Rubin (RSP) en data.lsst.cloud.

**Divulgación de Datos:** DP1

**Última verificación de ejecución:** 2025-06-28

**Objetivo de aprendizaje:** Utilizar el servicio Simple Image Access (SIA) (Protocolo para Acceso de Imágenes) para realizar consultas y obtener imágenes.

**Productos de datos LSST:** ``visit_image``

**Créditos:** Desarrollado originalmente por el equipo científico de la comunidad de Rubin.
Por favor, considerar reconocer su trabajo si este tutorial se utiliza para la preparación de artículos de revistas, lanzamientos de software u otros tutoriales.

**Soporte:** Se invita a toda la comunidad a hacer preguntas o plantear problemas en la `Categoría de asistencia <https://community.lsst.org/c/support/6>`_ del Foro de la Comunidad de Rubin. El equipo de Rubin responderá a todas las preguntas publicadas allí.

----

**1. Iniciar sesión en el RSP y acceder a la Faceta Portal.**
En un navegador web, ir a `data.lsst.cloud <https://data.lsst.cloud/>`_, seleccionar la Faceta Portal e iniciar sesión.

**2. Seleccionar la pestaña "Images SIAv2".**
En las pestañas de la página de inicio del Portal (o en el menú lateral), hacer clic en la pestaña denominada "DP1 Images SIAv2" (Imágenes DP1 SIAv2).

**3. Establecer las restricciones espaciales.**
Marcar la casilla junto a "Spatial" (Espacial).
Elegir un área cónica seleccionando la opción "Cone Shape" en el campo "Shape Type".
Utilizar el centro aproximado del campo ECDFS, RA, Dec = 53.0, -28.0 grados.
Utilizar un radio de 1 grado, aproximadamente el tamaño del campo.

**4. Establecer el tipo de observación y la fuente.**
Marcar la casilla junto a "Observation Type and Source" (Tipo de observación y fuente).
Seleccionar el nivel de calibración 2 (para PVI: imágenes procesadas de la visita) haciendo clic en la opción 2 de "Calibration Level",
establecer el tipo de producto de datos como imagen escribiendo "image" en el campo "Data Product Type", la instalación en Rubin:Simonyi en el campo "Facility",
el nombre del instrumento en LSSTComCam en el campo "Instrument Name", la colección en LSST.DP1 en el campo "Collection"
y el subtipo de producto de datos en "lsst.visit_image" en el campo "Data Product Subtype".

.. figure:: images/portal-102-2-1.png
    :name: portal-es-102-2-1
    :alt: Restricciones de búsqueda SIA.

    Figura 1: Configuración de las restricciones espaciales y de tipo de observación y fuente de las imágenes.


**5. Establecer el tiempo de observación.**
Marcar la casilla junto a "Timing" (Tiempo).
Para "Time of Observation" (Tiempo de observación), seleccionar "Overlapping specified range" (Superposición del rango especificado).
Seleccionar "MJD Values" (Valores MJD) e introducir 60625 para el "Start Time" (Tiempo de inicio) y 60630 para el "End Time" (Tiempo de finalización).

**6. Establecer la cobertura espectral (filtro).**
Seleccionar el tipo de consulta por bandas de filtros con la opción "By Filter Bands" en el campo "Query Type" y seleccionar la banda r.


.. figure:: images/portal-102-2-2.png
    :name: portal-es-102-2-2
    :alt:  Restricciones de búsqueda SIA.

    Figura 2: Configuración de las restricciones temporales y de cobertura espectral.


**7. Ejecutar la búsqueda.**
Hacer clic en el botón "Search" (Buscar) situado en la parte inferior izquierda.

**8. Revisar los resultados.**
La interfaz de resultados permite visualizar interactivamente las 81 imágenes de visitas que cumplen los criterios de búsqueda.

.. figure:: images/portal-102-2-3.png
    :name: portal-es-102-2-3
    :alt: La interfaz de resultados de imágenes.

    Figura 3: La interfaz de resultados de imágenes.


Próximos pasos: consultar los tutoriales de la serie sobre cómo manipular la interfaz de resultados de imágenes.
