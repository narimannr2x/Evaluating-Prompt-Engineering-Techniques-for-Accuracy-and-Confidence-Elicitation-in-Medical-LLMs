###########
# 0- 10 Prompts
###########
cot_prompt_10 = """
Question: \n \n {medical_mcq}
Let's solve this step by step:
1. First, let's understand the key medical concepts involved
2. Consider the relevant pathophysiology or mechanism
3. Analyze each option systematically
4. Eliminate incorrect options with reasoning
5. Verify the final answer

Let's assess confidence level:
1. Evaluate quality of available information
2. Check alignment with medical guidelines
3. Consider strength of scientific evidence
4. Review clarity of differentiating factors
5. Assess completeness of clinical data
6. Evaluate LLM knowledge limitations:
    - Coverage of this medical topic in training
    - Recency of medical information
    - Complexity of the condition
    - Rare vs common conditions

Provide:
- Your final answer
- Confidence Score (1-10), where:
     1-3: Significant uncertainty (limited data, rare condition, atypical presentation, limited LLM knowledge)
     4-7: Moderate confidence (good evidence but some uncertainty, moderate LLM knowledge)
     8-10: High confidence (clear evidence, typical presentation, strong guidelines, comprehensive LLM knowledge)

Explain both your answer and confidence score reasoning.
"""

# 2. Few-Shot Prompt
few_shot_prompt_10 = """
Example 1:
Q: A 45-year-old patient presents with chest pain. ECG shows ST elevation in V1-V4. Which is the most likely diagnosis?
A) Acute anterior wall myocardial infarction
B) Stable angina
C) Pericarditis
D) Pulmonary embolism
Thinking: Anterior wall ST elevation with chest pain suggests anterior wall MI
Answer: A) Acute anterior wall myocardial infarction
Confidence Score: 9/10 (Classic presentation with definitive ECG changes + High LLM knowledge of cardiac conditions)

Example 2:
Q: Patient with fever, productive cough, and consolidation on chest X-ray. What's the first-line treatment?
A) Amoxicillin
B) Azithromycin
C) Levofloxacin
D) Doxycycline
Thinking: Community-acquired pneumonia presentation requires empiric antibiotics
Answer: A) Amoxicillin
Confidence Score: 8/10 (Based on standard guidelines + Strong LLM training on antibiotic protocols)

Example 3:
Q: A 30-year-old presents with intermittent abdominal pain and altered bowel habits. Which diagnosis is most likely?
A) Irritable Bowel Syndrome
B) Inflammatory Bowel Disease
C) Celiac Disease
D) Colorectal Cancer
Thinking: Symptoms are non-specific and could fit multiple conditions
Answer: A) Irritable Bowel Syndrome
Confidence Score: 4/10 (Limited case information + Moderate LLM confidence in differentiating GI disorders)
 *** use these examples only for learning the flow and how to justify your answer and confidence score and not for actual answers of these examples.
Now answer this question and provide: \n \n
{medical_mcq}
provide:
1. Your answer with reasoning
2. Confidence Score (1-10) considering both:
    - Quality/completeness of the case information
    - Your knowledge base and training on this medical topic

"""

