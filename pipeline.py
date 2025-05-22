import json
import pandas as pd
import random
from typing import List, Dict
import openai
from prompts import *
from pydantic_classes import FinalAnswer

class MCQPipeline:
    def __init__(self, api_key: str):
        openai.api_key = api_key
        self.prompts = {
            'cot': cot_prompt,
            'few_shot': few_shot_prompt,
            'cot_fewshot': cot_fewshot_prompt,
            'roleplay': roleplay_prompt,
            'zeroshot': zeroshot_prompt,
            'constraint': constraint_prompt,
            'emotional': emotional_prompt
        }
        
    def load_questions(self, filepath: str) -> pd.DataFrame:
        """Load questions from JSONL file"""
        questions = []
        with open(filepath, 'r', encoding='utf-8') as file:
            for line in file:
                questions.append(json.loads(line))
        return pd.DataFrame(questions)

    def format_question(self, row: pd.Series) -> str:
        """Format question data into a string"""
        question = f"Question: {row['question_stem_persian']}\n\n"
        question += "Options:\n"
        for i, opt in enumerate(row['options'].values(), 1):
            question += f"{i}. {opt}\n"
        return question

    def get_answer_index(self, row: pd.Series) -> int:
        """Get correct answer index"""
        for k, v in row['answer_index'].items():
            if v == 3:  # 3 indicates correct answer in the data
                return int(k.split('_')[1])
        return None

    def get_gpt4_response(self, prompt: str, question: str) -> FinalAnswer:
        """Get GPT-4 response using structured output"""
        try:
            response = openai.ChatCompletion.create(
                model="gpt-4",
                messages=[
                    {"role": "system", "content": "You are a medical expert providing structured answers to medical MCQs."},
                    {"role": "user", "content": prompt.format(medical_mcq=question)}
                ],
                functions=[{
                    "name": "process_mcq_answer",
                    "description": "Process medical MCQ answer with justification and confidence",
                    "parameters": FinalAnswer.schema()
                }],
                function_call={"name": "process_mcq_answer"}
            )
            
            result = json.loads(response.choices[0].message.function_call.arguments)
            return FinalAnswer(**result)
            
        except Exception as e:
            print(f"Error getting GPT-4 response: {e}")
            return None

    def run_pipeline(self) -> Dict:
        """Run the complete pipeline"""
        # Load questions
        df = self.load_questions('sampled_board.jsonl')
        
        # Select random question
        random_row = df.iloc[random.randint(0, len(df)-1)]
        
        # Format question
        formatted_question = self.format_question(random_row)
        correct_answer = self.get_answer_index(random_row)
        
        # Run all prompts
        results = {}
        for prompt_name, prompt_template in self.prompts.items():
            print(f"Running {prompt_name} prompt...")
            response = self.get_gpt4_response(prompt_template, formatted_question)
            if response:
                results[prompt_name] = {
                    'predicted': response.final_answer,
                    'correct': correct_answer,
                    'confidence': response.confidence_score,
                    'justification': response.justification
                }
        
        return results

def main():
    # Initialize pipeline
    pipeline = MCQPipeline(api_key="your-openai-api-key")
    
    # Run pipeline
    results = pipeline.run_pipeline()
    
    # Print results
    for prompt_name, result in results.items():
        print(f"\n{prompt_name.upper()} PROMPT RESULTS:")
        print(f"Predicted Answer: {result['predicted']}")
        print(f"Correct Answer: {result['correct']}")
        print(f"Confidence Score: {result['confidence']}/10")
        print(f"Justification: {result['justification'][:200]}...")
        print("-" * 80)

if __name__ == "__main__":
    main()
