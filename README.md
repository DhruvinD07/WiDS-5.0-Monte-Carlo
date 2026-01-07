# WiDS 5.0

## Monte Carlo Simulations: From calculating area to Gambling in BlackJack

Welcome, everyone! This document will serve as our central hub for the project. Here you will find the weekly plan, learning resources, and assignments.

#### **The 5-Week Journey**

Our project is a structured journey designed to take you from a beginner to the architect of a simple artificial intelligence.

* **Week 1: The Toolbox:** Master the essential toolkit of Python and NumPy.
* **Week 2: Monte Carlo Estimation:** Use simulation to estimate the area of complex shapes and build intuition.
* **Week 3: RL Theory:** Learn the foundational concepts of agents, policies, and value functions.
* **Week 4: Monte Carlo Prediction and Control:** Build an engine to evaluate any strategy for the game of Blackjack. Then we empower an agent to learn the optimal strategy for Blackjack entirely on its own.
* **Week 5: The Optimising Agent**: Use techniques like off-policy MC, importance sampling, and hyper-parameter tuning to converge faster to the optimal strategy.

#### **NOTE:** The assignments and learning resources contain several optional sections. You are free to skip them because of time constraints. However, we recommend to try them out since they would help you gain a better understanding of Monte Carlo Methods, such as those used in RL

---

### **Week 1: The Toolbox - Python & NumPy Fundamentals**

**Objective:** By the end of this week, you will be comfortable with the basics of the Python language and the NumPy library. You will be able to write vectorized code to perform fast numerical operations and create simple visualizations. You'll also have a strong foundation in Probability and Statistics.

#### **Part 1: Learning Resources**

This is mainly for those new to Python, Numpy and Probability. Your goal this week is to go through these high-quality tutorials. You don't need to memorize everything, but focus on understanding the core concepts.

For those who are familiar, you may directly skip to the assignment, since it will be used later. Optionally, you can learn advanced tools like JAX and Cython and use them in your assignments instead of NumPy.

