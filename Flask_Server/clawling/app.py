from flask import Flask, request, redirect, url_for
import pymysql

# source bin/activate


app = Flask(__name__)
connection = pymysql.connect(
	host='localhost',
	user='root',
	password='lss018000',
	db='kream',
	charset='utf8mb4',
)
 
def cat_sel():
    cursor = connection.cursor()
    sql = "select * from product_cat"
    cursor.execute(sql)
    datas = cursor.fetchall()
    return_val = ''
    for data in datas:
        cat_no = data[1]
        cat_name = data[2]
        return_val = return_val + f'<option value="{cat_no}">{cat_name}</option>'
    cursor.close()
    return return_val


def product_list(cat, gen, q, page):
    cursor = connection.cursor()
    sql = "select *, (select cat_name from product_cat AS B where A.category = B.cat_no ) AS category_name from products AS A"
    if cat and gen and q:
        sql = sql + f" where category = '{cat}' and gender = '{gen}' and product_name like '%{q}%'"
    elif cat and gen:
        sql = sql + f" where category = '{cat}' and gender = '{gen}'"
    elif cat and q:
        sql = sql + f" where category = '{cat}' and product_name like '%{q}%'"
    elif gen and q:
        sql = sql + f" where gender = '{gen}' and product_name like '%{q}%'"
    elif cat:
        sql = sql + f" where category = '{cat}'"
    elif gen:
        sql = sql + f" where gender = '{gen}'"
    elif q:
        sql = sql + f" where product_name like '%{q}%'"
    
    sql = sql + " order by product_name ASC"
    # if page or page != '':
    sql = sql + f" LIMIT {int(page) * 10}, 10"

    cursor.execute(sql)
    datas = cursor.fetchall()
    return_val = ''
    
    for data in datas:
        id = data[0]
        category = data[1]
        category_name = data[8]
        brand = data[2]
        gender = data[3]
        if gender == 'men':
          gender = '남자';
        elif gender == 'women':
          gender = '여자';
        elif gender == 'kids':
          gender = '키즈';
        product_name_en = data[4]
        product_name = data[5]
        price = data[6]
        price_var = "%" in price
        if price_var:
          price_len = price.rfind('%') + 1;
          price = price[price_len:];
        else:
          price_len = 'a';
        kream_url = data[7]
        return_val = return_val + f'<tr><td><input type="checkbox" class="del_sel" id="del_sel" name="del_sel" onclick="del_chk_sel({id});" value="{id}"></td><td class="td_cat">{category_name}</td><td>{gender}</td><td>{brand}</td><td><span>{product_name}</span><a href="https://kream.co.kr{kream_url}" target="_blank" class="product_link">상품확인</a></td><td>{price}</td></tr>'
    cursor.close()
    return return_val

def product_cnt(cat, gen, q):
    cursor = connection.cursor()
    sql = "select * from products"
    if cat and gen and q:
        sql = sql + f" where category = '{cat}' and gender = '{gen}' and product_name like '%{q}%'"
    elif cat and gen:
        sql = sql + f" where category = '{cat}' and gender = '{gen}'"
    elif cat and q:
        sql = sql + f" where category = '{cat}' and product_name like '%{q}%'"
    elif gen and q:
        sql = sql + f" where gender = '{gen}' and product_name like '%{q}%'"
    elif cat:
        sql = sql + f" where category = '{cat}'"
    elif gen:
        sql = sql + f" where gender = '{gen}'"
    elif q:
        sql = sql + f" where product_name like '%{q}%'"

    cursor.execute(sql)
    datas = cursor.fetchall()
    cursor.close()
    return f'<input type="hidden" id="max_page" value="{len(datas)}">'



