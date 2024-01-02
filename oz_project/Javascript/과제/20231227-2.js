/*
 * ❗️❗️ 필독 ❗️❗️
 * - 함수 블록 내부에만 작성해주세요.
 * - 결과값을 return 하세요.
 * - 추가적인 test가 필요한 경우에는 기존 test 코드 밑에 추가해주세요.
 * - 코드 실행 시 모든 테스트가 true인 경우 통과입니다!
 */

/*  문제 출제
 *  자연수 n이 인수로 주어질 때, n을 나눠 나머지가 1이 되는 가장 작은 자연수를 구하는 함수를 구현해보세요!
 *
 *
 *
 *
 */

function question(n) {
    // 여기에서 코드 작성해주세요!
    let result;
    // let j = 0;
    let result_array = [];
    for(let i = 1;i < n; i++){
        if(n % i == 1){
            result_array.push(i);
            // result_array[j] = i;
            // j++;
        } else {

        }
    }
    result = Math.min.apply(null, result_array);
    // result = Math.min(result_array);
    console.log(result);
    return result;
}

// 여기는 결과값 함수이므로 신경쓰지 않으셔도 됩니다!
Test(question, [[10], [12]], [3, 11]);

function Test(question, conditions, results) {
    for (let index in results) {
        const result = question(...conditions[index]) === results[index];
        console.log(`테스트 ${+index + 1}`, result);
        if (!result) {
            console.log('테스트에 통과하지 못했습니다.');
            return;
        }
    }

    console.log('테스트에 통과하셨습니다!');
}