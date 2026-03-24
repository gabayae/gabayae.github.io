# Reinforcement Learning: From Theory to Practice — 5-Day Workshop

**Instructor:** Dr. Yaé Ulrich Gaba
**Duration:** 5 days (30 hours)
**Level:** Intermediate to Advanced
**Language:** English

---

## Overview

This workshop provides a rigorous yet practical introduction to reinforcement learning (RL), connecting mathematical foundations — including topological and metric-space perspectives — to modern deep RL algorithms. Participants implement classic and deep RL methods from scratch, apply them to real-world problems, and gain insight into the mathematical structures underlying convergence and optimality.

## Prerequisites

- Python programming (comfortable with NumPy, classes, basic OOP)
- Linear algebra basics (vectors, matrices, eigenvalues)
- Probability and statistics (distributions, expectation, conditional probability)
- Familiarity with neural networks (forward pass, backpropagation concepts)

## Learning Objectives

By the end of this workshop, participants will be able to:

1. Formalize sequential decision problems as Markov Decision Processes (MDPs)
2. Implement tabular RL algorithms (dynamic programming, Q-learning, SARSA)
3. Understand convergence guarantees through the lens of fixed point theory
4. Build deep RL agents (DQN, policy gradient, actor-critic)
5. Apply RL to practical problems (resource allocation, game playing, optimization)
6. Evaluate and debug RL systems

## Software Requirements

- Python 3.10+
- Libraries: numpy, gymnasium (OpenAI Gym), matplotlib, torch (PyTorch), stable-baselines3
- Optional: tensorboard, wandb

---

## Day-by-Day Program

### Day 1: Foundations — MDPs & Dynamic Programming

**Objectives:** Formalize RL problems and solve small MDPs exactly.

| Time | Topic |
|------|-------|
| 09:00–10:00 | **What is RL?** — The agent-environment loop, reward hypothesis, comparison with supervised/unsupervised learning, applications overview |
| 10:00–10:45 | **Markov Decision Processes** — States, actions, transitions, rewards, discount factor $$\gamma$$, policies, value functions $$V^\pi(s)$$ and $$Q^\pi(s,a)$$ |
| 10:45–11:00 | *Break* |
| 11:00–12:30 | **Bellman Equations** — Bellman expectation equation, Bellman optimality equation, the Bellman operator $$\mathcal{T}$$ as a contraction mapping |
| 12:30–14:00 | *Lunch* |
| 14:00–15:30 | **Dynamic Programming** — Policy evaluation (iterative), policy improvement, policy iteration, value iteration. Convergence proofs via Banach fixed point theorem |
| 15:30–15:45 | *Break* |
| 15:45–17:00 | **Implementation** — Code a GridWorld environment and solve it with policy iteration and value iteration. Visualize value functions and optimal policies |

**Lab 1:** Implement a complete MDP solver: define a GridWorld with obstacles and rewards, implement policy evaluation, policy improvement, and value iteration. Visualize the optimal policy as arrows on the grid.

**Homework:** Solve a different MDP (e.g., FrozenLake from Gymnasium) using your implementations.

---

### Day 2: Tabular Methods — MC, TD, Q-Learning

**Objectives:** Learn model-free RL methods that work without knowing the environment dynamics.

| Time | Topic |
|------|-------|
| 09:00–09:30 | **Homework Review** |
| 09:30–10:30 | **Monte Carlo Methods** — First-visit vs. every-visit MC, MC prediction, MC control with ε-greedy exploration, importance sampling |
| 10:30–10:45 | *Break* |
| 10:45–12:30 | **Temporal Difference Learning** — TD(0) prediction, the TD error $$\delta_t$$, SARSA (on-policy TD control), Q-Learning (off-policy TD control), convergence comparison |
| 12:30–14:00 | *Lunch* |
| 14:00–15:30 | **Exploration vs. Exploitation** — ε-greedy, softmax, UCB, optimistic initialization. The exploration-exploitation dilemma. Multi-armed bandits as a special case |
| 15:30–15:45 | *Break* |
| 15:45–17:00 | **Fixed Point Perspective** — The Bellman operator as a contraction in metric spaces, convergence rates, connections to quasi-metric structures, why Q-learning converges |

**Lab 2:** Implement Q-Learning and SARSA from scratch. Train agents on Gymnasium environments (Taxi-v3, CliffWalking). Compare learning curves, explore the effect of ε, α, and γ on convergence.

**Homework:** Implement n-step TD and compare with 1-step TD on the same environment.

---

### Day 3: Deep RL — DQN & Extensions

**Objectives:** Scale RL to high-dimensional problems with neural network function approximation.

