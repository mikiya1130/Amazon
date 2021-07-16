// 変更点
// 縦横判定の関数を削除. setInterval()のif文で直接判定
// videoのサイズ取得->840超えなら縮小

let doneProcess = true;	// 計算処理が終了しているか判定

window.onload = function Init(){
	startVideo();
}
// デフォルトでリアカメラを起動
// 無い場合はフロントカメラを起動
// カメラがない場合はアラートを出す
function startVideo() {
	navigator.mediaDevices.getUserMedia({video: {
			facingMode: { exact: "environment" }    // リアカメラ
		}, audio: false})
		.then(function (stream) {
			document.getElementById('local_video').srcObject = stream;
		}).catch(function (error) {
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

// 0.5秒ごとにスマホの向き判定
// 横向きならデータをサーバへ送信
setInterval(() => {
	if(window.innerHeight < window.innerWidth){
		
		if(doneProcess===true){
			takePicture();
			doneProcess = false;
		}
		//takePicture();
	}else{
		displayMessage = "画面を横向きにしてください"
		alert(displayMessage)
	}
}, 1000);


function takePicture() {
	let canvas = document.getElementById('canvas');	// videoのstreamをcanvasに書き出す方法.
	let video = document.getElementById('local_video');
	let ctx = canvas.getContext('2d');
	let originalWidth = video.offsetWidth;
	let originalHeight = video.offsetHeight;
	let width, height;
	if (originalWidth <= 840) {
		width = originalWidth;
		height = originalHeight;
	} else {
		width = 840;
		height = 840 * (originalHeight/originalWidth);
	}
	canvas.setAttribute("width", width);	// canvasに書き出すための横幅セット.
	canvas.setAttribute("height", height);	// canvasに書き出すための縦幅セット.
	ctx.drawImage(video, 0, 0, width, height);	// videoの画像をcanvasに書き出し.
	let base64 = canvas.toDataURL('image/jpg');	// canvas上の画像をbase64に変換.
	let picture = base64.replace(/^data:\w+\/\w+;base64,/, '');	// base64変換したデータのプレフィクスを削除.
	transferData(picture);
}

function transferData(picture){
	$.ajax({
		url: 'calc_volume/',//転送先URL
		type: "post",
		headers: { "X-CSRFToken": getCookie("csrftoken") },
		data:
			JSON.stringify({
				"img_base64": picture,
			}),
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
		const existGlass = data.exist_glass;
		const existChopsticks = data.exist_chopsticks;
		const volume = data.volume;
		getData(existGlass, existChopsticks, volume);
	}).fail(function() {
		console.log("error");
	});
}

// データを受け取った後の処理
function getData(existGlass, existChopsticks, volume){
	doneProcess = true;
	let errorMessages = [];
	if(existGlass === false){
		errorMessages.push("コップを映してください");
	}
	if(existChopsticks === false){
		errorMessages.push("割りばしを映してください");
	}
	if(errorMessages.length === 0){
		// volumeの表示を生成
		let ratio = 0.095;
		let volumeSize = Math.round(window.innerHeight * ratio);
		if(document.getElementById('volume')){
			document.getElementById('volume').remove();
		}
		let volumeWrapperElement = document.getElementById('volume_wrapper');
		let volumeElement = document.createElement('div');
		let volumeSizeStr = 'font-size:'+String(volumeSize)+'px;';
		volumeElement.setAttribute('style', volumeSizeStr);
		volumeElement.setAttribute('id', 'volume');
		volumeElement.innerHTML = Math.round(volume) + 'ml';
		volumeWrapperElement.appendChild(volumeElement);
		/*
		// HTMLの要素に書き込む場合
		// 四捨五入
		document.getElementById('volume').innerHTML = Math.round(volume) + 'ml';
		*/
		
	} else {
		let displayMessage = '';
		// アラート表示
		for (var i=0; i<errorMessages.length;i++){
			displayMessage += errorMessages[i] + '\n';
		}
		alert(displayMessage)
	}
}

function getCookie(name) {
	let cookieValue = null;
	if (document.cookie && document.cookie !== '') {
		const cookies = document.cookie.split(';');
		for (let i = 0; i < cookies.length; i++) {
			const cookie = cookies[i].trim();
			if (cookie.substring(0, name.length + 1) === (name + '=')) {
				cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
				break;
			}
		}
	}
	return cookieValue;
}
