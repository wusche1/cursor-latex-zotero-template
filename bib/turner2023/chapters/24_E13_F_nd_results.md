## E.1.3 F nd results

Proposition E.30 (How to transfer optimal policy sets across discount rates) . Suppose reward function R has optimal policy set Π ∗ ( R,γ ) at discount rate γ ∈ (0 , 1) . For any γ ∗ ∈ (0 , 1) , we can construct a reward function R ′ such that Π ∗ ( R ′ , γ ∗ ) = Π ∗ ( R,γ ) . Furthermore, V ∗ R ′ ( · , γ ∗ ) = V ∗ R ( · , γ ) .

Proof. Let R be any reward function. Suppose γ ∗ ∈ (0 , 1) and construct R ′ ( s ) := V ∗ R ( s, γ ) -γ ∗ max a E s ′ T ( s,a ) [ V ∗ R ( s ′ , γ ) ] .

<!-- formula-not-decoded -->

Let π ∈ Π be any policy. By the definition of optimal policies, π ∈ Π ∗ ( R ′ , γ ∗ ) iff for all s :

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

By the Bellman equations, R ′ ( s ) = V ∗ R ′ ( s, γ ∗ ) -γ ∗ max a ∈A E s ′ ∼ T ( s,a ) [ V ∗ R ′ ( s ′ , γ ∗ ) ] . By the definition of R ′ , V ∗ R ′ ( · , γ ∗ ) = V ∗ R ( · , γ ) must be the unique solution to the Bellman equations for R ′ at γ ∗ . Therefore, eq. (74) holds. Equation (75) follows by plugging in R ′ := V ∗ R ( s, γ ) -γ ∗ max a ∈A E s ′ ∼ T ( s,a ) [ V ∗ R ( s ′ , γ ) ] to eq. (74) and doing algebraic manipulation. Equation (76) follows because γ ∗ &gt; 0 .

<!-- formula-not-decoded -->

Definition E.31 (Evaluating sets of visit distribution functions at γ ) . For γ ∈ (0 , 1) , define F ( s, γ ) := { f ( γ ) | f ∈ F ( s ) } and F nd ( s, γ ) := { f ( γ ) | f ∈ F nd ( s ) } . If F ⊆ F ( s ) , then F ( γ ) := { f ( γ ) | f ∈ F } .

Lemma E.32 (Non-domination across γ values for expectations of visit distributions) . Let ∆ d ∈ ∆ ( R |S| ) be any state distribution and let F := { E s d ∼ ∆ d [ f π,s d ] | π ∈ Π } . f ∈ ND ( F ) iff ∀ γ ∗ ∈ (0 , 1) : f ( γ ∗ ) ∈ ND ( F ( γ ∗ ) ) .

Proof. Let f π ∈ ND ( F ) be strictly optimal for reward function R at discount rate γ ∈ (0 , 1) :

<!-- formula-not-decoded -->

Let γ ∗ ∈ (0 , 1) . By proposition E.30, we can produce R ′ such that Π ∗ ( R ′ , γ ∗ ) = Π ∗ ( R,γ ) . Since the optimal policy sets are equal, lemma E.1 implies that

<!-- formula-not-decoded -->

Therefore, f π ( γ ∗ ) ∈ ND ( F ( γ ∗ ) ) .

The reverse direction follows by the definition of ND ( F ) .

Lemma E.33 ( ∀ γ ∈ (0 , 1) : d ∈ F nd ( s, γ ) iff d ∈ ND ( F ( s, γ ) ) ) .

<!-- formula-not-decoded -->

<!-- formula-not-decoded -->

Proof. ND ( F ( s, γ ) ) = F nd ( s, γ ) by lemma E.33, so apply corollary E.11 with X := F ( s, γ ) .