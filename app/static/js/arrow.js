var a;
function show_hide(){
    if (a == 1){
        document.getElementById("topnavbar").style.visibility="visible";
        document.getElementById("grnav").className="navbar";
        document.getElementById("btnarrow").innerHTML="<span class='icon'><i class='fa-solid fa-angle-up'></i></span>";
        return a=0;
    } else {
        document.getElementById("topnavbar").style.visibility="hidden";
        document.getElementById("grnav").className="is-transparent";
        document.getElementById("btnarrow").innerHTML="<span class='icon'><i class='fa-solid fa-angle-down'></i></span>";
        return a=1;
    }
}