@app.route('/')
def adm_product_list():
    cat = request.args.get('cat', "")
    gen = request.args.get('gen', "")
    page = request.args.get('page', "1")
    q = request.args.get('q', "")
    return f'''<!DOCTYPE html>
<html lang="ko">
  <head>
    <title>Admin Page</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-4bw+/aepP/YC94hEpVNVgiZdgIC5+VKNBQNGCHeKRQN+PtmoHDEXuppvnDJzQIu9" crossorigin="anonymous">
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css">
    <script src='https://ajax.googleapis.com/ajax/libs/jquery/3.3.1/jquery.min.js'></script>
    <link href="static/style.css" rel="stylesheet">
  </head>
  <body>
    <div class="container mt-3">
      <h3 class="mt-5 mb-3">신규 등록 상품</h3>
      <div class="date">
        <span>오늘 날짜 : </span><span id="now_date"></span><br/>
        <span>마지막 업데이트 : </span><span id="update_date"></span><br/>
        <span>(매일 09:30 데이터 업데이트)</span><br/>
      </div>
      <form class="table_top" id="search_filter" action="/" method="GET">      
        <div class="left">
          <label class="visually-hidden" for="inlineFormSelectPref">Preference</label>
          <select class="form-select" id="catselect" name="cat">
            <!-- 카테고리 셀렉트 코드를 넣어주세요-->
            <option value="">카테고리</option>
            {cat_sel()}
          </select>
          <select class="form-select sex" id="sexselect" name="gen">
            <!-- 카테고리 셀렉트 코드를 넣어주세요-->
            <option selected value="">성별</option>
            <option value="men">남자</option>
            <option value="women">여자</option>
            <option value="kids">키즈</option>
          </select>
        </div>
        <div class="right">
          <div class="input-group mb-3">
            <input type="text" class="form-control" name="q" id="search_text" placeholder="제품명을 입력해주세요." aria-label="제품명을 입력해주세요." aria-describedby="button-addon2">
            <button class="btn btn-outline-secondary" type="submit" id="search">조회</button>
            <a href="/" class="btn btn-outline-secondary" >검색 조건 초기화</a>
            <!-- <a href="#;" id="json_referesh" class="btn btn-outline-secondary">상품 정보 업데이트</a> -->
          </div>
        </div>
      </form>
      <div class="del_area">
        <form action="/delete" method="GET">
		  <input type="hidden" id="del_datas" class="del_datas" name="del" value="0">
          <input type="submit" class="btn btn-secondary" id="sel_del" value="선택상품 삭제">
        </form>
      </div>
      <div class="container mt-3">      
        <table class="table table-sm">
          <thead>
            <!-- 열의 속성값을 나타내는 코드를 작성해주세요 (예 : 카테고리, 브랜드, 상품명, 가격) -->
            <tr>
              <th>선택</th>
              <th>카테고리</th>
              <th>성별</th>
              <th>브랜드</th>
              <th>상품명</th>
              <th>가격</th>
              <!-- <th>업데이트일</th> -->
            </tr>
          </thead>
          <tbody id="data-table">
          {product_list(cat,gen,q,page)}
            <!-- 추후 크롤링한 데이터가 들어가는 자리 -->
          </tbody>
        </table>
      </div>
      {product_cnt(cat, gen, q)}
      <!-- 페이지 네이션 코드를 넣어주세요 -->
      <nav aria-label="Page navigation example">
        <ul class="pagination justify-content-center" id="pagination" value="">
        </ul>
      </nav>
      <div class="author_link">
        <a href="https://github.com/lss018000/git_study/tree/main/oz_project/Admin%ED%8E%98%EC%9D%B4%EC%A7%80%EB%A7%8C%EB%93%A4%EA%B8%B0" target="_blank" class="git_link"><i class="bi bi-github"></i> lss018000 Github</a>
      </div>
    </div>
    <!-- <script src="https://pyscript.net/alpha/pyscript.js"></script> -->
    <script src="static/admin.js"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.1/dist/js/bootstrap.bundle.min.js" integrity="sha384-HwwvtgBNo3bZJJLYd8oVXjrBZt8cqVSpeBNS5n7C8IVInixGAoxmnlMuBnhbgrkm" crossorigin="anonymous"></script>
  </body>
</html>'''

@app.route('/delete')
def delete_product():
    # del_datas = []
    del_datas = request.args.get('del', "")
    del_datas = del_datas.split(',')
    cursor = connection.cursor()
    sql = "DELETE FROM products WHERE id = %s"
    for del_data in del_datas:
        cursor.execute(sql, del_data)
        connection.commit()
    cursor.close()
    return redirect('/')
    # return del_datas;

if __name__ == '__main__':
    app.run(debug=True)