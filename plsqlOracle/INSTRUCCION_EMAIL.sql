declare
from_user varchar2(50):='user_boss';
from_sndr varchar2(50):='jaimeretamal47@gmail.com';
rcpt_to varchar2(2000):='jaimeretamal47@gmail.com';
msubj varchar2(80):='PRUEBA DE PLSQL EMAIL';
mmsg varchar2(400):= 'ESTA ES UNA PRUEBA DE PLSQL EMAIL...';
ret_msg varchar2(400);
begin
ret_msg := USER_BOSS.send_email(from_user, from_sndr, rcpt_to, msubj, mmsg, 'abcd.pdf');
dbms_output.put_line(ret_msg);
end;

