## what are relational databases ?
- organize data into tables , where each table represents a specific type of entity . These tables are linked together based on relationships between the data , often using shared columns called keys . This structure allows for efficient storage , retrieval and management of large datasets while ensuring data integrity and consistency.

## RDBMS benefits and limitations :

-  a RDMS stores data in the form of tables and users relationships between tables through primary key and foreign keys.

-  Benefits :
 1. Data integrity : 
       - ensure data is accurate and consistent.
2. Reduces Data Redundancy 
     - Data in normalized to avoid duplication .
3. Data Security :  
    -  supports user authentication and role based access .
4. ACID properties :
   -  ensure reliable transactions :
     1. A :  Atomicity 
     2. c : consistency
     3. I : isolation
     4. D : Durability 
5. Easy data retrieval
6. Relationships between tables 
7. Backup and recovery
8. Multi-user supports
9. Data consistency 
10. Standardized language (SQL)


- Limitations: 
1. Complex design
2. Expensive for large systems
3. Scalability challenges
4. Slower for very large data
5. Fixed Schema
6. Storage overhead
7. Performance overhead
8. Less suitable for unstructured data

---

``` A basic DBMS may not provide all of these capabilities , especially strong relational features and transaction guarantees.
```