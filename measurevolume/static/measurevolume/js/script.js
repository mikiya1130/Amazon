window.onload = function Init(){
	startVideo();
}

let isHorizontal = false;	// スマホが横向きならtrue
// 0.5秒ごとにスマホの向き判定
// 横向きならデータをサーバへ送信
setInterval(() => {
	orientCheck();
	if(isHorizontal === true){
		takePicture();
		transferData();
	}else{
		alert("画面を横向きにしてください")
	}
}, 500);

// 画面の向きを判定
function orientCheck(){
	//正面設定と現在の向きを取得
    var orientation = screen.orientation || screen.mozOrientation || screen.msOrientation;
    if (orientation.type === "portrait-primary" || orientation.type === "portrait-secondary") {
		isHorizontal = false;
    } else {
		isHorizontal = true;
    }
};

function startVideo() {
	navigator.mediaDevices.getUserMedia({video: true, audio: false})
	.then(function (stream) {
		document.getElementById('local_video').srcObject = stream;
	}).catch(function (error) { // 失敗時の処理はこちら.
		console.error('mediaDevice.getUserMedia() error:', error);
		return;
	});
}

function takePicture() {
	var canvas = document.getElementById('canvas');	// videoのstreamをcanvasに書き出す方法.
  	var video = document.getElementById('local_video');
	var ctx = canvas.getContext('2d');
	var w = video.offsetWidth * 0.5;	// videoの横幅取得.
	var h = video.offsetHeight * 0.5;	// videoの縦幅取得.
	canvas.setAttribute("width", w);	// canvasに書き出すための横幅セット.
	canvas.setAttribute("height", h);	// canvasに書き出すための縦幅セット.
	ctx.drawImage(video, 0, 0, w, h);	// videoの画像をcanvasに書き出し.
	var base64 = canvas.toDataURL('image/jpg');	// canvas上の画像をbase64に変換.
	var picture = base64.replace(/^data:\w+\/\w+;base64,/, '');	// base64変換したデータのプレフィクスを削除.
    console.log(base64);
	transferData(picture);
}

function transferData(picture){
	return $.ajax({
		url: 'calc_volume',//転送先URL
		type: "post",
		data: {"img_base64": picture},
		/*
		success: function(){	// 転送成功時.
		console.log("success");
		},
		error: function (XMLHttpRequest, textStatus, errorThrown) {	// 転送失敗時.
			console.log("error");
		}
		*/
	}).done(function(result) {
		console.log("success");
		const obj = JSON.parse(result);
		const exist_glass = obj.exist_glass;
		const exist_chopsticks = obj.exist_chopsticks;
		const volume = obj.volume;
		getData(exist_glass, exist_chopsticks, volume);
	}).fail(function(result) {
		console.log("error");
	});
}

// データを受け取った後の処理
function getData(exist_glass, exist_chopsticks, volume){
	let error_messages = [];
	if(exist_glass === false){
		error_messages.push("コップを映してください");
	}
	if(exist_chopsticks === false){
		error_messages.push("割りばしを映してください");
	}
	if(error_messages.length === 0){
		document.getElementById('volume').innerHTML = volume;
	} 

	else{
		let display_message = '';
		// リスト表示
		/* 
		display_message += '<ul style="list-style: none">';
		for (var i=0; i<error_messages.length;i++){
			display_message += '<li>'+ error_messages[i] + '</li>';
		}
		display_message += '</ul>';
		console.log(display_message)
		document.getElementById('error_message').innerHTML = display_message;
		*/
		// アラート表示
		for (var i=0; i<error_messages.length;i++){
			display_message += error_messages[i] + '\n';
		}
		alert(display_message)
	}
}