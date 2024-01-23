function question(a, n) {
    // 여기에서 코드 작성해주세요! 
    let result = [];


    for(let i = 0; i < a.length; i +=2){
        let temp = 0
        for(let j = 0; j < a[i].length; j++)
            if(a[i][j] == a[i+1]){
                temp += 1
            }
        result.push(temp)
    }
 
   
    return result ;
}

console.log(question([['h', 'a', 'p', 'p', 'y'], 'p',
                      ['h', 'e', 'l', 'l', 'o'], 'o',
                      ['c', 'h', 'r', 'i', 's', 't', 'm', 'a', 's'], 'a',
                      ['네', '잎', '클', '로', '버', '로', '버', '오', '버'], '버']))

/*
// 여기는 결과값 함수이므로 신경쓰지 않으셔도 됩니다!
Test(
    question,
    [
        [['h', 'a', 'p', 'p', 'y'], 'p'],
        [['h', 'e', 'l', 'l', 'o'], 'o'],
        [['c', 'h', 'r', 'i', 's', 't', 'm', 'a', 's'], 'a'],
        [['네', '잎', '클', '로', '버', '로', '버', '오', '버'], '버']
    ],
    [2, 1, 1, 3]
);

*/

let a = 0 % 2
console.log(a)
