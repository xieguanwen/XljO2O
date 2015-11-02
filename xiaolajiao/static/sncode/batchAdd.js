$(function(){
    $("form").on("submit",function(event){
        if($("#uploadBatchAdd").val().split('.')[1] != 'csv') {
            $("#help").addClass("alert-danger")
            return false;
        }
    });
});