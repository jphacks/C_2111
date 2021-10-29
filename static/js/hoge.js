//csvをフロントで表示できるように読み込み

const output_csv = document.getElementById('color_list');

function csv_data(dataPath) {
    const request = new XMLHttpRequest(); // HTTPでファイルを読み込む
    request.addEventListener('load', (event) => { // ロードさせ実行
        const response = event.target.responseText; // 受け取ったテキストを返す
        csv_array(response); //csv_arrayの関数を実行
    });
    request.open('GET', dataPath, true); // csvのパスを指定
    request.send();
}

function csv_array(data) {
    const dataArray = []; //配列を用意
    const dataString = data.split('\n'); //改行で分割
    for (let i = 0; i < dataString.length; i++) { //あるだけループ
        dataArray[i] = dataString[i].split(',');
    }
    let insertElement = ''; //テーブルタグに表示する用の変数
    
    dataArray.forEach((element) => { //配列の中身を表示
        insertElement += '<tr>';
        element.forEach((childElement) => {
            insertElement += `<td>${childElement}</td>`
        });
        insertElement += '</tr>';
    });
    output_csv.innerHTML = insertElement; // 表示
}

csv_data('../static/js/test_data/lem.csv');
