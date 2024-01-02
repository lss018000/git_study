     // 현재 시간 값을 저장할 객체
     var currentTime = {
        days: null,
        hours: null,
        minutes: null,
        seconds: null,
      };

      // 페이드 아웃 효과를 위한 함수
      function fadeOutEffect(element) {
        element.classList.add("fade-effect");
      }

      // 페이드 인 효과를 위한 함수
      function fadeInEffect(element) {
        element.classList.remove("fade-effect");
      }

      // 카운트다운 타이머 시작 함수
      function startTimer(endDate) {
        // 지정된 매초마다 실행되는 함수
        var interval = setInterval(function () {
          var now = new Date().getTime(); // 현재 시간을 밀리초로 가져옴
          var distance = endDate - now; // 종료 시간까지 남은 밀리초 계산

          // 남은 시간을 일, 시, 분, 초로 계산
          // 이 부분은 남은 시간을 각각의 단위로 변환합니다.
          var days = Math.floor(distance / (24 * 60 * 60 * 1000));
          var hours = Math.floor((distance % (24 * 60 * 60 * 1000)) / (60 * 60 * 1000));
          var minutes = Math.floor((distance % (60 * 60 * 1000)) / (60 * 1000));
          var seconds = Math.floor((distance % (60 * 1000)) / 1000);

          // 각 시간 단위가 변경되었는지 확인하고, 변경된 경우에만 업데이트 및 애니메이션 적용
          updateWithFadeEffect("days", days, "days");
          updateWithFadeEffect("hours", hours, "hours");
          updateWithFadeEffect("minutes", minutes, "minutes");
          updateWithFadeEffect("seconds", seconds, "seconds");

          // 타이머가 0에 도달하면 종료
          if (distance < 0) {
            clearInterval(interval); // 타이머 중지
            document.getElementById("timer").textContent = "시간이 만료되었습니다!";
          }
        }, 1000); // 1000 밀리초(1초) 간격으로 반복
      }

      // 숫자 업데이트 및 페이드 효과 적용
      function updateWithFadeEffect(id, value, timeUnit) {
        var element = document.getElementById(id);
        var newValue = value < 10 ? "0" + value : value;

        if (newValue !== currentTime[timeUnit]) {
          fadeOutEffect(element);
          setTimeout(() => {
            element.textContent = newValue;
            fadeInEffect(element);
          }, 300); // 페이드 아웃 지속 시간에 맞춰 업데이트
          currentTime[timeUnit] = newValue;
        }
      }

      let sel_datetime = document.getElementById('sel_datetime');
      sel_datetime.addEventListener("change", function(){
        let endDate = new Date(sel_datetime.value).getTime();
        startTimer(endDate); // 타이머 시작

        // alert(sel_datetime_val);
      })
      document.getElementById('sel_datetime').min= new Date().toISOString().slice(0,-1);
      // 타이머 종료 날짜, 시간 설정
    //   var endDate = new Date(2023, 11, 31, 23, 59, 59).getTime(); // 월은 0부터 시작하므로 11은 12월을 의미합니다.
