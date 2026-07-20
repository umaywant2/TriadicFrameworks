# **ct_example_annotations.md**  
### *Human‑readable explanation of every field in `ct_example.json`*

This document explains the meaning of each field in the **Conscious Transfer Substrate Map v1** example instance.  
It is written for clarity, not for formal specification — the schema remains the authoritative source.

---

# **1. Behavioral Layer**

The behavioral layer captures **observable, repeatable patterns** in how an agent learns and performs tasks.

## **1.1 Conditioning Models**

### **classical.cs_us_mapping**  
Pairs of stimuli showing which conditioned stimulus (CS) predicts which unconditioned stimulus (US).  
Example: “tone → airpuff” means the tone reliably precedes an airpuff.

### **classical.acquisition_rate**  
How quickly the agent learns the CS–US association.

### **classical.extinction_rate**  
How quickly the association fades when the CS is no longer followed by the US.

### **operant.reinforcement_schedule**  
The rule governing when rewards are delivered (e.g., variable interval 30 seconds).

### **operant.learning_rate**  
How strongly new outcomes update behavior.

### **operant.discount_factor**  
How much future rewards matter relative to immediate ones.

---

## **1.2 Performance Metrics**

### **reaction_time_distribution**  
A sample of reaction times (in milliseconds) from a standard task.

### **accuracy**  
Proportion of correct responses.

### **error_types**  
Categories of mistakes the agent makes (e.g., omissions, commissions).

### **speed_accuracy_tradeoff.slope / intercept**  
How the agent balances speed vs. accuracy — a stable behavioral signature.

---

# **2. Cognitive Layer**

The cognitive layer captures **task‑bound computational operators** that survive RTT filtering.

## **2.1 Working Memory**

### **capacity**  
How many items can be actively maintained at once.

### **decay_rate**  
How quickly information fades without rehearsal.

### **refresh_rate**  
How quickly the agent can refresh or cycle items to keep them active.

---

## **2.2 Attention**

### **selective_filter_strength**  
How effectively irrelevant information is filtered out.

### **sustained_attention_stability**  
How consistently attention is maintained over time.

### **switching_cost**  
Extra time required to switch between tasks or rules.

---

## **2.3 Decision Models**

### **drift_diffusion.drift_rate**  
How quickly evidence accumulates toward a decision.

### **drift_diffusion.boundary_separation**  
How cautious or bold the decision threshold is.

### **drift_diffusion.non_decision_time**  
Time spent on perception and motor execution, not decision‑making.

### **signal_detection.sensitivity_d_prime**  
How well the agent distinguishes signal from noise.

### **signal_detection.criterion_c**  
Bias toward saying “yes” or “no” when uncertain.

---

## **2.4 Learning Models**

### **reinforcement_learning.learning_rate**  
How strongly new outcomes update value estimates.

### **reinforcement_learning.exploration_rate**  
How often the agent tries new actions instead of exploiting known ones.

### **reinforcement_learning.reward_sensitivity**  
How strongly rewards influence behavior.

---

# **3. Measurement Layer**

The measurement layer defines **how the substrate is validated**, not the substrate itself.

## **3.1 Psychometrics**

### **reliability_alpha**  
Internal consistency of measurement instruments.

### **test_retest_stability**  
How stable scores are across repeated testing.

### **factor_structure**  
Latent dimensions extracted from performance (e.g., working memory, attention).

---

## **3.2 Neuropsych Tests**

### **task_battery.task_name**  
Name of a standardized cognitive test.

### **task_battery.score**  
Raw performance score.

### **task_battery.normative_z**  
How the score compares to population norms (in standard deviations).

---

# **4. Anchoring Constraints**

These are **biological correlates** that meet RTT criteria — stable, traceable, and functionally meaningful.

## **4.1 Circuit Mappings**

### **region**  
Brain region with a known functional role.

### **associated_function**  
What cognitive/behavioral process the region supports.

### **lesion_effect**  
What happens when the region is damaged — a functional anchor.

---

## **4.2 Neurophysiological Signatures**

### **task**  
The task during which the signature appears.

### **frequency_band**  
EEG/MEG frequency or ERP component.

### **amplitude**  
Strength of the signal.

### **latency**  
Time delay between stimulus and neural response.

---

## **4.3 Pharmacological Profiles**

### **agent**  
Drug or compound with a known effect profile.

### **receptor_target**  
Primary biological target (e.g., dopamine transporter).

### **effect_profile**  
How the agent modulates behavior or cognitive parameters.

---

# **How to Use This File**

This annotation file is meant to:

- help researchers understand the meaning of each field  
- support onboarding into the Conscious Transfer substrate  
- clarify how the example instance relates to the schema  
- maintain conceptual cleanliness without narrative drift  

It is not a substitute for the schema — it is a **guide** to interpreting instances.
