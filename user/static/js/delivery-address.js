const addressForm = document.querySelector("#address-form");
const addAddressBtn = document.querySelector("#add-address");
let addressCount = -1;

addAddressBtn.addEventListener(
    'click',
    (event)=>{
        addressCount++;
        let newAddressDiv = document.createElement('div');
        newAddressDiv.classList.add('address-div');
        newAddressDiv.classList.add('closed');
        newAddressDiv.insertAdjacentHTML('afterbegin', 
            `
            <div class = 'closed-div'>
                <div>
                    <input type="radio" name = "address">
                    <span>м. Київ, Відділення №3: вул. Жулянська, 11</span>
                </div>
                <button type="button" class = "change-address-btn"></button>
            </div>

            <div class = 'inputs-container'>
            <form action = "/account?page=delivery_address" name = 'add-address' method = "post">
                <div>
                    <p><label for="city">Місто</label></p>
                    <input type="text" name = 'city' placeholder="Назва міста" required>
                </div>
                <div>
                    <p><label for="street">Вулиця</label></p>
                    <input type="text" name = 'street' placeholder="Назва вулиці" required> 
                </div>
                <div>
                    <p><label for="house">Будинок</label></p>
                    <input type="number" name = 'house' placeholder="Номер будинку" required>
                </div>
                <div>
                    <p><label for="appartment">Квартира</label></p>
                    <input type="number" name = 'appartment' placeholder="Номер квартири">
                </div>
                <div>
                    <p><label for="entrance">Під'їзд</label></p>
                    <input type="number" name="entrance" placeholder="Номер під'їзду">
                </div>
                <button class = "save-changes">Зберегти зміни</button>
                </form>
            </div>

            `
            )
        addressForm.insertAdjacentElement('beforeend',newAddressDiv);

        let changeAddressBtn = document.querySelectorAll(".change-address-btn")[addressCount];
        changeAddressBtn.addEventListener(
            'click',
            (event) =>{
                newAddressDiv.classList.toggle('openned');
                newAddressDiv.classList.toggle('closed');
            }
        )
    }
)

