$(document).ready(function()
{

$(document).on('scroll', function()
	{
		setHeader();
	});
	
	function setHeader()
	{
		//alert("enter");
		var header=$("#myHeader");
		 var sticky = header.offset();
		 console.log(sticky,"sticky_count");
		 var dummy=$(window).scrollTop();
		 console.log(dummy,"windowsize");
		if($(window).scrollTop() > 430)
		{
			console.log("fixed");
			header.addClass('sticky');
			
		}
		else
		{
			console.log("not fixed");
			header.removeClass('sticky');
		}
	}
	
});