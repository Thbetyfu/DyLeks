document.addEventListener('DOMContentLoaded', () => {
    const btnStart = document.getElementById('btn-start');
    const btnBack = document.getElementById('btn-back');
    const homePage = document.getElementById('home-page');
    const screeningPage = document.getElementById('screening-page');

    // Create random stars in background
    const bgContainer = document.querySelector('.background-container');
    for(let i = 0; i < 20; i++) {
        const star = document.createElement('div');
        star.classList.add('star');
        star.style.top = `${Math.random() * 100}%`;
        star.style.left = `${Math.random() * 100}%`;
        star.style.animationDelay = `${Math.random() * 3}s`;
        star.style.width = `${Math.random() * 3}px`;
        star.style.height = star.style.width;
        bgContainer.appendChild(star);
    }

    // Navigation Logic
    btnStart.addEventListener('click', () => {
        homePage.classList.remove('active');
        homePage.classList.add('hidden');
        
        setTimeout(() => {
            screeningPage.classList.remove('hidden');
            screeningPage.classList.add('active');
        }, 300);
    });

    btnBack.addEventListener('click', () => {
        screeningPage.classList.remove('active');
        screeningPage.classList.add('hidden');
        
        setTimeout(() => {
            homePage.classList.remove('hidden');
            homePage.classList.add('active');
        }, 300);
    });
});
