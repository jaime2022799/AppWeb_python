
create or replace NONEDITIONABLE PROCEDURE REGISTRO_CON_VALIDACION_SIGNUP (ID_SIGNUP_REGISTRO SIGNUP.ID_SIGNUP%TYPE,
EMAIL_SIGNUP_REGISTRO SIGNUP.EMAIL%TYPE, 
CLAVE_NUEVA_SIGNUP_REGISTRO SIGNUP.CLAVE_NUEVA%TYPE,
CLAVE_SIGNUP_REGISTRO SIGNUP.CLAVE%TYPE,
NOMBRE_SIGNUP_REGISTRO SIGNUP.NOMBRE%TYPE,
APELLIDO_SIGNUP_REGISTRO SIGNUP.APELLIDO%TYPE,
FECHA_SIGNUP_REGISTRO SIGNUP.FECHA%TYPE)
AS
--CURSOR INSERTAR REGISTRO SIGNUP
 CURSOR C_INSERTAR 
 IS 
 SELECT VALIDACION_SIGNUP_EMAIL(EMAIL_SIGNUP_REGISTRO),VALIDACION_SIGNUP_CLAVE(CLAVE_SIGNUP_REGISTRO) FROM SIGNUP
 WHERE EMAIL=EMAIL_SIGNUP_REGISTRO
 AND CLAVE=CLAVE_SIGNUP_REGISTRO;

 CUR_INSERT C_INSERTAR%ROWTYPE;

BEGIN
  OPEN C_INSERTAR;
  FETCH C_INSERTAR INTO CUR_INSERT;
  INSERT INTO SIGNUP VALUES (ID_SIGNUP_REGISTRO,EMAIL_SIGNUP_REGISTRO,CLAVE_NUEVA_SIGNUP_REGISTRO,
  CLAVE_SIGNUP_REGISTRO,NOMBRE_SIGNUP_REGISTRO,APELLIDO_SIGNUP_REGISTRO,FECHA_SIGNUP_REGISTRO);
  CLOSE C_INSERTAR;
  --
  COMMIT;
END;


