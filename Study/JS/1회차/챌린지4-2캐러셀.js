const prevBtn = document.querySelector('#prev');
const nextBtn = document.querySelector('#next');
const carousel = document.querySelector('.carousel');

let index = 0

/*
function indexCheck(btn){
    if (btn == "prevBtn"){
        if (index === 0)
            return;
        index -= 1;
        carousel.style.transform = 'translate3d(-${500 * index}pageXOffset, 0, 0)';
    } else {
        if (index === 2)
            return;
        index += 1;
        carousel.style.transform = 'translate3d(-${500 * index}pageXOffset, 0, 0)';
    }
}
 */

/* 내 나름 해보고 싶었음 */
prevBtn.addEventListener('click', () => {
    if (index === 0) return;
    index -= 1;
    
    carousel.style.transform = `translate3d(-${640 * index}px, 0, 0)`;
});
nextBtn.addEventListener('click', () => {
    if (index === 2) return;
    index += 1;
    
    carousel.style.transform = `translate3d(-${640 * index}px, 0, 0)`;
 });