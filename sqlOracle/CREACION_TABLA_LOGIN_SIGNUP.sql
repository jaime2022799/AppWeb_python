SELECT * FROM LOGIN;

SELECT * FROM SIGNUP;


CREATE TABLE LOGIN (
    ID_LOGIN NUMBER(10) PRIMARY KEY,
    EMAIL VARCHAR(100) NOT NULL,
    CLAVE VARCHAR(100) NOT NULL
);



CREATE TABLE SIGNUP (
   ID_SIGNUP NUMBER(10) PRIMARY KEY,
   EMAIL VARCHAR(100) NOT NULL,
   CLAVE_NUEVA VARCHAR(100) NOT NULL,
   CLAVE VARCHAR(100) NOT NULL,
   LOGIN_ID NUMBER(10) NOT NULL
);

ALTER TABLE SIGNUP 
ADD CONSTRAINT SIGNUP_ID_LOGIN_FK
FOREIGN KEY (LOGIN_ID) REFERENCES LOGIN (ID_LOGIN);

INSERT INTO LOGIN VALUES (3,'ESMERALDA2024@GMAIL.COM','ESMERALDA2024');
INSERT INTO SIGNUP VALUES (3,'ESMERALDA2024@GMAIL.COM','ESMERALDA2024','ESMERALDA2024',3);

SELECT * FROM LOGIN;
SELECT * FROM SIGNUP;