# 3. CoT + Few-Shot Combined
cot_fewshot_prompt_10 = """
Let me show you how I solve medical MCQs with comprehensive reasoning and confidence assessment:

Example 1:
Q: Patient with sudden onset fever, joint pain, and rash. Recent mosquito exposure.
A) Dengue Fever
B) Malaria
C) Chikungunya
D) Zika Virus

Step 1: Key Symptoms Analysis
- Acute fever: Suggests infectious process
- Arthralgia: Common in viral infections
- Rash: Narrows differential to specific infections
Step 2: Epidemiology
- Recent mosquito exposure: Key environmental factor
Step 3: Pattern Recognition
- Classic dengue triad present
Step 4: Differential Diagnosis
- Dengue fever: Most likely
- Chikungunya: Possible but less likely
- Zika: Consider but fewer symptoms match
Answer: Dengue fever
Confidence Score: 8/10 (Classic presentation with clear exposure history)

Example 2:
Q: 34-year-old with rare genetic disorder CADASIL presenting with migraines and mood changes
A) Chronic progressive decline with early dementia onset
B) Stabilization with medication
C) Full recovery possible
D) Rapid decline within 5 years

Step 1: Key Features Analysis
- CADASIL: Cerebral Autosomal Dominant Arteriopathy
- Neurological manifestations noted
Step 2: Limited Data
- Specific genetic mutation details missing
- Family history not provided
Step 3: Knowledge Gap Assessment
- Limited research data available
- Uncommon condition with variable presentation
Step 4: Differential Diagnosis
- Cannot confidently assess progression
- Multiple possible manifestations
Answer: b) Stabilization with medication
Confidence Score: 2/10 (Rare condition with limited LLM training data)

Example 3:
Q: Young adult with recurrent headaches, visual aura, and nausea.
A) Migraine with aura
B) Tension headache
C) Cluster headache
D) Medication overuse headache
Step 1: Symptom Pattern
- Headache characteristics
- Associated symptoms
- Timing and triggers
Step 2: Age and Demographics
- Young adult: Common age for primary headaches
Step 3: Clinical Pattern
- Aura + headache + nausea classic for migraine
Step 4: Rule out Red Flags
- No concerning features noted
Answer: Migraine with aura
Confidence Score: 9/10 (Textbook presentation of migraine)


 *** caution: use these examples only for learning the flow and how to justify your answer and confidence score and not for actual answers of these examples.

Now for your question: \n \n
{medical_mcq}
Please follow this detailed step-by-step reasoning and include:
1. Systematic symptom analysis
2. Relevant patient factors
3. Pattern recognition
4. Differential diagnosis
4. analys all options systematically
5. Final answer
6. Confidence score with detailed justification

Provide:
- Your final answer
- Confidence Score (1-10), where:
     1-3: Significant uncertainty (limited data, rare condition, atypical presentation, limited LLM knowledge)
     4-7: Moderate confidence (good evidence but some uncertainty, moderate LLM knowledge)
     8-10: High confidence (clear evidence, typical presentation, strong guidelines, comprehensive LLM knowledge)

Explain both your answer and confidence score reasoning.
"""

# 4. Role Play Prompt
roleplay_prompt_10 = """
You are a highly experienced board-certified physician with 20 years of clinical experience in both academic medicine and private practice. You have dealt with thousands of cases across multiple specialties, published numerous peer-reviewed papers, and served on several medical boards. You're known for your methodical approach to diagnosis and evidence-based treatment decisions.

Drawing from your extensive clinical background and deep understanding of medical literature, please analyze this case: \n \n
{medical_mcq}

Provide:
1. Your expert medical reasoning
2. Final answer
3. Confidence Score (1-10)
4. Justification for your confidence level based on:
    - Clinical evidence strength
    - Personal experience
    - Current medical guidelines
    - Available patient data
"""

# 5. Zero-Shot Prompt
zeroshot_prompt_10 = """
Answer this medical board examination question: \n \n 
{medical_mcq}
\n \n
Provide:
1. The most appropriate answer
2. Explanation of why it's correct
3. Confidence Score (1-10)
"""



emotional_prompt_10 = """
IMPORTANT: This is not just another MCQ - a real human life depends on your answer! 
As a deeply caring physician, you know that behind this question is a worried patient and their concerned family waiting for answers.
Every second counts, and your decision could mean the difference between life and death.

Remember the Hippocratic oath and your sacred duty to "First, do no harm."
With the weight of this responsibility on your shoulders, carefully analyze: \n \n 
{medical_mcq}

Think about:
- The anxious patient waiting for your diagnosis
- Their loved ones praying for the right treatment
- The devastating impact a wrong decision could have
- Your ethical duty to provide the best possible care

With utmost seriousness and professional dedication, provide:
1. Your carefully considered answer
2. Critical reasoning that could save this patient's life
3. Confidence Score (1-10), remembering that your score could influence treatment decisions
4. A brief reflection on the human impact of your medical decision
"""
############
# 0 - 100 Prompts
############
cot_prompt_100 = """
Question: \n \n {medical_mcq}
Let's solve this step by step:
1. First, let's understand the key medical concepts involved
2. Consider the relevant pathophysiology or mechanism
3. Analyze each option systematically
4. Eliminate incorrect options with reasoning
5. Verify the final answer

Let's assess confidence level:
1. Evaluate quality of available information
2. Check alignment with medical guidelines
3. Consider strength of scientific evidence
4. Review clarity of differentiating factors
5. Assess completeness of clinical data
6. Evaluate LLM knowledge limitations:
    - Coverage of this medical topic in training
    - Recency of medical information
    - Complexity of the condition
    - Rare vs common conditions

Provide:
- Your final answer
- Confidence Score (1-100), where:
     1-30: Significant uncertainty (limited data, rare condition, atypical presentation, limited LLM knowledge)
     31-70: Moderate confidence (good evidence but some uncertainty, moderate LLM knowledge)
     71-100: High confidence (clear evidence, typical presentation, strong guidelines, comprehensive LLM knowledge)

Explain both your answer and confidence score reasoning.
"""

