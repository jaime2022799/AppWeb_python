
create or replace NONEDITIONABLE PROCEDURE REGISTRO_INSERT_SIGNUP_ENVIO_EMAIL (

EMAIL_S SIGNUP.EMAIL%TYPE, 
CLAVE_NUEVA_S signup.clave_nueva%TYPE,
CLAVE_S signup.clave%TYPE,
FECHA_S SIGNUP.FECHA%TYPE,
NOMBRE_S signup.nombre%TYPE,
APELLIDO_S signup.apellido%TYPE,
HORA_S SIGNUP.HORA%TYPE)
AS

--VARIABLE EMAIL
from_user varchar2(50):='user_boss';
from_sndr varchar2(50):='jaimeretamal47@gmail.com';
rcpt_to varchar2(2000):='jaimeretamal47@gmail.com';
msubj varchar2(80):='PRUEBA DE PLSQL EMAIL';
mmsg varchar2(400):= 'ESTA ES UNA PRUEBA DE PLSQL EMAIL...';
ret_msg varchar2(400);


 CURSOR C_INSERTAR_SIGNUP 
 IS SELECT * FROM SIGNUP
 WHERE EMAIL=EMAIL_S;

 CUR_INSERT_SIGNUP C_INSERTAR_SIGNUP%ROWTYPE;

BEGIN

 OPEN C_INSERTAR_SIGNUP;
 FETCH C_INSERTAR_SIGNUP INTO CUR_INSERT_SIGNUP;
 INSERT INTO SIGNUP 
 VALUES (EMAIL_S,CLAVE_NUEVA_S,CLAVE_S,FECHA_S,NOMBRE_S,APELLIDO_S,HORA_S);

 CLOSE C_INSERTAR_SIGNUP;

 ret_msg := USER_BOSS.send_email(from_user, from_sndr, rcpt_to, msubj, mmsg, 'signup.TXT');

 COMMIT;
END;


--execute registro_insert_signup_envio_email('jaimeretamal47@gmail.com','jaime2024','jaime2024','12-06-2024','jaime','mendoza','13:44');
