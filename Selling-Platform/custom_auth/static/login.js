function validate_form(){
    event.preventDefault();
    if (validatingPassword())
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
