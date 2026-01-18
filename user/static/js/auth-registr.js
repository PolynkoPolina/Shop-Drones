let authRegistrModal = window.parent.document.getElementById('auth-registr-modal');
let openButton = window.parent.document.getElementById('auth-registr-button');
let closeButton = document.getElementById('close-auth-registr');
let backgroundBlurDiv = window.parent.document.querySelector('.background-blur-div');
let authLink = document.getElementById('auth-link');
let regisrtLink = document.getElementById('registr-link');
let logInLink = document.getElementById('log-in-link');
let arrayPasswordEyes = document.querySelectorAll(".password-eye")
// const form = document.querySelector('form');


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


function changeMosalSize(){
    if(authRegistrModal.style.height === '35rem'){
        authRegistrModal.style.height = '22rem';
    } else{
        authRegistrModal.style.height = '35rem';
    }
}


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


// fetch("/authorization", {
//     method: "POST",
//     body: new FormData(form)
// })

// .then(r => r.json())
// .then(data => {
//     if (data.message == 'is_authenticated'){
//         console.log(data.message);
//     }
// })