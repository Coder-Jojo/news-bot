// function submitData() {
// 	var obj = {};
// 	obj.secret_key = $("#secret_key").val();
// 	obj.audio_ = $("#audio_").val();

// 	var json = JSON.stringify(obj);
// 	var xhr = new XMLHttpRequest();

// 	xhr.open("POST", "/submitJSON1_", true);
// 	xhr.setRequestHeader("Content-type", "application/json; charset=utf-8");
// 	xhr.onload = function () {
// 		$("#output_div").append(xhr.response);
// 		// // $('#output_div').val(xhr.response)
// 		window.scrollBy(0, 700);

// 		if (xhr.readyState == 4 && xhr.status == "200") {
// 		} else {
// 		console.log("not ok");
// 		}
		
// 	};
// 	xhr.send(json);
// }

// function submitData1() {
// 	var obj = {};
// 	obj.secret_key = $("#secret_key").val();
// 	obj.encrypted_text = $("#encrypted_text").val();
// 	obj.par_text = $("#par_text").val();

// 	var json = JSON.stringify(obj);
// 	var xhr = new XMLHttpRequest();

// 	xhr.open("POST", "/submitJSON2_", true);
// 	xhr.setRequestHeader("Content-type", "application/json; charset=utf-8");
// 	xhr.onload = function () {
// 		$("#output_div").append(xhr.response);
// 		// // $('#output_div').val(xhr.response)
// 		window.scrollBy(0, 700);

// 		if (xhr.readyState == 4 && xhr.status == "200") {
// 		} else {
// 		console.log("not ok");
// 		}
		
// 	};
// 	xhr.send(json);
// }