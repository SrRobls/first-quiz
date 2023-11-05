# Seguridad App Paneles Solares Uber!

_Para esto voy tocar punto por punto (De cada vulnerabilidad) y como yoo gestionaría cada uno de mis "empleados" que tenago al mando_

**1. Broken Access Control.**

Esta vulnerabilidad es súper importante, Se trata de asegurarnos de que solo tengamos acceso a las partes o recursos de la aplicación que nos están permitidas. Los ingenieros poner controles de acceso fuertes para que no permitir entrar donde no debe, como espiar los datos de otros usuarios. Y los empleados, deben compremeter en no compartir contraseñas y información confidencial de los clientes.

**2. Cryptographic Failures.**

La idea aquí es mantener los "secretos" jeje, bien guardados. Los ingenieros tienen que hacer un cifrado a prueba de balas para proteger las cosas confidenciales, como contraseñas y datos de clientes, y asegurarse de que las "llaves del candado" estén bien cuidadas. Y los otros empleados, deben comprometerse en no compartir esto datos confidenciales.

**3. Injection.**

Esta vulnerabilidad se refiere a la importancia de validar y limpiar las entradas de usuario para prevenir ataques de inyección. Los ingenieros deben utilizar parámetros preparados en las consultas SQL para evitar vulnerabilidades de inyección.

**4. Insecure Design.**

La idea es diseñar desde el principio con seguridad en mente. Los ingenieros deben llevar a cabo revisiones de seguridad durante la fase de diseño y aplicar prácticas seguras para prevenir amenazas. Los empleados deben cumplir con políticas de acceso y diseño seguro para proteger la información del cliente.

**5. Security Misconfiguration.**

Esto se trata de asegurarse de que la configuración de la aplicación y los sistemas esté protegida. Esto conlleva garantizar que la aplicación y los sistemas estén seguros y no tengan ajustes incorrectos que puedan exponer datos sensibles. Los ingenieros deben configurar la aplicación y los sistemas de manera adecuada

**6. Vulnerable and Outdated Components.**

Implica mantener componentes actualizados y seguros. Los ingenieros deben mantener las bibliotecas actualizadas, y los trabajadores deben estar informados sobre actualizaciones de seguridad y evitar componentes obsoletos.

**7. Identification and Authentication Failures.**

Aquí se trata de garantizar una autenticación sólida. Los ingenieros deben implementar autenticación segura (se ocurre, aplicando JWT), y los trabajadores deben usar contraseñas seguras y notificar intentos de acceso no autorizado.

**8. Software and Data Integrity Failures.**

Aquí se trata de verificar la integridad de las actualizaciones y datos críticos. Los ingenieros deben verificar la integridad de las actualizaciones de software y datos críticos y aplicar políticas de seguridad en el proceso de CI/CD. Los empleados deben estar al tanto de las actualizaciones y cambios en los sistemas.

**9. Security Logging and Monitoring Failures.**

Esto implica configurar registros y sistemas de monitorización efectivos (significa configurar la aplicación para que registre lo que sucede y estar atento a eventos que podrían ser problemas de seguridad.). Los ingenieros deben configurar registros y sistemas para detectar actividades sospechosas.

**10. Server-Side Request Forgery.**

Aquí se trata de evitar solicitudes forjadas que puedan hacer que la aplicación hable con otras aplicaciones sin autorización. Los ingenieros deben implementar controles que validen y limiten las solicitudes de servidor a servidor.

Vale, ahora yo como Ingeniero Lider, lo que haria sería distribur a todo el equipo en subequipos para tratar cada vulnerabilidad. esto lo haria de la siguiente manera:

**Equipo 1 (Vulnerabilidades 1, 2 y 3)**

4 Ingenieros de Software: Para abordar las vulnerabilidades de Broken Access Control, Cryptographic Failures e Injection. Estos ingenieros se centrarán en implementar medidas de seguridad específicas para estas vulnerabilidades.

**Equipo 2 (Vulnerabilidades 4, 5 y 6)**

3 Ingenieros de Software: Para trabajar en las vulnerabilidades de Insecure Design, Security Misconfiguration y Vulnerable and Outdated Components. Este equipo se enfocará en el diseño seguro y la gestión de componentes.

**Equipo 3 (Vulnerabilidades 7, 8 y 9)**

4 Ingenieros de Software: Encargados de las vulnerabilidades relacionadas con Identification and Authentication Failures, Software and Data Integrity Failures, y Security Logging and Monitoring Failures. Estos ingenieros se centrarán en aspectos de autenticación, integridad de datos y monitorización.

**Equipo 4 (Vulnerabilidad 10)**

1 Ingenieros de Software: Para abordar la vulnerabilidad de Server-Side Request Forgery. Este equipo se enfocará en implementar controles para validar solicitudes de servidor a servidor.

Ahors para los asesores de ventas, se me ocurre que pueden estar involucrados en la concientización sobre seguridad y en la identificación de problemas de seguridad en las interacciones con los clientes.

**referencias:**

- https://owasp.org/Top10/
- https://www.youtube.com/watch?v=q1fGND4Qy3o
- https://www.youtube.com/watch?v=49Byc4PyY4E&t=692s
