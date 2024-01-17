/*CREATE DIRECTORY DIR_ARCHIVO_RUTA AS 'C:\Users';
GRANT READ ON DIRECTORY DIR_ARCHIVO_RUTA TO user_boss;*/
SELECT * FROM ARCHIVO_BLOB_COTIZADOR;

DECLARE 
    V_TEMP BLOB;
    V_BFILE BFILE;
    V_NOMBRE_FOTO VARCHAR(100);
    
BEGIN

    INSERT INTO ARCHIVO_BLOB_COTIZADOR VALUES (5, EMPTY_BLOB()) RETURNING ARCHIVO INTO V_TEMP;
    
    V_NOMBRE_FOTO := 'vision.png';
    
    V_BFILE := BFILENAME('DIR_ARCHIVO_RUTA_7', V_NOMBRE_FOTO);
    dbms_lob.open(V_BFILE, dbms_lob.lob_readonly);
    dbms_lob.loadfromfile(V_TEMP, V_BFILE, dbms_lob.getlength(v_bfile));
    dbms_lob.close(V_BFILE);
    COMMIT;
    

END;