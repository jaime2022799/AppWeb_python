CREATE OR REPLACE 
PACKAGE PCK_VALIDACION_PROCESO_FORMULARIO_APP AS 

PROCEDURE VALIDACION_INSERT_FORMULARIO_ADMINISTRATIVO(NOMBRE_FORMULARIO NUMBER,APELLIDO_FORMULARIO
VARCHAR2,TIPO_EVENTO_FORMULARIO VARCHAR2,CONTACTO_FORMULARIO VARCHAR2, DIRECCION_FORMULARIO VARCHAR2,
EMAIL_FORMULARIO VARCHAR2, FECHA_FORMULARIO VARCHAR2,HORA_FORMULARIO VARCHAR2);


  /* TODO enter package declarations (types, exceptions, methods etc) here */ 

END PCK_VALIDACION_PROCESO_FORMULARIO_APP;