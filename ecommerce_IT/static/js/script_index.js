let search = document.querySelector('#search');

let boxSearch = document.querySelector('.box-search');
let scrollbtn = document.querySelector('.scroll');
let up = document.querySelector('.btnUp');
let nav = document.querySelector('nav');
let nav_item = document.querySelector('.nav-item');

// search btn
search.onclick = function(){
    boxSearch.classList.toggle('active');
    lists.classList.remove('show-list');
    
    window.scrollTo({
        top: 0
    })
}
// navBar
window.onscroll = function(){
    if(scrollY >= 200){
        // to add btn scroll up
        up.classList.add('show');
        // to add bg for navbar
        nav.style.cssText = "background-color :#26292bc7 !important"
    }else{
        // to remove btn scroll up
        up.classList.remove('show');
        // to remove bg for navbar
        nav.style.cssText = "background-color : transperant"
    }
}
// return scroll to 0
up.onclick = function(){
    window.scrollTo({
        top: 0
    })
}