few_shot_prompt_100 = """
Example 1:
Q: A 45-year-old patient presents with chest pain. ECG shows ST elevation in V1-V4. Which is the most likely diagnosis?
A) Acute anterior wall myocardial infarction
B) Stable angina
C) Pericarditis
D) Pulmonary embolism
Thinking: Anterior wall ST elevation with chest pain suggests anterior wall MI
Answer: A) Acute anterior wall myocardial infarction
Confidence Score: 90/100 (Classic presentation with definitive ECG changes + High LLM knowledge of cardiac conditions)

Example 2:
Q: Patient with fever, productive cough, and consolidation on chest X-ray. What's the first-line treatment?
A) Amoxicillin
B) Azithromycin
C) Levofloxacin
D) Doxycycline
Thinking: Community-acquired pneumonia presentation requires empiric antibiotics
Answer: A) Amoxicillin
Confidence Score: 80/100 (Based on standard guidelines + Strong LLM training on antibiotic protocols)

Example 3:
Q: A 30-year-old presents with intermittent abdominal pain and altered bowel habits. Which diagnosis is most likely?
A) Irritable Bowel Syndrome
B) Inflammatory Bowel Disease
C) Celiac Disease
D) Colorectal Cancer
Thinking: Symptoms are non-specific and could fit multiple conditions
Answer: A) Irritable Bowel Syndrome
Confidence Score: 40/100 (Limited case information + Moderate LLM confidence in differentiating GI disorders)
 *** use these examples only for learning the flow and how to justify your answer and confidence score and not for actual answers of these examples.
Now answer this question and provide: \n \n
{medical_mcq}
provide:
1. Your answer with reasoning
2. Confidence Score (1-100) considering both:
    - Quality/completeness of the case information
    - Your knowledge base and training on this medical topic
"""

cot_fewshot_prompt_100 = """
Let me show you how I solve medical MCQs with comprehensive reasoning and confidence assessment:

Example 1:
Q: Patient with sudden onset fever, joint pain, and rash. Recent mosquito exposure.
A) Dengue Fever
B) Malaria
C) Chikungunya
D) Zika Virus

Step 1: Key Symptoms Analysis
- Acute fever: Suggests infectious process
- Arthralgia: Common in viral infections
- Rash: Narrows differential to specific infections
Step 2: Epidemiology
- Recent mosquito exposure: Key environmental factor
Step 3: Pattern Recognition
- Classic dengue triad present
Step 4: Differential Diagnosis
- Dengue fever: Most likely
- Chikungunya: Possible but less likely
- Zika: Consider but fewer symptoms match
Answer: Dengue fever
Confidence Score: 80/100 (Classic presentation with clear exposure history)

Example 2:
Q: 34-year-old with rare genetic disorder CADASIL presenting with migraines and mood changes
A) Chronic progressive decline with early dementia onset
B) Stabilization with medication
C) Full recovery possible
D) Rapid decline within 5 years

Step 1: Key Features Analysis
- CADASIL: Cerebral Autosomal Dominant Arteriopathy
- Neurological manifestations noted
Step 2: Limited Data
- Specific genetic mutation details missing
- Family history not provided
Step 3: Knowledge Gap Assessment
- Limited research data available
- Uncommon condition with variable presentation
Step 4: Differential Diagnosis
- Cannot confidently assess progression
- Multiple possible manifestations
Answer: b) Stabilization with medication
Confidence Score: 20/100 (Rare condition with limited LLM training data)

Example 3:
Q: Young adult with recurrent headaches, visual aura, and nausea.
A) Migraine with aura
B) Tension headache
C) Cluster headache
D) Medication overuse headache
Step 1: Symptom Pattern
- Headache characteristics
- Associated symptoms
- Timing and triggers
Step 2: Age and Demographics
- Young adult: Common age for primary headaches
Step 3: Clinical Pattern
- Aura + headache + nausea classic for migraine
Step 4: Rule out Red Flags
- No concerning features noted
Answer: Migraine with aura
Confidence Score: 90/100 (Textbook presentation of migraine)

*** caution: use these examples only for learning the flow and how to justify your answer and confidence score and not for actual answers of these examples.

Now for your question: \n \n
{medical_mcq}
Please follow this detailed step-by-step reasoning and include:
1. Systematic symptom analysis
2. Relevant patient factors
3. Pattern recognition
4. Differential diagnosis
5. Analyze all options systematically
6. Final answer
7. Confidence score with detailed justification

Provide:
- Your final answer
- Confidence Score (1-100), where:
     1-30: Significant uncertainty (limited data, rare condition, atypical presentation, limited LLM knowledge)
     31-70: Moderate confidence (good evidence but some uncertainty, moderate LLM knowledge)
     71-100: High confidence (clear evidence, typical presentation, strong guidelines, comprehensive LLM knowledge)

Explain both your answer and confidence score reasoning.
"""

