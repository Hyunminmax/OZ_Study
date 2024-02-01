-- 노션 과제 2번
-- 기본 조회 및 필터링
select customerName from customers;
select productName, buyPrice from products where productLine = 'Classic Cars';
select * from orders order by orderDate DESC limit 10;
select * from payments where amount >= 100; -- 100달러 이하의 값이 없는데...

-- 조인 쿼리
select orders.orderNumber, customers.customerName from customers join orders  on orders.customerNumber = customers.customerNumber;
select products.productName, productlines.textDescription from products join productlines on productlines.productLine = products.productLine;
select e1.firstName as 'employee Name', e2.firstName as 'Boss Name' from employees e1 left join employees e2 on e1.reportsTo = e2.employeeNumber;
select firstName, lastName from employees join offices on offices.officeCode = employees.officeCode where offices.city = 'San Francisco';

-- 그룹 쿼리
select productLine, count(*) from products group by productLine;
select c.customerNumber, c.customerName, sum(od.quantityOrdered * od.priceEach) as total
from customers c
join orders o on c.customerNumber = o.customerNumber
join orderdetails od on o.orderNumber = od.orderNumber
group by c.customerNumber; -- group by에 c.customerName을 넣는것은 의미가 없음. 
select p.productName, sum(od.quantityOrdered) from products p
join orderdetails od on p.productCode = od.productCode group by p.productName
order by sum(od.quantityOrdered) desc
limit 1;
-- erd가 알아보기 어렵다 직접 찾아보자!
-- select c.city, sum(od.quantityOrdered * od.priceEach) as total
-- from employees e 														-- 
-- join offices os on e.officeCode = os.officeCode							-- v
-- join customers c on c.salesRepEmployeeNumber = e.employeeNumber			-- v
-- join orders o on o.customerNumber = c.customerNumber						-- v
-- join orderdetails od on od.orderNumber = o.orderNumber					-- v
-- group by c.city
-- order by total DESC
-- limit 1;
SELECT o.city, SUM(od.quantityOrdered * od.priceEach) AS totalSales
FROM orders ord															-- 
JOIN orderdetails od ON ord.orderNumber = od.orderNumber				-- v
JOIN customers c ON ord.customerNumber = c.customerNumber				-- v
JOIN employees e ON c.salesRepEmployeeNumber = e.employeeNumber			-- v
JOIN offices o ON e.officeCode = o.officeCode 							-- v
GROUP BY o.city
ORDER BY totalSales DESC
LIMIT 1;

-- 서브쿼리
select orderNumber, sum(quantityOrdered * priceEach) as total 
from orderdetails 
group by orderNumber 
having total > 500;
-- where total > 500;  -- group by를 기준으로 group 짓기 전에는 where를 이후는 having을 사용해야 한다. 

select c.customerNumber, c.customerName, sum(p.amount) as total from payments p
join customers c on p.customerNumber = c.customerNumber
group by c.customerNumber
having total > (select avg(amount) from payments);

select c.customerName 
from customers c
where c.customerNumber not in (select customerNumber from orders);

-- 문제의 모호함. 평균이상결제를 이미 한 고객은 payments고 
-- 매출!은 아직 결제가 일어나지 않은 금액을 포함하는것이다.라는 설명이 어디에도 없음.
-- 강사님의 영상의 설명듣지 않으면 문제만 보고 풀기에는 너무 모호한 문제의 지문.
-- 문제를 명확하게 해주세요. ERD에 대한 어떠한 설명도 없이 풀기에는 혼란스럽습니다. ㅠㅜ
-- 문제에는 가장 많은 금액을 "지불할" 고객이 아니라 "지불한" 고객으로 되어있어서 payments에서 찾아야 할 것 같습니다. 
-- 이해 하기가 어려워요.
-- select c.customerName, sum(p.amount) as sum
-- from payments p 
-- join customers c on p.customerNumber = c.customerNumber
-- group by p.customerNumber
-- order by sum DESC
-- limit 1;

select c.customerName, sum(od.quantityOrdered * od.priceEach) as sum
from orderdetails od 
join orders o on od.orderNumber = o.orderNumber
join customers c on o.customerNumber = c.customerNumber
group by o.customerNumber
order by sum DESC
limit 1;

-- 데이터 수정 및 관리
insert into customers(
	customerNumber, customerName, contactLastName, contactFirstName, phone, 
    addressLine1, city, country)
    values(497, 'min\'s Office', 'Shin', 'Hyunmin', '010-0000-0000', '영통구', '수원', '경기도');

update products set buyPrice = buyPrice * 1.1 where productline = 'Classic Cars';

-- 특정고객의 이메일 주소를 변경하는 문제 고객은 이메일이 없음. 직원의 이메일 업데이트로 변경.
update employees set email = 'email_is_not_in_customers_table@classicmodelcars.com' where employeeNumber = 1002;

update employees set officeCode = '2' where employeeNumber = 1002;