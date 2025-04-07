import sys
from PIL import Image, ImageOps


def main():
    if len(sys.argv) != 3:
        print("Usage: shirt.py <image.jpg|png> <image.jpg|png>")
        sys.exit(1)

    if not sys.argv[1].endswith(".jpg") and not sys.argv[1].endswith(".png"):
        print("Usage: python scourgify.py <filename.csv> <filename.csv>")
        sys.exit(1)

    if not sys.argv[2].endswith(".jpg") and not sys.argv[2].endswith(".png"):
        print("Usage: python scourgify.py <filename.csv> <filename.csv>")
        sys.exit(1)
    
    try:
        image = Image.open(sys.argv[1])
        shirt = Image.open("shirt.png")
        cropped = ImageOps.fit(image)
        
        
            
    except Exception as e:
        print(f"An error occured: {e}")
        sys.exit(1)

    Image.save(cropped)
    



if __name__ == "__main__":
    main()