function remove(event){
    event.target.remove()
}
$(document).ready(function () {
    $("button").bind("click", remove)
});