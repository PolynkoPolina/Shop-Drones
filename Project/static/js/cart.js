let cart = document.getElementById("cart-modal");

function openCart(){
    if (cart.style.display === 'none'){
        cart.style.display= 'flex';
    } 
    else{
        cart.style.display= 'none';
    }
};

function closeCart(){
    cart.style.display= 'none';
}

