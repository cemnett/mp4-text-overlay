import subprocess


def modify_video(in_video, out_video, my_text):
    subprocess.check_call(['/Users/cemnett/PycharmProjects/mp4TextOverlay/modifyVideo.sh',
                           in_video, out_video, my_text])


def play_video(out_video):
    subprocess.check_call(['/Users/cemnett/PycharmProjects/mp4TextOverlay/playVideo.sh', out_video])


def get_info():
    customize = input("Would you like to customize file names and text overlay (y/n): ")

    input_video, output_video, text_overlay = "testVideo.mp4", "testVideoOverlay.mp4", "This is a test."

    if customize == 'y':
        input_video = input("Enter the name of your input file: ")
        output_video = input("Enter the name of your output file: ")
        text_overlay = input("Enter the text to be displayed: ")

    return input_video, output_video, text_overlay


if __name__ == '__main__':
    while True:
        cmd = input("Enter m to modify the video, p to play the video, b to modify AND play, or q to quit: ")
        if cmd == "q":
            break
        elif cmd == "m":
            input_file, output_file, text = get_info()
            modify_video(input_file, output_file, text)
        elif cmd == "p":
            output_file = input("Enter the name of your video: ")
            play_video(output_file)
        else:
            input_file, output_file, text = get_info()
            modify_video(input_file, output_file, text)
            play_video(output_file)
