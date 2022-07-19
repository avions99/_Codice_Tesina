# l'agente è il computer player
# envairomnet -> snake game
# Q value = quality of action. each action should improve the quality of the snake
# 0 init q value ( inizializzo il modello)
# 1 choose action (model.predict(state)) o faccio random -> trade off tra exploration and explotation
# 2 Perform action
# 3 Measure reward
# 4 Update Q value(+ train model)
# repeat 1-4
# equazione di belmann
# Q Update Rule simplified:
# Q = model.predict(state0)
# Q_new = R (reward) + gamma*max(Q(state1))
# Loss funtion: loss = (Q_new - Q)^2 ossia il Mean squared error
# State ha 11 valori : 3 su pericolo(dritto,sx,dx)
#                      4 su direzione e
#                      4 su posizione cibo
# modello 3 strati (11,hidden,3) Feedforward neural network
# reward: cibo preso -> +10
#         game over -> -10
# Action : [1,0,0] -> dritto,
#          [0,1,0] -> gira destra
#          [0,0,1] -> gira sinistra