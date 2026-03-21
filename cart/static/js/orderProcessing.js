const arrayAddressInpt = Array.from(document.querySelectorAll('.radio-inpt-delivery'));
const cart = document.getElementById('cart-modal');
const arrayPaymentInpt = Array.from(document.querySelectorAll('.radio-inpt-payment'));
const backgroundBlurDiv = window.parent.document.querySelector('.background-blur-div');


arrayAddressInpt.forEach(
    input => {
        input.addEventListener(
            'change',
            ()=> {
                arrayAddressInpt.forEach(inpt => {
                const parent = inpt.closest('.address');
                parent.classList.add('closed');
                parent.classList.remove('openned');
                });
    
            const parent = input.closest('.address');
            parent.classList.remove('closed');
            parent.classList.add('openned');
    
            const defaultCitiesSpan = parent.querySelector(".default-cities");
            const cityInput = parent.querySelector(".city-div");
            if(defaultCitiesSpan){
                defaultCitiesSpan.querySelectorAll("a").forEach(city=>{
                    city.addEventListener("click", 
                        (event)=>{
                            cityInput.value = city.textContent;
                        }
                    )
                })
            }
         })
    }
);


function editOrder(){
    cart.style.display = 'flex';
    backgroundBlurDiv.style.display = 'flex';
}

arrayPaymentInpt.forEach(
    input => {
        input.addEventListener(
            'change',
            ()=> {
                
                const parent = input.parentElement;
                const payNow = document.querySelectorAll('.pay-now')[0];
                const payLater = document.querySelectorAll('.pay-later')[0];
                if(parent.className == 'pay-later'){
                    payLater.style = "border: 1px solid var(--darkblue);";
                    payNow.classList.add('closed');
                    payNow.classList.remove('openned');
                } else{
                    payNow.classList.remove('closed');
                    payNow.classList.add('openned');
                    payLater.style = "border: 1px solid var(--lightgrey);";
                }
            }
        )
    }
);