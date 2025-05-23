create or replace NONEDITIONABLE PROCEDURE VALIDACION_SEGURIDAD_INSERT_LOGIN(
ID_REGISTRO login.id_login%TYPE,
EMAIL_REGISTRO LOGIN.EMAIL%TYPE,
CLAVE_REGISTRO LOGIN.CLAVE%TYPE,
FECHA_LOGIN_REGISTRO LOGIN.FECHA%TYPE,
HORA_LOGIN_REGISTRO LOGIN.HORA%TYPE)
AS

 
 CURSOR C_INSERTAR_LOGIN 
 IS SELECT VALIDACION_LOGIN_EMAIL(EMAIL_REGISTRO), VALIDACION_LOGIN_CLAVE(CLAVE_REGISTRO) FROM LOGIN
 WHERE EMAIL=EMAIL_REGISTRO
 AND CLAVE=CLAVE_REGISTRO;

 CUR_INSERT_LOGIN C_INSERTAR_LOGIN%ROWTYPE;


BEGIN

    IF EMAIL_REGISTRO IS NOT NULL AND CLAVE_REGISTRO IS NOT NULL THEN

     OPEN C_INSERTAR_LOGIN;
     FETCH C_INSERTAR_LOGIN INTO CUR_INSERT_LOGIN;

     INSERT INTO LOGIN 
     VALUES (ID_REGISTRO,EMAIL_REGISTRO,CLAVE_REGISTRO,FECHA_LOGIN_REGISTRO,HORA_LOGIN_REGISTRO);
     CLOSE C_INSERTAR_LOGIN;
     COMMIT;

     ELSE
        DBMS_OUTPUT.PUT_LINE('ERROR');

        ROLLBACK;

    END IF;

END;

EXECUTE VALIDACION_SEGURIDAD_INSERT_LOGIN(1,'JAIMERETAMAL2024@GMAIL.COM','JAIME2024','24/08/2024','15:33');

SELECT * FROM LOGIN WHERE EMAIL = 'JAIMERETAMAL2024@GMAIL.COM';