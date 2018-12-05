# inní models.video
def __repr__(self):
    return "Video('{}','{}','{}')".format(self.__title,self.__length,self.__genre)


#inní VideoRepository
def add_video(self, video):
    with open('./data/videos.txt', 'a+') as videos_file:
        videos_file.write(video.__repr__()+ '\n')

def get_videos(self):
    video = []
    with open('./data/videos.txt', 'r') as videos_file:
        for line in videos_file.readlines():
            video = eval(line.strip())
            videos.append(video)
        return videos

valid_brands = ["Suzuki","Honda", "Hyundai","Toyota", "Volkswagen","Lexus","Renault","Mazda",
"Kia","Opel","Ford","Skoda","Mercedez Benz","Nissan","Jeep","Land Rover","Mitsubishi","Volvo", 
"Citroen","VW","Audi","BMW","Chevrolet","Mini"]