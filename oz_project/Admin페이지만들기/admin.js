const urlStr = window.location.href;
const url = new URL(urlStr);
const urlParams = url.searchParams;
const cat = urlParams.get('cat');
const URLSearch = new URLSearchParams(location.search);

if(cat == '64'){
  cat_text = '상의';
} else if(cat == '65'){
  cat_text = '하의';
} else if(cat == '34'){
  cat_text = '신발';
} else if(cat == '7'){
  cat_text = '패션잡화';
} else {
  cat_text = '';
}
const gen = urlParams.get('gen');
if(gen == 'men'){
  gen_text = '남자';
}else if(gen == 'women'){
  gen_text = '여자';
}else{
  gen_text = '';
}
const search_text = urlParams.get('q');
let page = Number(urlParams.get('page'));
if(page){ } else { page = 1; }

const catselect = document.getElementById('catselect'); 
const catsel_len = catselect.options.length; 
for (let i=0; i<catsel_len; i++){  
  if(catselect.options[i].value == cat){
    catselect.options[i].selected = true;
  }
}  
const sexselect = document.getElementById('sexselect'); 
const sexsel_len = sexselect.options.length; 
for (let i=0; i<sexsel_len; i++){  
  if(sexselect.options[i].value == gen){
    sexselect.options[i].selected = true;
  }
}  
const q = document.getElementById('search_text'); 
q.value = search_text;

// 크롤링한 데이터를 아래와 같은 형태의 객체 배열로 가정합니다.
$(document).ready(function() {
  $("#catselect").on("change", function(){
    //selected value
    $(this).val();
    const cat_val = $("option:selected", this).attr("value");
    const URLSearch = new URLSearchParams(location.search);
    URLSearch.set('cat', String(cat_val));
    URLSearch.set('page', '1');
    const newParam = URLSearch.toString();
    window.open(location.pathname + '?' + newParam, '_self');
  });
  $("#sexselect").on("change", function(){
    const sex_val = $("option:selected", this).attr("value");
    URLSearch.set('gen', String(sex_val));
    URLSearch.set('page', '1');
    const newParam = URLSearch.toString();
    window.open(location.pathname + '?' + newParam, '_self');
  });
  const Url = './json_data/kream_data_total.json';
    $.ajax({
      url: Url,
      type: "GET",
      async: false,
      contentType: 'application/json; charset=utf-8',
      dataType:"json",
      success: function(result) {
        console.log(result.length);
        let product_cnt = 0;
        let page_no_cnt = 1;
        result.forEach((item) => {
          const compare_title = item.product;
          if(cat){
            if((item.category == cat_text) && ((item.sex == gen_text) || (item.sex == '남자/여자'))){
              if(search_text){
                if((compare_title.indexOf(search_text) != -1) && (item.category == cat_text) && ((item.sex == gen_text) || (item.sex == '남자/여자'))){
                  row_html(item, product_cnt);
                  product_cnt++;
                }
              } else {
                row_html(item, product_cnt);
                product_cnt++;
              }  
            }
          } else {
            if(search_text){
              if(compare_title.indexOf(search_text) != -1){
                row_html(item, product_cnt);
                product_cnt++;
              }
            } else {
              row_html(item, product_cnt);
              product_cnt++;
            }
          }
        });
        document.getElementById('max_page').value = product_cnt;
      },
      error:function(error) {
        console.log(`Error ${error}`)
      },
    })
    const max_page = document.getElementById('max_page').value;
    const pagination = document.getElementById('pagination');
    const page_cnt = Math.round(max_page / 20);
    if(page == 1){
      let temp = '<li class="page-item disabled"><a class="page-link" href="#" onclick="callFunction('+(page-1)+');">Previous</a></li>';
      $('.pagination').append(temp);
    } else {
      let temp = '<li class="page-item"><a class="page-link" href="#" onclick="callFunction('+(page-1)+');">Previous</a></li>';
      $('.pagination').append(temp);
    }
    for(let j = 1; page_cnt+1 > j; j++){
      if(page == j){
        temp = '<li class="page-item"><a class="page-link active" href="#" onclick="callFunction('+j+');">'+j+'</a></li>';
        $('.pagination').append(temp);
      } else {
        temp = '<li class="page-item"><a class="page-link" href="#" onclick="callFunction('+j+');">'+j+'</a></li>';
        $('.pagination').append(temp);
      }
    }
    if(page == page_cnt){
      temp = '<li class="page-item disabled"><a class="page-link" href="#" onclick="callFunction('+(page+1)+');">Next</a></li>';
      $('.pagination').append(temp);
    } else {
      temp = '<li class="page-item"><a class="page-link" href="#" onclick="callFunction('+(page+1)+');">Next</a></li>';
      $('.pagination').append(temp);
    }

    function row_html(item, product_cnt){
      if((product_cnt < page * 20) && (product_cnt >= page * 20 - 20)){
        const dataTable = document.getElementById('data-table');
        const row = dataTable.insertRow();
        row.insertCell(0).innerHTML = '<input type="checkbox">'
        row.insertCell(1).innerHTML = item.category;
        row.insertCell(2).innerHTML = item.sex;
        row.insertCell(3).innerHTML = item.brand;
        row.insertCell(4).innerHTML = '<span>'+item.product+'</span><a href="https://kream.co.kr'+item.url+'" target="_blank" class="product_link">상품확인</a>';
        row.insertCell(5).innerHTML = item.price;
        //row.insertCell(6).innerHTML = item.update;
      }
    }

})
// 추후 데이터베이스에 있는 데이터를 쿼리문으로 불러 올 수 있게 쿼리르 작성해 볼 수 있음

function callFunction(obj) {
  URLSearch.set('page', String(obj));
  const newParam = URLSearch.toString();
  window.open(location.pathname + '?' + newParam, '_self');
}
let today = new Date();   
let year = today.getFullYear(); // 년도
let month = today.getMonth() + 1;  // 월
let date = today.getDate();  // 날짜
let day = today.getDay();  // 요일

const now_date = document.getElementById('now_date');

now_date.textContent = year + '/' + month + '/' + date;

const search_btn = document.getElementById('search');
const del_btn = document.getElementById('sel_del');

del_btn.addEventListener('click', function(){
  if(confirm('삭제할까요?')){
    let xhttp = new XMLHttpRequest();
    xhttp.open("GET", "./json_data/kream_data_total.json", true);
    xhttp.onreadystatechange = function() {
      if(this.readyState == 4 && this.status == 200) {
        let storage = JSON.parse(this.response);
        // console.log(storage);
        for(i in storage){
          console.log(storage.length);
        }

      }
    };
    xhttp.send();

    alert("삭제되었습니다.");
  } else {
    alert("삭제가 취소되었습니다.");
  }
})


const json_file = new File(["data"], "/Users/devhypnos_i9_64g/Desktop/Git/oz_project/Admin페이지만들기/json_data/kream_data_total.json");
// console.log(json_file);
const creationDate = new Date(json_file.lastModified);
let file_y = creationDate.getFullYear(); // 년도
let file_m = creationDate.getMonth() + 1;  // 월
let file_d = creationDate.getDate();  // 날짜

const file_date = document.getElementById('update_date');

file_date.textContent = file_y + '/' + file_m + '/' + file_d;

console.log(creationDate); // Fri Jan 20 2023 00:00:00 GMT+0900


