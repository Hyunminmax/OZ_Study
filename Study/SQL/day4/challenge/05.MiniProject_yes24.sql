use yes24;
SELECT * FROM yes24.books;
-- 기본 조회 및 필터링
select title, author From books;
select title, rating from books where rating >= 4;
select title, review from books where review >= 100;
select title, price from books where price < 20000;
select title, ranking_weeks from books where ranking_weeks >= 4;
select title, author from books where author = 'ETS';
select title, publisher from books where publisher = '데이원';

-- 조인 및 관계
select author, count(*) from books group by author;
select publisher, count(*) from books group by publisher order by count(*) DESC limit 1;
select author, avg(rating) from books group by author order by avg(rating) DESC limit 1;
select title, author from books where ranking = 1;
select title from books order by sales DESC, review DESC limit 10;
select title, publishing from books order by publishing DESC limit 5;

-- 집계 및 그룹화
select author, avg(rating) from books group by author order by avg(rating) DESC;
select publishing, count(*) from books group by publishing order by publishing DESC;
select title, avg(price) from books group by title;
select title, review from books order by review DESC limit 5;
select ranking, avg(review) from books group by ranking;

-- 서브쿼리 및 고급 기능
select title, rating from books where rating > (select avg(rating) from books) order by rating DESC;
select title, price from books where price > (select avg(price) from books) order by price DESC;
-- 강사님이 지운 문제. 최대값을 초과하는 값이라니...
select title, review from books where review > (select max(review) from books);
select title, sales from books where price < (select avg(sales) from books) order by sales DESC;
select title, publishing from books where author = (select author from books group by author order by count(*) DESC limit 1) order by publishing DESC limit 1 ;
select author, count(*) from books group by author order by count(*) DESC limit 1;

-- 데이터 수정 및 관리
-- Safe mode disable 
update books set price = 880000 where bookID = 1;
update books set title = '나도 단타 잘하고 싶다.' where author = '홍인기';
-- 강사님 방법으로 불가능 1093에러 발생
delete from books where sales = (select * from (select min(sales) from books) as temp);
update books set rating = rating + 1 where publisher = '길벗';

-- 데이터 분석 예제
select author, avg(rating), avg(sales) from books group by author order by avg(rating) DESC, avg(sales) DESC;
select publishing, avg(price) from books group by publishing order by publishing;
-- 문제는 출판사별 출판수와 리뷰의 평균을 구해라. -> 강사님은 출판사별 출판수와 리뷰의 합을 구해라. 문제와 다른 풀이.. 
select publisher, count(*), avg(review) from books group by publisher;
select ranking, avg(sales) from books group by ranking order by ranking;
select price, avg(review), avg(rating) from books group by price order by price;

-- 난이도 있는 문제
select publisher, author, avg(sales) from books group by publisher, author order by publisher, avg(sales) DESC;
select title, review, price from books where review > (select avg(review) from books) and  price < (select avg(price) from books);
select author, count(distinct title) from books group by author order by count(*) DESC limit 1;
select b.author, b.title, b.sales from books b join (select author, max(sales) as max from books group by author) sub on b.author = sub.author and b.sales = sub.max;
select year(publishing), count(*), avg(price) from books group by year(publishing);
select publisher, max(rating) - min(rating) as gap from books group by publisher order by gap DESC limit 1;
select title, rating / sales as ratio from books where author = '최태성' order by ratio DESC limit 1;

SELECT * FROM yes24.books;