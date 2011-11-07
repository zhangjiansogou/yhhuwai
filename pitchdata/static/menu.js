$(function(){
	var span = '<span></span>';
	$('.menu li a').wrapInner(span);
	$('.menu_content ul:gt(0)').hide();
	
	var menu_li = $('.menu li');
	
	$('.menu li').mouseover(function(){
		$(this).addClass('selected')
			   .siblings().removeClass('selected');
		
		var index = menu_li.index(this);
		$('.menu_content ul').eq(index).show()
							 .siblings().hide();
		
		return false;
	});
	
	
});