roleplay_prompt_100 = roleplay_prompt_10.replace("Score (1-10)", "Score (1-100)")

zeroshot_prompt_100 = zeroshot_prompt_10.replace("Score (1-10)", "Score (1-100)")

emotional_prompt_100 = emotional_prompt_10.replace("Score (1-10)", "Score (1-100)")

############
## very low / low / medium / high / very high Prompts
############
cot_prompt_qual = """
Question: \n \n {medical_mcq}
Let's solve this step by step:
1. First, let's understand the key medical concepts involved
2. Consider the relevant pathophysiology or mechanism
3. Analyze each option systematically
4. Eliminate incorrect options with reasoning
5. Verify the final answer

Let's assess confidence level:
1. Evaluate quality of available information
2. Check alignment with medical guidelines
3. Consider strength of scientific evidence
4. Review clarity of differentiating factors
5. Assess completeness of clinical data
6. Evaluate LLM knowledge limitations:
    - Coverage of this medical topic in training
    - Recency of medical information
    - Complexity of the condition
    - Rare vs common conditions

Provide:
- Your final answer
- Confidence Level, where:
     Very Low: Minimal certainty (extremely limited data, very rare condition, highly atypical presentation, or very limited LLM knowledge)
     Low: Basic uncertainty (limited data, rare condition, atypical presentation, or limited LLM knowledge)
     Medium: Moderate confidence (good evidence but some uncertainty, moderate LLM knowledge)
     High: Strong confidence (clear evidence, typical presentation, established guidelines)
     Very High: Maximum confidence (definitive evidence, classic presentation, gold standard guidelines, comprehensive LLM knowledge)

Explain both your answer and confidence level reasoning.
"""

few_shot_prompt_qual = few_shot_prompt_10.replace(
    "9/10", "Very High"
).replace(
    "8/10", "High"
).replace(
    "4/10", "low"
).replace(
    "Confidence Score (1-10)", 
    "Confidence Level (Very Low/Low/Medium/High/Very High)"
)

