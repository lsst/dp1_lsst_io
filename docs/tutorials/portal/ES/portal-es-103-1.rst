.. _portal-es-103-1:

###################################################################
103.1. Convertir una consulta de la interfaz de usuario (UI) a ADQL
###################################################################

Para la Faceta Portal de la Plataforma Científica de Rubin en data.lsst.cloud.

**Divulgación de Datos:** DP1

**Última verificación de ejecución:** 2025-06-28

**Objetivo de aprendizaje:** Convertir una consulta de la interfaz gráfica UI en una sentencia en
`Lenguaje de consulta de datos astronómicos (ADQL) <https://www.ivoa.net/documents/latest/ADQL.html>`_.

**Productos de datos LSST:** Tabla ``Object``

**Créditos:** Desarrollado originalmente por el equipo científico de la comunidad de Rubin.
Por favor, considerar reconocer su trabajo si este tutorial se utiliza para la preparación de artículos de revistas, lanzamientos de software u otros tutoriales.

**Soporte:** Se invita a toda la comunidad a hacer preguntas o plantear problemas en la `Categoría de asistencia <https://community.lsst.org/c/support/6>`_ del Foro de la Comunidad de Rubin.
El equipo de Rubin responderá a todas las preguntas publicadas allí.

----

**1. Configurar una consulta en la interfaz UI.**
Ir a la pestaña "DP1 Catalogs" (Catálogos DP1) en la interfaz UI del Portal.
Introducir los criterios de búsqueda como se muestra en la Figura 1.

.. figure:: images/portal-103-1-1.png
    :name: portal-es-103-1-1
    :alt: La interfaz UI del portal.

    Figura 1: La interfaz UI del Portal con una consulta configurada.


**2. Convertir la consulta de la interfaz UI en una consulta ADQL.**
Hacer clic en el botón "Populate and edit ADQL" (Completar y editar ADQL), situado en la parte inferior central de la Figura 1.
La interfaz cambiará a la interfaz ADQL y completará el cuadro de consulta ADQL con una sentencia ADQL que representa exactamente la misma consulta (Figura 2).

.. figure:: images/portal-103-1-2.png
    :name: portal-es-103-1-2
    :alt: La interfaz ADQL del Portal.

    Figura 2: La interfaz ADQL del Portal, completada automáticamente con la consulta de la interfaz UI de la Figura 1, convertida en una sentencia ADQL.


**3. Editar y/o ejecutar la consulta.**
Editar la consulta o hacer clic en el botón "Search" (Buscar) en la parte inferior izquierda para ejecutarla.
Los resultados aparecerán en la pestaña "Results".

**¡Advertencia!**
Si se realizan cambios en la sentencia ADQL y luego se vuelve a cambiar a la interfaz de tabla única (asistida por la interfaz UI) utilizando el botón de la parte inferior derecha de la Figura 1 ("Single Table (UI assisted)"),
esos cambios no se reflejarán en la interfaz UI.
La conversión sólo funciona en una dirección: de la interfaz UI a ADQL.


Próximos pasos: para obtener más detalles sobre el formato de las sentencias ADQL, continuar con el siguiente tutorial.
