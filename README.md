# Dzongkha Spell Checker

## Project Overview
The dzongkha spell checker project is designed to provide accurate and efficient spelling correction for the dzongkha language. It addresses the challenges of writing in dzongkha on digital platforms, where spelling errors can hinder clarity and understanding.

## Table of Contents
-[Usage](#usage)
-[Implementation Details](#Implementation Details)
-[Data Structures](#Data Structures)
-[Algorithms](#Algorithms)
-[Challenges and Solutions](#Challenges and Solutions)
-[Future Improvements](#Future Improvements)
-[References](#References)

## Usage

## Implementation Details
Overall structure of the code-- the dzongkha spell checker is organized into various key modules; 
-Input handling: reads and processes text in utf-8 format, ensuring support for dzongkha characters.
-Dictionary Management: maintain a default dictionary of dzongkha words and allows users to load a custom dictionary for specialized vocabulary.
-Spell Checker Logic: Analyzes the input text to identify misspelled words. like, error detection: comparing words against the dictionary.
-Output Formatting: generates output that can be displayed in the terminal, highlighting misspelled words and providing suggestions.

Important implementation decisions;
- UTF-8 encoding: using utf-8 ensures accurate processing of dzongkha characters.

## Data Structures
Dictionary: A hash map where keys are words and value indicate validity. (stores valid dzongkha words for fast lookup during spell checking) 
List: A list of strings, each repressenting a line or a word. (Holds the input text lines and words for processing.) Reason for choice- allows for easy iteration and indexing,simplifying the text processing workflow. 
Tuple: A tuple with the misspelled word and a list of suggestions. (Pairs misspelled words with their corresponding suggestion) Reason for choice- Tuples maintain a consistent association between words and their suggestions.
Set: A set containing potential corrections. (collects unique suggestion for misspelled words to avoid corrections) Reason for choice- Set provide efficient average time complexity. 

## Algorithms
- dictionary lookup algorithm: quickly checks if a word exists in the dictionary. Utilizes a hash map where each word is a key, allowing for average time complexity during lookups. this anables rapid verification of words.
- cleaning the dictionary file algorithm: cleans the dictionary by removing invalid entries. Method: Reads the file,normalizes words, filters out invalids and use a set to ensure uniqueness. 
Spell checking algorithm: Identifies misspellings and generates suggestions. Checks words against the dictionary.

## Performance Analysis
Time complexity:
- Dictionary lookup: O(1) on average, allowing quick word validation.
-dictionary cleaning: O(n), where n is the number of words in the dictionary.
Space complexity:
- Dictionary storage: O(n) for unique words.
Performance Optimizations:
- Hash Map: enables fast dictionary lookups.
- set for suggestions: ensure unique correction and optimizes memory.
- Dictionary preprocessing: cleans the dictionary for faster lookups.

## Challenges and Solutions
Challenges: 1.Dzongkha's unique characters complicated processing. 2.large dictionaries affected memory and lookup times.
Solutions: 1.Used utf-8 encoding for proper character handling. 2.Implemented a hash map for quick lookups and a cleaning algorithm to remove duplicates.