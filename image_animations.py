import customtkinter as ctk
from PIL import Image, ImageTk
from os import walk
 
# exercise
# create an animation that runs for ever

class AnimatedButton(ctk.CTkButton):
    def __init__(self, parent, light_path, dark_path):
        
        # animation logic

        self.frames = self.import_folders(light_path, dark_path)
        self.frame_index =0
        # print(self.frames)
        self.animation_length = len(self.frames) -1
        self.animation_status = ctk.StringVar(value='start')
        self.animation_status.trace_add('write', self.animate)
        super().__init__(master= parent,
                          text='An animated button',
                          image=self.frames[self.frame_index],
                          command=self.infinite)
        self.pack(expand=True)

    def import_folders(self, light_path, dark_path):
        image_path= []
        for path in (light_path, dark_path):
            for folder, subfolder, image_data in walk(path):
                sorted_data = sorted(image_data, 
                                     key=lambda item: int(item.split('.')[0][::]))
                full_path = [path + '/' + item for item in sorted_data]
                image_path.append(full_path)
                # print(image_path)
        image_path = zip(*image_path)
        # print(image_path)
        image_path = list(image_path)
        # print(image_path)
        ctk_images = []
        for imag in image_path:
            # print(imag)
            ctk_image = ctk.CTkImage(
                light_image=Image.open(imag[0]),
                dark_image=Image.open(imag[1])
                                     )
            ctk_images.append(ctk_image)
        return ctk_images

    def trigger_animate(self):
        if self.animation_status.get() == 'start':
            self.frame_index = 0
            self.animation_status.set('forward')
        # if self.animation_status.get() == 'end':
        #     self.frame_index = self.animation_length
        #     self.animation_status.set('backward')


    def animate(self, *args):
        if self.animation_status.get() == 'forward':
            self.frame_index += 1
            self.configure(image=self.frames[self.frame_index])

            if self.frame_index < self.animation_length:
                self.after(20, self.animate)
            else:
                self.animation_status.set('backward')
                self.animate()
            
        if self.animation_status.get() == 'backward':
            self.frame_index -= 1
            self.configure(image=self.frames[self.frame_index])

            if self.frame_index > 0:
                self.after(20, self.animate)
            else:
                self.animation_status.set('forward')
                self.animate()
                # self.animate()
        # self.trigger_animate()
        # self.animate()
    def infinite(self):
        self.frame_index += 1
        self.frame_index = 0 if self.frame_index > self.animation_length else self.frame_index
        self.configure(image=self.frames[self.frame_index])
        self.after(20, self.infinite)
            
        


# window
window = ctk.CTk()
window.title('Animated')
window.geometry('300x200')

AnimatedButton(window, 'icons', 'icons')

# run the app
if __name__ == '__main__':
    window.mainloop()