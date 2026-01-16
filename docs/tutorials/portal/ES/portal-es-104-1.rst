.. _portal-es-104-1:

#######################################################
104.1. Navegando la interfaz de resultados del catálogo
#######################################################

Para la Faceta Portal de la Plataforma Científica de Rubin (RSP) en data.lsst.cloud.

**Divulgación de Datos:** DP1

**Última verificación de ejecución:** 2025-07-23

**Objetivo de aprendizaje:** Navegar por la interfaz multipanel para ver los resultados de los datos del catálogo.

**Productos de datos LSST:** Tabla ``Object``

**Créditos:** Desarrollado originalmente por el equipo científico de la comunidad de Rubin.
Por favor, considerar reconocer su trabajo si este tutorial se utiliza para la preparación de artículos de revistas, lanzamientos de software u otros tutoriales.

**Soporte:** Se invita a toda la comunidad a hacer preguntas o plantear problemas en la `Categoría de asistencia <https://community.lsst.org/c/support/6>`_ del Foro de la Comunidad de Rubin.
El equipo de Rubin responderá a todas las preguntas publicadas allí.

----

**1. Iniciar sesión en la Faceta Portal del RSP.**
Iniciar sesión en el Portal, hacer clic en la pestaña DP1 Catalogs (Catálogos DP1) y cambiar a la interfaz ADQL.

**2. Ejecutar una consulta.**
Ingresar la siguiente consulta en el recuadro ADQL y hacer clic en "Search" (Buscar).
Esta consulta devuelve las coordenadas y magnitudes de los objetos cercanos al centro del campo ECDFS que son más brillantes que 22 mag en *g* y *r*.

.. code-block:: SQL

  SELECT coord_dec, coord_ra, g_cModelMag, r_cModelMag
  FROM dp1.Object
  WHERE CONTAINS(POINT('ICRS', coord_ra, coord_dec),
        CIRCLE('ICRS', 53.0, -28.0, 1.0)) =1
        AND g_cModelMag < 22 AND r_cModelMag < 22


**3. Ver la interfaz de resultados.**
El diseño predeterminado de la interfaz de resultados se muestra en la Figura 1.

.. figure:: images/portal-104-1-1.png
    :name: portal-es-104-1-1
    :alt: La interfaz de resultados.

    Figura 1: La interfaz de resultados tras ejecutar una consulta muestra por defecto una pantalla dividida en tres partes: el mapa de cobertura (A), el gráfico interactivo (B) y la tabla (C).


**3.1. Gráfico de cobertura.**
La ubicación predeterminada del gráfico de cobertura se encuentra en la parte superior izquierda; A en la Figura 1.
La vista predeterminada es una grilla de píxeles `HEALPix <https://healpix.sourceforge.io/>`_ que muestra el número de objetos devueltos por píxel de la grilla.
Los pequeños cuadrados de color marcan los objetos individuales fuera de la grilla.
El fondo es un mapa `HiPS <https://aladin.cds.unistra.fr/hips/>`_ en la banda r de las imágenes ``deep_coadd``.

**3.2. Gráfico interactivo.**
La ubicación predeterminada del gráfico interactivo se encuentra en la parte superior derecha; B en la Figura 1.
El gráfico predeterminado corresponderá a las dos primeras columnas de la tabla de datos obtenida.
En la Figura 1, se muestra RA vs. Dec.
Este gráfico cambiará a un histograma bidimensional si se devuelven tantos objetos que no permita distinguir los puntos individuales.

**3.3. Tabla.**
La ubicación predeterminada de la tabla se encuentra en la parte inferior; C en la Figura 1.
Una tabla navegable y filtrable de los datos obtenidos, con la primera fila seleccionada de forma predeterminada y mostrada en naranja.
Notar que el punto naranja en el gráfico interactivo corresponde a la fila seleccionada.


**4. Ver opciones de diseño.**
En la parte superior izquierda, hacer clic en el ícono del menú (tres líneas horizontales) para abrir el menú lateral.
En "Results Layout" (Diseño de resultados), hacer clic en el ícono del diseño predeterminado (flechas "arriba-abajo" o "A" en la Figura 2) para ver todas las opciones de diseño.
Tener en cuenta que el recuadro "Results Layout" sólo aparece después de haber realizado una "búsqueda".

.. figure:: images/portal-104-1-2.png
    :name: portal-es-104-1-2
    :alt: El menú lateral con opciones para el diseño de la vista de resultados.
    :width: 200

    Figura 2: El menú lateral con opciones para el diseño de la vista de resultados.

**5. Cambio de diseño.**
En el menú lateral de la Figura 2, seleccionar la vista de dos paneles con los gráficos de cobertura ("Coverage Charts") a la izquierda y las tablas ("Tables") a la derecha.
Observar que el gráfico interactivo sigue estando disponible como pestaña en la parte superior izquierda bajo el nombre "Active Chart".
Abrir nuevamente el menú lateral para probar otros diseños y volver a la vista predeterminada de tres paneles.

**6. Ejecutar una consulta diferente.**
Hacer clic en la pestaña "DP1 Catalogs" (Catálogos DP1) para volver a la interfaz ADQL.
Cambiar la consulta para que devuelva objetos más débiles en una región más pequeña, utilizando las sentencias ADQL que se indican a continuación.
Ejecutar la consulta.

.. code-block:: SQL

  SELECT coord_dec, coord_ra, g_cModelMag, r_cModelMag
  FROM dp1.Object
  WHERE CONTAINS(POINT('ICRS', coord_ra, coord_dec),
        CIRCLE('ICRS', 53.0, -28.0, 0.2)) =1
        AND g_cModelMag < 25 AND r_cModelMag < 25


**7. Ver los resultados de múltiples consultas.**
La interfaz de resultados ahora se completa con los datos de la nueva consulta (Figura 3).
La tabla (C en la Figura 3) ahora tiene dos pestañas, una para la consulta anterior (en rojo) y otra para la nueva (en cian).
El gráfico de cobertura (A en la Figura 3) incluye marcadores para ambas consultas, en colores que se corresponden con los de la tabla.
El gráfico interactivo (B en la Figura 3) es el gráfico predeterminado para la nueva consulta, la tabla seleccionada.
Los resultados de consultas no deseadas pueden ser eliminados haciendo clic en la "X" de la pestaña correspondiente situada encima de la tabla.

.. figure:: images/portal-104-1-3.png
    :name: portal-es-104-1-3
    :alt: La pestaña Resultados después de ejecutar una segunda consulta.

    Figura 3: Similar a la Figura 1, pero con los resultados de dos consultas.


**7. Alternar entre múltiples resultados de consultas.**
Hacer clic en la pestaña de la primera consulta y observar que el gráfico de cobertura, la tabla y el gráfico interactivo cambian.

**8. Eliminar los resultados de consultas no deseadas.**
En la tabla, hacer clic en la X de la pestaña de los resultados de la primera consulta (a la izquierda) para eliminarlos.
