var a;
function show_hide(){
    if (a == 1){
        document.getElementById("topnavbar").style.display="block";
        return a=0;
    } else {
        document.getElementById("topnavbar").style.display="none";
        return a=1;
    }
}