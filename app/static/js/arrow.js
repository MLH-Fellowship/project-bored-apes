var a;
function show_hide(){
    if (a == 1){
        document.getElementById("topnavbar").style.visibility="visible";
        document.getElementById("btnarrow").innerHTML="<span class='icon'><i class='fa-solid fa-angle-up'></i></span>";
        a = 0;
    } else {
        document.getElementById("topnavbar").style.visibility="hidden";
        document.getElementById("btnarrow").innerHTML="<span class='icon'><i class='fa-solid fa-angle-down'></i></span>";
        a = 1;
    }
}

