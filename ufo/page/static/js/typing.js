var typing = document.getElementById('home_typing');

var typewriter = new Typewriter(typing, {
    loop: true
});

typewriter.typeString('우리 주변의 선택')
    .pauseFor(2500)
    .deleteAll()
    .typeString('우주선')
    .pauseFor(2500)
    .deleteAll()
    .start();
