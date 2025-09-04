파워쉘 키고, 아래거 실행
psql -U postgres -h localhost
CREATE DATABASE ticket_system;
exit

psql 나오고 난뒤 아래거 실행
psql -U postgres -d ticket_system -f init2.sql
