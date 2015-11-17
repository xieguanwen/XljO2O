$(function(){
    $("form").on("submit",function(event){
        console.log($(this).find("select").val());
        if($(this).find("select").val() == 0){
            $("#help").addClass("alert-danger").html("请选择代理商");
            return false;
        }
        if($("#uploadBatchAdd").val().split('.')[1] != 'csv') {
            $("#help").addClass("alert-danger");
            return false;
        }
    });
});