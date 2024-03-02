let contentIcon = document.querySelector('.content-icon');
let leftSide = document.querySelector('.left-side');
let lists = document.querySelectorAll('.lists li a');


for (let i = 0; i < lists.length; i++) {
    console.log(lists[i]);
    lists[i].onclick = function(){
        leftSide.classList.remove('active-left-side');
    }
}
// left side
contentIcon.onclick = function(){
    leftSide.classList.toggle('active-left-side');
}

