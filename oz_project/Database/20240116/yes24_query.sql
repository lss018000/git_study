-- USE yes24;

-- [기본 조회 및 필터링]
-- 모든 책의 제목과 저자를 조회하세요.
-- SELECT title, author FROM Books;

-- 평점이 8 이상인 책 목록을 조회하세요.
-- SELECT title, rating FROM Books WHERE rating >= 4;

-- 리뷰 수가 100개 이상인 책들의 제목과 리뷰 수를 조회하세요.
-- SELECT title, review FROM Books WHERE review >= 100;

-- 가격이 20,000원 미만인 책들의 제목과 가격을 조회하세요.
-- SELECT title, price FROM Books WHERE price < 20000;

-- 국내도서TOP100에 4주 이상 머문 책들을 조회하세요.
-- SELECT title, ranking_weeks FROM Books WHERE ranking_weeks >= 4;

-- 특정 저자의 모든 책을 조회하세요.
-- SELECT title FROM Books WHERE author like '%용수%';

-- 특정 출판사가 출판한 책들을 조회하세요.
-- SELECT title FROM Books WHERE publisher like '%벗%';


-- [조인 및 관계]
-- 저자별로 출판한 책의 수를 조회하세요.
-- SELECT author, COUNT(*) FROM Books GROUP BY author;
 
-- 가장 많은 책을 출판한 출판사를 찾으세요.
-- SELECT publisher, COUNT(*) AS num_books FROM Books GROUP BY publisher ORDER BY num_books DESC LIMIT 1;

-- 가장 높은 평균 평점을 가진 저자를 찾으세요.
-- SELECT author, AVG(rating) AS avg_rating FROM Books GROUP BY author ORDER BY avg_rating DESC LIMIT 1;

-- 국내도서랭킹이 1위인 책의 제목과 저자를 조회하세요.
-- SELECT title, author FROM Books WHERE ranking = 1;

-- 판매지수와 리뷰 수가 모두 높은 상위 10개의 책을 조회하세요.
-- SELECT title, sales, review FROM Books ORDER BY sales DESC, review DESC LIMIT 10;

-- 가장 최근에 출판된 5권의 책을 조회하세요.
-- SELECT title, publishing FROM Books ORDER BY publishing DESC LIMIT 5;


-- [집계 및 그룹화]
-- 저자별 평균 평점을 계산하세요.
-- SELECT author, AVG(rating) FROM Books GROUP BY author;

-- 출판일별 출간된 책의 수를 계산하세요.
-- SELECT publishing, COUNT(*) FROM Books GROUP BY publishing;

-- 책 제목별 평균 가격을 조회하세요.
-- SELECT title, AVG(price) FROM Books GROUP BY title;

-- 리뷰 수가 가장 많은 상위 5권의 책을 찾으세요.
-- SELECT title, review FROM Books ORDER BY review DESC LIMIT 5;

-- 국내도서랭킹 별 평균 리뷰 수를 계산하세요.
-- SELECT ranking, AVG(review) FROM Books GROUP BY ranking;


--  [서브쿼리 및 고급 기능]
-- 평균 평점보다 높은 평점을 받은 책들을 조회하세요.
-- SELECT title, rating FROM Books WHERE rating > (SELECT AVG(rating) FROM Books);

-- 평균 가격보다 비싼 책들의 제목과 가격을 조회하세요.
-- SELECT title, price FROM Books WHERE price > (SELECT AVG(price) FROM Books);

-- 가장 많은 리뷰를 받은 책보다 많은 리뷰를 받은 다른 책들을 조회하세요.
-- SELECT MAX(review) FROM Books;
-- SELECT title, review FROM Books WHERE review >= (SELECT MAX(review) FROM Books);

-- 평균 판매지수보다 낮은 판매지수를 가진 책들을 조회하세요.
-- SELECT title, sales FROM Books WHERE sales < (SELECT AVG(sales) FROM Books);

-- 가장 많이 출판된 저자의 책들 중 최근에 출판된 책을 조회하세요.
-- SELECT title, publishing FROM Books WHERE author = (SELECT author FROM Books GROUP BY author ORDER BY COUNT(*) DESC LIMIT 1) ORDER BY publishing DESC LIMIT 1;


-- [데이터 수정 및 관리]
-- 특정 책의 가격을 업데이트하세요.
-- UPDATE Books SET price = '30000' WHERE title like '별의 길';

