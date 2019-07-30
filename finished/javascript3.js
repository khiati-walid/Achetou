//script for categories and subcategories
//----------------------------------------------------------------

var subcategory = {
    MODE: ["Vêtements femme","Vêtements homme","Chaussures femme","Chaussures homme","Accessoire femme","Accessoire homme"],
    ELÉCTROMÉNAGER: ["Télévisions","Appareil photo","Audio","Accessoires TV","Caméras"],
    BEAUTÉ: ["Maquillage","Parfum","Cheveux","Coiffure","Soin"],
    INFORMATIQUE: ["Ordinateurs","Téléphones","Tablettes","Périphériques","Imprimantes","Scanners"],
    LIFESTYLE: ["Sports,Fitness","Musique","Accessoires"],
    AUTRES: ["Bébé,puériculture","Jeux,jouets"]
}

function makeSubmenu(value) {
    if (value.length == 0) document.getElementById("categorySelect").innerHTML = "<option></option>";
    else {
        var citiesOptions = "";
        for (categoryId in subcategory[value]) {
            citiesOptions += "<option>" + subcategory[value][categoryId] + "</option>";
        }
        document.getElementById("categorySelect").innerHTML = citiesOptions;
    }
}

function displaySelected() {
    var country = document.getElementById("category").value;
    var city = document.getElementById("categorySelect").value;
    alert(country + "\n" + city);
}

function resetSelection() {
    document.getElementById("category").selectedIndex = 0;
    document.getElementById("categorySelect").selectedIndex = 0;
}
//script for drop image    
//----------------------------------------------------------------------------

$(document).ready( function() {
        $(document).on('change', '.btn-file :file', function() {
        var input = $(this),
            label = input.val().replace(/\\/g, '/').replace(/.*\//, '');
        input.trigger('fileselect', [label]);
        });

        $('.btn-file :file').on('fileselect', function(event, label) {
            
            var input = $(this).parents('.input-group').find(':text'),
                log = label;
            
            if( input.length ) {
                input.val(log);
            } else {
                if( log ) alert(log);
            }
        
        });
        function readURL(input) {
            if (input.files && input.files[0]) {
                var reader = new FileReader();
                
                reader.onload = function (e) {
                    $('#img-upload').attr('src', e.target.result);
                }
                
                reader.readAsDataURL(input.files[0]);
            }
        }

        $("#imgInp").change(function(){
            readURL(this);
        });     
    });