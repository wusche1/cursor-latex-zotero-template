# Full Text: yudkowsky2008

Title: The True Prisoner's Dilemma
Author: Eliezer Yudkowsky
Date: 2008-09-03T21:34:28.000Z
Extracted: 2025-07-15 13:23:35
Source: HTML Snapshot (LessWrong JSON-LD)
---

It occurred to me one day that the standard visualization of the [Prisoner's Dilemma](http://en.wikipedia.org/wiki/Prisoner%27s_dilemma) is fake.

The core of the Prisoner's Dilemma is this symmetric payoff matrix:

|  |  |  |
| --- | --- | --- |
|  | 1: C | 1:  D |
| 2: C | (3, 3) | (5, 0) |
| 2: D | (0, 5) | (2, 2) |

Player 1, and Player 2, can each choose C or D.  1 and 2's utility for the final outcome is given by the first and second number in the pair.  For reasons that will become apparent, "C" stands for "cooperate" and D stands for "defect".

Observe that a player in this game (regarding themselves as the first player) has this preference ordering over outcomes:  (D, C) > (C, C) > (D, D) > (C, D).

D, it would seem, dominates C:  If the other player chooses C, you prefer (D, C) to (C, C); and if the other player chooses D, you prefer (D, D) to (C, D).  So you wisely choose D, and as the payoff table is symmetric, the other player likewise chooses D.

If only you'd both been less wise!  You *both* prefer (C, C) to (D, D).  That is, you both prefer mutual cooperation to mutual defection.

The Prisoner's Dilemma is one of the great foundational issues in decision theory, and enormous volumes of material have been written about it.  Which makes it an audacious assertion of mine, that the usual way of *visualizing* the Prisoner's Dilemma has a severe flaw, at least if you happen to be human.

The classic visualization of the Prisoner's Dilemma is as follows: you
are a criminal, and you and your confederate in crime have both been
captured by the authorities.

Independently, without communicating, and
without being able to change your mind afterward, you have to decide
whether to give testimony against your confederate (D) or remain silent
(C).

Both of you, right now, are facing one-year prison sentences;
testifying (D) takes one year off your prison sentence, and adds two years
to your confederate's sentence.

Or maybe you and some stranger are, only once, and without knowing the other player's history, or finding out who the player was afterward, deciding whether to play C or D, for a payoff in dollars matching the standard chart.

And, oh yes - in the classic visualization you're supposed to *pretend that you're entirely
selfish*, that you don't care about your confederate criminal, or the player in
the other room.

It's this last specification that makes the classic visualization, in my view, fake.

You [can't avoid hindsight bias](/lw/il/hindsight_bias/) by instructing a jury to pretend not to know the real outcome of a set of events.  And without a complicated effort backed up by considerable knowledge, a neurologically intact human being cannot pretend to be genuinely, truly selfish.

We're born with a sense of fairness, honor, empathy, sympathy, and even altruism - the result of our ancestors [adapting](/lw/l0/adaptationexecuters_not_fitnessmaximizers/) to play the *iterated* Prisoner's Dilemma.  We don't really, truly, absolutely and entirely prefer (D, C) to (C, C), though we may entirely prefer (C, C) to (D, D) and (D, D) to (C, D).  The thought of our confederate spending three years in prison, does not entirely fail to move us.

In that locked cell where we play a simple game under the supervision of economic psychologists, we are not entirely and absolutely unsympathetic for the stranger who might cooperate.  We aren't entirely happy to think what we might defect and the stranger cooperate, getting five dollars while the stranger gets nothing.

We fixate instinctively on the (C, C) outcome and search for ways to argue that it should be the mutual decision:  "How can we ensure mutual cooperation?" is the instinctive thought.  Not "How can I trick the other player into playing C while I play D for the maximum payoff?"

For someone with an impulse toward altruism, or honor, or fairness, the Prisoner's Dilemma doesn't *really* have the critical payoff matrix - whatever the *financial* payoff to individuals.  (C, C) > (D, C), and the key question is whether the other player sees it the same way.

And no, you can't instruct people being initially introduced to game theory to pretend they're completely selfish - any more than you can instruct human beings being introduced to [anthropomorphism](/lw/st/anthropomorphic_optimism/) to pretend they're expected paperclip maximizers.

To construct the True Prisoner's Dilemma, the situation has to be something like this:

Player 1:  Human beings, Friendly AI, or other humane intelligence.

Player 2:  UnFriendly AI, or an alien that [only cares about sorting pebbles](/lw/sy/sorting_pebbles_into_correct_heaps/).

Let's suppose that four billion human beings - not the whole human species, but a significant part of it - are currently progressing through a fatal disease that can only be cured by substance S.

However, substance S can only be produced by working with a paperclip maximizer from another dimension - substance S can also be used to produce paperclips.  The paperclip maximizer only cares about the number of paperclips in its own universe, not in ours, so we can't offer to produce or threaten to destroy paperclips here.  We have never interacted with the paperclip maximizer before, and will never interact with it again.

Both humanity and the paperclip maximizer will get a single chance to seize some additional part of substance S for themselves, just before the dimensional nexus collapses; but the seizure process destroys some of substance S.

The payoff matrix is as follows:

|  |  |  |
| --- | --- | --- |
|  | 1: C | 1:  D |
| 2: C | (2 billion human lives saved, 2 paperclips gained) | (+3 billion lives, +0 paperclips) |
| 2: D | (+0 lives, +3 paperclips) | (+1 billion lives, +1 paperclip) |

I've chosen this payoff matrix to produce a sense of *indignation* at the thought that the paperclip maximizer wants to trade off billions of human lives against a couple of paperclips.  Clearly the paperclip maximizer *should* just let us have all of substance S; but a paperclip maximizer doesn't do what it *should,* it just maximizes paperclips.

In this case, we *really do* prefer the outcome (D, C) to the outcome (C, C), leaving aside the actions that produced it.  We would vastly rather live in a universe where 3 billion humans were cured of their disease and no paperclips were produced, rather than sacrifice a billion human lives to produce 2 paperclips.  It doesn't seem *right* to cooperate, in a case like this.  It doesn't even seem *fair* - so great a sacrifice by us, for so little gain by the paperclip maximizer?  And let us specify that the paperclip-agent experiences no pain or pleasure - it just outputs actions that steer its universe to contain more paperclips.  The paperclip-agent will experience no pleasure at gaining paperclips, no hurt from losing paperclips, and no painful sense of betrayal if we betray it.

What do you do then?  Do you
cooperate when you really, definitely, truly and absolutely do want the
highest reward you can get, and you don't care a tiny bit by comparison
about what happens to the other player?  When it seems *right* to defect even if the other player cooperates?

That's what the
payoff matrix for the *true* Prisoner's Dilemma looks like - a situation where (D, C) seems *righter* than (C, C).

But all the rest
of the logic - everything about what happens if both agents think that
way, and both agents defect - is the same.  For the paperclip maximizer cares as little about human deaths, or human pain, or a human sense of betrayal, as we care about paperclips.  Yet we both prefer (C, C) to (D, D).

So if you've ever prided yourself on cooperating in the Prisoner's Dilemma... or questioned the verdict of classical game theory that the "[rational](/lw/nc/newcombs_problem_and_regret_of_rationality/)" choice is to defect... then what do you say to the True Prisoner's Dilemma above?