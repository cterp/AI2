## AI2 take-home problem

### Usage instructions
+ Install PrettyTable 
	+ For example, ```$ pip install PrettyTable```
+ In the main() function of ```term_freq_script.py```, call the function ```term_frequency``` with a list of words for which to compute term frequency scores.
	+ For example, ```term_frequency(["ishmael"])```.
	+ Note that if only a word is given instead of a list (e.g. ```term_frequency("ishmael")```), this program will compute maximum term frequency scores for each letter.

### Assumptions
+ Term frequency scores are represented by Decimal numbers, because they can be represented exactly. Precision was arbitrarily set to 8 digits.
+ There are text files in the same directory as the script.
+ Instead of showing the fully qualified path and name for each file in the results table, for clarity only the filename is shown.
+ Stop words were not removed (e.g. "the", "is", "at").

### Output
Output for the words “queequeg”, “whale”, and “sea”:
+----------+-----------------------+----------------------+<br>
|   word   |        document       | term frequency score |<br>
+----------+-----------------------+----------------------+<br>
| queequeg | mobydick-chapter4.txt |     0.0077751196     |<br>
|  whale   | mobydick-chapter1.txt |     0.0013380910     |<br>
|   sea    | mobydick-chapter1.txt |     0.0057983943     |<br>
+----------+-----------------------+----------------------+<br>