function formSubmit(){
	$(".btn").click(function(){
		$.ajax({
			type:'POST',
			url:'form',
			data:$("#form1").serialize(),
			success:function(result){
				addHtml(result);
			},
			error:function(){
				alert("异常！");
			}
		});
	});
}
function addHtml(data){
	
}