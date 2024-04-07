const fs = require('fs')

fs.readFile('number_one.txt', 'utf8', (err, data) => {
    if(err){
        console.log('error', err)
        return;
    }
    console.log('data:', data)
})

let content = 'hello'
fs.writeFile('number_four.txt', content, (err) => {
    if(err){
        console.log('error', err)
        return;
    }
    console.log('쓰기 완료')
})

content = 'hello stranger'
fs.appendFile('newfile.txt', content, (err) => {
    if(err){
        console.log('error', err)
        return;
    }
    console.log('생성 및 쓰기 완료')
})


content = 'hello stranger again'
fs.appendFile('newfile.txt', content, (err) => {
    if(err){
        console.log('error', err)
        return;
    }
    console.log('생성 및 쓰기 완료')
})