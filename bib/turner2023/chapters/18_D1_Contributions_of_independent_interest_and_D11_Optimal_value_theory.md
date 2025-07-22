## D.1 Contributions of independent interest

We developed new basic MDP theory by exploring the structural properties of visit distribution functions. Echoing Wang et al. [2007, 2008], we believe that this area is interesting and underexplored.

## D.1.1 Optimal value theory

Lemma E.40 shows that f ( γ ∗ ) := lim γ ∗ → γ (1 -γ ∗ ) V ∗ R ( s, γ ∗ ) is Lipschitz continuous on γ ∈ [0 , 1] , with Lipschitz constant depending only on ‖ R ‖ 1 . For all states s and policies π ∈ Π , corollary E.5 shows that V π R ( s, γ ) is rational on γ .

Optimal value has a well-known dual formulation: V ∗ R ( s, γ ) = max f ∈F ( s ) f ( γ ) glyph[latticetop] r .

Lemma E.34 ( ∀ γ ∈ [0 , 1) : V ∗ R ( s, γ ) = max f ∈F nd ( s ) f ( γ ) glyph[latticetop] r ) .

In a fixed rewardless MDP, lemma E.34 may enable more efficient computation of optimal value functions for multiple reward functions.