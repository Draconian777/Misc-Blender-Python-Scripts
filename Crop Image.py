import os
from PIL import Image


def crop_images_in_directory(directory,delete_original=False):
    #target Resolution
    target_width=2560
    target_height=1440

    #loop through all files in directory
    for filename in os.listdir(directory):
        if filename.lower().endswith(('.png','jpeg','.jpg')):
            filepath = os.path.join(directory,filename)

            #open image
            with Image.open(filepath) as img:
                width,height = img.size

                #check if resolution exceeds target
                if width >target_width or height > target_height:
                    #calc crop box
                    left=max(0,(width -target_width)//2)
                    upper=max(0, (height-target_height)//2)
                    right = left + target_width
                    lower = upper +target_height

                    cropped_img = img.crop((left, upper, right, lower))

                    # Create new filename
                    name, ext = os.path.splitext(filename)
                    new_filename = f"{name}_cropped{ext}"
                    new_filepath = os.path.join(directory, new_filename)

                    #save
                    cropped_img.save(new_filepath)

                    print(f"Cropped image saved as:{new_filename}")

                    #Delete Orignal??

                    if delete_original:
                        os.remove(filepath)
                        print(f"Deleted original image: {filename}")

                else:
                    print(f"Image {filename} does not exceed target resolution. Skipping.")


#Driver
directory_path = r'C:\Users\Draconian\Desktop\Test'  # Replace with the path to your directory
crop_images_in_directory(directory_path, delete_original=False)