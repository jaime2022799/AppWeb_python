
SELECT * FROM formulario_administrativo;

create or replace PROCEDURE REGISTRO_INSERT_FORMULARIO_ENVIO_EMAIL (
NOMBRE_F formulario_administrativo.NOMBRE%TYPE,
APELLIDO_F formulario_administrativo.APELLIDO%TYPE,
TIPO_EVENTO_F formulario_administrativo.TIPO_EVENTO%TYPE,
CONTACTO_F formulario_administrativo.CONTACTO%TYPE,
DIRECCION_F formulario_administrativo.DIRECCION%TYPE,
EMAIL_F formulario_administrativo.EMAIL%TYPE, 
FECHA_F formulario_administrativo.FECHA%TYPE,
HORA_F formulario_administrativo.HORA%TYPE,
ID_FORMULARIO_F formulario_administrativo.id_formulario%TYPE)
AS

--VARIABLE EMAIL
from_user varchar2(50):='user_boss';
from_sndr varchar2(50):='jaimeretamal47@gmail.com';
rcpt_to varchar2(2000):='jaimeretamal47@gmail.com';
msubj varchar2(80):='PRUEBA DE PLSQL EMAIL';
mmsg varchar2(400):= 'ESTA ES UNA PRUEBA DE PLSQL EMAIL...';
ret_msg varchar2(400);


 CURSOR C_INSERTAR_FORMULARIO 
 IS SELECT * FROM formulario_administrativo
 WHERE EMAIL=EMAIL_F;

 CUR_INSERT_FORMULARIO C_INSERTAR_FORMULARIO%ROWTYPE;

BEGIN

 OPEN C_INSERTAR_FORMULARIO;
 FETCH C_INSERTAR_FORMULARIO INTO CUR_INSERT_FORMULARIO;
 INSERT INTO formulario_administrativo 
 VALUES (nombre_f,apellido_f,tipo_evento_f,contacto_f,direccion_f,email_f,fecha_f,hora_f,id_formulario_f);

 CLOSE C_INSERTAR_FORMULARIO;
 
 ret_msg := USER_BOSS.send_email(from_user, from_sndr, rcpt_to, msubj, mmsg, 'FORMULARIO.TXT');
 
 COMMIT;
END;

--execute REGISTRO_INSERT_FORMULARIO_ENVIO_EMAIL('JAIME_PRUEBA','MENDOZA','AUTOMOTRIZ','990383274','PUENTE ALTO','JAIMERETAMAL47@GMAIL.COM','11-06-2024','18:11',200);
