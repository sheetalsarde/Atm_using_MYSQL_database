 
                  ATM using MYSQL Database
******************************************************************************************************
Create MYSQL Database ---------

create table user_info(UserName varchar(30) primary key,Pin int(4),amount float(12,2));

create table trans(UserName varchar(30),constraint UserName_fk foreign key (UserName) 
references user_info(UserName),amount float(12,2),dot date,ttype char(8));

insert into user_info values('sheetal',2222,5000),('aditi',1122,6000),('shraddha',2233,8000);

________________________________________________________________________________________________________

store the database for ATM
user names and their  pins are 

users = [sheetal,aditi,shraddha]
pins = ['2222', '1122', '2233']
