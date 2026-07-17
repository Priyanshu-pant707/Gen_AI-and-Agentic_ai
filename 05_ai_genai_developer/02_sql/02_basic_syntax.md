# SQL keywords :

-  these are the reserved words that have predefined meaning in SQL. They are used to perform operations such as creating tables,inserting data,uploading records,deleting,records,querying data,and managing databases.


1. DDL (data definition language)
 - create :  create a database ,table , view
 - alter :  modifies an existing table 
 - drop :  deletes a tables or database permanently
 - truncate :  removes all rows from a table but keeps the table structure 
 - rename :  rename a table or column

```sql
CREATE TABLE Students(
    id INT PRIMARY KEY,
    name VARCHAR(50),
    age INT
);

ALTER TABLE Students
ADD city VARCHAR(30);

RENAME TABLE Students TO Student;

TRUNCATE TABLE Student;

DROP TABLE Student;
```

---


2. DML (Data Manipulation Language)
- used to manipulate data inside tables :
 1. insert
 2. update
 3. delete
 4. merge
```sql
INSERT INTO Students(name, age)
VALUES('Priyanshu',21);

UPDATE Students
SET age = 22
WHERE name = 'Priyanshu';

DELETE FROM Students
WHERE age < 18;
```


---

3. DQL (Data Quey Language)
- select :  retrieves data from one or more tables 



---

4. DCL (Data control language)
 1. GRANT -  gives privileges to users
 2. REVOKE -  removes privileges

---

5. TCL (Transaction control language)
 1. COMMIT :  saves the transaction permanently
 2. ROLLBACK :  undoes changes since the last month
 3. SAVEPOINT :  creates a point to roll back to

---

6. Filtering Keywords : 
- where
- and
- or
- not
- between
- in
- like
- is null
- is not null

```sql
SELECT * FROM Students
WHERE age BETWEEN 18 AND 25;

SELECT * FROM Students
WHERE city IN ('Delhi', 'Mumbai');

SELECT * FROM Students
WHERE name LIKE 'P%';

SELECT * FROM Students
WHERE city IS NULL;
```

---

7. Sorting keywords :
- order by
- asc
-  desc

---

8. Grouping keywords :
- Group by
- having

---

9. join keywords :
-  join
- inner join
- left join
- right join
- full outer join
- cross join
- self join



---


10. Aggregate function keywords :
-  count
- sum
- avg
- min
- max
