

let scrollbtn = document.querySelector('.scroll');
let up = document.querySelector('.btnUp');
let nav = document.querySelector('nav');
let nav_item = document.querySelector('.nav-item');

let contentIcon = document.querySelector('.profile_content_icon');
let leftSide = document.querySelector('.profile_left_side');
let lists = document.querySelectorAll('.lists li a');

// navBar
onscroll = function(){
    if(scrollY >= 150){
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
    // return scroll to 0
    up.onclick = function(){
        scrollTo({
            top: 0,
            behavior:"smooth"
        });
    }
}


// left side
contentIcon.addEventListener('click', function(){
    leftSide.classList.toggle('active-left-side')
});
// contentIcon.onclick = function(){
//     leftSide.classList.toggle('active-left-side');
// }

for (let i = 0; i < lists.length; i++) {
    // console.log(lists[i]);
    lists[i].onclick = function(){
        leftSide.classList.remove('active-left-side');
    }
}