* **Python Basics (for those: new to the language):**
  * **Tutorial:** ([FreeCodeCamp Tutorial video](https://www.youtube.com/watch?v=eWRfhZUzrAc))
  * **Reference:** The Official Python Tutorial ([docs.python.org](https://docs.python.org/3/tutorial/index.html))

  * **Focus on:** Get comfortable with basic syntax. Focus especially on the later parts such as Object Oriented Programming in Python.

* **NumPy - The Core of Scientific Computing:**
  * **Tutorial** ([FreeCodeCamp Tutorial Video](https://www.youtube.com/watch?v=QUT1VHiLmmI&pp=ygUgbnVtcHkgdHV0b3JpYWwgZm9yIGJlZ2lubmVycyBmY2M%3D))
  * **Resource:** NumPy: The absolute basics for beginners ([numpy.org](https://numpy.org/doc/stable/user/absolute_beginners.html))
  * **Focus on:** What is a NumPy array? How do you create arrays? What is array indexing, slicing, and, most importantly, **vectorization**? This concept is the key to writing fast, modern data science code.
  * For those who are already proficient in NumPy, look up advanced features like universal functions, Numpy strides, and array siblings. Also look up advanced features such such as JIT compilation for numpy (using Numba). You can also look up other advanced tools such as JAX and Cython, and use them instead of Numpy in the assignments.
* **Matplotlib - Our Visualization Tool:**
  * **Tutorial** ([FreeCodeCamp Tutorial Video](https://www.youtube.com/watch?v=3Xc3CA655Y4))
  * **Resource:** Pyplot Tutorial ([matplotlib.org](https://matplotlib.org/stable/tutorials/pyplot.html))
  * **Focus on:** How to make a simple `plt.plot()` and `plt.scatter()`. We only need the very basics for now.

* **Probability and Statistics** -  A strong foundation in Probability is essential for RL.
  * **Visuals:** [Seeing Theory: Brown University](https://seeing-theory.brown.edu/)
  * **Lecture Slides:** Check out the following slides from Prof. Rajwade for CS215
    * [Random Variables](https://docs.google.com/presentation/d/1sI-8arcM2yYnNZ4sHUWIWfBFTLbc-Bpe/edit).
    * **Focus on:** Understanding Random Variables, CDF, PDF, LOTUS, Independence, Law of Large Numbers
    * **Ignore for now:** Moment Generating Functions(MGFs), Chebyshev's inquality, Markov inequality, covariance
  * **Optional:** Read about the Cental Limit Theorem. 3Blue1Brown's video is an excellent starting point.

#### **Part 2: Assignments**

Assignments have been uploaded in the week 1 directory of this repository. The purpose of these assignments is to ensure a working, practical knowledge of Python and Numpy. For week 1, we'll build games in Python! These same games will be used later on when we train our models to play them. We'll also get started with NumPy and see how vectorization can improve our code speed.

#### **Part 3: Submission**

Please submit your completed your python code by the end of the week. This will confirm you have your environment set up and are comfortable. After the deadline gets over, the solutions for some of the games the same will be uploaded here.

Good luck, and don't hesitate to ask questions!

#### **What did I do and learn**
I did Numpy and Matplotlib tutorials and got used to writing code in Python and visualising data as arrays along with reading lectures on statistics. I built games such as Blackjack in python to understand how to modularize code and learning the steps that go towards building a small project such as that and how to plan the code. I also used LLMs to learn how to convert my code to a graphical interface along with actual displays of cards as I choose to hit or stay which is visually pleasing. 

### **Week 2: Monte Carlo in Geometry - Vectorization & Integration**

**Objective:** This week we bridge the gap between "coding" and "scientific computing" and understand what Monte Carlo simulations are by getting our hands dirty. You will learn how to use random sampling to solve math problems (calculating areas and integrals) that are hard or impossible to solve analytically. You will also learn the most important rule of Python Data Science: **No For Loops.**

#### **Part 1: Learning Resources**

* **Monte Carlo Simulation (The Concept):**
  * **Video:** [Estimating Pi using Monte Carlo Simulation](https://www.youtube.com/watch?v=ELetCV_wX_c) (5 mins). A visual introduction to the core concept of this week.
  * **Article:** [Monte Carlo Integration Explained](https://www.scratchapixel.com/lessons/mathematics-physics-for-computer-graphics/monte-carlo-methods-in-practice/monte-carlo-integration.html). Skim through to understand how we turn random points into an area estimate.

* **High Dimensions (The Challenge):**
  * **Video:** [3Blue1Brown: Thinking about high dimensions](https://www.youtube.com/watch?v=zwAD6dRSVyI). This will help you visualize the "Hypersphere" task and understand why grids fail in high dimensions (The Curse of Dimensionality).

**Note:** this week will be more on the practical side, with a longer assignment. You are encouraged to move to the assignment as soon as possible as the theoretical learning resources are scarce. Try to work through as much optional assignment tasks as you can for developing a better understanding of how and where monte carlo mehtods can be used.

#### **Part 2: Assignment**

The assignment `Week2_Geometry_Vectorization.pdf` is uploaded in the Week 2 directory.

* **Core Tasks:** Estimating $\pi$, Estimating Euler's number ($e$), and comparing Monte Carlo vs. Riemann Sums.
* **The Iron Rule:** You are **not allowed** to use `for` loops for the calculation logic. You must use NumPy vectorization.
* **Optional:** Explore the volume of a 10-dimensional hypersphere and see how Monte Carlo beats deterministic methods in high dimensions.

Another optional assignment regarding the application of Monte Carlo methods in predicting pricing of options.

#### **Part 3: Submission**

Submission will be via a Google Form. Make sure your convergence plots are visible in the notebook. Further instructions are available in assignment pdf.

#### **What did I do and learn**
I read and saw lectures based on higher dimensions and Monte Carlo estimations to understand this topic. I then implemented the code while trying to avoid loops to make the code faster for estimating pi or euler's number, and also how to calculate volume of a few basic shapes.
### **Week 3: Getting Started with Reinforcement Learning**

Reinforcement Learning is an exciting field in AI and Machine Learning. It was mainly brought into spotlight by Google's Deep RL agents to play Atari Games in 2013, and then a further public milestone was their AlphaGo model to beat a professional human Go player.

#### **Part 1: Learning Resources**

In this week, we will explore the theoretical foundations of Reinforcement Learning. In any field, a rigorous and thorough understanding is essential before we tackle problems and their algorithmic solutions. The following resources will help you to gain a rigorous understanding of RL.

* **Textbook:** Reinforcement Learning: An Introduction(Sutton & Barto, 2nd Edition)
  * Read through chapter 1 which covers an introduction to the RL problem
  * Read through chapter 3 for a discussion of Finite Markov Decision Processes, which are needed to formalise the RL problem.
* **Video Lecture**: David Silver's 2015 Lectures on Reinforcement Learning, DeepMind x UCL. Available on DeepMind's YouTube channel. Watch Lecture 1 and Lecture 2. **Must Watch** through the Student MDP example.
* **Focus on:** Intuitively understanding what we are trying to solve. Also understand the Bellman Equations. One might say them to be the fundamental equations of RL!

Fun Fact: The word "Dynamic Programming", commonly used in the context of algorithmic design, came from Bellman. He was looking for a unsuspicious word to hide his research from the government. He felt a very positive vibe in the word "Dynamic"!

Another Fun Fact: Richard Sutton and Andrew Barto recieved the 2025 ACM Turing award for their fundamental contributions to Reinforcement Learning.

#### **Part 2: Assignment**

This week's assignment consists of a theoretical problem sheet. It has been uploaded in the week 3 directory of this repository.

#### **Part 3: Submission**

Please submit your answers in pdf format. Both handwritten(provided they are legible) and LaTeX solutions are accepted. A google form will be released for the same. After the deadline gets over, the solutions will be uploaded in the week 3 directory of this repository.

### **Week 4: Monte Carlo Methods (Prediction & Control)**

**Goal:** Move from "Running a simulation" to "Learning from it". Understand how to update the Value Function $V(s)$ and Policy $\pi(s)$ based on episodes.

#### **Part 1: Learning Resources**

* **Video Lectures:** David Silver - Lecture 4: Model-Free Prediction & Lecture 5: Model-Free Control
  * Note: He also covers Temporal Diference Learning methods such as SARSA and Q-Learning in these lectures. You may freely skip over those sections since they are not needed for our purposes.
* **Textbook Reading:** Sutton & Barto, Chapter 5 (Monte Carlo Methods)
  * **Sections 5.1 - 5.4:** This covers First-visit MC, MC Estimation of Action Values, and MC Control.

#### **Part 2: Assignment**

Uploaded in the week4 directory of this repo. Note that if you were not able to build a correct game in week 1, you are free to use OpenAI Gymnasium environments. However, we highly recommend to debug your own code and use that, since the topics covered in the next week are optional.

#### Part 3: Submission

The submission form will be released *after* completion of week 5. Week 5 is optional and you may continue to work on week 4 assignment if you wish.

### **Week 5: The Optimising Agent (Off-Policy & Tuning)**

**Goal:** The agent plays 500,000 games. It starts dumb, explores random moves, and eventually converges to the mathematically optimal "Basic Strategy" chart.

#### **Part 1: Learning resources**

* **Topic:** **Off-Policy Learning via Importance Sampling**.
* **The Problem:** How do you learn the *Optimal* Strategy (Greedy) while following an *Exploratory* Strategy (Random)?
* **Sutton & Barto:** Sections 5.5  - 5.7.

#### Part 2: Assignment

**NOTE:** You should **only** attempt this if you have **completed** the previous implementation of MC control. If not, this week acts as a buffer week where you can catch-up any remaining topics.

The assignment is to apply Importance sampling to your existing agent. A small suggestion: weighted importance sampling is usually preferred over ordinary in implementation because of bounded variance. Since this is a continuation of the previous assignment, there is no separate document.You should upload the final version with importance sampling for the week 5 google form.

#### Part 3: Submission

The submission form will be released at end of week 5. We will also give 3 days buffer time for submission. Note that along with the Week 4 - Week 5 code, you also have to submit a report consisting of whatever you have learned throughout this WiDS. For the final week, include a "Learning curve" plot (episodes in X axis vs average reward on Y-axis) Any additional insights are welcome!  
