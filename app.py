from flask import Flask, render_template, request
import threading
import time
import pyttsx3
import pygame
import os

app = Flask(__name__)

# Global variables to store error counts
total_errors = 0
resolved_errors = 0

# Initialize lock for music playing
music_lock = threading.Lock()
music_thread_started = threading.Event()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/update_errors', methods=['POST'])
def update_errors():
    global total_errors, resolved_errors
    total_errors = int(request.form['total_errors'])
    resolved_errors = int(request.form['resolved_errors'])
    return 'Updated', 200

def speak(message):
    engine = pyttsx3.init()
    engine.say(message)
    engine.runAndWait()

def check_status():
    while True:
        time.sleep(10)  # Check every 30 minutes
        message = "How is your project going? How many errors have you encountered and resolved?"
        speak(message)
        time.sleep(10)  # Wait a bit before fetching the updated numbers
        speak(f"You have encountered {total_errors} errors and resolved {resolved_errors} of them.")

def play_music():
    pygame.mixer.init()
    # List of music files
    playlist = ['song.mp3', 'song.mp3']  # Replace with your music files
    playlist = [os.path.join('./music', song) for song in playlist]  # Update the path as necessary

    while True:
        for song in playlist:
            with music_lock:
                if not pygame.mixer.music.get_busy():
                    pygame.mixer.music.load(song)
                    pygame.mixer.music.play()
                    while pygame.mixer.music.get_busy():  # Wait for the music to finish playing
                        pygame.time.Clock().tick(10)  # Check every 100ms

if __name__ == '__main__':
    # Start the check_status thread
    threading.Thread(target=check_status).start()

    # Ensure only one music thread is started
    if not music_thread_started.is_set():
        music_thread = threading.Thread(target=play_music)
        music_thread.start()
        music_thread_started.set()

    # Start the Flask app
    app.run(debug=True, host='0.0.0.0', port=8080)
