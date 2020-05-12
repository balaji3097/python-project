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
		 console.log(sticky['top'],"sticky_count");
		 var dummy=$(window).scrollTop();
		 console.log(dummy,"windowsize");
		 var topview=sticky['top'];
		if(  dummy > 370)
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

	
	// Activate Carousel
	$("#myCarousel").carousel();
	  
	// Enable Carousel Indicators
	$(".item1").click(function(){
	  $("#myCarousel").carousel(0);
	});
	$(".item2").click(function(){
	  $("#myCarousel").carousel(1);
	});

	
	  

 
});







