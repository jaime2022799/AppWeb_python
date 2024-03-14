

create or replace procedure email_signup_3 (p_recip varchar2) is
 begin

     utl_mail.send(
     sender=>'jaimeretamal47@gmail.com',
     recipients=>p_recip,
     subject=>'My subject',
     message=>'My message');
     
end;

EXECUTE email_signup_3 ('jaimeretamal47@gmail.com');
