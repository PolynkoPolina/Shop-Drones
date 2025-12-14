let cart = document.getElementById("cart-modal");
let listIdProduct = document.cookie.split('=')[1];
let uniqueListProducts = new Set(listIdProduct);
let cartCircle = document.getElementById('full-cart');
let cartCircleText = document.getElementById('full-cart').getElementsByTagName('span')[0]

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
};


if (listIdProduct){
    cartCircle.style.display = 'flex';
    cartCircleText.textContent = uniqueListProducts.size - 1;
} else{
    cartCircle.style.display = 'none';
};