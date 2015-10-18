(function(){
    $(document).ready(function() {
        $(".chosen-select").chosen();

        // Bootstrap theme for chosen inputs
        var
            $chosenChoices = $("ul.chosen-choices"),
            $formGroup = $chosenChoices.closest(".form-group ");

        if($formGroup.hasClass("has-error")){
            $chosenChoices.css("border-color","#a94442");
        } else if($formGroup.hasClass("has-success")){
            $chosenChoices.css("border-color","#3c763d");
        }
    });
})();
