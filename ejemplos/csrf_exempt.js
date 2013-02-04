$.ajax({
	type:'POST',
	url:'/ajax/',
	data:'usuario=1213213',
	success: function(test){
		alert(test);
	}
});