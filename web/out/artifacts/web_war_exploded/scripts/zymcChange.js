$(document).ready(
	function(){
		$("#mllb").change(function(){
			var selecter=document.getElementById("mllb");
			var subject=selecter.options[selecter.selectedIndex].value;
			var data={};
			data['subject']=subject;
			$.ajax({
				type:"POST",
				url:"MajorChangeServlet",
				data:JSON.stringify(data),
				contentType:'application/json;charset=UTF-8',
				success:function(data){
					//addselect(data);
				}
			});		//发送ajax
		});
	}
);
/*
function addselect(data){
	var options=data.split(" ");	//得到专业名称的集合
	var select=document.getElementById("zymc");		//得到专业名称的select标签
	$("#zymc").empty();		//调用jquery对select标签清空
	for(var i=0;i<options.length;i++){
		var newElement=document.createElement("option");
		var elementText=document.createTextNode(options[i]);
		newElement.appendChild(elementText);
		newElement.value=options[i];
		select.appendChild(newElement);
	}
}
*/

