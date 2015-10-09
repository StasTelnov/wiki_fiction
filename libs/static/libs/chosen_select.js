(function(){
    $(document).ready(function() {
        $(".chosen-select").chosen();

        // Bootstrap theme for inputs
        var
            $formGroup = $('#tags_chosen').closest(".form-group "),
            $chosenChoices = $('#tags_chosen').find("ul.chosen-choices");

        if($formGroup.hasClass("has-error")){
            $chosenChoices.css("border-color","#a94442");
        } else if($formGroup.hasClass("has-success")){
            $chosenChoices.css("border-color","#3c763d");
        }
    });
})();
