import tensorflow_probability as tfp
import tensorflow as tf

overall_winrate = float(input("overall_winrate: "))/100
winrate_after_vic = float(input("winrate_after_vic: "))/100
winrate_after_def = float(input("winrate_after_def: "))/100



tfd = tfp.distributions
initial_distribution = tfd.Categorical(probs=[1-overall_winrate,overall_winrate]) #Overall winrate// right - win / left - loss
transition_distribution = tfd.Categorical(probs=[[1-winrate_after_def, winrate_after_def],
                                                 [1-winrate_after_vic, winrate_after_vic]])
observation_distribution = tfd.Normal(loc=[-24.923076, 23.545454], scale=[-4., 3.])


model = tfd.HiddenMarkovModel(
    initial_distribution=initial_distribution,
    transition_distribution=transition_distribution,
    observation_distribution=observation_distribution,
    num_steps=20)

mean = model.mean()

import tensorflow_probability as tfp
import tensorflow as tf

overall_winrate = float(input("overall_winrate: "))/100
winrate_after_vic = float(input("winrate_after_vic: "))/100
winrate_after_def = float(input("winrate_after_def: "))/100



tfd = tfp.distributions
initial_distribution = tfd.Categorical(probs=[1-overall_winrate,overall_winrate]) #Overall winrate// right - win / left - loss
transition_distribution = tfd.Categorical(probs=[[1-winrate_after_def, winrate_after_def],
                                                 [1-winrate_after_vic, winrate_after_vic]])
observation_distribution = tfd.Normal(loc=[-24.923076, 23.545454], scale=[-4., 3.])


model = tfd.HiddenMarkovModel(
    initial_distribution=initial_distribution,
    transition_distribution=transition_distribution,
    observation_distribution=observation_distribution,
    num_steps=20)

mean = model.mean()

with tf.compat.v1.Session() as sess:
  print(mean.numpy())




