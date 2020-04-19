BEGIN;
--
-- 1. Create model Author
--
CREATE TABLE "snippets_author" ("id" serial NOT NULL PRIMARY KEY, "name" varchar(200) NOT NULL, "email" varchar(254) NOT NULL);
--
-- 2. Create model Blog
--
CREATE TABLE "snippets_blog" ("id" serial NOT NULL PRIMARY KEY, "name" varchar(100) NOT NULL, "tagline" text NOT NULL);
--
-- 3. Create model Entry
--
--
-- 3.1 Create snippets_entry
--
CREATE TABLE "snippets_entry" ("id" serial NOT NULL PRIMARY KEY, "headline" varchar(255) NOT NULL, "body_text" text NOT NULL, "pub_date" date NOT NULL, "mod_date" date NOT NULL, "number_of_comments" integer NOT NULL, "number_of_pingbacks" integer NOT NULL, "rating" integer NOT NULL, "blog_id" integer NOT NULL);
--
ALTER TABLE "snippets_entry" ADD CONSTRAINT "snippets_entry_blog_id_453648b9_fk_snippets_blog_id" FOREIGN KEY ("blog_id") REFERENCES "snippets_blog" ("id") DEFERRABLE INITIALLY DEFERRED;
CREATE INDEX "snippets_entry_blog_id_453648b9" ON "snippets_entry" ("blog_id");
--
-- 3.2 Create snippets_entry_authors
--
CREATE TABLE "snippets_entry_authors" ("id" serial NOT NULL PRIMARY KEY, "entry_id" integer NOT NULL, "author_id" integer NOT NULL);
--
ALTER TABLE "snippets_entry_authors" ADD CONSTRAINT "snippets_entry_authors_entry_id_18c195d1_fk_snippets_entry_id" FOREIGN KEY ("entry_id") REFERENCES "snippets_entry" ("id") DEFERRABLE INITIALLY DEFERRED;
--
ALTER TABLE "snippets_entry_authors" ADD CONSTRAINT "snippets_entry_authors_author_id_011fc758_fk_snippets_author_id" FOREIGN KEY ("author_id") REFERENCES "snippets_author" ("id") DEFERRABLE INITIALLY DEFERRED;
--
ALTER TABLE "snippets_entry_authors" ADD CONSTRAINT "snippets_entry_authors_entry_id_author_id_6d870cc5_uniq" UNIQUE ("entry_id", "author_id");
--
CREATE INDEX "snippets_entry_authors_entry_id_18c195d1" ON "snippets_entry_authors" ("entry_id");
CREATE INDEX "snippets_entry_authors_author_id_011fc758" ON "snippets_entry_authors" ("author_id");
COMMIT;












Second highest salary -SELECT MAX(Salary) FROM Employees
WHERE Salary NOT IN (SELECT MAX(Salary) FROM Employees )
Create - 
create table employee(emp_id varchar(10), emp_name varchar(10),  sal number(10), phn_no varchar(10),doj date);
Insert -
insert into employee(emp_id , emp_name,  sal , phn_no ,doj) values('1001','kapil',30000,'8871337193','29-nov-1993')
insert into employee  values('1001','kapil',30000,'8871337193','29-nov-1993')
insert into manger 

Display – 
Select * from employee
Select emp_id, emp_name, sal, sal+300,doj,phn_no from employee 
Aliase - Select emp_id, emp_name, sal+300  temp,doj,phn_no from employee where temp is an alternative name of sal+300                                                                                                                          				or
 Select emp_id, emp_name,sal ,sal+300 as "new salary",doj,phn_no from employee
concatination - Select 'The employee id' ||  emp_id  ||'  is of  '||emp_name||  ' whose salary was '|| sal temp from employee
where clause - select * from employee where emp_id='1001'
                                             or 
select * from employee where sal>30001
                                             or
