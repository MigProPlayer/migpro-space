
define a = Character("Álvaro Madureira")
define r = Character("Tu (Rebeca)")

image entretanto = Text("Entretanto...",size=45)
image demo = Text("Este foi o fim da demo do {b}Álvaro Madureira Dating Simulator{/b}!",size=30)
image demo 1 = Text("Espero que tenhas gostado!",size=30)
image demo 2 = Text("Estou a trabalhar numa versão completa do jogo.",size=30)
image demo 3 = Text("Por isso, fica atento.",size=30)
image demo 4 = Text("Adeus, e até lá!",size=30)
image dica = Text("{b}Dica:{/b} Podes sempre repetir o jogo e ver as outras escolhas!",size=30)

transform pull:
    xalign 0.5 yalign 2.0
    linear 1.0 yalign 0.95
transform push:
    xalign 0.5 yalign 0.95
    linear 1.0 yalign 2.0
transform phone:
    xalign 0.5 yalign 0.95

label start:

    stop music fadeout 1.0
    scene reuniao
    with fade
    a "... e então, como não podiam chegar às árvores, as mais pequenas morreram, e apenas ficaram as maiores."
    a "E as maiores, como sobreviveram, reproduziram-se, e passaram as suas características às novas gerações."
    a "E é por isso que as girafas têm pescoços longos!"
    window hide
    play sound "audio/palmas.ogg"
    pause 5.8

    scene black
    with dissolve
    stop sound fadeout 1.0
    pause 0.5
    show entretanto with dissolve:
        xalign 0.5
        yalign 0.5
    pause 2.5
    hide entretanto with dissolve
    scene corredor
    with dissolve
    pause 0.8
    scene corredor-1
    play sound "audio/passo 1.mp3"
    pause 0.8
    scene corredor-2
    play sound "audio/passo 2.mp3"
    pause 0.8
    scene corredor-3
    play sound "audio/passo 3.mp3"
    pause 0.8
    scene corredor-4
    play sound "audio/passo 4.mp3"
    pause 0.8
    scene corredor-5
    play sound "audio/passo 5.mp3"
    pause 0.8
    scene corredor-6
    play sound "audio/passo 6.mp3"
    pause 0.8
    scene corredor-7
    play sound "audio/passo 7.mp3"
    pause 0.8
    scene corredor-8
    play sound "audio/passo 8.mp3"
    pause 0.8
    scene corredor-9
    play sound "audio/passo 9.mp3"
    pause 0.8
    scene corredor-10
    play sound "audio/bonk.ogg"
    with vpunch
    pause 1.5
    scene corredor-11
    play sound "audio/passo 10.mp3"

    window show
    a "Desculpa!"
    r "Desculpa!"
    a "Oh, olá menina Rebeca!"
    r "Olá, Álvaro!"
    a "Então, como vai o trabalho?"
    r "Vai bem, acabei agora as reuniões da manhã, por isso agora tenho a tarde livre."
    r "E tu?"
    a "Eu também acabei agora a parte da manhã com esta reunião, mas ainda tenho que ir ao Colégio de São Miguel para dar aulas aos meus {b}ilustres{/b}."
    window hide

    menu:
        "Perguntar quem são os {b}ilustres{/b}":
            jump ilustres
        "Procurar o significado de {b}ilustres{/b}":
            jump significado
    return

label significado:
    window show
    "Decides procurar o significado de \"{b}ilustres{/b}\" no Google."
    window hide
    show telemovel-lock at pull
    pause 2.0
    show telemovel at phone with dissolve
    pause 0.5
    hide telemovel-lock
    window show
    "Há dois significados:"
    "1. {i}que se distingue por seu brilhantismo, por qualidades dignas de louvor; célebre, eminente, notável.{/i}"
    "2. {i}que adquiriu celebridade; conhecido, famoso.{/i}"
    "Decides ir pela primeira opção."
    window hide
    show telemovel at push
    pause 1.5
    hide telemovel
    window show
    jump embora
    return

label ilustres:
    window show
    r "Quem são os seus {b}ilustres{/b}?"
    a "Os {b}ilustres{/b} são os meus alunos."
    a "Chamo-lhes assim porque são muito bons, portam-se muito bem (a maior parte), e porque gosto muito deles!"
    jump embora
    return

label embora:
    a "Bem, eu gostava muito de continuar aqui a conversar, mas tenho que ir andando para não chegar atrasado."
    a "Adeus Rebeca!"
    r "Adeus Álvaro!"
    window hide
    pause 0.5
    scene corredor
    with dissolve
    pause 0.5
    window show
    "Decides voltar para casa e descansar um bocado."
    jump demo
    return

label demo:
    window hide
    scene black
    with dissolve
    pause 1.5
    show demo with dissolve:
        xalign 0.5
        yalign 0.5
    pause 4.0
    hide demo with dissolve
    pause 0.5
    show demo 1 with dissolve:
        xalign 0.5
        yalign 0.5
    pause 3.5
    hide demo 1 with dissolve
    pause 0.5
    show demo 2 with dissolve:
        xalign 0.5
        yalign 0.5
    pause 3.5
    hide demo 2 with dissolve
    pause 0.5
    show demo 3 with dissolve:
        xalign 0.5
        yalign 0.5
    pause 3.5
    hide demo 3 with dissolve
    pause 0.5
    show demo 4 with dissolve:
        xalign 0.5
        yalign 0.5
    pause 3.5
    hide demo 4 with dissolve
    pause 0.5
    show dica with dissolve:
        xalign 0.5
        yalign 0.5
    pause 4.0
    hide dica with dissolve
    pause 0.5
    return
