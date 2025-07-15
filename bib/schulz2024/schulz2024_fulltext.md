# Full Text: schulz2024

Extracted: 2025-07-15 13:22:01
Source: HTML Snapshot
---

A short 'derivation' of Watanabe's Free Energy Formula — LessWrong

This website requires javascript to properly function. Consider activating javascript to get access to all site functionality. 

[LESSWRONG](https://www.lesswrong.com/)
---------------------------------------

[Wuschel Schulz](https://www.lesswrong.com/users/wuschel-schulz)

[A short 'derivation' of Watanabe's Free Energy Formula](#)

8 min read

•

[Background: Statistical Learning Theory](#Background__Statistical_Learning_Theory)

•

[The Probabilistic Model](#The_Probabilistic_Model)

•

[The True Distribution](#The_True_Distribution)

•

[The Parameters](#The_Parameters)

•

[The Data](#The_Data)

•

[The Negative Log-Likelihood](#The_Negative_Log_Likelihood)

•

[Prior over the Parameters](#Prior_over_the_Parameters)

•

[Posterior Distribution](#Posterior_Distribution)

•

[Free Energy](#Free_Energy)

+[Free Energy Principle](https://www.lesswrong.com/w/free-energy-principle)[Singular Learning Theory](https://www.lesswrong.com/w/singular-learning-theory)[AI](https://www.lesswrong.com/w/ai)[Frontpage](https://www.lesswrong.com/posts/5conQhfa4rgb4SaWx/site-guide-personal-blogposts-vs-frontpage-posts)

13
==

[A short 'derivation' of Watanabe's Free Energy Formula](https://www.lesswrong.com/posts/ry9ch69xY7PkCS8td/a-short-derivation-of-watanabe-s-free-energy-formula)
================================================================================================================================================================

by [Wuschel Schulz](https://www.lesswrong.com/users/wuschel-schulz?from=post_header)

30th Jan 2024

*Epistemic status: I wrote the post mostly for myself, in the process of understanding the theory behind Singular Learning Theory, based on the* [*SLT low lecture series*](https://youtube.com/playlist?list=PL4vaU_gO_6LIf5CHU3Z3CT39fha55pe16&si=q9YW_U-Uq5YlhDa_)*. This is a proof sketch with the thoroughness level of an experimental physics lecture: enough to get the intuitions but consult someone else for details.*

Background: Statistical Learning Theory
=======================================

In the framework of statistical learning theory, we aim to establish a model that can predict an outcome y given an input x with a certain level of confidence. This prediction is typically governed by a set of parameters w , which need to be learned from the data. Let us begin by defining the primary components of this framework.

The Probabilistic Model
-----------------------

The probabilistic model  p(y|x,w) represents the likelihood of observing the outcome  y given the input x and the parameters w. This model is parametric, meaning that the form of the probability distribution is predefined, and the specific behavior of the model is determined by the parameters w.

The True Distribution
---------------------

The true distribution q(y|x)  is the actual distribution from which the data points are sampled. In practice, this distribution is not known and  p(y|x,w) attempts to approximate it through the learning process.

The Parameters
--------------

The parameters w  are the weights or coefficients within our model that determine its behavior. The goal of learning is to find the values of w that make p(y|x,w) as close as possible to the true distribution q(y|x).

The Data
--------

The data D={xi,yi}  consist of pairs of input values xi  and their corresponding outcomes yi. These data points are used to train the model, adjusting the parameters w to fit the observed outcomes.

The Negative Log-Likelihood
---------------------------

The negative log-likelihood is a measure of how well our model p(y|x,w) fits the data D . It is defined as the negative sum of the logarithms of the model probabilities assigned to the true outcomes yi:

NLL(w)=−∑Ni=1logp(yi|xi,w),

where N is the number of data points in D. Minimizing the negative log-likelihood is equivalent to maximizing the likelihood of the data under the model, which is a central objective in the training of probabilistic models.

Prior over the Parameters
-------------------------

In a Bayesian framework, we incorporate our prior beliefs about the parameters w  before observing the data through a prior distribution φ(w). This prior distribution encapsulates our assumptions about the values that w can take based on prior knowledge or intuition. For instance, a common choice is a Gaussian distribution, which encodes a preference for smaller (in magnitude) parameter values, promoting smoother model functions.

Posterior Distribution
----------------------

Once we have observed the data  D, we can update our belief about the parameters w using Bayes' theorem. The updated belief is captured by the posterior distribution, which combines the likelihood of the data given the parameters with our prior beliefs about the parameters. The posterior distribution is defined as:

P(w|D)=1Znexp(−NLL(w))Φ(w),

where  NLL(w) is the negative log-likelihood of the parameters given the data, Φ(w) is the prior over the parameters, and Zn is the normalization constant, also known as the partition function. The partition function ensures that the posterior distribution is a valid probability distribution by integrating (or summing) over all possible values of w:

Zn=∫exp(−NLL(w))φ(w)dw.

The posterior distribution reflects how likely different parameter values are after taking into account the observed data and our prior beliefs.

Free Energy
===========

This formulation looks like the Boltzmann distribution from statistical physics. This distribution also describes a probability: the probability that a system can be found in a particular microstate is e−E with E being the energy (here assuming, that the temperature is 1). This formalism can be expanded to macrostates, when changing the Energy to Free Energy, taking into account that microstates that have many realizations are more likely.  
We can do a similar step with the Posterior of our model weights, by considering neighborhoods around local minima as macrostates. This opens up the question of what the correct formula for the Free Energy of these macrostates are, so we can make predictions about the behavior of learning machines.  
First, let us consider the case of large datasets. In that case, we can replace the negative Log-Likelihood with n times its average:

NLL(w)=−N∑i=1logp(yi|xi,w)≈n∫log(p(y|x,w))q(y|x)q(x)dx=n(∫log(p(y|x,w)q(y|x))q(y|x)q(x)dx−∫log(q(y|x))q(y|x)q(x)dx)=n<KL(pw|q)−S(q)>q(x)  
  
We see that we can compose the negative Log likelihood into the number of data points n, the expected Kullback–Leibler divergence of the model with the true distribution, and the expected entropy of the true distribution. As we see here, the expected entropy term does not contribute to the posterior of the parameters:  
P(w|n)=1Znexp(−NLL(w))Φ(w)=exp((−NLL(w))Φ(w)∫exp(−NLL(w))Φ(w)dw=exp(−n⟨KL(pw∥q)−S(q)⟩q(x))Φ(w)∫exp(−n⟨KL(pw∥q)−S(q)⟩q(x))Φ(w)dw=exp(−n⟨KL(pw∥q)⟩q(x))Φ(w)∫exp(−n⟨KL(pw∥q)⟩q(x))Φ(w)dw  
The macrostates, aka the regions in parameter space we are now interested in analyzing are the vicinities of local minima in the Loss landscape. Let us assume we decompose our parameter space into macrostates W=∪αWα.  
P(w∈Wα)=∫w∈Wαp(w|n)dw=∫w∈Wα1Znexp(−L(w))Φ(w)dw∑α∫w∈Wα1Znexp(−L(w))Φ(w)dw=∫w∈Wαexp(−n⟨KL(pw∥q)⟩q(x))Φ(w)dw∑α∫w∈Wαexp(−n⟨KL(pw∥q)⟩q(x))Φ(w)dw=exp−F(Wα,n)∑αexp−F(Wα,n)F(Wα,n)=−log(∫w∈Wαexp(−n⟨KL(pw∥q)⟩q(x))Φ(w)dw)

We call this F the free energy of this area, as it serves the same function as the Free Energy in statistical physics. We have constructed Wα such that it only contains one minimum of the expected Kulberg Leibler divergence (from here on  we abbreviate KL(pw∥q)⟩q(x) as K(ω)). These minima don't have to be points but can be different sets  within Wα.![](data:image/png;base64,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)

Examples of sets where  K has a minimum. a): A point b): A submanifold. c): An algebraic set with Singularity.

 Since we assume, that K(ω) is smooth, it can locally be approximated by its Taylor series at any point. How the leading order terms of the Taylor series look at its minimum depends on the geometry of the minimum. Let's look at an example of how that might look like from the figure above. In a) we have a simple minimum point, so the Taylor series of K at this point might look like x2+y2, going up in each direction. In b) our minimum is a one-dimensional submanifold, and so the Taylor expansion of K will look like x0+y2, increasing in one dimension, but staying flat when going along another. The situation in c) looks almost the same, except in the center, where the line crosses itself. There the Taylor expansion will look like x2⋅y2, locally staying flat in either direction. Points like these, where the directions you can go in while staying on the set suddenly change, are called singularities.  
Let us now calculate the Free Energy around a point ω∗, where K has a minimum. In general the leading order term of the K at a minimum looks like this:  
K(ω∗+x)=Kmin+a∏ix2kii:=Kmin+a→x2→k  
Here Kmin is the value of the KL-divergence at its minimum.  
To get it into this form, we have to make a change of coordinates for x (for example when we are at a singularity where the different parts of the minimum come in from an angle). A process called blowup guarantees us, that we are always able to find such coordinates. Since we are at a minimum, we know that all leading order exponents are even.  
Let's also approximate our prior over the weights  Φ(w∗+x) on this point in the same basis as its leading order term:  
Φ(ω)=b∏ixhii:=b→x→h  
For large n, the Free Energy at any point far away from the minima gets exponentially suppressed. To see how much the minimal point ω∗ contributes to the integral we can integrate it in its vicinity. Here we choose to integrate from 0 to 1.

Why not from −1 to 1?[[1]](#fnuzzvy7qpglm)  
F(ω∗,n)=−log(∫10exp(−n(Kmin+a→x2→k)(b→x→hd→x)  
The first thing we can do is pull out the Kmin term as it does not depend on x.  
F(ω∗,n)=nKmin−log(∫10exp(−na→x2→k)b→x→hd→x)  
To solve the remaining integral, we first do a Laplace and then a Mellin transform, as this brings the integral into a form, that is easier to solve.  
L(∫10exp(−na→x2→k)b→x→hd→x)=∫∞0(∫10exp(−na→x2→k)b→x→hd→x)e−ntdt=∫10δ(t−a→x2→k)b→x→hd→xM(L(∫10exp(−na→x2→k)b→x→hd→x))=∫∞0(∫10δ(t−a→x2→k)b→x→hd→x)tzdt=∫10(a→x2→k)zb→x→hd→x=azb∏i∫10x2zki+hii=azb1∏i(2zki+hi+1)

Next, we group the dimensions i along, such that within each group Iα, the value λα=hi+12ki is the same. Later in the derivation, it will turn out, that only the biggest λ will contribute for large n.   
M(L(∫10exp(−na→x2→k)b→x→hd→x))=azb1∏α∏i∈Iα2ki(z+λi)  
Now we go backward, and reverse the Mellin and the Laplace transform:  
L(∫10exp(−na→x2→k)b→x→hd→x)=∫+i∞−i∞azb2πi1∏α∏i∈Iα2ki(z+λi)t−z−1dz=b2πit∫+i∞−i∞ezlog(at)∏α∏i∈Iα2ki(z+λi)dz  
We can solve this integral with the Residue Theorem, closing the integral path over the negative half of the if a>t. Since all λα have to be positive, when we close the integral over the negative half, we enclose no residues and the integral comes out as zero. Otherwise each unique λi, which appears m times, being a residual of degree m:  
L(∫10exp(−na→x2→k)b→x→hd→x)=b2πit∑α1mα−1(ddz)mα−1ezlog(at)∣∣∣z=−λα=⎧⎪⎨⎪⎩b2πit∑αlog(at)mα−1mα−1e−λαlog(at),if a>t,0,if a≤t.  
When we now reverse the Laplace transform, we only have to integrate up to a.  
∫10exp(−na→x2→k)b→x→hd→x=∫a0b2πi∑αa−λαlog(at)mα−1mα−1tλα−1e−ntdt∣∣∣τ=nat=b2πi∑αa−λαmα−1∫n0log(nτ)mα−1(aτn)λα−1e−τaandτ=b2πi∑αn−λαmα−1∫n0τλα−1e−τa(log(n)−log(τ))mα−1dτ=b2πi∑αn−λαmα−1∫n0τλα−1e−τamα−1∑j=0(mα−1j)log(n)mα−1−j(−log(τ)j)dτ=b2πi∑αn−λαmα−1mα−1∑j=0(mα−1j)log(n)mα−1−j∫n0τλα−1e−τa(−log(τ)j)dτ  
This integral now is asymptotically going towards some number as n goes to infinity. So we can pick out the term that is the highest order in n as the one with the smallest λα and j=0.  
∫10exp(−na→x2→k)b→x→hd→x∝n−λα∗log(n)mα∗−1+O(n−λα∗log(n)mα∗−2)  
We can combine this into the Formula for Free Energy.  
F(ω∗,n)=nKmin+λlog(n)−(m−1)log(log(n))  
This expression tells us now, how much mass of the posterior distribution is centered around certain points in parameter space. The leading order term consists of the KL divergence between the training distribution and the distribution of our model. Intuitively, this corresponds to our training loss. In the second term the λ inversely scales with the multiplicity of the minimum. Intuitively it corresponds to symmetries in the algorithm that the Network implements. The third term scales with the number of parameters that have a minimum of the same multiplicity. Intuitively this gives a set of parameters an extra advantage when multiple parameter sets implement algorithms that independently lead to minimal loss.

1. **[^](#fnrefuzzvy7qpglm)**

   I would have expected, that we integrate the whole vicinity:  
   F(ω∗,n)=−log(∫1−1exp(−n(Kmin+a→x2→k)(b→x→hd→x)  
   This, however, makes the derivation quite ugly:  
   L(∫1−1exp(−na→x2→k)b→x→hd→x)=∫∞0(∫1−1exp(−na→x2→k)b→x→hd→x)e−ntdt=∫1−1δ(t−a→x2→k)b→x→hd→xM(L(∫1−1exp(−na→x2→k)b→x→hd→x))=∫∞0(∫1−1δ(t−a→x2→k)b→x→hd→x)tzdt=∫1−1(a→x2→k)zb→x→hd→x=azb∏i∫1−1x2zki+hii=azb∏i(2zki+hi+1)∏i(12zki+hi−(−1)2zki+hi)  
   L(∫1−1exp(−na→x2→k)b→x→hd→x)=b2πi∮azt−z−1∏i(2zki+hi+1)∏i(1−(−1)2zki+hi)dz=b2πit∫+i∞−i∞ezlog(at)∏α∏i∈Iα2ki(z+λi)∏i(1−(−1)2ki(z+λi))dz=b2πit∑α1mα−1(ddz)mα−1ezlog(at)(1−(−1)2ki(z+λi))∣∣∣z=−λα=⎧⎨⎩b2πit∑α1mα−1e−λαlog(at)∑j(mα−1j)(log(at)mα−1−j(2πiki)j,if a>t,0,if a≤t.  
   We can proceed with the rest of the calculation with each summand j and just have a smaller mα. This does not change anything about the leading terms, that are relevant for the Free Energy formula.

   I am still confused, about why the lecture went from 0 to 1, and would be grateful for an explanation in the comments.

1.

I would have expected, that we integrate the whole vicinity:  
F(ω∗,n)=−log(∫1−1exp(−n(Kmin+a→x2→k)(b→x→hd→x)  
This, however, makes the derivation quite ugly:  
L(∫1−1exp(−na→x2→k)b→x→hd→x)=∫∞0(∫1−1exp(−na→x2→k)b→x→hd→x)e−ntdt=∫1−1δ(t−a→x2→k)b→x→hd→xM(L(∫1−1exp(−na→x2→k)b→x→hd→x))=∫∞0(∫1−1δ(t−a→x2→k)b→x→hd→x)tzdt=∫1−1(a→x2→k)zb→x→hd→x=azb∏i∫1−1x2zki+hii=azb∏i(2zki+hi+1)∏i(12zki+hi−(−1)2zki+hi)  
L(∫1−1exp(−na→x2→k)b→x→hd→x)=b2πi∮azt−z−1∏i(2zki+hi+1)∏i(1−(−1)2zki+hi)dz=b2πit∫+i∞−i∞ezlog(at)∏α∏i∈Iα2ki(z+λi)∏i(1−(−1)2ki(z+λi))dz=b2πit∑α1mα−1(ddz)mα−1ezlog(at)(1−(−1)2ki(z+λi))∣∣∣z=−λα=⎧⎨⎩b2πit∑α1mα−1e−λαlog(at)∑j(mα−1j)(log(at)mα−1−j(2πiki)j,if a>t,0,if a≤t.  
We can proceed with the rest of the calculation with each summand j and just have a smaller mα. This does not change anything about the leading terms, that are relevant for the Free Energy formula.

I am still confused, about why the lecture went from 0 to 1, and would be grateful for an explanation in the comments.

13
==

[A short 'derivation' of Watanabe's Free Energy Formula](#)

[4Daniel Murfet](#kP5pLEtiaP88g87wj)

[1Wuschel Schulz](#c3Qfci7WhEaJAtFmb)

[1Wuschel Schulz](#pJmqduRqpmtYEPcsj)

[3Daniel Murfet](#hYqvxRgGG4Xzh4deG)

[1James Camacho](#xK6b6Rsprb3HQ57iB)

[1James Camacho](#xBk4Nc7q5ddex3TiX)

New Comment

Submit

6 comments, sorted by

top scoring

No new comments since 01/02/2025

[-][Daniel Murfet](https://www.lesswrong.com/users/daniel-murfet)[1y](https://www.lesswrong.com/posts/ry9ch69xY7PkCS8td/a-short-derivation-of-watanabe-s-free-energy-formula?commentId=kP5pLEtiaP88g87wj)40

There was a sign error somewhere, you should be getting + lambda and - (m-1). Regarding the integral from 0 to 1, since the powers involved are even you can do that and double it rather than -1 to 1 (sorry if this doesn't map exactly onto your calculation, I didn't read all the details).

Reply

[-][Wuschel Schulz](https://www.lesswrong.com/users/wuschel-schulz)[1y](https://www.lesswrong.com/posts/ry9ch69xY7PkCS8td/a-short-derivation-of-watanabe-s-free-energy-formula?commentId=c3Qfci7WhEaJAtFmb)10

Ok, the sign error was just in the end, taking the -log of the result of the integral vs. taking the log. fixed it, thanks.

Reply

[-][Wuschel Schulz](https://www.lesswrong.com/users/wuschel-schulz)[1y](https://www.lesswrong.com/posts/ry9ch69xY7PkCS8td/a-short-derivation-of-watanabe-s-free-energy-formula?commentId=pJmqduRqpmtYEPcsj)10

Thanks, Ill look for the sign-error!  
  
I agree, that K is symmetric around our point of integration, big the prior phi is not. We integrate over e-(nk)\*phi, wich does not have have to be symetric, right?

Reply

[-][Daniel Murfet](https://www.lesswrong.com/users/daniel-murfet)[1y](https://www.lesswrong.com/posts/ry9ch69xY7PkCS8td/a-short-derivation-of-watanabe-s-free-energy-formula?commentId=hYqvxRgGG4Xzh4deG)30

Yes, good point, but if the prior is positive it drops out of the asymptotic as it doesn't contribute to the order of vanishing, so you can just ignore it from the start.

Reply![](data:image/svg+xml;base64,PD94bWwgdmVyc2lvbj0iMS4wIiBlbmNvZGluZz0iVVRGLTgiPz4KPHN2ZyB3aWR0aD0iMTIwMHB0IiBoZWlnaHQ9IjEyMDBwdCIgdmVyc2lvbj0iMS4xIiB2aWV3Qm94PSIwIDAgMTIwMCAxMjAwIiB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciPgogPHBhdGggZD0ibTExMjQuNCAxODIuOTFjLTIuMjUtOC44NjMzLTEwLjY3Ni0xNC43NzctMTkuNjI5LTE0LjEwOS0zMTAuMDQgMjQuMDIzLTU2Ny43NyAyMzUuNjEtNjk2LjAzIDU2OC43Ny03MS40MS0xMDkuMDctMTc5LjI3LTEyNi40Ni0yNDAuNzUtMTI2LjQ2LTQ1LjcwMyAwLTc4LjAxMiA4Ljk2MDktNzkuMzY3IDkuMzQ3Ny03LjIyMjcgMi4wNDMtMTIuNTM1IDguMTgzNi0xMy41MDQgMTUuNjI5czIuNjAxNiAxNC43MzggOS4wNTQ3IDE4LjU1OWMxNDguNjQgODcuODE2IDI0MC4wMiAyMzUuMjMgMjkwLjUgMzQzLjQzIDkuNTUwOCAyMC40NTcgMjguNzY2IDMzLjE2NCA1MC4xNjQgMzMuMTY0IDI0LjYyOSAwIDQ1LjYwOS0xNi4wNTEgNTMuNDY5LTQwLjg5OCAxODMuMTUtNTc5LjU2IDYzMC45OS03ODMuNzEgNjM1LjUtNzg1LjcxIDguMzQzOC0zLjY5NTMgMTIuODMyLTEyLjg3OSAxMC41OTgtMjEuNzN6Ii8+Cjwvc3ZnPgo=)1

[-][James Camacho](https://www.lesswrong.com/users/james-camacho)[1y](https://www.lesswrong.com/posts/ry9ch69xY7PkCS8td/a-short-derivation-of-watanabe-s-free-energy-formula?commentId=xK6b6Rsprb3HQ57iB)10

> To see how much the minimal point ω∗ contributes to the integral we can integrate it in its vicinity

I think you should be looking at the entire stable island, not just integrating from zero to one. I expect you could get a decent approximation with Lie transform perturbation theory, and this looks similar to the idea of macro-states in condensed matter physics, but I'm not knowledgeable in these areas.

Reply

[-][James Camacho](https://www.lesswrong.com/users/james-camacho)[1y](https://www.lesswrong.com/posts/ry9ch69xY7PkCS8td/a-short-derivation-of-watanabe-s-free-energy-formula?commentId=xBk4Nc7q5ddex3TiX)10

> −N∑i=1logp(yi|xi,w)

You have a typo, the equation after **Free Energy** should start with NLL(w)=−∑log(p(y|xi,wi))q(yi|xi).

Also the third line should be ∫⋯+∫, not minus.

Also, usually people use θ for model parameters (rather than w). I don't know the etymology, but game theorists use the same letter (for "types" = models of players).

Reply

[Moderation Log](https://www.lesswrong.com/moderation)

More from [Wuschel Schulz](https://www.lesswrong.com/users/wuschel-schulz)

125[Steering Llama-2 with contrastive activation additions](https://www.lesswrong.com/posts/v7f8ayBxLhmMFRzpa/steering-llama-2-with-contrastive-activation-additions)

[Ω](https://alignmentforum.org/posts/v7f8ayBxLhmMFRzpa/steering-llama-2-with-contrastive-activation-additions)

[Nina Panickssery](https://www.lesswrong.com/users/nina-panickssery), [Wuschel Schulz](https://www.lesswrong.com/users/wuschel-schulz), [NickGabs](https://www.lesswrong.com/users/nickgabs), [Meg](https://www.lesswrong.com/users/meg), [evhub](https://www.lesswrong.com/users/evhub), [TurnTrout](https://www.lesswrong.com/users/turntrout)

2y

29

38[A caveat to the Orthogonality Thesis](https://www.lesswrong.com/posts/qoTpit4zFPni54GSo/a-caveat-to-the-orthogonality-thesis)

[Wuschel Schulz](https://www.lesswrong.com/users/wuschel-schulz)

3y

10

46[There is a line in the sand, just not where you think it is](https://www.lesswrong.com/posts/Nx6orWyRaHGN86aSn/there-is-a-line-in-the-sand-just-not-where-you-think-it-is)

[Wuschel Schulz](https://www.lesswrong.com/users/wuschel-schulz)

3y

3

[View more](https://www.lesswrong.com/users/wuschel-schulz)

Curated and popular this week

140[Comparing risk from internally-deployed AI to insider and outsider threats from humans](https://www.lesswrong.com/posts/DCQ8GfzCqoBzgziew/comparing-risk-from-internally-deployed-ai-to-insider-and)

[Ω](https://alignmentforum.org/posts/DCQ8GfzCqoBzgziew/comparing-risk-from-internally-deployed-ai-to-insider-and)

[Buck](https://www.lesswrong.com/users/buck)

5d

20

234[Generalized Hangriness: A Standard Rationalist Stance Toward Emotions](https://www.lesswrong.com/posts/naAeSkQur8ueCAAfY/generalized-hangriness-a-standard-rationalist-stance-toward)

[johnswentworth](https://www.lesswrong.com/users/johnswentworth)

5d

19

164[Surprises and learnings from almost two months of Leo Panickssery](https://www.lesswrong.com/posts/vFfwBYDRYtWpyRbZK/surprises-and-learnings-from-almost-two-months-of-leo)

[Nina Panickssery](https://www.lesswrong.com/users/nina-panickssery)

2d

4

[6Comments](#comments)