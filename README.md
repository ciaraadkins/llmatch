# LLMatch Algorithm 2.0

LLMatch Algorithm 2.0 is a methodology for ranking and recommending language models based on user preferences and model attributes. This project provides a detailed mathematical framework and a proof-of-concept implementation in Python.

## Overview

The LLMatch Algorithm 2.0 takes into account various user preferences, such as security, energy usage, model freshness, context window, coding ability, budget, and speed. It then ranks the available language models based on how closely they align with the user's preferences and their performance on benchmarks like HumanEval.

## Methodology

The methodology involves the following steps:

1. **User Preference Vector (U)**: Construct a vector representing the user's preferences for different model attributes. Each component of the vector is mapped to a specific attribute and ranges from 0 to 1 or -1 to 1, indicating preference intensity or direction.

2. **Model Attribute Matrix (M)**: Create a matrix where each row represents a language model, and each column represents a normalized attribute value.

3. **Weight Vector (W)**: Define a weight vector that adjusts the impact of each model attribute based on user preferences. Higher weights indicate greater importance of the corresponding attribute in the ranking process.

4. **Distance Calculation**: Calculate the weighted Euclidean distance between the user preference vector and each model's attribute vector. This distance represents how closely a model aligns with the user's preferences.

5. **Scoring and Ranking**:
   - Normalize the MMLU scores (representing model quality) and the calculated distances to ensure they are comparable.
   - Compute a composite score for each model by multiplying the normalized MMLU score and the inverted normalized distance.
   - Rank the models based on their composite scores in descending order.

For a detailed explanation of the mathematical framework and methodology, please refer to the [LLMatch Algorithm 2.0 Methodology document](https://github.com/ciaraadkins/llmatch/blob/main/LLMatch_Methodology.pdf).

## Proof of Concept

A proof-of-concept implementation of the LLMatch Algorithm 2.0 is available in the [LLMatch POC Jupyter Notebook](https://github.com/ciaraadkins/llmatch/blob/main/LLMatch_POC_2_0.ipynb). The notebook demonstrates how to:

1. Load and preprocess the language model data
2. Collect user preferences
3. Construct the user preference vector, model attribute matrix, and weight vector
4. Calculate distances and rank the models based on user preferences and model attributes
5. Display the top recommended models

## Usage

To use the LLMatch Algorithm 2.0 proof of concept:

1. Clone this repository
2. Open the [LLMatch POC Jupyter Notebook]([link-to-notebook](https://github.com/ciaraadkins/llmatch/blob/main/LLMatch_POC_2_0.ipynb)) in Google Colab or Jupyter Notebook
3. Follow the instructions in the notebook to input your preferences and run the algorithm
4. View the top recommended language models based on your preferences

## Contributing

Contributions to the LLMatch Algorithm 2.0 project are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the [MIT License](https://opensource.org/license/mit).

## Contact

For any questions or inquiries, please contact [Ciara Adkins](mailto:adkins.ciara@gmail.com).
