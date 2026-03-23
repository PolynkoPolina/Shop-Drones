const cart = window.parent.document.getElementById('cart-modal');
let listIdProduct = document.cookie.split('=')[1];
let backgroundBlurDiv = window.parent.document.querySelector('.background-blur-div');

if (window.parent.window.location.pathname != "/order/processing"){

    let uniqueListProducts = new Set(listIdProduct);
    let cartCircle = window.parent.document.getElementById('full-cart');
    let cartCircleText = cartCircle.getElementsByTagName('span')[0];
    let cartButton = window.parent.document.getElementById('cart-button');
    const button = document.querySelector('#create-order');
    
    if (listIdProduct){
        cartCircle.style.display = 'flex';
        cartCircleText.textContent = uniqueListProducts.size - 1;
    } else{
        cartCircle.style.display = 'none';
    };
    
    if(listIdProduct == undefined || listIdProduct.length <= 0){
        cart.style.height = '25.3rem';
    }
    
    
    
    button.addEventListener(
        'click',
        (event)=>{
            closeCart();
            window.parent.window.location.replace("/order/processing")
        }
    )
    

    cartButton.addEventListener(
        'click',
        (event) => {
            if (cart.style.display == 'none'){
                cart.style.display = 'flex';
            } 
            else{
                cart.style.display= 'none';
            }
        }
    );
}


function closeCart(value){
    cart.style.display = 'none';
    if( backgroundBlurDiv){
        backgroundBlurDiv.style.display = 'none';
    }
    if (value=='save'){
        window.parent.window.location.reload()
    }
    };
