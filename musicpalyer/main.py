import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = 'hide'
import pygame

# Function to play the selected music
def play_music(folder, song_name):
    # Join file with songs to test if exists
    file_path = os.path.join(folder, song_name)
    if not os.path.exists(file_path):
        print('!!File not found!!')
        return
    
    # Start pygame music
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play()
    print(f'\nNow playing: {song_name}')
    print('Commands:[P]ause, [R]esume, [S]top')

    # Loop for pygame commands
    while True:
        command = input('> ').upper()
        if command == 'P':
            pygame.mixer.music.pause()
            print('Paused!')
        elif command == 'R':
            pygame.mixer.music.unpause()
            print('Resumed!')
        elif command == 'S':
            pygame.mixer.music.stop()
            print('Stopped!')
            return
        else:
            print('!!Invalid command!!')
 

# Main function
def main():
    # Test pygame
    try:
        pygame.mixer.init()
    except pygame.error as e:
        print('!!Audio initialization failed!!', e)

    # Test to see is the folder exists
    folder = 'musicpalyer/music'
    if not os.path.isdir(folder):
        print(f'!!Folder "{folder}" not found!!')
        return

    # LIst fo musics
    mp3_files = [file for file in os.listdir(folder) if file.endswith('.mp3')]
    if not mp3_files:
        print('No .mp3 files found!')

    while True:
        print('\n**********************')
        print('***** MP3 PLAYER *****')
        print('**********************')
        print('My songs list:')

        for index, song in enumerate(mp3_files, start=1):
            print(f'{index}. {song}')
        
        choice_input = input('\nEnter the song number to play (or "q" to quit): ').lower()
        if choice_input == 'q':
            print('Goodbye!')
            break

        if not choice_input.isdigit():
            print('!!Enter a valid number!!')
            continue

        choice_input = int(choice_input) - 1
        if 0 <= choice_input < len(mp3_files):
            play_music(folder, mp3_files[choice_input])
        else:
            print('!!Invalid choice!!')


if __name__ == '__main__':
    main()