# 웹스크래핑 미니 프로젝트

### 요구사항
- [x] 데이터 스크래핑 **(필수)**
    - data_get/cat_insert_db.py : kream 상위 탭 링크를 카테고리로 database 저장
    - data_get/product_insert_db.py : 저장된 카테고리 및 성별 기준으로 kream 사이트의 상품 데이터 크롤링하여 database 저장
- [x] 크롤링한 데이터 데이터베이스에 저장 **(필수)**
    - 상동
- [x] FLASK에 기존에 만든 Bootstrap 적용하기 **(선택 - 챌린지)**
- [x] FLASK에 스크래핑된 결과를 저장한 데이터베이스 연동하기 **(선택 - 챌린지)**
- [x] 데이터베이스의 데이터를 Bootstrap 화면에 보여주기 **(선택 - 챌린지)**
- [x] github에 등록하기 **(필수)**
- [x] readme.md 작성 **(필수)**

---

### 주요 기능
- 상품 검색기능
- 카테고리 분류 및 성별 분류 기능
- 선택 상품 삭제 기능
- pagination 기능
- 검색 초기화 기능
- crontab을 통한 매일 9:30 데이터 업데이트 기능

---
#### 처음 접속 페이지 캡쳐
<img src="https://raw.githubusercontent.com/lss018000/git_study/main/Flask_Server/clawling/img/img0.png">

#### 저장된 카테고리 노출 캡쳐
<img src="https://raw.githubusercontent.com/lss018000/git_study/main/Flask_Server/clawling/img/img1.png">

#### 검색 기능 캡쳐
<img src="https://raw.githubusercontent.com/lss018000/git_study/main/Flask_Server/clawling/img/img2.png">

#### 카테고리 및 성별 선택 필터링 캡쳐
<img src="https://raw.githubusercontent.com/lss018000/git_study/main/Flask_Server/clawling/img/img3.png">

#### 페이지네이션 기능 캡쳐
<img src="https://raw.githubusercontent.com/lss018000/git_study/main/Flask_Server/clawling/img/img4.png">

