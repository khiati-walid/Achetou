/************************for incrementing the number pf products in a the basket*********************************/
var counter=0;
function count()
{
  $('.show').addClass("notification");
            $(".show").html(counter);
}
 $('.add').on('click',function(){
      counter++
      count();
 });
    

/********************************************for the message after adding a product to cart*******************/
function launch_toast() {
    var x = document.getElementById("toast")
    x.className = "appear";
    setTimeout(function(){ x.className = x.className.replace("appear", ""); }, 5000);
}
/******************************************************************************************************************/
function addAndBuy(){
	launch_toast();
	
}


