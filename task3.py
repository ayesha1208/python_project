import tkinter as tk
from tkinter import messagebox
import requests
from bs4 import BeautifulSoup

# Function to fetch lyrics by scraping Genius.com
def get_lyrics_from_genius():
    song_name = entry_song.get()
    artist_name = entry_artist.get()
    
    if not song_name or not artist_name:
        messagebox.showwarning("Input Error", "Both fields are required!")
        return

    # Construct the Genius search URL
    search_url = f"https://genius.com/search?q={song_name}%20{artist_name}"
    
    try:
        # Send request to search the song
        response = requests.get(search_url)
        
        # Parse the HTML content of the page
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Find the first song link (usually the best match)
        song_link = soup.find("a", class_="mini_card")["href"]
        
        # Visit the song's Genius page to get the lyrics
        song_page = requests.get(song_link)
        song_soup = BeautifulSoup(song_page.text, "html.parser")
        
        # Extract lyrics
        lyrics = song_soup.find("div", class_="lyrics").get_text()
        
        # Display the lyrics
        text_lyrics.delete(1.0, tk.END)  # Clear previous lyrics
        text_lyrics.insert(tk.END, lyrics)
    
    except Exception as e:
        messagebox.showerror("Error", f"Error fetching lyrics: {e}")

# Set up the Tkinter GUI
root = tk.Tk()
root.title("Song Lyrics Finder")
root.geometry("500x400")

# Song and Artist input fields
label_song = tk.Label(root, text="Song Name:")
label_song.pack(pady=5)

entry_song = tk.Entry(root, width=40)
entry_song.pack(pady=5)

label_artist = tk.Label(root, text="Artist Name:")
label_artist.pack(pady=5)

entry_artist = tk.Entry(root, width=40)
entry_artist.pack(pady=5)

# Button to fetch lyrics
button_get_lyrics = tk.Button(root, text="Get Lyrics", command=get_lyrics_from_genius)
button_get_lyrics.pack(pady=10)

# Text area to display lyrics
text_lyrics = tk.Text(root, width=50, height=15)
text_lyrics.pack(pady=10)

# Start the Tkinter event loop
root.mainloop()
