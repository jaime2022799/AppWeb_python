create or replace NONEDITIONABLE PROCEDURE VALIDACION_INSERT_FORMULARIO_ADMINISTRATIVO (
NOMBRE_FORMULARIO         FORMULARIO_ADMINISTRATIVO.NOMBRE%TYPE,
APELLIDO_FORMULARIO         FORMULARIO_ADMINISTRATIVO.APELLIDO%TYPE,
TIPO_EVENTO_FORMULARIO     FORMULARIO_ADMINISTRATIVO.TIPO_EVENTO%TYPE,
CONTACTO_FORMULARIO       FORMULARIO_ADMINISTRATIVO.CONTACTO%TYPE,
DIRECCION_FORMULARIO        FORMULARIO_ADMINISTRATIVO.DIRECCION%TYPE,
EMAIL_FORMULARIO        FORMULARIO_ADMINISTRATIVO.EMAIL%TYPE,
FECHA_FORMULARIO        FORMULARIO_ADMINISTRATIVO.FECHA%TYPE,
HORA_FORMULARIO         FORMULARIO_ADMINISTRATIVO.HORA%TYPE)
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


END;