import pytube
from kivymd.app import MDApp
from kivymd.uix.screen import MDScreen
from kivymd.uix.textfield import MDTextFieldRect
from kivymd.uix.button import MDRectangleFlatButton
from kivymd.uix.dialog import MDDialog


class YoutubeDownloader(MDApp):
    dialog = None

    def build(self):
        screen = MDScreen()
        button = MDRectangleFlatButton(text="Download",
                                       on_release=self.showdialog,
                                       pos_hint={'center_x': 0.5, 'center_y': 0.3})
        self.textfield = MDTextFieldRect(
            hint_text="Enter the links below",
            pos_hint={'center_x': 0.5, 'center_y': 0.15},
            size_hint_x=None, width=700, size_hint_y=None, height=100)
        screen.add_widget(button)
        screen.add_widget(self.textfield)
        return screen

    def showdialog(self, obj):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Confirm download",
                pos_hint={'center_x': 0.5, 'center_y': 0.5},
                buttons=[MDRectangleFlatButton(text="Download", on_release=self.download),
                         MDRectangleFlatButton(text="Cancel", on_release=self.showdialog)]
            )
            self.dialog.open()

        else:
            self.dialog.dismiss()
            self.dialog = None

    def download(self, obj):

        self.dialog.dismiss()
        self.dialog = None

        links = self.textfield.text.replace(" ", "\n").split("\n")
        print(links)

        for i in range(len(links)):
            yt = pytube.YouTube(links[i])
            try:
                video = yt.streams.get_highest_resolution()
                print(f"downloading video number {i + 1}")
                video.download("D:\\")
            except Exception as e:
                print(e)
                pass


YoutubeDownloader().run()
