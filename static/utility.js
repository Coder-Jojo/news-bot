function submitData() {
	var obj = {};
	obj.search_val = $("#Search").val();

	var json = JSON.stringify(obj);
	var xhr = new XMLHttpRequest();
	$("#output_div").empty();

	xhr.open("POST", "/submitJSON", true);
	xhr.setRequestHeader("Content-type", "application/json; charset=utf-8");
	xhr.onload = function () {
	    $("#output_div").empty();
		$("#output_div").append(xhr.response);
//		$("#car3").append("<img class=\"img-fluid w-100\" src=\"static/img/news-500x280-3.jpg\" style=\"object-fit: cover;\">")
		// // $('#output_div').val(xhr.response)
		window.scrollBy(0, 700);

		if (xhr.readyState == 4 && xhr.status == "200") {
		} else {
		console.log("not ok");
		}
		
	};
	xhr.send(json);
}

function loadText() {
    console.log("working load text");
    var xhr = new XMLHttpRequest();
    var json = JSON.stringify({"hell": "0"});
    xhr.open("POST", "/loadNews", true);
	xhr.setRequestHeader("Content-type", "application/json; charset=utf-8");
	xhr.onload = function () {
	    console.log("yes")
//		$("#carousel-hehe").append(xhr.response);
        var obj = jQuery.parseJSON(xhr.response);
		$("#car_test1").append(obj[1]);
		$("#car_test2").append(obj[2]);
		$("#car_test3").append(obj[3]);
		$("#car_test4").append(obj[4]);
		$("#car_test5").append(obj[5]);
		$("#car_test6").append(obj[6]);
		$("#car_test7").append(obj[7]);
//		$("#output_div").append(obj[0]);
//		console.log(obj[0])

		window.scrollBy(0, 700);

		if (xhr.readyState == 4 && xhr.status == "200") {
		} else {
		console.log("not ok");
		}
	};
	xhr.send(json)
}

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