-- 특정 저자의 책 제목을 변경하세요.
-- UPDATE Books SET title = '별의길 수정2' WHERE author like '%양세형%';

-- 판매지수가 가장 낮은 책을 데이터베이스에서 삭제하세요.
-- DELETE FROM Books WHERE sales = (SELECT MIN(sales) FROM Books);

-- 특정 출판사가 출판한 모든 책의 평점을 1점 증가시키세요.
-- UPDATE Books SET rating = rating + 1 WHERE publisher = '민음사';


-- [데이터 분석 예제]
-- 저자별 평균 평점 및 판매지수를 분석하여 인기 있는 저자를 확인합니다.
-- SELECT author, AVG(rating) as avg_rating, AVG(sales) as avg_sales FROM Books GROUP BY author;

-- 출판일에 따른 책 가격의 변동 추세를 분석합니다.
-- SELECT publishing, AVG(price) as avg_price FROM Books GROUP BY publishing;

-- 출판사별 출간된 책의 수와 평균 리뷰 수를 비교 분석합니다.
-- SELECT publisher, COUNT(*) as num_books, AVG(review) as avg_review FROM Books GROUP BY publisher;

-- 국내도서랭킹과 판매지수의 상관관계를 분석합니다.
-- SELECT ranking, AVG(sales) as avg_sales FROM Books GROUP BY ranking;

-- 가격 대비 리뷰 수와 평점의 관계를 분석하여 가성비 좋은 책을 찾습니다.
-- SELECT price, AVG(review) as avg_review, AVG(rating) as avg_rating FROM Books GROUP BY price;


-- [난이도 있는 문제]
-- 출판사별 평균 판매지수가 가장 높은 저자 찾기
-- 각 출판사별로 평균 판매지수가 가장 높은 저자의 이름과 그 평균 판매지수를 조회하세요.
-- SELECT publisher, author, AVG(sales) as avg_sales
-- FROM Books
-- GROUP BY publisher, author
-- ORDER BY publisher, avg_sales DESC;

-- 리뷰 수가 평균보다 높으면서 가격이 평균보다 낮은 책 조회
-- 리뷰 수와 가격의 전체 평균을 계산한 후, 이보다 리뷰 수는 높고 가격은 낮은 책들을 조회하세요.
-- SELECT title, review, price
-- FROM Books
-- WHERE review > (SELECT AVG(review) FROM Books) AND price < (SELECT AVG(price) FROM Books);

-- 가장 많은 종류의 책을 출판한 저자 찾기
-- 서로 다른 제목의 책을 가장 많이 출판한 저자를 찾으세요.
-- SELECT author, COUNT(DISTINCT title) as num_books
-- FROM Books
-- GROUP BY author
-- ORDER BY num_books DESC
-- LIMIT 1;

-- 각 저자별로 가장 높은 판매지수를 기록한 책 조회
-- 각 저자별로 가장 높은 판매지수를 기록한 책의 제목과 그 판매지수를 조회하세요.
-- SELECT author, title, MAX(sales) as max_sales
-- FROM Books
-- GROUP BY author, title;


-- 연도별 출판된 책 수와 평균 가격 비교
-- 연도별로 출판된 책의 수와 그 해 출판된 책들의 평균 가격을 비교 분석하세요.
-- SELECT YEAR(publishing) as year, COUNT(*) as num_books, AVG(price) as avg_price
-- FROM Books
-- GROUP BY year;

-- 출판사가 같은 책들 중 평점 편차가 가장 큰 출판사 찾기
-- 같은 출판사에서 출판된 책들 중 평점 편차가 가장 큰 출판사와 그 편차를 조회하세요.
-- SELECT publisher, MAX(rating) - MIN(rating) as rating_difference
-- FROM Books
-- GROUP BY publisher
-- ORDER BY rating_difference DESC
-- LIMIT 1;

-- 특정 저자의 책들 중 판매지수 대비 평점이 가장 높은 책 찾기
-- 특정 저자의 책들 중 판매지수 대비 평점이 가장 높은 책의 제목과 그 비율을 조회하세요.
-- SELECT title, rating / sales as ratio
-- FROM Books
-- WHERE author = 'ETS 저'
-- ORDER BY ratio DESC
-- LIMIT 1;