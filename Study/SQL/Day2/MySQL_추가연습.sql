use classicmodels;
-- 1. 생성(C)
-- 고급
-- 1. 
INSERT INTO customers (customerNumber, customerName, contactLastName) VALUES (888, 'Hyunmin', 'Shin');
INSERT INTO orders (orderNumber,orderDate,requiredDate,status,customerNumber) VALUES (99999,'2024-02-05','2024-02-10','Shipped',888);
INSERT INTO orderdetails (orderNumber,productCode,quantityOrdered, priceEach, orderLineNumber) VALUES (99999, 'S10_1678', 98, 333.00, 3);

-- 2. 
INSERT INTO employees (employeeNumber,lastName,firstName,extension,email,officeCode,jobTitle) VALUES (8888, 'Shin', 'Hyunmin', 'x5800', '안알랴줌@abc.com', 1, 'Sales'); 
UPDATE employees SET reportsTo = 1002 WHERE employeeNumber = 8888;

-- 3. 
INSERT INTO products (productCode,productName,productLine,productScale,productVendor,productDescription,quantityInStock,buyPrice,MSRP) VALUES ('S700_8888', 'HMS Bounty', 'Ships', '1:700', 'Unimax Art Galleries', 'Measures 30 inches Long x 27 1/2 inches High x 4 3/4 inches Wide. Many extras including rigging, long boats, pilot house, anchors, etc. Comes with three masts, all square-rigged.' , 3501, 99.99, 99.90);
INSERT INTO orders (orderNumber,orderDate,requiredDate,status,customerNumber) VALUES (88888,'2024-02-05','2024-02-10','Shipped',888);
INSERT INTO orderdetails (orderNumber,productCode,quantityOrdered, priceEach, orderLineNumber) VALUES (88888, 'S700_8888', 98, 333.00, 3);

-- 4. 
INSERT INTO orders (orderNumber,orderDate,requiredDate,status,customerNumber) VALUES (77777,'2024-02-05','2024-02-10','Shipped',888);
INSERT INTO payments (customerNumber,checkNumber,paymentDate,amount) VALUES (888, 'HXKGQ123', '2024-02-05', 30);

-- 5. 
INSERT INTO orders (orderNumber,orderDate,requiredDate,status,customerNumber) VALUES (55555,'2024-02-05','2024-02-10','Shipped',888);
INSERT INTO orderdetails (orderNumber,productCode,quantityOrdered, priceEach, orderLineNumber) VALUES (55555, 'S700_8888', 98, 333.00, 3);
UPDATE products SET quantityInStock = quantityInStock - 98 WHERE productCode = 'S700_8888';

-- 2. 읽기(R)
-- 고급
-- 1. 
select city, count(customerNumber) from customers group by city;

-- 2. 
select productLine, avg(buyPrice) from products group by productLine;

-- 3. 
select officeCode, count(employeeNumber) from employees group by officeCode;

-- 4. 
-- 없는 급여를 어찌 줍니까.. ㅠㅜ
select * from offices; -- 급여정보 없음
select * from employees; -- 급여정보 없음

-- 5. 
select productCode, sum(quantityOrdered) from orderdetails group by productCode order by sum(quantityOrdered) DESC limit 5;

-- 3. 갱신(U)
-- 고급
-- 1. 
update orders set status = "갱신" where Year(orderDate) = Year(current_date())-1; 

-- 2. 
update orderdetails set quantityOrdered = 1, priceEach = 10, orderLineNumber = 2 where orderNumber = 10100 and productCode = 'S18_1749';

-- 3. 
update payments set amount = 1004 where if(Month(current_date()) = 1, Year(paymentDate) = Year(current_date())-1 and Month(paymentDate) = 12, Year(paymentDate) = Year(current_date()) and Month(paymentDate) = Month(current_date())-1);

-- 4. 
update productlines set textDescription = '갱신';

-- 5. 
update customers set addressLine1 = '갱신';

-- 4.삭제(D)
-- 고급
-- 1. 
delete from orders where Year(orderDate) = Year(current_date())-1; -- 없는 데이터 지우기

-- 2. -- 예시에는 존재하지 않는 productID, IN을 지원하지 않는 버전임.
delete o1 from orderdetails o1 join (select productCode from orderdetails order by quantityOrdered limit 1) as o2 on o1.productCode = o2.productCode; 

-- 3. 
delete from payments where amount < 35;

-- 4. 제품이 없는 제품라인이 없음. IN을 지원하는 버전이 아님. @@ productline의 pk가 products의 fk 인데 productline에서 product가 없는 productline이 존재 할 수 없는것 아닌가요?
-- 아래 5번과 같이 product테이블의 productLine이 Not Null, FK인 상황으로 제품이 없는 제품라인도 없고 애초에 FK를 해제하지 않으면 삭제도 불가능한것 아닌가요?
DELETE FROM productlines WHERE productLine NOT IN (SELECT DISTINCT productLine FROM products); -- 이렇게 하면 쿼리는 돌아가지만 애초에 불가능 한 상황이 아닌가 싶습니다. 

select * from productlines pl join products p on pl.productLine = p.productLine;
select productLine from products group by productLine;
select * from productlines;
select * from products;

-- 5. lastOrderDate라는 것은 없음. orders 테이블의 customerNumber는 Not Null이고 FK이기도 해서 테이블에서 FK를 해제하기 전에는 불가능한것 아닌가요?
delete c1 from customers c1 join (
	select orderNumber, customerNumber
    from orders 
    where 365 < datediff(current_date(), orderDate)) as o on c1.customerNumber = o.customerNumber;
    );
    
DELETE FROM productlines WHERE productLine NOT IN (SELECT DISTINCT productLine FROM products);



