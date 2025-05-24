CREATE OR REPLACE FUNCTION USER_BOSS.send_email(P_USERID IN VARCHAR2,
                                           P_FROM IN VARCHAR2,
                                             P_TO IN VARCHAR2, 
                                        P_SUBJECT IN VARCHAR2, 
                                            P_MSG IN VARCHAR2,
                                       P_FILENAME IN VARCHAR2)
RETURN VARCHAR2
AS
  V_MAIL_HOST VARCHAR2 (64); 
  V_PORT PLS_INTEGER;
  V_ACCOUNT VARCHAR2(500);
  V_PWD VARCHAR2(500);
  V_MAIL_CONN UTL_SMTP.CONNECTION;
  V_USER VARCHAR2(200);
  V_PASS VARCHAR2(200);
  TYPE T IS TABLE OF VARCHAR2(50);
  T_TO T := T();
  V_COUNT PLS_INTEGER :=1;
  P_MAIL_TO VARCHAR2(2000) := P_TO;
  V_TEST VARCHAR2(60);
  -- mime blocks (the sections of the email body that can become attachments)
  -- must be delimited by a string, this particular string is just an example
  c_mime_boundary CONSTANT VARCHAR2(256) := '-----AABCDEFBBCCC0123456789DE';
  v_clob                   CLOB := EMPTY_CLOB();
  v_len                    INTEGER;
  v_index                  INTEGER;
  p_ret                    VARCHAR2(400);
BEGIN
   ------ X_SERVER, X_PORT, X_ACCOUNT, CRYPTIT.DECRYPT(X_PWD)
   SELECT 'smtp.gmail.com', '587', 'jaimeretamal47@gmail.com', 'Jaime2024' 
     INTO V_MAIL_HOST, V_PORT, V_ACCOUNT, V_PWD
     FROM DUAL;
     --FROM user_boss.GET_SMTP_ACCOUNT
    --WHERE X_USERID = P_USERID;
   --
   -- Build the contents before connecting to the mail server
   -- that way you can begin pumping the data immediately
   -- and not risk an SMTP timeout
   FOR x IN (SELECT *
               FROM all_objects
              WHERE ROWNUM < 20)
   LOOP
       v_clob :=
              v_clob
           || x.owner
           || ','
           || x.object_name
           || ','
           || x.object_type
           || ','
           || TO_CHAR(x.created, 'yyyy-mm-dd hh24:mi:ss')
           || UTL_TCP.crlf;
   END LOOP;
   --
   --
   LOOP
     IF (INSTR(P_MAIL_TO,',') !=0) THEN
        T_TO.EXTEND(1);
        T_TO(V_COUNT) := TRIM(SUBSTR(P_MAIL_TO,1,INSTR(P_MAIL_TO,',') -1));
        P_MAIL_TO := SUBSTR(P_MAIL_TO, INSTR(P_MAIL_TO,',') + 1, LENGTH(P_MAIL_TO) - INSTR(P_MAIL_TO,',') + 1);
        V_COUNT := V_COUNT + 1;
     ELSE
        T_TO.EXTEND(1);
        T_TO(V_COUNT) := TRIM(P_MAIL_TO);
        EXIT;
     END IF;
   END LOOP;
   --
   V_MAIL_CONN := UTL_SMTP.OPEN_CONNECTION(V_MAIL_HOST, V_PORT);
   UTL_SMTP.EHLO(V_MAIL_CONN, V_MAIL_HOST);
   -- 
   UTL_SMTP.COMMAND(V_MAIL_CONN, 'AUTH LOGIN');
   UTL_SMTP.COMMAND(V_MAIL_CONN, UTL_RAW.CAST_TO_VARCHAR2(UTL_ENCODE.BASE64_ENCODE(UTL_RAW.CAST_TO_RAW(V_ACCOUNT))));
   UTL_SMTP.COMMAND(V_MAIL_CONN, utl_raw.cast_to_varchar2(utl_encode.base64_encode( utl_raw.cast_to_raw(v_pwd))));
   V_MAIL_CONN := UTL_SMTP.OPEN_CONNECTION (V_MAIL_HOST, V_PORT);
   UTL_SMTP.HELO (V_MAIL_CONN, V_MAIL_HOST);
   UTL_SMTP.MAIL (V_MAIL_CONN, P_FROM);
   -- send list of repeients ( one or more, comma seperated )
   FOR I IN 1..T_TO.LAST LOOP
       V_TEST := T_TO(I);
       UTL_SMTP.RCPT (V_MAIL_CONN, T_TO(I));
   END LOOP;
   -- 
   UTL_SMTP.OPEN_DATA (V_MAIL_CONN);
   UTL_SMTP.WRITE_DATA (V_MAIL_CONN,
   'Date: '
   || TO_CHAR (SYSDATE, 'DD-MON-YYYY HH24:MI:SS')
   || UTL_TCP.CRLF
   );
   UTL_SMTP.WRITE_DATA (V_MAIL_CONN, 'FROM: ' || P_FROM || UTL_TCP.CRLF);
   UTL_SMTP.WRITE_DATA (V_MAIL_CONN, 'SUBJECT: ' || P_SUBJECT || UTL_TCP.CRLF);
   UTL_SMTP.WRITE_DATA (V_MAIL_CONN, 'TO: ' || P_TO || UTL_TCP.CRLF);
   UTL_SMTP.WRITE_DATA (V_MAIL_CONN, UTL_TCP.CRLF);
   UTL_SMTP.WRITE_DATA (V_MAIL_CONN, P_MSG);
   UTL_SMTP.write_data(
       V_MAIL_CONN,
       'Content-Type: multipart/mixed; boundary="' || c_mime_boundary || '"' || UTL_TCP.crlf
   );
   UTL_SMTP.write_data(V_MAIL_CONN, UTL_TCP.crlf);
   UTL_SMTP.write_data(
       V_MAIL_CONN,
       'This is a multi-part message in MIME format.' || UTL_TCP.crlf
   );
   UTL_SMTP.write_data(V_MAIL_CONN, '--' || c_mime_boundary || UTL_TCP.crlf);
   UTL_SMTP.write_data(V_MAIL_CONN, 'Content-Type: text/plain' || UTL_TCP.crlf);
   IF P_FILENAME IS NOT NULL THEN
     -- Set up attachment header
     UTL_SMTP.write_data(
         V_MAIL_CONN,
            'Content-Disposition: attachment; filename="'
         || P_FILENAME
         || '"'
         || UTL_TCP.crlf
     );
     UTL_SMTP.write_data(V_MAIL_CONN, UTL_TCP.crlf);
     -- Write attachment contents
     v_len := DBMS_LOB.getlength(v_clob);
     v_index := 1;
     WHILE v_index <= v_len
     LOOP
         UTL_SMTP.write_data(V_MAIL_CONN, DBMS_LOB.SUBSTR(v_clob, 32000, v_index));
         v_index := v_index + 32000;
     END LOOP;
     --
     -- End attachment
   END IF;
   UTL_SMTP.CLOSE_DATA (V_MAIL_CONN);
   UTL_SMTP.QUIT (V_MAIL_CONN);
   p_ret := 'Successfull sent email...';
   return p_ret;
EXCEPTION
    WHEN OTHERS
    THEN
        p_ret := DBMS_UTILITY.format_error_stack;
        return p_ret;
END send_email;
