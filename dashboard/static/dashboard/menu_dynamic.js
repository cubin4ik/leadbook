// Menu: making active page link underlined

const currentLocation = location.href;
const menuItem = document.querySelectorAll('a.nav-link');
const menuLength = menuItem.length

for (let i =  0; i < menuLength; i++){
    if(menuItem[i].href === currentLocation){
        menuItem[i].className += " border-bottom"
    }
}