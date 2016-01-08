$(function(){
    $("form").on("submit",function(event){
        if($(this).find("select").val() == 0){
            $("#help").addClass("alert-danger").html("请选择代理商");
            return false;
        }
        console.log($("#uploadBatchAdd").val().split('.')[1]);
        if(!($("#uploadBatchAdd").val().split('.')[1] == 'csv' || $("#uploadBatchAdd").val().split('.')[1] == 'txt')) {
            $("#help").addClass("alert-danger");
            return false;
        }
    });
});