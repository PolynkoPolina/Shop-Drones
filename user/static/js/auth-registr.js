let authRegistrModal = window.parent.document.getElementById('auth-registr-modal');
let openButton = window.parent.document.getElementById('auth-registr-button');
let closeButton = document.getElementById('close-auth-registr');
let backgroundBlurDiv = window.parent.document.querySelector('.background-blur-div');
let authLink = document.getElementById('auth-link');
let regisrtLink = document.getElementById('registr-link');
let logInLink = document.getElementById('log-in-link');
let arrayPasswordEyes = document.querySelectorAll(".password-eye");
const changeSizeLinks = [ document.getElementById('auth-link'), document.getElementById('registr-link'), document.querySelector("#restore-password"), document.querySelectorAll(".cancel-button-rest-pass")[0], document.getElementById("log-in-link"), document.getElementsByClassName("reg-button")[0]];
let modalStatus = 'authorization';


openButton.addEventListener(
    'click',
    (event) =>{
        if (authRegistrModal.style.display === 'none'){
            authRegistrModal.style.display = 'flex';
            backgroundBlurDiv.style.display = 'flex';
        } 
        else{
            authRegistrModal.style.display= 'none';
            backgroundBlurDiv.style.display = 'none';
        }
    }
);
changeSizeLinks.forEach((button) => {
    if (button){
        button.addEventListener(
            'click',
            (event) => {
                let successBody = document.querySelectorAll(".success-body")[0];
                
                if(button.id == "auth-link" || button.className == 'cancel-button-rest-pass' || button.id == "log-in-link"){
                    modalStatus = 'authorization';
                } else if ( button.id == 'registr-link'){
                    modalStatus = 'registration';
                } else if (button.id == "restore-password"){
                    modalStatus = 'restore-password';
                } else if ( button.className == "reg-button" && successBody != undefined){
                    modalStatus = 'succesRegisrt';
                } else{
                    modalStatus = 'registration';
                }

                if(modalStatus == 'authorization'){
                    authRegistrModal.style.height = '22rem';
                    console.log(modalStatus)
                } else if( modalStatus == 'registration'){
                    authRegistrModal.style.height = '35rem';
                    console.log(modalStatus)
                    console.log(successBody)
                } else if (modalStatus == 'restore-password'){
                    authRegistrModal.style.height = '15rem';
                    console.log(modalStatus)
                } else if (  modalStatus == 'succesRegisrt'){
                    authRegistrModal.style.height = '12rem';
                    console.log(modalStatus)
                }
            }
        )
    }

});



function closeAuthRegistr(){
    authRegistrModal.style.display= 'none';
    backgroundBlurDiv.style.display = 'none';
};

for(let i=0; i < arrayPasswordEyes.length; i++){
    let inputObject = arrayPasswordEyes[i].parentElement.getElementsByTagName('input')[0];
    arrayPasswordEyes[i].addEventListener(
        'click',
        (event)=>{
            if(inputObject.type !='text'){
                inputObject.type ='text';
                arrayPasswordEyes[i].style.backgroundImage = 'url(user/static/icon/eye-show.svg)';
            } else{
                inputObject.type ='password';
                arrayPasswordEyes[i].style.backgroundImage = ' url(user/static/icon/eye-not-show.svg)';
            }
        }
    )
}
