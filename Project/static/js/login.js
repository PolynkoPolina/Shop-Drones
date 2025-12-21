let logIn = document.getElementById("login-modal");


function openLogIn(){
    if (logIn.style.display === 'none'){
        logIn.style.display= 'flex';
    } 
    else{
        logIn.style.display= 'none';
    }
};

function closeLogIn(){
    logIn.style.display= 'none';
};