| Time | Topic |
|------|-------|
| 09:00–09:30 | **Homework Review** |
| 09:30–10:30 | **Function Approximation** — Why tabular methods don't scale, linear function approximation, the deadly triad (function approximation + bootstrapping + off-policy), neural networks as approximators |
| 10:30–10:45 | *Break* |
| 10:45–12:30 | **Deep Q-Networks (DQN)** — Experience replay, target networks, the DQN loss, ε-decay schedules. Implementation with PyTorch |
| 12:30–14:00 | *Lunch* |
| 14:00–15:30 | **DQN Extensions** — Double DQN, Dueling DQN, Prioritized Experience Replay, Noisy Nets, Rainbow DQN (overview) |
| 15:30–15:45 | *Break* |
| 15:45–17:00 | **Practical DQN** — Hyperparameter tuning, debugging tips, common failure modes, when DQN works well and when it doesn't |

**Lab 3:** Implement DQN from scratch in PyTorch. Train on CartPole-v1 and LunarLander-v2. Implement Double DQN and compare performance. Log training curves with TensorBoard.

**Homework:** Train DQN on a new environment and analyze the learned Q-values.

---

### Day 4: Policy Gradient & Actor-Critic Methods

**Objectives:** Learn policy-based methods and modern actor-critic algorithms.

| Time | Topic |
|------|-------|
| 09:00–09:30 | **Homework Review** |
| 09:30–10:30 | **Policy Gradient Methods** — Why optimize policies directly, the policy gradient theorem, REINFORCE algorithm, variance reduction with baselines |
| 10:30–10:45 | *Break* |
| 10:45–12:30 | **Actor-Critic Methods** — Advantage function $$A(s,a)$$, A2C (Advantage Actor-Critic), GAE (Generalized Advantage Estimation), entropy regularization |
| 12:30–14:00 | *Lunch* |
| 14:00–15:30 | **PPO — Proximal Policy Optimization** — Clipped surrogate objective, trust regions (intuition), PPO implementation, why PPO is the workhorse of modern RL |
| 15:30–15:45 | *Break* |
| 15:45–17:00 | **Stable-Baselines3** — Using SB3 for rapid prototyping: PPO, A2C, SAC. Custom environments, callbacks, evaluation, hyperparameter tuning with Optuna |

**Lab 4:** Implement REINFORCE from scratch. Then use Stable-Baselines3 to train PPO on continuous control tasks (MountainCarContinuous, Pendulum). Compare sample efficiency and stability across algorithms.

**Homework:** Train a PPO agent on a custom environment relevant to your research.

---

### Day 5: Applications & Advanced Topics

**Objectives:** Apply RL to real-world problems and explore cutting-edge directions.

| Time | Topic |
|------|-------|
| 09:00–09:30 | **Homework Presentations** |
| 09:30–10:30 | **RL for Resource Allocation** — Wireless network optimization (DQN for channel allocation), energy grid management, scheduling problems. Connection to the instructor's research |
| 10:30–10:45 | *Break* |
| 10:45–12:00 | **Multi-Agent RL** — Independent learners, centralized training with decentralized execution (CTDE), communication, cooperative vs. competitive settings |
| 12:00–12:30 | **Topological Perspectives on RL** — Topology of state/action/policy spaces, how topological structure affects convergence, connections to the instructor's research on RL foundations |
| 12:30–14:00 | *Lunch* |
| 14:00–15:30 | **Advanced Topics Survey** — Model-based RL, offline RL, reward shaping, inverse RL, RL from Human Feedback (RLHF), safe RL |
| 15:30–15:45 | *Break* |
| 15:45–16:30 | **Capstone Project Work** — Complete and polish final projects |
| 16:30–17:00 | **Presentations & Wrap-Up** — Project demos, discussion, resources for continued learning, certificates |

**Lab 5 (Capstone):** Choose one project:
- **Resource allocator:** DQN agent for wireless network channel allocation
- **Game agent:** Train an agent to play a classic Atari game using DQN or PPO
- **Control system:** PPO agent for a continuous control task with custom reward shaping
- **Custom application:** Apply RL to a problem from your own research domain

---

## Assessment

- **Daily labs** (40%) — Working implementations and analysis
- **Capstone project** (40%) — Complete RL application with evaluation
- **Participation** (20%) — Engagement, homework, and discussions

## Resources

- [Sutton & Barto — Reinforcement Learning: An Introduction (2nd ed.)](http://incompleteideas.net/book/the-book-2nd.html)
- [Stable-Baselines3 Documentation](https://stable-baselines3.readthedocs.io/)
- [Gymnasium Documentation](https://gymnasium.farama.org/)
- [Spinning Up in Deep RL (OpenAI)](https://spinningup.openai.com/)
- [Topological Foundations of RL (Gaba, 2024)](https://arxiv.org/abs/2410.03706)
- [The Shape of Data](https://nostarch.com/shapeofdata)

## Certificate

Participants who complete all labs and the capstone project receive a certificate of completion.
