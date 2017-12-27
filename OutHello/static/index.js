
function toNum(num) {
	if (num<10) {
		return '0'+num;
	} else {
		return num;
	}
}

window.onload = function() {
	function ShowTime() {
		var time = new Date()
		var time_str = toNum(time.getHours())+':'+toNum(time.getMinutes())+':'+toNum(time.getSeconds());
		document.getElementById("header-time").innerText = time_str;

		setTimeout(ShowTime, 1000);
	}

	window.setTimeout(ShowTime, 1000);
}