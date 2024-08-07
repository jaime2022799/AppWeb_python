create or replace NONEDITIONABLE PACKAGE BODY PCK_VALIDACION_PROCESO_FORMULARIO_APP
AS

PROCEDURE VALIDACION_INSERT_FORMULARIO_ADMINISTRATIVO(NOMBRE_FORMULARIO NUMBER,APELLIDO_FORMULARIO
VARCHAR2,TIPO_EVENTO_FORMULARIO VARCHAR2,CONTACTO_FORMULARIO VARCHAR2, DIRECCION_FORMULARIO VARCHAR2,
EMAIL_FORMULARIO VARCHAR2, FECHA_FORMULARIO VARCHAR2,HORA_FORMULARIO VARCHAR2)

AS

 CURSOR C_INSERTAR_FORMULARIO_ADMINISTRATIVO  
 IS SELECT *
 FROM FORMULARIO_ADMINISTRATIVO;

 CUR_INSERT_FORMULARIO_ADMINISTRATIVO  C_INSERTAR_FORMULARIO_ADMINISTRATIVO%ROWTYPE;

BEGIN

IF NOMBRE_FORMULARIO IS NOT NULL AND EMAIL_FORMULARIO IS NOT NULL THEN

 OPEN C_INSERTAR_FORMULARIO_ADMINISTRATIVO;
 FETCH C_INSERTAR_FORMULARIO_ADMINISTRATIVO INTO CUR_INSERT_FORMULARIO_ADMINISTRATIVO;
 INSERT INTO FORMULARIO_ADMINISTRATIVO 
 VALUES (NOMBRE_FORMULARIO,APELLIDO_FORMULARIO,
 TIPO_EVENTO_FORMULARIO,CONTACTO_FORMULARIO,DIRECCION_FORMULARIO,
 EMAIL_FORMULARIO,FECHA_FORMULARIO,HORA_FORMULARIO);

 CLOSE C_INSERTAR_FORMULARIO_ADMINISTRATIVO;
 COMMIT;

ELSE
    DBMS_OUTPUT.PUT_LINE('ERROR');
    ROLLBACK;

END IF;


END VALIDACION_INSERT_FORMULARIO_ADMINISTRATIVO;

----------

END PCK_VALIDACION_PROCESO_FORMULARIO_APP;