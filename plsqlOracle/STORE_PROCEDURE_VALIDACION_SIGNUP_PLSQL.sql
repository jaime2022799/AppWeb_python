--SELECT * FROM SIGNUP;

create or replace NONEDITIONABLE PROCEDURE VALIDACION_SEGURIDAD_INSERT_SIGNUP(

EMAIL_REGISTRO SIGNUP.EMAIL%TYPE,
CLAVE_REGISTRO SIGNUP.CLAVE_NUEVA%TYPE,
CLAVE SIGNUP.CLAVE%TYPE,
FECHA SIGNUP.FECHA%TYPE,
NOMBRE SIGNUP.NOMBRE%TYPE,
APELLIDO SIGNUP.APELLIDO%TYPE,
HORA_REGISTRO SIGNUP.HORA%TYPE)
AS

 
 CURSOR C_INSERTAR_SIGNUP
 IS SELECT  VALIDACION_LOGIN_EMAIL(EMAIL_REGISTRO), VALIDACION_LOGIN_CLAVE(CLAVE_REGISTRO) FROM SIGNUP
 WHERE EMAIL=EMAIL_REGISTRO
 AND CLAVE=CLAVE_REGISTRO;

 CUR_INSERT_SIGNUP C_INSERTAR_SIGNUP%ROWTYPE;


BEGIN

    IF EMAIL_REGISTRO IS NOT NULL AND CLAVE_REGISTRO IS NOT NULL THEN
    
     OPEN C_INSERTAR_SIGNUP;
     FETCH C_INSERTAR_SIGNUP INTO CUR_INSERT_SIGNUP;
    
     INSERT INTO SIGNUP 
     VALUES (EMAIL_REGISTRO,CLAVE_REGISTRO,CLAVE,FECHA,NOMBRE,APELLIDO,HORA_REGISTRO);
     CLOSE C_INSERTAR_SIGNUP;
     COMMIT;
     
    ELSE
        DBMS_OUTPUT.PUT_LINE('ERROR');
        ROLLBACK;

    END IF;
    
END;

--EXECUTE VALIDACION_SEGURIDAD_INSERT_SIGNUP('JAIME@GMAIL.COM','JAIME','JAIME','07/08/24','JAIME','RETAMAL','17:06');

--SELECT * FROM SIGNUP WHERE FECHA = '07/08/24';   