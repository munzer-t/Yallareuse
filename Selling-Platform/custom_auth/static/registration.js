function validate_form(){
    event.preventDefault();
    if (validatePassword())
        if (validateUserType())
            return true;

    return false;
}

function validatingPassword(){
    var password = document.getElementById("password").value;
    var passError = document.getElementById("passwordError");

    if (password.length < 6){
        passError.textContent = "Password must be at least 6 characters";
        passError.style.color = "red";
        document.getElementById("password").style.borderColor = "red";
        return false;
    }
    else{
        passError.textContent = "Looks Good!";
        passError.style.color = "green";
        document.getElementById("password").style.borderColor = "green";
        return true;
    }

}


function validatingRepeatPassword(){
    var password1 = document.getElementById("password").value;
    var password = document.getElementById("repeatPassword").value;
    var passError = document.getElementById("repeatPasswordError");

    if (password.length < 6){
        passError.textContent = "Password must be at least 6 characters";
        passError.style.color = "red";
        document.getElementById("repeatPassword").style.borderColor = "red";
        return false;
    }
    else if (password !== password1){
        passError.textContent = "Password must be same as above";
        passError.style.color = "red";
        document.getElementById("repeatPassword").style.borderColor = "red";
        return false;
    }
    else{
        passError.textContent = "Passowrd Matched";
        passError.style.color = "green";
        document.getElementById("repeatPassword").style.borderColor = "green";
        return true;
    }

}
  
function validatePassword(){
    if (validatingPassword())
        if (validatingRepeatPassword())
            return true;
        else return false;
    else
        return false;
}

function validateUserType(){

    var selectElement = document.getElementById("userSelection");
    var selectedIndex = selectElement.selectedIndex;
    if (selectedIndex === 0){
        document.getElementById("errorUserSelection").textContent = "Please select a user type.";
        document.getElementById("errorUserSelection").style.color="red";
    }
    else{
        document.getElementById("errorUserSelection").textContent = "";
        return true;
    }
    return false;
}