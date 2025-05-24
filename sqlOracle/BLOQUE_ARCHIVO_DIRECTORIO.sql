SELECT * FROM archivo_bfile_cotizador;


SELECT * FROM archivo_bfile_cotizador;
--delete from archivo_bfile_cotizador where id_cotizador in (10,20,40,30,50,70);


BEGIN 

--INSERT INTO archivo_bfile_cotizador VALUES (80, 'VISION_2', BFILENAME('DIR_ARCHIVO_RUTA','vision.png'));
  INSERT INTO archivo_bfile_cotizador VALUES (50, 'vision', bfilename('DIR_ARCHIVO_RUTA_7','vision.png'));

END;

delete from archivo_bfile_cotizador where id_cotizador=50;



--DROP TABLE EXT_TBL_ARCHIVO_TXT;