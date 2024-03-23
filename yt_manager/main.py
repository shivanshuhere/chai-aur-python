import json 
# load and dumb

def load_data ():
    try:
        with open("youtube.txt", 'r') as file:
            test = json.load(file)
            return test
    except FileNotFoundError:
        return []

def list_all_videos (video):
    pass

def add_video (video):
    pass

def update_video (video):
    pass

def delete_video (video):
    pass

def main ():
    videos = load_data()
    print ("\n Youtube Manager\n")
    print("1. All videos\n2. Add Videos\n3. Update Videos\n4. Delete Videos\n 5. Exit")
    choice = input("Enter your choice :")

    match choice :
        case "1":
            list_all_videos(video)
        case "2":
            add_video(video)
        case "3":
            update_video(video)
        case "4":
            delete_video(vidoe)
        case "5":
            break
        case _:
            print("Invalid choice")

if __name__ == "__main__":
    main()

