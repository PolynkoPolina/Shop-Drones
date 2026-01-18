const cart = window.parent.document.getElementById('cart-modal');
let listIdProduct = document.cookie.split('=')[1];
let uniqueListProducts = new Set(listIdProduct);
let cartCircle = window.parent.document.getElementById('full-cart');
let cartCircleText = window.parent.document.getElementById('full-cart').getElementsByTagName('span')[0]
let cartButton = window.parent.document.getElementById('cart-button');

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


function closeCart(){
    cart.style.display = 'none';
};


if (listIdProduct){
    cartCircle.style.display = 'flex';
    cartCircleText.textContent = uniqueListProducts.size - 1;
} else{
    cartCircle.style.display = 'none';
};

if(listIdProduct == undefined || listIdProduct.length <= 0){
    cart.style.height = '47.6vh';
}