select *  from employee where emp_name is null
Between - select * from employee  where sal  between 25000 and 32000(32000>=sal>=25000)
In - select * from employee  where emp_id in('1001','1003')
Like – underscore means single character and % mean’s zero or more.
select * from employee  where emp_name like ('_a%')
select * from employee  where emp_id like ('%3')
Logical operater – and, or, not
select * from employee  where emp_id='1003' and sal=25000
Eliminate the duplicate row – temporary eliminate
select distinct * from employee  

Backup - create table emp as select * from employee  
Alter – 
Add - alter table emp add (dor  date)
Modify - alter table emp modify (sal number(12))
Delete – alter table emp  drop column dor
Rename – rename  emp to emp1 
Delete – delete from emp1 where sal=32000 for only specific row or delete from emp1 for all row
Drop – drop table emp1 (all row + schema)
Truncate – truncate table employee (all record without schema)
Update –
       1.    update    manager     set phn_no='9876543210'    where emp_id='1005'
       2.    update manager    set phn_no= (select phn_no from employee where sal=30000)
         where emp_id=(select emp_id from employee where sal=30000)
Order by – (Sorting)  select * from  employee order by doj  desc
Group by - select sum(sal) ,emp_name from employee group by emp_name
Aggrigate Function -    sum,max,min,avg,count
                                        select count(emp_id) from employee
Constraints – 
Check - create table emp( emp_id varchar(10), sal number(10) constraints esal check(sal>0))
                          insert into emp values('1001',0) it gives error because sal never be less then 0
                                                                          or
                      create table student (branch varchar(10) constraint chk check(branch in ('cs','ec','it')))
Not Null –   doj date not null
Primary Key - emp_id number(5)primary key
Unique Key - email varchar(30) unique
Foreign Key - dept_id varchar(10) references department (dept_id)
Default : DEFAULT 'Sandnes'

CREATE TABLE Persons (
    ID int NOT NULL,
    LastName varchar(255) NOT NULL,
    FirstName varchar(255),
    Age int,
    City varchar(255) DEFAULT 'Sandnes'
);
Example –
Create tale department (dept_id varchar(10) primary key)




create table employee(
 emp_id number(5)primary key,
                doj date not null,
                email varchar(30) unique,
                dept_id varchar(10) references department (dept_id)
                )
Composite Key – 
                Create table emp(
                 Emp_id varchar(10),
                 D_O_J date constraint doj not null,
                 Email varchar(30),
                 Dep_id  varchar(10),
                 Constraint emp_ck primary key(emp_id,email)
                 )
Dropping Constraints – 
               Alter table emp  drop constraint doj
Adding Constraints – 
               Alter table emp  add constraint emp_id_pk primary key(emp_id)
  Join- 
Equi Join- Select  emp_id, sal       From emp, dept
                                  Where emp.dept_id = dept . dept_id(=,<,>,<=,>= etc)
Natural join -    Select  emp_id,sal,dept_name
                                           From emp natural join dept
Non Equi Join - Select  emp_id, sal    From emp, dept
                                           Where emp.dept_id > dept . dept_id(<,  >,  <=,  >=   etc.)

Cartesion Product -    select emp_id, dept_name
                                                      from emp,dept
Outer Join – 
Left Outer Join - select emp_id,dept_name
                                                                  from emp e,dept d
                                                                  where e.dept_id(+)=d.dept_id
Right Outer Join - select emp_id,dept_name
                                                                    from emp e right outer join dept d
                                                                    on(e.dept_id=d.dept_id)
Full Outer Join -   select emp_id,dept_name
                                                                   from emp e full outer join dept d
                                                                  on(e.dept_id=d.dept_id)
PostgreSQL COALESCE function syntax
The syntax of the COALESCE function is as follows:
1	COALESCE (argument_1, argument_2, …);
The COALESCE function accepts unlimited number of arguments. It returns the first argument that is not null. If all arguments are null, the COALESCE function will return null.
The COALESCE function evaluates arguments from left to right until it finds the first non-null argument. All the remaining arguments from the first non-null argument are not evaluated.
The COALESCE function provides the same functionality as NVL or IFNULL function provided by SQL-standard. MySQL has IFNULL function, while Oracle provides NVL function.






