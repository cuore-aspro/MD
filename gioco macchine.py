import turtle
import random

# Funzione per creare un ostacolo
def crea_ostacolo():
    ostacolo = turtle.Turtle()
    ostacolo.shape("square")
    ostacolo.color("red")
    ostacolo.shapesize(stretch_wid=1, stretch_len=random.randint(1, 3))
    ostacolo.penup()
    ostacolo.goto(300, random.randint(-200, 200))
    return ostacolo

# Funzione per muovere la macchina verso l'alto
def muovi_su():
    y = macchina.ycor()
    if y < 250:
        macchina.sety(y + 20)

# Funzione per muovere la macchina verso il basso
def muovi_giu():
    y = macchina.ycor()
    if y > -240:
        macchina.sety(y - 20)

# Impostazioni della finestra del gioco
finestra = turtle.Screen()
finestra.title("Gioco di Macchine")
finestra.bgcolor("lightblue")
finestra.setup(width=800, height=600)
finestra.tracer(0)

# Crea la macchina giocatore
macchina = turtle.Turtle()
macchina.shape("square")
macchina.color("blue")
macchina.shapesize(stretch_wid=1, stretch_len=2)
macchina.penup()
macchina.goto(-350, 0)

# Creazione della lista per gli ostacoli
ostacoli = []

# Aggiungi eventi per muovere la macchina con i tasti su e giù
finestra.listen()
finestra.onkeypress(muovi_su, "Up")
finestra.onkeypress(muovi_giu, "Down")

# Ciclo principale del gioco
while True:
    finestra.update()

    # Crea un nuovo ostacolo ogni 100 punti
    if len(ostacoli) < 3 and macchina.xcor() > 0:
        ostacoli.append(crea_ostacolo())

    # Muovi gli ostacoli verso sinistra
    for ostacolo in ostacoli:
        ostacolo.setx(ostacolo.xcor() - 15)

        # Se la macchina e l'ostacolo si scontrano
        if (ostacolo.distance(macchina) < 30 and ostacolo.ycor() - 30 < macchina.ycor() < ostacolo.ycor() + 30):
            macchina.color("red")
            print("Gioco Finito!")
            finestra.bye()

        # Se l'ostacolo esce dallo schermo, rimuovilo dalla lista e ricreane uno nuovo
        if ostacolo.xcor() < -400:
            ostacolo.clear()
            ostacoli.remove(ostacolo)
