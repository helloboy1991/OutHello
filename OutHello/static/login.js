
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

	function HiddenWelcom() {
		$("#welcome-panel").hide();
	}

	$("#search-input").click(function(){
		$("#search-input").val("");
	});

	ShowTime();
	// window.setTimeout(HiddenWelcom, 2000);
}