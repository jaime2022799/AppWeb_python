create or replace procedure email_formulario_administrativo (p_recip varchar2) is
 begin

     utl_mail.send(
     sender=>'jaimeretamal47@gmail.com',
     recipients=>p_recip,
     subject=>'My subject',
     message=>'My message');
     
end;

execute email_formulario_administrativo ('jaimeretamal47@gmail.com')