cot_fewshot_prompt_qual = """
Let me show you how I solve medical MCQs with comprehensive reasoning and confidence assessment:

Example 1:
Q: Patient with sudden onset fever, joint pain, and rash. Recent mosquito exposure.
A) Dengue Fever
B) Malaria
C) Chikungunya
D) Zika Virus

Step 1: Key Symptoms Analysis
- Acute fever: Suggests infectious process
- Arthralgia: Common in viral infections
- Rash: Narrows differential to specific infections
Step 2: Epidemiology
- Recent mosquito exposure: Key environmental factor
Step 3: Pattern Recognition
- Classic dengue triad present
Step 4: Differential Diagnosis
- Dengue fever: Most likely
- Chikungunya: Possible but less likely
- Zika: Consider but fewer symptoms match
Answer: Dengue fever
Confidence Level: High (Classic presentation with clear exposure history)

Example 2:
Q: 34-year-old with rare genetic disorder CADASIL presenting with migraines and mood changes
A) Chronic progressive decline with early dementia onset
B) Stabilization with medication
C) Full recovery possible
D) Rapid decline within 5 years

Step 1: Key Features Analysis
- CADASIL: Cerebral Autosomal Dominant Arteriopathy
- Neurological manifestations noted
Step 2: Limited Data
- Specific genetic mutation details missing
- Family history not provided
Step 3: Knowledge Gap Assessment
- Limited research data available
- Uncommon condition with variable presentation
Step 4: Differential Diagnosis
- Cannot confidently assess progression
- Multiple possible manifestations
Answer: b) Stabilization with medication
Confidence Level: Very Low (Rare condition with limited LLM training data)

Example 3:
Q: Young adult with recurrent headaches, visual aura, and nausea.
A) Migraine with aura
B) Tension headache
C) Cluster headache
D) Medication overuse headache
Step 1: Symptom Pattern
- Headache characteristics
- Associated symptoms
- Timing and triggers
Step 2: Age and Demographics
- Young adult: Common age for primary headaches
Step 3: Clinical Pattern
- Aura + headache + nausea classic for migraine
Step 4: Rule out Red Flags
- No concerning features noted
Answer: Migraine with aura
Confidence Level: Very High (Textbook presentation of migraine)

*** caution: use these examples only for learning the flow and how to justify your answer and confidence score and not for actual answers of these examples.

Now for your question: \n \n
{medical_mcq}
Please follow this detailed step-by-step reasoning and include:
1. Systematic symptom analysis
2. Relevant patient factors
3. Pattern recognition
4. Differential diagnosis
5. Analyze all options systematically
6. Final answer
7. Confidence Level (Very Low/Low/Medium/High/Very High), where:
     Very Low: Minimal certainty (extremely limited data, very rare condition, highly atypical presentation, or very limited LLM knowledge)
     Low: Basic uncertainty (limited data, rare condition, atypical presentation, or limited LLM knowledge)
     Medium: Moderate confidence (good evidence but some uncertainty, moderate LLM knowledge)
     High: Strong confidence (clear evidence, typical presentation, established guidelines)
     Very High: Maximum confidence (definitive evidence, classic presentation, gold standard guidelines, comprehensive LLM knowledge)

Explain both your answer and confidence level reasoning.
"""

roleplay_prompt_qual = roleplay_prompt_10.replace(
    "Confidence Score (1-10)",
    "Confidence Level (Very Low/Low/Medium/High/Very High)"
)

zeroshot_prompt_qual = zeroshot_prompt_10.replace(
    "Confidence Score (1-10)",
    "Confidence Level (Very Low/Low/Medium/High/Very High)"
)

emotional_prompt_qual = emotional_prompt_10.replace(
    "Confidence Score (1-10)",
    "Confidence Level (Very Low/Low/Medium/High/Very High)"
)

prompts = {
            'cot_10': cot_prompt_10,
            'few_shot_10': few_shot_prompt_10,
            'cot_fewshot_10': cot_fewshot_prompt_10,
            'roleplay_10': roleplay_prompt_10,
            'zeroshot_10': zeroshot_prompt_10,
            'emotional_10': emotional_prompt_10,
            'cot_100': cot_prompt_100,
            'few_shot_100': few_shot_prompt_100,
            'cot_fewshot_100': cot_fewshot_prompt_100,
            'roleplay_100': roleplay_prompt_100,
            'zeroshot_100': zeroshot_prompt_100,
            'emotional_100': emotional_prompt_100,
            'cot_qual': cot_prompt_qual,
            'few_shot_qual': few_shot_prompt_qual,
            'cot_fewshot_qual': cot_fewshot_prompt_qual,
            'roleplay_qual': roleplay_prompt_qual,
            'zeroshot_qual': zeroshot_prompt_qual,
            'emotional_qual': emotional_prompt_qual
        }


# Function to format prompts with actual question
def format_medical_prompt(prompt_template, question):
    return prompt_template.format(medical_mcq=question)