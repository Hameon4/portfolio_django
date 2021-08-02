function scrollUp(){
    const btnScrollUp = document.getElementById("btnScrollUp");
    btnScrollUp.addEventListener("click", function() {//Gotta Check this out!!!!!!
    //window.scrollTo(0, 0);

    window.scrollTo ({top:0, left:0, behaviour:"smooth"});

    //$("html, body").animate({scrollTop: 0}, "slow");
    });
}