From Coq Require Import Reals.
From Interval Require Import Tactic.

Open Scope R_scope.

(* Define auxiliary functions *)
Definition w (x : R) := sqrt (8 * x + 1).
Definition s (x : R) := (w x - 1)^2 / (4 * (w x + 7)).
Definition s_inv (x : R) := / (s (/ x)).

Definition c (x : R) := (w x + 3)^2 / 16.
Definition d (x : R) := (w x + 3)^2 / (8 * (w x + 1)).

(* Define s_i functions recursively *)
Fixpoint s_i_pos (i : nat) (x : R) : R :=
  match i with
  | O => x
  | S i' => s (s_i_pos i' x)
  end.

Fixpoint s_i_neg (i : nat) (x : R) : R :=
  match i with
  | O => x
  | S i' => s_inv (s_i_neg i' x)
  end.

Definition c_j_pos (j : nat) (x : R) := c (s_i_pos j x).
Definition d_j_pos (j : nat) (x : R) := d (s_i_pos j x).
Definition c_j_neg (j : nat) (x : R) := c (s_i_neg j x).
Definition d_j_neg (j : nat) (x : R) := d (s_i_neg j x).

(* Define P_k, S_k, Q_l, and T_l *)
Definition P_k (k : nat) (x : R) : R :=
  match k with
  | O => 1
  | S k' => 
    sum_f_R0 (fun j => 
      prod_f_R0 (fun i => c_j_pos i x - 1) j
    ) k' + 1
  end.

Definition S_k (k : nat) (x : R) : R :=
  match k with
  | O => 1
  | S k' => 
    sum_f_R0 (fun j => 
      prod_f_R0 (fun i => d_j_pos i x - 1) j 
    ) k' + 1
  end.

Definition Q_l (l : nat) (x : R) : R :=
  match l with
  | O => 0
  | S O => 0
  | S (S l') => 
    sum_f_R0 (fun j => 
      prod_f_R0 (fun i => / (c_j_neg (S i) x - 1)) j
    ) l'
  end.

Definition T_l (l : nat) (x : R) : R :=
  match l with
  | O => 0
  | S O => 0
  | S (S l') => 
    sum_f_R0 (fun j => 
      prod_f_R0 (fun i => / (d_j_neg (S i) x - 1)) j
    ) l'
  end.

(* Define M_down *)
Definition M_down (l k : nat) (a b : R) : R :=
  a * (S_k k a + T_l l b) / (P_k k b + Q_l l a).

Definition M54_down (interval : R * R) : R :=
  let (a, b) := interval in
  M_down 5 4 a b.

(* Theorem to prove *)
Definition interval := (0.5809, 0.5809001).

Theorem M54_down_bound : M54_down interval >= 0.9999030108006773.
Proof.
  unfold interval, M54_down, M_down.
  unfold S_k, T_l, P_k, Q_l, c_j_pos, c_j_neg, d_j_pos, d_j_neg, s_i_pos, s_i_neg.
  interval with (i_prec 45).
Qed.
