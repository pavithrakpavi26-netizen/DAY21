content = """
# Types of Machine Learning

## 1. Supervised Learning
Supervised Learning is a type of Machine Learning where the data has labels (correct answers).
The model learns from input-output pairs and predicts outputs for new unseen data.

## 2. Unsupervised Learning
Unsupervised Learning is a type of Machine Learning where the data has no labels.
The model finds hidden patterns or clusters in the data.

## 3. Reinforcement Learning
Reinforcement Learning is a type of Machine Learning where an agent learns by interacting 
with an environment and receives rewards or penalties based on its actions.

---

# Comparison Table

| Learning Type          | Data Has Labels? | How It Learns                          | Real-World Examples |
|------------------------|------------------|----------------------------------------|---------------------|
| Supervised Learning    | Yes              | Learns from input-output pairs        | Spam Detection, House Price Prediction |
| Unsupervised Learning  | No               | Finds hidden patterns or clusters     | Customer Segmentation, Market Basket Analysis |
| Reinforcement Learning | Reward-based     | Learns using rewards & penalties      | Self-driving Cars, Game Playing AI |

---

# Why Choosing the Correct Type Matters

Choosing the wrong learning framework can cause your model to fail.
For example:
- Using Unsupervised Learning for spam detection will not work because spam detection needs labeled data.
- Using Supervised Learning without labels makes training impossible.
- Using Reinforcement Learning for simple classification makes the system unnecessarily complex.
"""

with open("Day21_ML_Types_Comparison.md", "w") as file:
    file.write(content)

print("File 'Day21_ML_Types_Comparison.md' created successfully!")