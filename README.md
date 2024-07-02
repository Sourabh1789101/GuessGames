# GuessGames
 This code is a number guessing game with three difficulty levels: easy, medium, and hard. Players guess a randomly generated number, and the game tracks the number of attempts. It saves the best scores, can reset scores, and displays current scores. The main menu allows mode selection and game initiation.
markdown

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
</head>
<body>

<h1>Number Guessing Game</h1>

<p>This is a Python-based number guessing game with three difficulty levels: Easy, Medium, and Hard. Players try to guess a randomly generated number, with the game providing hints if the guess is too high or too low. The game tracks the number of attempts and saves the best scores for each difficulty level.</p>

<h2>Features</h2>
<ul>
    <li>Three difficulty levels:
        <ul>
            <li>Easy: Guess a number between 1 and 10</li>
            <li>Medium: Guess a number between 1 and 50</li>
            <li>Hard: Guess a number between 1 and 100</li>
        </ul>
    </li>
    <li>Score tracking and saving of best scores</li>
    <li>Option to reset scores</li>
    <li>Display current best scores</li>
</ul>

<h2>Requirements</h2>
<ul>
    <li>Python 3.x</li>
    <li><code>pyautogui</code> library</li>
</ul>

<h2>Installation</h2>
<ol>
    <li>Clone the repository or download the code files.</li>
    <li>Install the <code>pyautogui</code> library if not already installed:
        <pre><code>pip install pyautogui</code></pre>
    </li>
</ol>

<h2>How to Run</h2>
<ol>
    <li>Ensure you have the required dependencies installed.</li>
    <li>Run the main script:
        <pre><code>python &lt;script_name&gt;.py</code></pre>
    </li>
    <li>The game will start, and you can select from the main menu to play a game, view scores, or reset scores.</li>
</ol>

<h2>Code Description</h2>
<ul>
    <li>The script initializes score files for each difficulty level if they do not exist.</li>
    <li>Three functions (<code>game_easy</code>, <code>game_medium</code>, <code>game_hard</code>) handle the game logic for each difficulty level.</li>
    <li>The <code>reset_scores</code> function resets all scores to a default value.</li>
    <li>The <code>show_scores</code> function displays the best scores for each difficulty level.</li>
    <li>The <code>main_menu</code> function presents the main menu options to the user.</li>
</ul>

<h2>Main Menu Options</h2>
<ul>
    <li><strong>Easy</strong>: Starts the game in Easy mode.</li>
    <li><strong>Medium</strong>: Starts the game in Medium mode.</li>
    <li><strong>Hard</strong>: Starts the game in Hard mode.</li>
    <li><strong>Score</strong>: Displays the current best scores.</li>
    <li><strong>Reset</strong>: Resets the scores to default values.</li>
    <li><strong>Exit</strong>: Exits the game.</li>
</ul>

<h2>Example</h2>
<ol>
    <li>When you start the game, a menu will appear with options to select a difficulty level, view scores, reset scores, or exit.</li>
    <li>If you select a difficulty level, you will be prompted to guess a number within the specified range.</li>
    <li>The game will provide hints if your guess is too high or too low.</li>
    <li>Once you guess the correct number, the game will inform you of the number of steps taken and update the best score if applicable.</li>
    <li>You can choose to play again or exit.</li>
</ol>

<h2>Author</h2>
<p>This script was created by [Your Name].</p>

<h2>License</h2>
<p>This project is licensed under the MIT License - see the LICENSE file for details.</p>

</body>
</html>
