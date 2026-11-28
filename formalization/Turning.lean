import Mathlib.Topology.MetricSpace.Pseudo.Lemmas
import Mathlib.Topology.Order.Basic
import Mathlib.Tactic
open Filter Topology
namespace TurningObstruction
/-- Both image arcs of the same curve must be counted: the local arc has a
large turning witness, and the other passes through a fixed separated point. -/
theorem no_uniform_turning {S : Type*} [PseudoMetricSpace S]
    (z a b : ℕ → S) (w zlim : S) (A B Klocal : ℕ → ℝ)
    (local_witness : ∀ n, dist (z n) (a n) ≤ A n)
    (other_witness : ∀ n, dist (z n) w ≤ B n)
    (separated : 0 < dist zlim w) (hz : Tendsto z atTop (𝓝 zlim))
    (endpoints : Tendsto (fun n => dist (z n) (b n)) atTop (𝓝 0))
    (nonzero : ∀ n, 0 < dist (z n) (b n))
    (diverges : Tendsto Klocal atTop atTop)
    (distortion : ∀ n, Klocal n * dist (z n) (b n) ≤ dist (z n) (a n)) :
    ¬ ∃ C : ℝ, ∀ n, min (A n) (B n) ≤ C * dist (z n) (b n) := by
  rintro ⟨C,hC⟩
  have local_big : ∀ᶠ n in atTop, C < Klocal n := diverges.eventually (eventually_gt_atTop C)
  have limitC : Tendsto (fun n => C * dist (z n) (b n)) atTop (𝓝 0) := by
    simpa using endpoints.const_mul C
  have sepLimit : Tendsto (fun n => dist (z n) w) atTop (𝓝 (dist zlim w)) :=
    hz.dist tendsto_const_nhds
  have other_big := Filter.Tendsto.eventually_lt limitC sepLimit separated
  obtain ⟨n, hn, hw⟩ := (local_big.and other_big).exists
  have left := mul_lt_mul_of_pos_right hn (nonzero n)
  have ha := left.trans_le ((distortion n).trans (local_witness n))
  have hb := hw.trans_le (other_witness n)
  exact (lt_min ha hb).not_ge (hC n)
end TurningObstruction
#print axioms TurningObstruction.no_uniform_turning
