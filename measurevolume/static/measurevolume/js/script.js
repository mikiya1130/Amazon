// TODO
// videoサイズ
// エラーメッセージ表示について
//     -> alert表示 or 画像下部にメッセージを表示

window.onload = function Init(){
	startVideo();
}

//document.getElementById('error_message').innerHTML = "test message";
//document.getElementById('volume').innerHTML = "test volume";

// 0.5秒ごとにスマホの向き判定
// 横向きならデータをサーバへ送信
// TODO: captureボタンのみにするべき？
setInterval(() => {
	let isVertical = orientCheck();
	if(isVertical === false){
		takePicture();
	}else{
		displayMessage = "画面を横向きにしてください"
		// 画面表示
		// document.getElementById('error_message').innerHTML = displayMessage;
		// アラート表示
		alert(displayMessage)
	}
}, 500);

// 画面の向きを判定
function orientCheck(){
    if (window.innerHeight > window.innerWidth) {
        /* 縦画面時の処理 */
		return false;

    } else {
        /* 横画面時の処理 */
		return true;
    }
};

// デフォルトでリアカメラを起動
// 無い場合はフロントカメラを起動
// カメラがない場合はアラートを出す
function startVideo() {
	navigator.mediaDevices.getUserMedia({video: {
		facingMode: { exact: "environment" }    // リアカメラ
	  　}, audio: false})
	.then(function (stream) {
		document.getElementById('local_video').srcObject = stream;
	}).catch(function (error) { // 失敗時
		console.error('mediaDevice.getUserMedia() error:', error);
		console.log('There is not rear camera.')
		navigator.mediaDevices.getUserMedia({video: {
			facingMode: "user"    // フロントカメラ
		 　 }, audio: false})
		.then(function (stream) {
			document.getElementById('local_video').srcObject = stream;
		}).catch(function (error) {
			console.error('mediaDevice.getUserMedia() error:', error);
			alert('本体にカメラが付いていません。');
			return;
		});
		return;
	});
}

function takePicture() {
	let canvas = document.getElementById('canvas');	// videoのstreamをcanvasに書き出す方法.
  	let video = document.getElementById('local_video');
	let ctx = canvas.getContext('2d');
	let w = video.offsetWidth * 0.5;	// videoの横幅取得.
	let h = video.offsetHeight * 0.5;	// videoの縦幅取得.
	canvas.setAttribute("width", w);	// canvasに書き出すための横幅セット.
	canvas.setAttribute("height", h);	// canvasに書き出すための縦幅セット.
	ctx.drawImage(video, 0, 0, w, h);	// videoの画像をcanvasに書き出し.
	let base64 = canvas.toDataURL('image/jpg');	// canvas上の画像をbase64に変換.
	let picture = base64.replace(/^data:\w+\/\w+;base64,/, '');	// base64変換したデータのプレフィクスを削除.
    console.log(base64);
	transferData(picture);
}

function transferData(picture){
	$.ajax({
	    url: 'calc_volume',//転送先URL
		type: "post",
		data: {"img_base64": picture},
		contentType: "application/json; charset=UTF-8"
		/*
		success: function(){	// 転送成功時.
		console.log("success");
		},
		error: function (XMLHttpRequest, textStatus, errorThrown) {	// 転送失敗時.
			console.log("error");
		}
		*/
	}).done(function(data) {
		console.log("success");
		const obj = JSON.parse(data);
		const existGlass = obj.exist_glass;
		const existChopsticks = obj.exist_chopsticks;
		const volume = obj.volume;
		getData(existGlass, existChopsticks, volume);
	}).fail(function() {
		console.log("error");
	});
}

// データを受け取った後の処理
function getData(existGlass, existChopsticks, volume){
	let errorMessages = [];
	if(existGlass === false){
		errorMessages.push("コップを映してください");
	}
	if(existChopsticks === false){
		errorMessages.push("割りばしを映してください");
	}
	if(errorMessages.length === 0){
		document.getElementById('volume').innerHTML = volume;
	} else {
		let displayMessage = '';
		// リスト表示
		/* 
		displayMessage += '<ul style="list-style: none">';
		for (var i=0; i<errorMessages.length;i++){
			displayMessage += '<li>'+ errorMessages[i] + '</li>';
		}
		displayMessage += '</ul>';
		console.log(displayMessage)
		document.getElementById('error_message').innerHTML = displayMessage;
		*/
		// アラート表示
		for (var i=0; i<errorMessages.length;i++){
			displayMessage += errorMessages[i] + '\n';
		}
		alert(display_message)
	}
}